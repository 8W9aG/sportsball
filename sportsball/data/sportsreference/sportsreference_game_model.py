"""Sports Reference game model."""

# pylint: disable=too-many-locals,too-many-statements,unused-argument,protected-access,too-many-arguments,use-maxsplit-arg,too-many-branches
import datetime
import io
import logging
import urllib.parse

import dateutil
import pandas as pd
import pytest_is_running
import requests
import requests_cache
from bs4 import BeautifulSoup, Tag
from dateutil.parser import parse

from ...cache import MEMORY
from ...proxy_session import X_NO_WAYBACK
from ..game_model import GameModel
from ..league import League
from ..season_type import SeasonType
from ..team_model import TeamModel
from .sportsreference_team_model import create_sportsreference_team_model
from .sportsreference_venue_model import create_sportsreference_venue_model

_NON_WAYBACK_URLS: set[str] = set()
_MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def _find_old_dt(
    dfs: list[pd.DataFrame],
    session: requests_cache.CachedSession,
    soup: BeautifulSoup,
    url: str,
    league: League,
    player_urls: set[str],
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
    response: requests.Response,
) -> tuple[datetime.datetime, list[TeamModel], str | None]:
    teams: list[TeamModel] = []

    def _process_team_row(df: pd.DataFrame):
        team_rows = [str(df.iat[0, x]) for x in range(len(df.columns.values))]
        team_rows = [x for x in team_rows if x != "nan"]
        if len(team_rows) == 1:
            team_row = team_rows[0]
            for sentinel in ["Next Game", "Prev Game"]:
                if sentinel in team_row:
                    team_rows = [
                        team_row[: team_row.find(sentinel) + len(sentinel)].strip(),
                        team_row[team_row.find(sentinel) + len(sentinel) :]
                        .strip()
                        .replace("/ Next Game ⇒", "")
                        .replace("⇒", "")
                        .strip(),
                    ]
                    last_splits = team_rows[1].split()
                    if last_splits:
                        if last_splits[0] in _MONTHS:
                            continue
                    break
            if not team_rows[1]:
                sentinel = "Next Game"
                team_rows = [
                    team_row[: team_row.find(sentinel) + len(sentinel)].strip(),
                    team_row[team_row.find(sentinel) + len(sentinel) :]
                    .strip()
                    .replace("⇒", "")
                    .strip(),
                ]
            if not team_rows[1]:
                sentinel = "Prev Game"
                team_rows = [
                    team_row[: team_row.find(sentinel) + len(sentinel)].strip(),
                    team_row[team_row.find(sentinel) + len(sentinel) :]
                    .strip()
                    .replace("⇒", "")
                    .strip(),
                ]
        for team_row in team_rows:
            if team_row.startswith("⇒"):
                team_row = team_row[1:]
            team_row = team_row.strip()
            if "Prev Game" in team_row:
                team_name_points = (
                    team_row.split("⇐")[0]
                    .strip()
                    .replace("Prev Game", "")
                    # .replace("/", "")
                    .strip()
                )
            else:
                team_name_points = (
                    team_row.split("⇒")[0].replace("Next Game", "").strip()
                )
            # Handle team name points like "Indiana Pacers 97 45-37 (Won 3)"
            if "-" in team_name_points:
                dash_splits = team_name_points.split("-")
                # Handle team name points like "Kansas City-Omaha Kings 89"
                # and cases like "Kansas City-Omaha Kings 95 44-38 (Won 1) ⇐ Prev Game"
                for i in range(len(dash_splits) - 1):
                    if (
                        dash_splits[i].split()[-1].isdigit()
                        and dash_splits[i + 1].split()[0].isdigit()
                    ):
                        team_name_points = " ".join(
                            "-".join(dash_splits[: i + 1]).strip().split()[:-1]
                        )
                        break
            for marker in ["Lost", "Won"]:
                team_name_points = team_name_points.split(marker)[0].strip()
            points = int(team_name_points.split()[-1].strip())
            team_name = " ".join(team_name_points.split()[:-1]).strip()
            if " at " in team_name:
                team_name = team_name.split(" at ")[0].strip()
            if " vs " in team_name:
                team_name = team_name.split(" vs ")[0].strip()
            for month in _MONTHS:
                month_split = " " + month + " "
                if month_split in team_name:
                    team_name = team_name.split(month_split)[0].strip()
                    points = int(team_name.split()[-1].strip())
                    team_name = " ".join(team_name.split()[:-1]).strip()
                    break
            team_a = soup.find("a", text=team_name, href=True)
            if not isinstance(team_a, Tag):
                raise ValueError("team_a is not a tag.")
            team_url = urllib.parse.urljoin(url, str(team_a.get("href")))
            if dt is None:
                raise ValueError("dt is null.")
            teams.append(
                create_sportsreference_team_model(
                    session,
                    team_url,
                    dt,
                    league,
                    player_urls,
                    points,
                    fg,
                    fga,
                    offensive_rebounds,
                    assists,
                    turnovers,
                )
            )

    dt = None
    venue_name = None
    for df in dfs:
        if len(df) == 2:
            test_row = df.iat[0, 0]
            test_row_2 = df.iat[1, 0]

            if (
                "Prev Game" in test_row
                or "Next Game" in test_row
                or "Lost" in test_row
                or "PM," in test_row_2
            ):
                date_venue_split = df.iat[1, 0].split()
                current_idx = 5
                try:
                    dt = parse(" ".join(date_venue_split[:current_idx]))
                except dateutil.parser._parser.ParserError:  # type: ignore
                    try:
                        current_idx = 3
                        dt = parse(" ".join(date_venue_split[:current_idx]))
                    except dateutil.parser._parser.ParserError:  # type: ignore
                        dt = parse(
                            " ".join(",".join(test_row.split(",")[1:]).split()[:3])
                        )
                venue_name = " ".join(date_venue_split[current_idx:])
                _process_team_row(df)
                break

    if dt is None:
        title_tag = soup.find("title")
        if not isinstance(title_tag, Tag):
            raise ValueError("title_tag is not a tag.")
        title = title_tag.get_text().strip().split("|")[0].strip()
        date = title[title.find(",") :].strip()
        dt = parse(date)
        for df in dfs:
            test_row = df.iat[0, 0]
            if "Prev Game" in test_row:
                _process_team_row(df)
                break

    if venue_name is not None and not venue_name.replace(",", "").strip():
        venue_name = None

    if dt is None:
        raise ValueError("dt is null.")
    if venue_name is None:
        logging.warning("venue_name is null.")

    return (dt, teams, venue_name)


