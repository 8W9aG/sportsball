"""AFL AFLTables game model."""

# pylint: disable=too-many-arguments,too-many-branches,too-many-statements
import datetime
import urllib.parse
from urllib.parse import urlparse

import pytest_is_running
from bs4 import BeautifulSoup, Tag
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...game_model import VERSION, GameModel
from ...league import League
from ...season_type import SeasonType
from .afl_afltables_team_model import create_afl_afltables_team_model
from .afl_afltables_umpire_model import create_afl_afltables_umpire_model
from .afl_afltables_venue_model import create_afl_afltables_venue_model

_FINALS_WEEK_ADDITION_MAP = {
    "Qualifying Final": 1,
    "Elimination Final": 1,
    "Semi Final": 2,
    "Preliminary Final": 3,
    "Grand Final": 4,
}


def _find_end_dt(
    soup: BeautifulSoup, dt: datetime.datetime
) -> datetime.datetime | None:
    end_dt = None
    for b in soup.find_all("b"):
        b_text = b.get_text().strip()
        if "Game time:" in b_text:
            b_text = b_text[b_text.find("Game time:") :]
            b_text = b_text.replace("Game time:", "")
            if ")" in b_text:
                b_text = b_text[: b_text.find(")")]
            b_text = b_text[: b_text.find("s")]
            min_text, sec_text = b_text.split(" ")[-2:]
            end_dt = dt + datetime.timedelta(
                minutes=int(min_text.replace("m", "")),
                seconds=int(sec_text.replace("s", "").replace(")", "")),
            )
            break
    return end_dt


def _find_team_info(tr: Tag, url: str) -> tuple[str, str, int] | None:
    team_url = None
    team_name = None
    team_points = None
    for a in tr.find_all("a", href=True):
        team_url = urllib.parse.urljoin(url, a.get("href"))
        team_name = a.get_text().strip()
    for b in tr.find_all("b"):
        try:
            team_points = int(b.get_text().strip())
        except ValueError:
            pass
    if team_url is None or team_name is None or team_points is None:
        return None
    return team_url, team_name, team_points


def _find_season_metadata(
    soup: BeautifulSoup,
    url: str,
    last_round_number: int,
) -> tuple[
    datetime.datetime,
    str,
    int,
    list[tuple[str, str, int]],
    datetime.datetime | None,
    int | None,
]:
    # pylint: disable=too-many-locals,too-many-branches
    def _parse_date_text(date_text: str) -> datetime.datetime:
        date_text = td_text[td_text.find("Date:") + 5 :]
        date_text = date_text[: date_text.find("Attendance:")]
        if "(" in date_text:
            date_text = date_text[: date_text.find("(") - 1]
        date_text = date_text.strip()
        return parse(date_text)

    dt = None
    venue_url = None
    week = None
    team_infos: dict[str, tuple[str, int]] = {}
    attendance = None
    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            for td in tr.find_all("td"):
                td_text = td.get_text()
                if "Date:" in td_text:
                    dt = _parse_date_text(td_text)
                if "Venue:" in td_text:
                    for a in td.find_all("a", href=True):
                        venue_url = urllib.parse.urljoin(url, a.get("href"))
                if "Round:" in td_text:
                    round_text = td_text[td_text.find("Round:") + 6 :]
                    round_text = round_text[: round_text.find("Venue:")]
                    round_text = round_text.strip()
                    week_addition = _FINALS_WEEK_ADDITION_MAP.get(round_text)
                    if week_addition is None:
                        week = int(round_text)
                    else:
                        week = last_round_number + week_addition
                if "Attendance:" in td_text:
                    attendance_text = td_text[
                        td_text.find("Attendance:") + 11 :
                    ].strip()
                    attendance = int(attendance_text)
            team_info = _find_team_info(tr, url)
            if team_info is not None:
                team_infos[team_info[0]] = (team_info[1], team_info[2])

    if dt is None:
        raise ValueError("dt is null.")
    if venue_url is None:
        raise ValueError("venue_url is null.")
    if week is None:
        raise ValueError("week is null.")
    dt = dt.replace(tzinfo=None)

    return (
        dt,
        venue_url,
        week,
        [(k, v[0], v[1]) for k, v in team_infos.items()],
        _find_end_dt(soup, dt),
        attendance,
    )


