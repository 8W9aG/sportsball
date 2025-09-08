"""TennisAbstract game model."""

# pylint: disable=duplicate-code,too-many-statements,too-many-branches,too-many-locals,too-many-nested-blocks
import io
import logging
import os
import urllib
import urllib.parse
import warnings
from urllib.parse import urlparse

import numpy as np
import pandas as pd
import pytest_is_running
from bs4 import BeautifulSoup
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..game_model import VERSION, GameModel
from ..league import League
from .tennisabstract_team_model import create_tennisabstract_team_model
from .tennisabstract_venue_model import create_tennisabstract_venue_model


def _ratio_string(ratio: str) -> float:
    ratio_split = ratio.split("/")
    try:
        return float(ratio_split[0]) / float(ratio_split[1])
    except ZeroDivisionError:
        return 0.0


def _create_tennisabstract_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    version: str,
) -> GameModel:
    warnings.simplefilter("ignore", category=FutureWarning)
    try:
        o = urlparse(url)
        filename = os.path.basename(o.path)
        dt = parse(filename.split("-")[0])

        with session.wayback_disabled():
            response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        venue = None
        for h2 in soup.find_all("h2"):
            game_title = " ".join(h2.get_text().strip().split(":")[0].split()[1:-1])
            venue = create_tennisabstract_venue_model(game_title, session, dt)

        points = [0 for _ in range(2)]
        for b in soup.find_all("b"):
            description = b.get_text().strip()
            for word in description.split():
                if "-" not in word:
                    continue
                word_points = np.array(
                    [int(x.split("(")[0].strip()) for x in word.split("-")]
                )
                points[np.argmax(word_points)] += 1

        ace_percentages = []
        double_fault_percentages = []
        first_serves_ins = []
        first_serve_percentages = []
        second_serve_percentages = []
        break_points_saveds = []
        return_points_won_percentages = []
        winners = []
        winners_fronthands = []
        winners_backhands = []
        unforced_errors = []
        unforced_errors_fronthand = []
        unforced_errors_backhands = []
        serve_points = []
        serves_won = []
        serves_aces = []
        serves_unreturned = []
        serves_forced_error_percentage = []
        serves_won_in_three_shots_or_less = []
        serves_wide_percentage = []
        serves_body_percentage = []
        serves_t_percentage = []
        serves_wide_deuce_percentage = []
        serves_body_deuce_percentage = []
        serves_t_deuce_percentage = []
        serves_wide_ad_percentage = []
        serves_body_ad_percentage = []
        serves_t_ad_percentage = []
        serves_net_percentage = []
        serves_wide_direction_percentage = []
        shots_deep_percentage = []
        shots_deep_wide_percentage = []
        shots_foot_errors_percentage = []
        shots_unknown_percentage = []
        points_won_percentage = []
        for script in soup.find_all("script"):
            script_text = script.get_text().strip()
            if "<table" not in script_text:
                continue
            for line in script_text.split("\n"):
                if "<table" not in line:
                    continue
                html_text = ("'<" + line.split("'<")[-1]).split("';")[0]
                handle = io.StringIO()
                handle.write(html_text)
                handle.seek(0)
                dfs = pd.read_html(handle)
                for df in dfs:
                    cols = set(df.columns.values.tolist())
                    found_total = False
                    for val in df[df.columns.values.tolist()[0]]:
                        if isinstance(val, str) and "Total" in val:
                            found_total = True
                            break
                    if found_total:
                        df = df[
                            df[df.columns.values.tolist()[0]]
                            .str.contains("Total")
                            .fillna(False)
                        ]
                    if "A%" in cols:
                        ace_percentages = [
                            float(x.replace("%", ""))
                            for x in df["A%"].dropna().tolist()
                        ]
                    if "DF%" in cols:
                        double_fault_percentages = [
                            float(x.replace("%", ""))
                            for x in df["DF%"].dropna().tolist()
                        ]
                    if "1stIn" in cols:
                        first_serves_ins = [
                            float(x.split("(")[0].strip().replace("%", ""))
                            for x in df["1stIn"].dropna().tolist()
                        ]
                    if "1st%" in cols:
                        first_serve_percentages = [
                            float(x.replace("%", ""))
                            for x in df["1st%"].dropna().tolist()
                        ]
                    if "2nd%" in cols:
                        second_serve_percentages = [
                            float(x.replace("%", ""))
                            for x in df["2nd%"].dropna().tolist()
                        ]
                    if "BPSaved" in cols:
                        break_points_saveds = [
                            _ratio_string(x) for x in df["BPSaved"].dropna().tolist()
                        ]
                    if "RPW%" in cols:
                        return_points_won_percentages = [
                            float(x.replace("%", ""))
                            for x in df["RPW%"].dropna().tolist()
                        ]
                    if "Winners (FH/BH)" in cols:
                        winners = [
                            int(x.split("(")[0].strip())
                            for x in df["Winners (FH/BH)"].dropna().tolist()
                        ]
                        winners_fronthands = [
                            int(x.split("(")[1].split("/")[0].strip())
                            for x in df["Winners (FH/BH)"].dropna().tolist()
                        ]
                        winners_backhands = [
                            int(
                                x.split("(")[1]
                                .split("/")[1]
                                .strip()
                                .split(")")[0]
                                .strip()
                            )
                            for x in df["Winners (FH/BH)"].dropna().tolist()
                        ]
                    if "UFE (FH/BH)" in cols:
                        unforced_errors = [
                            int(x.split("(")[0].strip())
                            for x in df["UFE (FH/BH)"].dropna().tolist()
                        ]
                        unforced_errors_fronthand = [
                            int(x.split("(")[1].split("/")[0].strip())
                            for x in df["UFE (FH/BH)"].dropna().tolist()
                        ]
                        unforced_errors_backhands = [
                            int(
                                x.split("(")[1]
                                .split("/")[1]
                                .strip()
                                .split(")")[0]
                                .strip()
                            )
                            for x in df["UFE (FH/BH)"].dropna().tolist()
                        ]
                    if "Pts" in cols:
                        serve_points = [int(x) for x in df["Pts"].dropna().tolist()]
                    if "Won---%" in cols:
                        serves_won = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                                .replace("-", "0")
                            )
                            for x in df["Won---%"].dropna().tolist()
                        ]
                    if "Aces---%" in cols:
                        serves_aces = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                                .replace("-", "0")
                            )
                            for x in df["Aces---%"].dropna().tolist()
                        ]
                    if "Unret---%" in cols:
                        serves_unreturned = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Unret---%"].dropna().tolist()
                        ]
                    if "FcdE---%" in cols:
                        serves_forced_error_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                                .replace("-", "0")
                            )
                            for x in df["FcdE---%"].dropna().tolist()
                        ]
                    if "<=3W---%" in cols:
                        serves_won_in_three_shots_or_less = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                                .replace("-", "0")
                            )
                            for x in df["<=3W---%"].dropna().tolist()
                        ]
                    if "Wide---%" in cols:
                        serves_wide_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Wide---%"].dropna().tolist()
                        ]
                    if "Body---%" in cols:
                        serves_body_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Body---%"].dropna().tolist()
                        ]
                    if "T---%" in cols:
                        serves_t_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["T---%"].dropna().tolist()
                        ]
                    if "Dc-Wide-%" in cols:
                        serves_wide_deuce_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Dc-Wide-%"].dropna().tolist()
                        ]
                    if "Dc-Body-%" in cols:
                        serves_body_deuce_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Dc-Body-%"].dropna().tolist()
                        ]
                    if "Dc-T---%" in cols:
                        serves_t_deuce_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Dc-T---%"].dropna().tolist()
                        ]
                    if "Ad-Wide-%" in cols:
                        serves_wide_ad_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Ad-Wide-%"].dropna().tolist()
                        ]
                    if "Ad-Body-%" in cols:
                        serves_body_ad_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Ad-Body-%"].dropna().tolist()
                        ]
                    if "Ad-T---%" in cols:
                        serves_t_ad_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["Ad-T---%"].dropna().tolist()
                        ]
                    if "net---%" in cols:
                        serves_net_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["net---%"].dropna().tolist()
                        ]
                    if "wide---%" in cols:
                        serves_wide_direction_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["wide---%"].dropna().tolist()
                        ]
                    if "deep---%" in cols:
                        shots_deep_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["deep---%"].dropna().tolist()
                        ]
                    if "w&d---%" in cols:
                        shots_deep_wide_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["w&d---%"].dropna().tolist()
                        ]
                    if "foot---%" in cols:
                        shots_foot_errors_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["foot---%"].dropna().tolist()
                        ]
                    if "unk---%" in cols:
                        shots_unknown_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["unk---%"].dropna().tolist()
                        ]
                    if "PtsW----%" in cols:
                        points_won_percentage = [
                            float(
                                x.split("(")[-1]
                                .strip()
                                .replace("%", "")
                                .replace(")", "")
                            )
                            for x in df["PtsW----%"].dropna().tolist()
                        ]

        player_urls = []
        for a in soup.find_all("a"):
            player_url = urllib.parse.urljoin(url, a.get("href"))
            o = urlparse(player_url)
            filename = os.path.basename(o.path)
            if filename.endswith("player.cgi"):
                player_urls.append(player_url)

        return GameModel(
            dt=dt,
            week=None,
            game_number=None,
            venue=venue,
            teams=[
                create_tennisabstract_team_model(
                    session=session,
                    dt=dt,
                    league=league,
                    player_urls=[x],
                    ace_percentages=ace_percentages,
                    double_fault_percentages=double_fault_percentages,
                    first_serves_ins=first_serves_ins,
                    first_serve_percentages=first_serve_percentages,
                    second_serve_percentages=second_serve_percentages,
                    break_points_saveds=break_points_saveds,
                    return_points_won_percentages=return_points_won_percentages,
                    winners=winners,
                    winners_fronthands=winners_fronthands,
                    winners_backhands=winners_backhands,
                    unforced_errors=unforced_errors,
                    unforced_errors_fronthand=unforced_errors_fronthand,
                    unforced_errors_backhand=unforced_errors_backhands,
                    serve_points=serve_points,
                    serves_won=serves_won,
                    serves_aces=serves_aces,
                    serves_unreturned=serves_unreturned,
                    serves_forced_error_percentage=serves_forced_error_percentage,
                    serves_won_in_three_shots_or_less=serves_won_in_three_shots_or_less,
                    serves_wide_percentage=serves_wide_percentage,
                    serves_body_percentage=serves_body_percentage,
                    serves_t_percentage=serves_t_percentage,
                    serves_wide_deuce_percentage=serves_wide_deuce_percentage,
                    serves_body_deuce_percentage=serves_body_deuce_percentage,
                    serves_t_deuce_percentage=serves_t_deuce_percentage,
                    serves_wide_ad_percentage=serves_wide_ad_percentage,
                    serves_body_ad_percentage=serves_body_ad_percentage,
                    serves_t_ad_percentage=serves_t_ad_percentage,
                    serves_net_percentage=serves_net_percentage,
                    serves_wide_direction_percentage=serves_wide_direction_percentage,
                    shots_deep_percentage=shots_deep_percentage,
                    shots_deep_wide_percentage=shots_deep_wide_percentage,
                    shots_foot_errors_percentage=shots_foot_errors_percentage,
                    shots_unknown_percentage=shots_unknown_percentage,
                    points_won_percentage=points_won_percentage,
                    points=float(points[count]),
                )
                for count, x in enumerate(player_urls)
            ],
            league=str(league),
            year=dt.year,
            season_type=None,
            end_dt=None,
            attendance=None,
            postponed=None,
            play_off=None,
            distance=None,
            dividends=[],
            pot=None,
            version=version,
            umpires=[],
        )
    except ValueError as exc:
        logging.warning(str(exc))
        logging.warning("url: %s", url)
        raise exc


@MEMORY.cache(ignore=["session"])
def _cached_create_tennisabstract_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    version: str,
) -> GameModel:
    return _create_tennisabstract_game_model(
        session=session,
        url=url,
        league=league,
        version=version,
    )


def create_tennisabstract_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
) -> GameModel:
    """Create a TennisAbstract game model."""
    if not pytest_is_running.is_running():
        return _cached_create_tennisabstract_game_model(
            session=session,
            url=url,
            league=league,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_tennisabstract_game_model(
            session=session,
            url=url,
            league=league,
            version=VERSION,
        )