def _find_new_dt(
    soup: BeautifulSoup,
    scorebox_meta_div: Tag,
    url: str,
    session: requests_cache.CachedSession,
    league: League,
    player_urls: set[str],
    scores: list[float],
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
) -> tuple[datetime.datetime, list[TeamModel], str]:
    in_divs = scorebox_meta_div.find_all("div")
    current_in_div_idx = 0
    in_div = in_divs[current_in_div_idx]
    in_div_text = in_div.get_text().strip()
    current_in_div_idx += 1
    if "Tournament" in in_div_text:
        in_div_text = in_divs[1].get_text().strip()
        current_in_div_idx += 1
    try:
        dt = parse(in_div_text)
    except dateutil.parser._parser.ParserError as exc:  # type: ignore
        logging.error("Failed to parse date for URL: %s", url)
        raise exc
    venue_div = in_divs[current_in_div_idx]
    venue_name = venue_div.get_text().strip()
    scorebox_div = soup.find("div", class_="scorebox")
    if not isinstance(scorebox_div, Tag):
        raise ValueError("scorebox_div is not a Tag.")

    teams: list[TeamModel] = []
    for a in scorebox_div.find_all("a"):
        team_url = urllib.parse.urljoin(url, a.get("href"))
        if "/schools/" in team_url:
            teams.append(
                create_sportsreference_team_model(
                    session,
                    team_url,
                    dt,
                    league,
                    player_urls,
                    scores[len(teams)],
                    fg,
                    fga,
                    offensive_rebounds,
                    assists,
                    turnovers,
                )
            )

    return (dt, teams, venue_name)