def _create_afl_afltables_game_model(
    game_number: int,
    session: ScrapeSession,
    url: str,
    last_round_number: int,
    last_ladder_ranks: dict[str, int] | None,
    league: League,
    season_year: int | None,
    season_type: SeasonType | None,
    version: str,
) -> GameModel:
    # pylint: disable=too-many-locals
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    def _find_teams_metadata(
        soup: BeautifulSoup, team_infos: list[tuple[str, str, int]]
    ) -> list[
        tuple[
            str,
            list[
                tuple[
                    str,
                    str,
                    int | None,
                    str,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    float | None,
                ]
            ],
            int,
        ]
    ]:
        def _is_correct_table(table: Tag, name: str) -> bool:
            for th in table.find_all("th"):
                header_text = th.get_text().strip()
                if name + " Match Statistics" in header_text:
                    return True
            return False

        def _find_players(
            table: Tag,
        ) -> list[
            tuple[
                str,
                str,
                int | None,
                str,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                int | None,
                float | None,
            ]
        ]:
            players: list[
                tuple[
                    str,
                    str,
                    int | None,
                    str,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    int | None,
                    float | None,
                ]
            ] = []
            for tr in table.find_all("tr"):
                player_row = False
                player_url = None
                for a in tr.find_all("a", href=True):
                    player_url = urllib.parse.urljoin(url, a.get("href"))
                    o = urlparse(player_url)
                    if "players" in o.path.split("/"):
                        player_row = True
                if player_row and player_url is not None:
                    jersey = None
                    name = None
                    kicks = None
                    marks = None
                    handballs = None
                    disposals = None
                    goals: int | None = None
                    behinds = None
                    hit_outs = None
                    tackles = None
                    rebounds = None
                    insides = None
                    clearances = None
                    clangers = None
                    free_kicks_for = None
                    free_kicks_against = None
                    brownlow_votes = None
                    contested_possessions = None
                    uncontested_possessions = None
                    contested_marks = None
                    marks_inside = None
                    one_percenters = None
                    bounces = None
                    goal_assists = None
                    percentage_played = None
                    for count, td in enumerate(tr.find_all("td")):
                        if count == 0:
                            jersey = td.get_text().strip()
                        elif count == 1:
                            name = " ".join(
                                [
                                    x.strip()
                                    for x in reversed(td.get_text().strip().split(","))
                                ]
                            )
                        elif count == 2:
                            kicks_text = td.get_text().strip()
                            if kicks_text:
                                kicks = int(kicks_text)
                        elif count == 3:
                            marks_text = td.get_text().strip()
                            if marks_text:
                                marks = int(marks_text)
                        elif count == 4:
                            handballs_text = td.get_text().strip()
                            if handballs_text:
                                handballs = int(handballs_text)
                        elif count == 5:
                            disposals_text = td.get_text().strip()
                            if disposals_text:
                                disposals = int(disposals_text)
                        elif count == 6:
                            goals_text = td.get_text().strip()
                            if goals_text:
                                goals = int(goals_text)
                        elif count == 7:
                            behinds_text = td.get_text().strip()
                            if behinds_text:
                                behinds = int(behinds_text)
                        elif count == 8:
                            hit_outs_text = td.get_text().strip()
                            if hit_outs_text:
                                hit_outs = int(hit_outs_text)
                        elif count == 9:
                            tackles_text = td.get_text().strip()
                            if tackles_text:
                                tackles = int(tackles_text)
                        elif count == 10:
                            rebounds_text = td.get_text().strip()
                            if rebounds_text:
                                rebounds = int(rebounds_text)
                        elif count == 11:
                            insides_text = td.get_text().strip()
                            if insides_text:
                                insides = int(insides_text)
                        elif count == 12:
                            clearances_text = td.get_text().strip()
                            if clearances_text:
                                clearances = int(clearances_text)
                        elif count == 13:
                            clangers_text = td.get_text().strip()
                            if clangers_text:
                                clangers = int(clangers_text)
                        elif count == 14:
                            free_kicks_for_text = td.get_text().strip()
                            if free_kicks_for_text:
                                free_kicks_for = int(free_kicks_for_text)
                        elif count == 15:
                            free_kicks_against_text = td.get_text().strip()
                            if free_kicks_against_text:
                                free_kicks_against = int(free_kicks_against_text)
                        elif count == 16:
                            brownlow_votes_text = td.get_text().strip()
                            if brownlow_votes_text:
                                brownlow_votes = int(brownlow_votes_text)
                        elif count == 17:
                            contested_possessions_text = td.get_text().strip()
                            if contested_possessions_text:
                                contested_possessions = int(contested_possessions_text)
                        elif count == 18:
                            uncontested_possessions_text = td.get_text().strip()
                            if uncontested_possessions_text:
                                uncontested_possessions = int(
                                    uncontested_possessions_text
                                )
                        elif count == 19:
                            contested_marks_text = td.get_text().strip()
                            if contested_marks_text:
                                contested_marks = int(contested_marks_text)
                        elif count == 20:
                            marks_inside_text = td.get_text().strip()
                            if marks_inside_text:
                                marks_inside = int(marks_inside_text)
                        elif count == 21:
                            one_percenters_text = td.get_text().strip()
                            if one_percenters_text:
                                one_percenters = int(one_percenters_text)
                        elif count == 22:
                            bounces_text = td.get_text().strip()
                            if bounces_text:
                                bounces = int(bounces_text)
                        elif count == 23:
                            goal_assists_text = td.get_text().strip()
                            if goal_assists_text:
                                goal_assists = int(goal_assists_text)
                        elif count == 24:
                            percentage_played_text = td.get_text().strip()
                            if percentage_played_text:
                                percentage_played = float(percentage_played_text)

                    if jersey is None:
                        raise ValueError("jersey is null.")
                    if name is None:
                        raise ValueError("name is null")

                    players.append(
                        (
                            player_url,
                            jersey,
                            kicks,
                            name,
                            marks,
                            handballs,
                            disposals,
                            goals,
                            behinds,
                            hit_outs,
                            tackles,
                            rebounds,
                            insides,
                            clearances,
                            clangers,
                            free_kicks_for,
                            free_kicks_against,
                            brownlow_votes,
                            contested_possessions,
                            uncontested_possessions,
                            contested_marks,
                            marks_inside,
                            one_percenters,
                            bounces,
                            goal_assists,
                            percentage_played,
                        )
                    )
            return players

        team_metadata = []
        for team_url, name, points in team_infos:
            for table in soup.find_all("table"):
                if _is_correct_table(table, name):
                    players = _find_players(table)
                    team_metadata.append((team_url, players, points))
                    break
        return team_metadata

    dt, venue_url, week, team_infos, end_dt, attendance = _find_season_metadata(
        soup, url, last_round_number
    )

    umpire_urls = []
    for a in soup.find_all("a", href=True):
        umpire_url = urllib.parse.urljoin(url, a.get("href"))
        if "/umpires/" in umpire_url:
            umpire_urls.append(umpire_url)

    return GameModel(
        dt=dt,
        week=week,
        game_number=game_number,
        venue=create_afl_afltables_venue_model(venue_url, session, dt),
        teams=[
            create_afl_afltables_team_model(
                team_url,
                players,
                float(points),
                session,  # pyright: ignore
                last_ladder_ranks,
                dt,
                league,
            )
            for team_url, players, points in _find_teams_metadata(soup, team_infos)
        ],
        end_dt=end_dt,
        attendance=attendance,
        league=str(league),
        year=season_year,
        season_type=season_type,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[create_afl_afltables_umpire_model(x, session) for x in umpire_urls],
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_afl_afltables_game_model(
    game_number: int,
    session: ScrapeSession,
    url: str,
    last_round_number: int,
    last_ladder_ranks: dict[str, int] | None,
    league: League,
    season_year: int | None,
    season_type: SeasonType | None,
    version: str,
) -> GameModel:
    return _create_afl_afltables_game_model(
        game_number=game_number,
        session=session,
        url=url,
        last_round_number=last_round_number,
        last_ladder_ranks=last_ladder_ranks,
        league=league,
        season_year=season_year,
        season_type=season_type,
        version=version,
    )


def create_afl_afltables_game_model(
    game_number: int,
    session: ScrapeSession,
    url: str,
    last_round_number: int,
    last_ladder_ranks: dict[str, int] | None,
    league: League,
    season_year: int | None,
    season_type: SeasonType | None,
) -> GameModel:
    """Create a game model from AFL Tables."""
    if not pytest_is_running.is_running():
        return _cached_create_afl_afltables_game_model(
            game_number=game_number,
            session=session,
            url=url,
            last_round_number=last_round_number,
            last_ladder_ranks=last_ladder_ranks,
            league=league,
            season_year=season_year,
            season_type=season_type,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_afl_afltables_game_model(
            game_number=game_number,
            session=session,
            url=url,
            last_round_number=last_round_number,
            last_ladder_ranks=last_ladder_ranks,
            league=league,
            season_year=season_year,
            season_type=season_type,
            version=VERSION,
        )
