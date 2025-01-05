"""NBA NBA league model."""

import datetime
from typing import Iterator, TypedDict

import pandas as pd
import requests
import tqdm
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from nba_api.library.http import NBAHTTP  # type: ignore
from nba_api.stats.endpoints import leaguegamefinder  # type: ignore

from ...game_model import GameModel
from ...league import League
from ...league_model import LeagueModel
from .nba_nba_game_model import create_nba_nba_game_model


def _combine_team_games(df: pd.DataFrame, keep_method="home") -> pd.DataFrame:
    """Combine a TEAM_ID-GAME_ID unique table into rows by game. Slow.

    Parameters
    ----------
    df : Input DataFrame.
    keep_method : {'home', 'away', 'winner', 'loser', ``None``}, default 'home'
        - 'home' : Keep rows where TEAM_A is the home team.
        - 'away' : Keep rows where TEAM_A is the away team.
        - 'winner' : Keep rows where TEAM_A is the losing team.
        - 'loser' : Keep rows where TEAM_A is the winning team.
        - ``None`` : Keep all rows. Will result in an output DataFrame the same
            length as the input DataFrame.

    Returns
    -------
    result : DataFrame
    """
    # Join every row to all others with the same game ID.
    joined = pd.merge(
        df, df, suffixes=["_A", "_B"], on=["SEASON_ID", "GAME_ID", "GAME_DATE"]
    )
    # Filter out any row that is joined to itself.
    result = joined[joined.TEAM_ID_A != joined.TEAM_ID_B]
    # Take action based on the keep_method flag.
    if keep_method is None:
        # Return all the rows.
        pass
    elif keep_method.lower() == "home":
        # Keep rows where TEAM_A is the home team.
        result = result[result.MATCHUP_A.str.contains(" vs. ")]
    elif keep_method.lower() == "away":
        # Keep rows where TEAM_A is the away team.
        result = result[result.MATCHUP_A.str.contains(" @ ")]
    elif keep_method.lower() == "winner":
        result = result[result.WL_A == "W"]
    elif keep_method.lower() == "loser":
        result = result[result.WL_A == "L"]
    else:
        raise ValueError(f"Invalid keep_method: {keep_method}")
    return result


class NBANBALeagueModel(LeagueModel):
    """NBA NBA implementation of the league model."""

    class _SeasonInfo(TypedDict):
        start: datetime.datetime
        games: int

    def __init__(self, session: requests.Session) -> None:
        super().__init__(League.NBA, session)
        self._league_id = "00"
        NBAHTTP.set_session(session)

    def _produce_games(
        self,
        all_games: pd.DataFrame,
        seasons: dict[str, _SeasonInfo],
        from_date: datetime.date,
    ) -> Iterator[GameModel]:
        for _, row in tqdm.tqdm(
            all_games.iterrows(), desc=f"NBA API Games from {from_date}"
        ):
            season_id = row["SEASON_ID"]
            dt = parse(row["GAME_DATE"])
            season_info = seasons.get(
                season_id,
                {
                    "start": dt,
                    "games": 0,
                },
            )
            week = int((dt - season_info["start"]).days / 7)
            yield create_nba_nba_game_model(  # type: ignore
                row,
                self.league,
                week,
                season_info["games"],  # type: ignore
            )
            season_info["games"] += 1
            seasons[season_id] = season_info

    @property
    def games(self) -> Iterator[GameModel]:
        to_date = datetime.datetime.today().date()
        seasons: dict[str, NBANBALeagueModel._SeasonInfo] = {}
        while True:
            next_date = to_date - relativedelta(years=1)
            result = leaguegamefinder.LeagueGameFinder(
                league_id_nullable=self._league_id,
                date_from_nullable=next_date.strftime("%m/%d/%Y"),
                date_to_nullable=to_date.strftime("%m/%d/%Y"),
            )
            all_games = _combine_team_games(result.get_data_frames()[0])
            all_games = all_games.sort_values(by="GAME_DATE", ascending=True)
            if all_games.empty:
                break
            yield from self._produce_games(all_games, seasons, next_date)
            to_date = next_date
