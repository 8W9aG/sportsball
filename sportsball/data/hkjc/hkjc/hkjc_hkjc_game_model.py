"""HKJC HKJC game model."""

# pylint: disable=too-many-nested-blocks,too-many-statements,too-many-branches,too-many-locals,too-many-return-statements,too-many-boolean-expressions,use-maxsplit-arg
import datetime
import io
import logging
import urllib.parse
from urllib.parse import urlparse

import pandas as pd
import pytest_is_running
from bs4 import BeautifulSoup
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...game_model import VERSION, GameModel
from ...league import League
from ...venue_model import VERSION as VENUE_VERSION
from ..position import position_from_str
from .hkjc_hkjc_dividend_model import create_hkjc_hkjc_dividend_model
from .hkjc_hkjc_odds_model import create_hkjc_hkjc_odds_model
from .hkjc_hkjc_team_model import create_hkjc_hkjc_team_model
from .hkjc_hkjc_venue_model import create_hkjc_hkjc_venue_model

RACE_DATE_QUERY_KEY = "RaceDate"
RACE_NUMBER_QUERY_KEY = "RaceNo"
RACE_COURSE_QUERY_KEY = "Racecourse"


def _create_hkjc_hkjc_game_model(
    session: ScrapeSession,
    html: str,
    url: str,
    version: str,
) -> GameModel | None:
    soup = BeautifulSoup(html, "lxml")
    for div in soup.find_all("div", {"id": "errorContainer"}):
        div_text = div.get_text().strip()
        if div_text.lower() == "no information.":
            return None
    for div in soup.find_all("div"):
        div_text = div.get_text().strip()
        if "this race is declared abandoned" in div_text.lower():
            return None
        if "this race is declared void" in div_text.lower():
            return None
        if "information will be released shortly" in div_text.lower():
            return None
        if "unofficial dividends" in div_text.lower():
            return None
        if "this race has been abandoned" in div_text.lower():
            return None

    o = urlparse(url)
    query = urllib.parse.parse_qs(o.query)
    try:
        dt = parse(query[RACE_DATE_QUERY_KEY][0])
    except KeyError as exc:
        logging.warning(url)
        logging.warning(str(exc))
        return None
    game_number = int(query[RACE_NUMBER_QUERY_KEY][0])
    venue_code = query[RACE_COURSE_QUERY_KEY][0]

    handle = io.StringIO()
    handle.write(html)
    handle.seek(0)
    dfs = pd.read_html(handle)
    race_track = None
    distance = None
    pot = None
    teams = []
    dividends = []
    for count, df in enumerate(dfs):
        if count == 1:
            race_track = ""
            try:
                race_track = str(df.iat[2, 2]).split("-", maxsplit=1)[0].strip()
            except IndexError:
                logging.error(url)
                raise

            distance = 0.0
            try:
                distance = float(df.iat[1, 0].split("-")[1].strip().replace("M", ""))
            except IndexError:
                logging.error(html)
                logging.error(url)
                raise
            pot = float(df.iat[3, 0].split()[-1].strip().replace(",", ""))
        elif count == 2:
            for _, row in df.iterrows():
                horse_name = None
                try:
                    horse_name = "(".join(row["Horse"].split("(")[:-1]).strip()
                except KeyError:
                    logging.error(url)
                    continue

                jockey_name = row["Jockey"].split("(")[0].strip()

                trainer_name = None
                try:
                    trainer_name = row["Trainer"].split("(")[0].strip()
                except KeyError:
                    logging.warning("Failed to find trainer name for %s", url)

                place_str = str(row["Pla."]).strip()
                place = None
                if place_str.isnumeric():
                    place = int(place_str)

                jersey = str(row["Horse No."])

                handicap_weight = None
                try:
                    act_wt = str(row["Act. Wt."])
                    if act_wt != "---":
                        handicap_weight = float(act_wt) * 0.453592
                except KeyError:
                    logging.warning("Failed to find handicap weight for %s", url)

                horse_weight = None
                try:
                    horse_weight_str = row["Declar. Horse Wt."]
                    if horse_weight_str != "---":
                        horse_weight = float(horse_weight_str) * 0.453592
                except KeyError:
                    logging.warning("Failed to find horse weight for %s", url)

                starting_position = None
                starting_position_str = str(row["Dr."]).strip()
                if starting_position_str.strip() != "---":
                    starting_position = position_from_str(starting_position_str.strip())

                lbw: float | None = 0.0
                lbw_str = str(row["LBW"]).strip()
                lbw_str = lbw_str.split(" /")[0].strip()
                lbw_str = (
                    lbw_str.replace("/SHS", "")
                    .replace("5/H", "")
                    .replace("/HS", "")
                    .replace("/HD", "")
                    .replace("/NS", "")
                    .replace("/NK", "")
                    .replace("/H", "")
                    .replace("/SH", "")
                    .replace("/N", "")
                    .replace(" N", "")
                    .strip()
                )
                if lbw_str.endswith("/"):
                    lbw_str = lbw_str[:-1]
                if lbw_str in {"HD", "H", "HDS"}:
                    lbw = 2.4 * 0.2
                elif lbw_str in {"SH", "SHS", "SHSS", "HS", "S"}:
                    lbw = 2.4 * 0.2 * 0.5
                elif lbw_str in {"NOSE", "N", "NS"}:
                    lbw = 2.4 * 0.05
                elif lbw_str == "ML":
                    lbw = None
                elif lbw_str == "TO":
                    lbw = 100.0
                elif lbw_str in {"+NOSE", "+N"}:
                    lbw = 2.4 * 0.07
                elif lbw_str == "+SH":
                    lbw = 2.4 * 0.2 * 0.5
                elif lbw_str in {"HD+", "+HD"}:
                    lbw = 2.4 * 0.2 * 1.5
                elif lbw_str == "NK":
                    lbw = 2.4 * 0.4
                elif (
                    lbw_str
                    and lbw_str != "-"
                    and lbw_str != "---"
                    and lbw_str != "nan"
                    and lbw_str != "DNF"
                    and lbw_str != "M.L."
                    and lbw_str != "T.O."
                    and lbw_str != "U/R"
                    and lbw_str != "M. L."
                    and lbw_str != "TNP"
                    and lbw_str != "T.0."
                    and lbw_str != "D.N.F."
                    and lbw_str != "P.U."
                    and lbw_str != "U.R."
                    and lbw_str != "P U."
                    and lbw_str != "T 0."
                    and lbw_str != "3N"
                    and lbw_str != "4H"
                    and lbw_str != "SHDH"
                    and lbw_str != "NDH"
                ):
                    if lbw is not None:
                        if "-" in lbw_str:
                            lbw_horses, lbw_str = lbw_str.split("-")
                            lbw += 2.4 * int(lbw_horses)
                        if "/" in lbw_str:
                            lbw += 2.4 * (1.0 / int(lbw_str.split("/")[-1]))
                        else:
                            lbw += 2.4 * int(lbw_str.split()[0].strip())

                finish_time_str = row["Finish Time"].strip()
                end_dt = None
                if finish_time_str != "---":
                    end_t = datetime.datetime.strptime(finish_time_str, "%M:%S.%f")
                    end_dt = dt + datetime.timedelta(
                        minutes=end_t.minute,
                        seconds=end_t.second,
                        microseconds=end_t.microsecond,
                    )

                win_odds = str(row["Win Odds"]).strip()
                odds = None
                if win_odds != "---" and end_dt is not None:
                    odds = create_hkjc_hkjc_odds_model(float(win_odds), end_dt)

                horse_url = None
                jockey_url = None
                trainer_url = None
                for a in soup.find_all("a", href=True):
                    a_text = a.get_text().strip()
                    if a_text == horse_name:
                        a_url = urllib.parse.urljoin(url, a.get("href"))
                        o = urlparse(a_url)
                        if o.path.endswith("/Horse/Horse.aspx"):
                            horse_url = a_url
                    elif a_text == jockey_name:
                        a_url = urllib.parse.urljoin(url, a.get("href"))
                        o = urlparse(a_url)
                        if o.path.endswith("/Jockey/JockeyProfile.aspx"):
                            jockey_url = a_url
                    elif trainer_name is not None and a_text == trainer_name:
                        a_url = urllib.parse.urljoin(url, a.get("href"))
                        o = urlparse(a_url)
                        if o.path.endswith("/Trainers/TrainerProfile.aspx"):
                            trainer_url = a_url

                if place is None:
                    continue
                if horse_url is None:
                    logging.error(url)
                    logging.error(row)
                    raise ValueError("horse_url is null")

                team_model = create_hkjc_hkjc_team_model(
                    session=session,
                    horse_url=horse_url,
                    jockey_url=jockey_url,
                    trainer_url=trainer_url,
                    points=place,
                    jersey=jersey,
                    handicap_weight=handicap_weight,
                    horse_weight=horse_weight,
                    starting_position=starting_position,
                    lbw=lbw,
                    end_dt=end_dt,
                    odds=[] if odds is None else [odds],
                )
                teams.append(team_model)
        elif count == 3:
            for _, row in df.iterrows():
                row_df = row.to_frame()
                pool = str(row_df.iat[0, 0]).strip()

                try:
                    dividend_str = str(row_df.iat[2, 0]).strip().lower()
                    if dividend_str == "details":
                        continue
                    if dividend_str == "refund":
                        continue
                    if dividend_str == "not win":
                        continue
                    if dividend_str == "detail":
                        continue
                    dividend_str = (
                        dividend_str.split("/", maxsplit=1)[0]
                        .replace(",", "")
                        .replace("$", "")
                        .replace("(", "")
                        .replace(")", "")
                    )
                    if dividend_str == "win":
                        continue
                except IndexError:
                    continue
                dividend = float(dividend_str)

                combination = None
                next_td = False
                for td in soup.find_all("td"):
                    td_text = td.get_text().strip()
                    if td_text == pool:
                        next_td = True
                    else:
                        if next_td:
                            combination = []
                            for combo in td_text.split(","):
                                for sub_combo in combo.split("/"):
                                    combination.append(sub_combo)
                            break
                        next_td = False

                if combination is None:
                    continue

                dividend_model = create_hkjc_hkjc_dividend_model(
                    pool=pool,
                    combination=combination,
                    team_models=teams,
                    dividend=float(dividend),
                )
                dividends.append(dividend_model)

    if race_track is None:
        logging.error(url)
        raise ValueError("race_track is null")

    end_dts = [x.end_dt for x in teams if x.end_dt is not None]
    end_dt = None if not end_dts else min(end_dts)

    return GameModel(
        dt=dt,
        week=None,
        game_number=game_number,
        venue=create_hkjc_hkjc_venue_model(
            session=session,
            dt=dt,
            venue_code=venue_code,
            race_track=race_track,
            version=VENUE_VERSION,
        ),
        teams=teams,
        end_dt=end_dt,
        attendance=None,
        league=str(League.HKJC),
        year=dt.year,
        season_type=None,
        postponed=None,
        play_off=None,
        distance=distance,
        dividends=dividends,
        pot=pot,
        version=version,
        umpires=[],
        best_of=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_hkjc_hkjc_game_model(
    session: ScrapeSession,
    html: str,
    url: str,
    version: str,
) -> GameModel | None:
    """Create a game model from NBA API."""
    return _create_hkjc_hkjc_game_model(
        session=session, html=html, url=url, version=version
    )


def create_hkjc_hkjc_game_model(
    session: ScrapeSession,
    html: str,
    url: str,
) -> GameModel | None:
    """Create a game model from NBA API."""
    if not pytest_is_running.is_running():
        return _cached_create_hkjc_hkjc_game_model(
            session=session, html=html, url=url, version=VERSION
        )
    with session.cache_disabled():
        return _cached_create_hkjc_hkjc_game_model(
            session=session, html=html, url=url, version=VERSION
        )
