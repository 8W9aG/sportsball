"""FootballData league model."""

import csv
import io
import urllib.parse
from typing import Any, Iterator

import tqdm
from bs4 import BeautifulSoup
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ..epl.position import Position
from ..game_model import GameModel
from ..league import League
from ..league_model import SHUTDOWN_FLAG, LeagueModel, needs_shutdown
from .footballdata_game_model import create_footballdata_game_model


class FootballDataLeagueModel(LeagueModel):
    """FootballData implementation of the league model."""

    def __init__(
        self,
        league: League,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(league, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "footballdata-league-model"

    @classmethod
    def position_validator(cls) -> dict[str, str]:
        """Football position validators."""
        return {str(x): str(x) for x in Position}

    def _row_to_game(self, row: Any) -> GameModel | None:
        division_cell = str(row["Div"])
        if division_cell in {"E0"}:
            return None
        date_cell = str(row["Date"]).strip()
        time_cell = str(row.get("Time", "")).strip()
        home_team_cell = str(row["HomeTeam"]).strip()
        away_team_cell = str(row["AwayTeam"]).strip()
        full_time_home_goals_cell = str(row["FTHG"]).strip()
        full_time_away_goals_cell = str(row["FTAG"]).strip()
        referee_cell = row.get("Referee")
        home_shots_cell = row.get("HS")
        away_shots_cell = row.get("AS")
        home_shots_on_target_cell = row.get("HST")
        away_shots_on_target_cell = row.get("AST")
        home_fouls_cell = row.get("HF")
        away_fouls_cell = row.get("AF")
        home_yellow_cards_cell = row.get("HY")
        away_yellow_cards_cell = row.get("AY")
        home_red_cards_cell = row.get("HR")
        away_red_cards_cell = row.get("AR")
        home_odds_cell = row.get("B365H")
        away_odds_cell = row.get("B365A")
        return create_footballdata_game_model(
            session=self.session,
            league=self.league,
            date=date_cell,
            time=time_cell,
            home_team=home_team_cell,
            away_team=away_team_cell,
            full_time_home_goals=full_time_home_goals_cell,
            full_time_away_goals=full_time_away_goals_cell,
            referee=referee_cell,
            home_shots=home_shots_cell,
            away_shots=away_shots_cell,
            home_shots_on_target=home_shots_on_target_cell,
            away_shots_on_target=away_shots_on_target_cell,
            home_fouls=home_fouls_cell,
            away_fouls=away_fouls_cell,
            home_yellow_cards=home_yellow_cards_cell,
            away_yellow_cards=away_yellow_cards_cell,
            home_red_cards=home_red_cards_cell,
            away_red_cards=away_red_cards_cell,
            home_odds=home_odds_cell,
            away_odds=away_odds_cell,
        )

    @property
    def games(self) -> Iterator[GameModel]:
        """Find all the games."""
        with self.session.wayback_disabled():
            try:
                with tqdm.tqdm(position=self.position) as pbar:
                    url = self._url
                    response = None
                    with self.session.cache_disabled():
                        self.session.cache.delete(urls=[url])
                        response = self.session.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, "lxml")
                    csv_urls = []
                    for a in soup.find_all("a", href=True):
                        if needs_shutdown():
                            return
                        csv_url = urllib.parse.urljoin(url, a.get("href"))
                        if not csv_url.endswith(".csv"):
                            continue
                        if (
                            (self.league == League.EPL and csv_url.endswith("E0.csv"))
                            or (
                                self.league == League.LALIGA
                                and csv_url.endswith("SP1.csv")
                            )
                            or (
                                self.league == League.BUNDESLIGA
                                and csv_url.endswith("D1.csv")
                            )
                        ):
                            csv_urls.append(csv_url)

                    for count, csv_url in enumerate(sorted(csv_urls, reverse=True)):
                        response = None
                        if count == 0:
                            with self.session.cache_disabled():
                                self.session.cache.delete(urls=[csv_url])
                                response = self.session.get(csv_url)
                        else:
                            response = self.session.get(csv_url)
                        response.raise_for_status()
                        handle = io.StringIO(response.text)
                        cr = csv.DictReader(handle)
                        for row in cr:
                            game_model = self._row_to_game(row)
                            if game_model is not None:
                                pbar.update(1)
                                pbar.set_description(f"FootballData - {game_model.dt}")
                                yield game_model
            except Exception as exc:
                SHUTDOWN_FLAG.set()
                raise exc

    @property
    def _url(self) -> str:
        if self.league == League.EPL:
            return "https://www.football-data.co.uk/englandm.php"
        elif self.league == League.LALIGA:
            return "https://www.football-data.co.uk/spainm.php"
        elif self.league == League.BUNDESLIGA:
            return "https://www.football-data.co.uk/germanym.php"
        else:
            raise ValueError(f"League {self.league} not supported")
