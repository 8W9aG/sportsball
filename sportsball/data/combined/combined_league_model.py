"""Combined league model."""

# pylint: disable=raise-missing-from,too-many-locals
import datetime
import logging
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Iterator

import tqdm
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ..game_model import GameModel
from ..league import League
from ..league_model import LeagueModel
from .combined_game_model import create_combined_game_model


def _produce_league_games(league_model: LeagueModel) -> list[dict[str, Any]]:
    return [x.model_dump() for x in league_model.games]


class CombinedLeagueModel(LeagueModel):
    """The class implementing the combined league model."""

    def __init__(
        self,
        session: ScrapeSession,
        league: League,
        league_models: list[LeagueModel],
        league_filter: str | None,
    ) -> None:
        super().__init__(league, session)
        if league_filter is not None:
            league_models = [x for x in league_models if x.name() == league_filter]
        if not league_models:
            raise ValueError("No league models to run")
        self._league_models = league_models

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        """A map to resolve the different teams identities to a consistent identity."""
        raise NotImplementedError(
            "team_identity_map not implemented on CombinedLeagueModel parent class."
        )

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        """A map to resolve the different venue identities to a consistent identity."""
        raise NotImplementedError(
            "venue_identity_map not implemented on CombinedLeagueModel parent class."
        )

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        """A map to resolve the different player identities to a consistent identity."""
        return {}

    @property
    def games(self) -> Iterator[GameModel]:
        games: dict[str, list[GameModel]] = {}
        team_identity_map = self.team_identity_map()
        for league_model in self._league_models:
            league_model.clear_session()
        with ThreadPoolExecutor(
            min(multiprocessing.cpu_count(), len(self._league_models))
        ) as p:
            # We want to terminate immediately if any of our runners runs into trouble.

            futures = {
                p.submit(_produce_league_games, model): model
                for model in self._league_models
            }

            results = []
            try:
                for future in as_completed(futures):
                    result = future.result()  # Raises if an exception occurred
                    results.append(result)
            except Exception:
                # Cancel all pending futures
                for f in futures:
                    f.cancel()
                raise  # Optionally re-raise the exception
        game_lists = [[GameModel.model_validate(y) for y in x] for x in results]

        for game_list in game_lists:
            for game_model in game_list:
                old_game_components = [
                    str(game_model.dt.date() - datetime.timedelta(days=1))
                ]
                game_components = [str(game_model.dt.date())]
                for team in game_model.teams:
                    if team.identifier not in team_identity_map:
                        logging.warning(
                            "%s for team %s not found in team identity map.",
                            team.identifier,
                            team.name,
                        )
                    team_identifier = team_identity_map.get(
                        team.identifier, team.identifier
                    )
                    old_game_components.append(team_identifier)
                    game_components.append(team_identifier)
                old_game_components = sorted(game_components)
                game_components = sorted(game_components)
                key = "-".join(old_game_components)
                if key in games:
                    games[key].append(game_model)
                else:
                    key = "-".join(game_components)
                    games[key] = [game_model]
        names: dict[str, str] = {}
        coach_names: dict[str, str] = {}
        player_ffill: dict[str, dict[str, Any]] = {}
        team_ffill: dict[str, dict[str, Any]] = {}
        coach_ffill: dict[str, dict[str, Any]] = {}
        umpire_ffill: dict[str, dict[str, Any]] = {}
        last_game_number = None
        for game_models in tqdm.tqdm(games.values(), desc="Combining Game Models"):
            game_model = create_combined_game_model(  # type: ignore
                game_models=game_models,
                venue_identity_map=self.venue_identity_map(),
                team_identity_map=team_identity_map,
                player_identity_map=self.player_identity_map(),
                session=self.session,
                names=names,
                coach_names=coach_names,
                last_game_number=last_game_number,
                player_ffill=player_ffill,
                team_ffill=team_ffill,
                coach_ffill=coach_ffill,
                umpire_ffill=umpire_ffill,
            )
            last_game_number = game_model.game_number
            yield game_model