def _create_sportsreference_game_model(
    session: requests_cache.CachedSession,
    url: str,
    league: League,
) -> GameModel:
    # pylint: disable=too-many-branches
    headers = {}
    if url in _NON_WAYBACK_URLS:
        headers = {X_NO_WAYBACK: "1"}
    response = session.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    page_title = soup.find("h1", class_="page_title")

    # If the page_title is bad, try fetching from a non wayback source
    if page_title is not None:
        if page_title.get_text().strip() == "File Not Found":
            with session.cache_disabled():
                response = session.get(url, headers={X_NO_WAYBACK: "1"})
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")

    player_urls = set()
    for a in soup.find_all("a"):
        player_url = urllib.parse.urljoin(url, a.get("href"))
        if "/players/" in player_url and not player_url.endswith("/players/"):
            player_urls.add(player_url)

    scores = []
    for score_div in soup.find_all("div", class_="score"):
        scores.append(float(score_div.get_text().strip()))

    handle = io.StringIO()
    handle.write(response.text)
    handle.seek(0)
    dfs = pd.read_html(handle)
    fg = {}
    fga = {}
    offensive_rebounds = {}
    assists = {}
    turnovers = {}
    for df in dfs:
        if df.index.nlevels > 1:
            df.columns = df.columns.get_level_values(1)
        if "Starters" in df.columns.values:
            players = df["Starters"].tolist()
            if "FG" in df.columns.values:
                fgs = df["FG"].tolist()
                for idx, player in enumerate(players):
                    fg[player] = fgs[idx]
            if "FGA" in df.columns.values:
                fgas = df["FGA"].tolist()
                for idx, player in enumerate(players):
                    fga[player] = fgas[idx]
            if "OREB" in df.columns.values:
                orebs = df["OREB"].tolist()
                for idx, player in enumerate(players):
                    offensive_rebounds[player] = orebs[idx]
            if "AST" in df.columns.values:
                asts = df["AST"].tolist()
                for idx, player in enumerate(players):
                    assists[player] = asts[idx]
            if "TOV" in df.columns.values:
                tovs = df["TOV"].tolist()
                for idx, player in enumerate(players):
                    turnovers[player] = tovs[idx]

    scorebox_meta_div = soup.find("div", class_="scorebox_meta")
    if not isinstance(scorebox_meta_div, Tag):
        dt, teams, venue_name = _find_old_dt(
            dfs,
            session,
            soup,
            url,
            league,
            player_urls,
            fg,
            fga,
            offensive_rebounds,
            assists,
            turnovers,
            response,
        )
    else:
        dt, teams, venue_name = _find_new_dt(
            soup,
            scorebox_meta_div,
            url,
            session,
            league,
            player_urls,
            scores,
            fg,
            fga,
            offensive_rebounds,
            assists,
            turnovers,
        )

    season_type = SeasonType.REGULAR
    for h2 in soup.find_all("h2"):
        a = h2.find("a")
        if a is None:
            continue
        season_text = a.get_text().strip()
        match season_text:
            case "Big Sky Conference":
                season_type = SeasonType.REGULAR
            case "Big East Conference":
                season_type = SeasonType.REGULAR
            case "Big West Conference":
                season_type = SeasonType.REGULAR
            case "Big Ten Conference":
                season_type = SeasonType.REGULAR
            case "Mid-American Conference":
                season_type = SeasonType.REGULAR
            case "Horizon League":
                season_type = SeasonType.REGULAR
            case "Atlantic 10 Conference":
                season_type = SeasonType.REGULAR
            case "Mountain West Conference":
                season_type = SeasonType.REGULAR
            case "West Coast Conference":
                season_type = SeasonType.REGULAR
            case "American Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Coastal Athletic Association":
                season_type = SeasonType.REGULAR
            case "Conference USA":
                season_type = SeasonType.REGULAR
            case "America East Conference":
                season_type = SeasonType.REGULAR
            case "Sun Belt Conference":
                season_type = SeasonType.REGULAR
            case "Metro Atlantic Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Atlantic Sun Conference":
                season_type = SeasonType.REGULAR
            case "Ohio Valley Conference":
                season_type = SeasonType.REGULAR
            case "Mid-Eastern Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Big South Conference":
                season_type = SeasonType.REGULAR
            case "Summit League":
                season_type = SeasonType.REGULAR
            case "Western Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Big 12 Conference":
                season_type = SeasonType.REGULAR
            case "Southeastern Conference":
                season_type = SeasonType.REGULAR
            case "Patriot League":
                season_type = SeasonType.REGULAR
            case "Southern Conference":
                season_type = SeasonType.REGULAR
            case "Missouri Valley Conference":
                season_type = SeasonType.REGULAR
            case "Atlantic Coast Conference":
                season_type = SeasonType.REGULAR
            case "Southwest Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Southland Conference":
                season_type = SeasonType.REGULAR
            case "Northeast Conference":
                season_type = SeasonType.REGULAR
            case "Ivy League":
                season_type = SeasonType.REGULAR
            case "NCAA Men's Tournament":
                season_type = SeasonType.REGULAR
            case "Pac-12 Conference":
                season_type = SeasonType.REGULAR
            case "Colonial Athletic Association":
                season_type = SeasonType.REGULAR
            case "Pacific-12 Conference":
                season_type = SeasonType.REGULAR
            case "NCAA Women's Tournament":
                season_type = SeasonType.REGULAR
            case _:
                logging.warning("Unrecognised Season Text: %s", season_text)
        break

    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=create_sportsreference_venue_model(venue_name, session, dt),  # pyright: ignore
        teams=teams,
        league=str(league),
        year=dt.year,
        season_type=season_type,
        end_dt=None,
        attendance=None,
        postponed=None,
        play_off=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsreference_game_model(
    session: requests_cache.CachedSession,
    url: str,
    league: League,
) -> GameModel:
    return _create_sportsreference_game_model(session, url, league)


def create_sportsreference_game_model(
    session: requests_cache.CachedSession,
    url: str,
    league: League,
    dt: datetime.datetime,
) -> GameModel:
    """Create a sports reference game model."""
    if not pytest_is_running.is_running():
        return _cached_create_sportsreference_game_model(session, url, league)
    with session.cache_disabled():
        return _create_sportsreference_game_model(session, url, league)
