"""Sports Reference game model."""

# pylint: disable=too-many-locals,too-many-statements,unused-argument,protected-access,too-many-arguments,use-maxsplit-arg,too-many-branches,duplicate-code,broad-exception-caught,too-many-lines,line-too-long
import datetime
import io
import logging
import math
import os
import re
import urllib.parse
from collections import Counter
from typing import Any
from urllib.parse import urlparse

import datefinder  # type: ignore
import dateutil
import pandas as pd
import pytest_is_running
import requests
from bs4 import BeautifulSoup, Tag
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..game_model import VERSION, GameModel
from ..league import League
from ..season_type import SeasonType
from ..team_model import TeamModel
from .sportsreference_team_model import create_sportsreference_team_model
from .sportsreference_umpire_model import create_sportsreference_umpire_model
from .sportsreference_venue_model import create_sportsreference_venue_model

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
_NUMBER_PARENTHESIS_PATTERN = r"\(\d+\)"
_NON_WAYBACK_URLS: set[str] = {
    "https://www.sports-reference.com/cfb/boxscores/2025-01-20-notre-dame.html",
    "https://www.pro-football-reference.com/boxscores/202502090phi.htm",
    "https://www.sports-reference.com/cfb/boxscores/2025-01-09-penn-state.html",
    "https://www.sports-reference.com/cfb/boxscores/2024-12-31-alabama.html",
    "https://www.hockey-reference.com/boxscores/202410050NJD.html",
    "https://www.hockey-reference.com/boxscores/202410040BUF.html",
    "https://www.hockey-reference.com/boxscores/202311190MIN.html",
    "https://www.hockey-reference.com/boxscores/202311180OTT.html",
    "https://www.hockey-reference.com/boxscores/202311170DET.html",
    "https://www.hockey-reference.com/boxscores/202311160OTT.html",
    "https://www.hockey-reference.com/boxscores/202210080SJS.html",
    "https://www.hockey-reference.com/boxscores/202210070NSH.html",
    "https://www.baseball-reference.com/boxes/OAK/OAK202405081.shtml",
    "https://www.hockey-reference.com/boxscores/202001010DAL.html",
    "https://www.baseball-reference.com/boxes/CLE/CLE202108220.shtml",
    "https://www.hockey-reference.com/boxscores/202304130NSH.html",
}


def _find_old_dt(
    dfs: list[pd.DataFrame],
    session: ScrapeSession,
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
    positions_validator: dict[str, str],
    minutes_played: dict[str, datetime.timedelta],
    three_point_field_goals: dict[str, int],
    three_point_field_goals_attempted: dict[str, int],
    free_throws: dict[str, int],
    free_throws_attempted: dict[str, int],
    defensive_rebounds: dict[str, int],
    steals: dict[str, int],
    blocks: dict[str, int],
    personal_fouls: dict[str, int],
    player_points: dict[str, int],
    game_scores: dict[str, float],
    point_differentials: dict[str, int],
    goals: dict[str, int],
    penalties_in_minutes: dict[str, datetime.timedelta],
    even_strength_goals: dict[str, int],
    power_play_goals: dict[str, int],
    short_handed_goals: dict[str, int],
    game_winning_goals: dict[str, int],
    even_strength_assists: dict[str, int],
    power_play_assists: dict[str, int],
    short_handed_assists: dict[str, int],
    shots_on_goal: dict[str, int],
    shooting_percentage: dict[str, float],
    shifts: dict[str, int],
    time_on_ice: dict[str, datetime.timedelta],
    decision: dict[str, str],
    goals_against: dict[str, int],
    shots_against: dict[str, int],
    saves: dict[str, int],
    save_percentage: dict[str, float],
    shutouts: dict[str, int],
    individual_corsi_for_events: dict[str, int],
    on_shot_ice_for_events: dict[str, int],
    on_shot_ice_against_events: dict[str, int],
    corsi_for_percentage: dict[str, float],
    relative_corsi_for_percentage: dict[str, float],
    offensive_zone_starts: dict[str, int],
    defensive_zone_starts: dict[str, int],
    offensive_zone_start_percentage: dict[str, float],
    hits: dict[str, int],
    true_shooting_percentage: dict[str, float],
    at_bats: dict[str, int],
    runs_scored: dict[str, int],
    runs_batted_in: dict[str, int],
    bases_on_balls: dict[str, int],
    strikeouts: dict[str, int],
    plate_appearances: dict[str, int],
    hits_at_bats: dict[str, float],
    obp: dict[str, float],
    slg: dict[str, float],
    ops: dict[str, float],
    pitches: dict[str, int],
    strikes: dict[str, int],
    win_probability_added: dict[str, float],
    average_leverage_index: dict[str, float],
    wpa_plus: dict[str, float],
    wpa_minus: dict[str, float],
    cwpa: dict[str, float],
    acli: dict[str, float],
    re24: dict[str, float],
    putouts: dict[str, int],
    innings_pitched: dict[str, int],
    earned_runs: dict[str, int],
    home_runs: dict[str, int],
    era: dict[str, float],
    batters_faced: dict[str, int],
    strikes_by_contact: dict[str, int],
    strikes_swinging: dict[str, int],
    strikes_looking: dict[str, int],
    ground_balls: dict[str, int],
    fly_balls: dict[str, int],
    line_drives: dict[str, int],
    inherited_runners: dict[str, int],
    inherited_scores: dict[str, int],
    effective_field_goal_percentage: dict[str, float],
    penalty_kicks_made: dict[str, int],
    penalty_kicks_attempted: dict[str, int],
    shots_total: dict[str, int],
    shots_on_target: dict[str, int],
    yellow_cards: dict[str, int],
    red_cards: dict[str, int],
    touches: dict[str, int],
    expected_goals: dict[str, float],
    non_penalty_expected_goals: dict[str, float],
    expected_assisted_goals: dict[str, float],
    shot_creating_actions: dict[str, int],
    goal_creating_actions: dict[str, int],
    passes_completed: dict[str, int],
    passes_attempted: dict[str, int],
    pass_completion: dict[str, int],
    progressive_passes: dict[str, int],
    carries: dict[str, int],
    progressive_carries: dict[str, int],
    take_ons_attempted: dict[str, int],
    successful_take_ons: dict[str, int],
    total_passing_distance: dict[str, int],
    progressive_passing_distance: dict[str, int],
    passes_completed_short: dict[str, int],
    passes_attempted_short: dict[str, int],
    pass_completion_short: dict[str, int],
    passes_completed_medium: dict[str, int],
    passes_attempted_medium: dict[str, int],
    pass_completion_medium: dict[str, int],
    passes_completed_long: dict[str, int],
    passes_attempted_long: dict[str, int],
    pass_completion_long: dict[str, int],
    expected_assists: dict[str, float],
    key_passes: dict[str, int],
    passes_into_final_third: dict[str, int],
    passes_into_penalty_area: dict[str, int],
    crosses_into_penalty_area: dict[str, int],
    live_ball_passes: dict[str, int],
    dead_ball_passes: dict[str, int],
    passes_from_free_kicks: dict[str, int],
    through_balls: dict[str, int],
    switches: dict[str, int],
    crosses: dict[str, int],
    throw_ins_taken: dict[str, int],
    corner_kicks: dict[str, int],
    inswinging_corner_kicks: dict[str, int],
    outswinging_corner_kicks: dict[str, int],
    straight_corner_kicks: dict[str, int],
    passes_offside: dict[str, int],
    passes_blocked: dict[str, int],
    tackles_won: dict[str, int],
    tackles_in_defensive_third: dict[str, int],
    tackles_in_middle_third: dict[str, int],
    tackles_in_attacking_third: dict[str, int],
    dribblers_tackled: dict[str, int],
    dribbles_challenged: dict[str, int],
    percent_of_dribblers_tackled: dict[str, float],
    challenges_lost: dict[str, int],
    shots_blocked: dict[str, int],
    tackles_plus_interceptions: dict[str, int],
    errors: dict[str, int],
    touches_in_defensive_penalty_area: dict[str, int],
    touches_in_defensive_third: dict[str, int],
    touches_in_middle_third: dict[str, int],
    touches_in_attacking_third: dict[str, int],
    touches_in_attacking_penalty_area: dict[str, int],
    live_ball_touches: dict[str, int],
    successful_take_on_percentage: dict[str, float],
    times_tackled_during_take_ons: dict[str, int],
    tackled_during_take_ons_percentage: dict[str, int],
    total_carrying_distance: dict[str, int],
    progressive_carrying_distance: dict[str, int],
    carries_into_final_third: dict[str, int],
    carries_into_penalty_area: dict[str, int],
    miscontrols: dict[str, int],
    dispossessed: dict[str, int],
    passes_received: dict[str, int],
    progressive_passes_received: dict[str, int],
    second_yellow_card: dict[str, int],
    fouls_committed: dict[str, int],
    fouls_drawn: dict[str, int],
    offsides: dict[str, int],
    penalty_kicks_won: dict[str, int],
    penalty_kicks_conceded: dict[str, int],
    own_goals: dict[str, int],
    ball_recoveries: dict[str, int],
    aerials_won: dict[str, int],
    aerials_lost: dict[str, int],
    percentage_of_aerials_won: dict[str, float],
    shots_on_target_against: dict[str, int],
    post_shot_expected_goals: dict[str, int],
    passes_attempted_minus_goal_kicks: dict[str, int],
    throws_attempted: dict[str, int],
    percentage_of_passes_that_were_launched: dict[str, float],
    average_pass_length: dict[str, float],
    goal_kicks_attempted: dict[str, int],
    percentage_of_goal_kicks_that_were_launched: dict[str, float],
    average_goal_kick_length: dict[str, float],
    crosses_faced: dict[str, int],
    crosses_stopped: dict[str, int],
    percentage_crosses_stopped: dict[str, float],
    defensive_actions_outside_penalty_area: dict[str, int],
    average_distance_of_defensive_actions: dict[str, float],
    three_point_attempt_rate: dict[str, float],
    tackles: dict[str, int],
    interceptions: dict[str, int],
    clearances: dict[str, int],
    free_throw_attempt_rate: dict[str, float],
    offensive_rebound_percentage: dict[str, float],
    defensive_rebound_percentage: dict[str, float],
    total_rebound_percentage: dict[str, float],
    assist_percentage: dict[str, float],
    steal_percentage: dict[str, float],
    block_percentage: dict[str, float],
    turnover_percentage: dict[str, float],
    usage_percentage: dict[str, float],
    offensive_rating: dict[str, int],
    defensive_rating: dict[str, int],
    box_plus_minus: dict[str, float],
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
            team_name = " ".join(
                re.sub(_NUMBER_PARENTHESIS_PATTERN, "", team_name).split()
            ).strip()
            team_a = soup.find("a", text=team_name, href=True)
            if not isinstance(team_a, Tag):
                logging.error(team_name)
                logging.error(response.url)
                logging.error(response.text)
                raise ValueError("team_a is not a tag.")
            team_url = urllib.parse.urljoin(url, str(team_a.get("href")))
            if dt is None:
                raise ValueError("dt is null.")
            teams.append(
                create_sportsreference_team_model(
                    session=session,
                    url=team_url,
                    dt=dt,
                    league=league,
                    player_urls=player_urls,
                    points=points,
                    fg=fg,
                    fga=fga,
                    offensive_rebounds=offensive_rebounds,
                    assists=assists,
                    turnovers=turnovers,
                    team_name=team_name,
                    positions_validator=positions_validator,
                    minutes_played=minutes_played,
                    three_point_field_goals=three_point_field_goals,
                    three_point_field_goals_attempted=three_point_field_goals_attempted,
                    free_throws=free_throws,
                    free_throws_attempted=free_throws_attempted,
                    defensive_rebounds=defensive_rebounds,
                    steals=steals,
                    blocks=blocks,
                    personal_fouls=personal_fouls,
                    player_points=player_points,
                    game_scores=game_scores,
                    point_differentials=point_differentials,
                    goals=goals,
                    penalties_in_minutes=penalties_in_minutes,
                    even_strength_goals=even_strength_goals,
                    power_play_goals=power_play_goals,
                    short_handed_goals=short_handed_goals,
                    game_winning_goals=game_winning_goals,
                    even_strength_assists=even_strength_assists,
                    power_play_assists=power_play_assists,
                    short_handed_assists=short_handed_assists,
                    shots_on_goal=shots_on_goal,
                    shooting_percentage=shooting_percentage,
                    shifts=shifts,
                    time_on_ice=time_on_ice,
                    decision=decision,
                    goals_against=goals_against,
                    shots_against=shots_against,
                    saves=saves,
                    save_percentage=save_percentage,
                    shutouts=shutouts,
                    individual_corsi_for_events=individual_corsi_for_events,
                    on_shot_ice_for_events=on_shot_ice_for_events,
                    on_shot_ice_against_events=on_shot_ice_against_events,
                    corsi_for_percentage=corsi_for_percentage,
                    relative_corsi_for_percentage=relative_corsi_for_percentage,
                    offensive_zone_starts=offensive_zone_starts,
                    defensive_zone_starts=defensive_zone_starts,
                    offensive_zone_start_percentage=offensive_zone_start_percentage,
                    hits=hits,
                    true_shooting_percentage=true_shooting_percentage,
                    at_bats=at_bats,
                    runs_scored=runs_scored,
                    runs_batted_in=runs_batted_in,
                    bases_on_balls=bases_on_balls,
                    strikeouts=strikeouts,
                    plate_appearances=plate_appearances,
                    hits_at_bats=hits_at_bats,
                    obp=obp,
                    slg=slg,
                    ops=ops,
                    pitches=pitches,
                    strikes=strikes,
                    win_probability_added=win_probability_added,
                    average_leverage_index=average_leverage_index,
                    wpa_plus=wpa_plus,
                    wpa_minus=wpa_minus,
                    cwpa=cwpa,
                    acli=acli,
                    re24=re24,
                    putouts=putouts,
                    innings_pitched=innings_pitched,
                    earned_runs=earned_runs,
                    home_runs=home_runs,
                    era=era,
                    batters_faced=batters_faced,
                    strikes_by_contact=strikes_by_contact,
                    strikes_swinging=strikes_swinging,
                    strikes_looking=strikes_looking,
                    ground_balls=ground_balls,
                    fly_balls=fly_balls,
                    line_drives=line_drives,
                    inherited_runners=inherited_runners,
                    inherited_scores=inherited_scores,
                    effective_field_goal_percentage=effective_field_goal_percentage,
                    penalty_kicks_made=penalty_kicks_made,
                    penalty_kicks_attempted=penalty_kicks_attempted,
                    shots_total=shots_total,
                    shots_on_target=shots_on_target,
                    yellow_cards=yellow_cards,
                    red_cards=red_cards,
                    touches=touches,
                    expected_goals=expected_goals,
                    non_penalty_expected_goals=non_penalty_expected_goals,
                    expected_assisted_goals=expected_assisted_goals,
                    shot_creating_actions=shot_creating_actions,
                    goal_creating_actions=goal_creating_actions,
                    passes_completed=passes_completed,
                    passes_attempted=passes_attempted,
                    pass_completion=pass_completion,
                    progressive_passes=progressive_passes,
                    carries=carries,
                    progressive_carries=progressive_carries,
                    take_ons_attempted=take_ons_attempted,
                    successful_take_ons=successful_take_ons,
                    total_passing_distance=total_passing_distance,
                    progressive_passing_distance=progressive_passing_distance,
                    passes_completed_short=passes_completed_short,
                    passes_attempted_short=passes_attempted_short,
                    pass_completion_short=pass_completion_short,
                    passes_completed_medium=passes_completed_medium,
                    passes_attempted_medium=passes_attempted_medium,
                    pass_completion_medium=pass_completion_medium,
                    passes_completed_long=passes_completed_long,
                    passes_attempted_long=passes_attempted_long,
                    pass_completion_long=pass_completion_long,
                    expected_assists=expected_assists,
                    key_passes=key_passes,
                    passes_into_final_third=passes_into_final_third,
                    passes_into_penalty_area=passes_into_penalty_area,
                    crosses_into_penalty_area=crosses_into_penalty_area,
                    live_ball_passes=live_ball_passes,
                    dead_ball_passes=dead_ball_passes,
                    passes_from_free_kicks=passes_from_free_kicks,
                    through_balls=through_balls,
                    switches=switches,
                    crosses=crosses,
                    throw_ins_taken=throw_ins_taken,
                    corner_kicks=corner_kicks,
                    inswinging_corner_kicks=inswinging_corner_kicks,
                    outswinging_corner_kicks=outswinging_corner_kicks,
                    straight_corner_kicks=straight_corner_kicks,
                    passes_offside=passes_offside,
                    passes_blocked=passes_blocked,
                    tackles_won=tackles_won,
                    tackles_in_defensive_third=tackles_in_defensive_third,
                    tackles_in_middle_third=tackles_in_middle_third,
                    tackles_in_attacking_third=tackles_in_attacking_third,
                    dribblers_tackled=dribblers_tackled,
                    dribbles_challenged=dribbles_challenged,
                    percent_of_dribblers_tackled=percent_of_dribblers_tackled,
                    challenges_lost=challenges_lost,
                    shots_blocked=shots_blocked,
                    tackles_plus_interceptions=tackles_plus_interceptions,
                    errors=errors,
                    touches_in_defensive_penalty_area=touches_in_defensive_penalty_area,
                    touches_in_defensive_third=touches_in_defensive_third,
                    touches_in_middle_third=touches_in_middle_third,
                    touches_in_attacking_third=touches_in_attacking_third,
                    touches_in_attacking_penalty_area=touches_in_attacking_penalty_area,
                    live_ball_touches=live_ball_touches,
                    successful_take_on_percentage=successful_take_on_percentage,
                    times_tackled_during_take_ons=times_tackled_during_take_ons,
                    tackled_during_take_ons_percentage=tackled_during_take_ons_percentage,
                    total_carrying_distance=total_carrying_distance,
                    progressive_carrying_distance=progressive_carrying_distance,
                    carries_into_final_third=carries_into_final_third,
                    carries_into_penalty_area=carries_into_penalty_area,
                    miscontrols=miscontrols,
                    dispossessed=dispossessed,
                    passes_received=passes_received,
                    progressive_passes_received=progressive_passes_received,
                    second_yellow_card=second_yellow_card,
                    fouls_committed=fouls_committed,
                    fouls_drawn=fouls_drawn,
                    offsides=offsides,
                    penalty_kicks_won=penalty_kicks_won,
                    penalty_kicks_conceded=penalty_kicks_conceded,
                    own_goals=own_goals,
                    ball_recoveries=ball_recoveries,
                    aerials_won=aerials_won,
                    aerials_lost=aerials_lost,
                    percentage_of_aerials_won=percentage_of_aerials_won,
                    shots_on_target_against=shots_on_target_against,
                    post_shot_expected_goals=post_shot_expected_goals,
                    passes_attempted_minus_goal_kicks=passes_attempted_minus_goal_kicks,
                    throws_attempted=throws_attempted,
                    percentage_of_passes_that_were_launched=percentage_of_passes_that_were_launched,
                    average_pass_length=average_pass_length,
                    goal_kicks_attempted=goal_kicks_attempted,
                    percentage_of_goal_kicks_that_were_launched=percentage_of_goal_kicks_that_were_launched,
                    average_goal_kick_length=average_goal_kick_length,
                    crosses_faced=crosses_faced,
                    crosses_stopped=crosses_stopped,
                    percentage_crosses_stopped=percentage_crosses_stopped,
                    defensive_actions_outside_penalty_area=defensive_actions_outside_penalty_area,
                    average_distance_of_defensive_actions=average_distance_of_defensive_actions,
                    three_point_attempt_rate=three_point_attempt_rate,
                    tackles=tackles,
                    interceptions=interceptions,
                    clearances=clearances,
                    free_throw_attempt_rate=free_throw_attempt_rate,
                    offensive_rebound_percentage=offensive_rebound_percentage,
                    defensive_rebound_percentage=defensive_rebound_percentage,
                    total_rebound_percentage=total_rebound_percentage,
                    assist_percentage=assist_percentage,
                    steal_percentage=steal_percentage,
                    block_percentage=block_percentage,
                    turnover_percentage=turnover_percentage,
                    usage_percentage=usage_percentage,
                    offensive_rating=offensive_rating,
                    defensive_rating=defensive_rating,
                    box_plus_minus=box_plus_minus,
                )
            )

    dt = None
    venue_name = None
    for df in dfs:
        if len(df) == 2:
            test_row = df.iat[0, 0]
            test_row_2 = df.iat[1, 0]
            if isinstance(test_row, float):
                continue

            try:
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
            except TypeError as exc:
                logging.error(test_row)
                logging.error(response.url)
                logging.error(response.text)
                raise exc

    if dt is None:
        title_tag = soup.find("title")
        if not isinstance(title_tag, Tag):
            raise ValueError("title_tag is not a tag.")
        title = title_tag.get_text().strip().split("|")[0].strip()
        date = title[title.find(",") :].strip()
        dt = parse(date)
        for df in dfs:
            test_row = df.iat[0, 0]
            if isinstance(test_row, float):
                continue
            try:
                if "Prev Game" in test_row:
                    _process_team_row(df)
                    break
            except TypeError as exc:
                logging.error(test_row)
                logging.error(response.url)
                logging.error(response.text)
                raise exc

    if venue_name is not None and not venue_name.replace(",", "").strip():
        venue_name = None

    if dt is None:
        raise ValueError("dt is null.")
    if venue_name is None:
        logging.warning("venue_name is null for %s.", url)

    return (dt, teams, venue_name)


def _find_new_dt(
    soup: BeautifulSoup,
    scorebox_meta_div: Tag,
    url: str,
    session: ScrapeSession,
    league: League,
    player_urls: set[str],
    scores: list[float],
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
    positions_validator: dict[str, str],
    minutes_played: dict[str, datetime.timedelta],
    three_point_field_goals: dict[str, int],
    three_point_field_goals_attempted: dict[str, int],
    free_throws: dict[str, int],
    free_throws_attempted: dict[str, int],
    defensive_rebounds: dict[str, int],
    steals: dict[str, int],
    blocks: dict[str, int],
    personal_fouls: dict[str, int],
    player_points: dict[str, int],
    game_scores: dict[str, float],
    point_differentials: dict[str, int],
    goals: dict[str, int],
    penalties_in_minutes: dict[str, datetime.timedelta],
    even_strength_goals: dict[str, int],
    power_play_goals: dict[str, int],
    short_handed_goals: dict[str, int],
    game_winning_goals: dict[str, int],
    even_strength_assists: dict[str, int],
    power_play_assists: dict[str, int],
    short_handed_assists: dict[str, int],
    shots_on_goal: dict[str, int],
    shooting_percentage: dict[str, float],
    shifts: dict[str, int],
    time_on_ice: dict[str, datetime.timedelta],
    decision: dict[str, str],
    goals_against: dict[str, int],
    shots_against: dict[str, int],
    saves: dict[str, int],
    save_percentage: dict[str, float],
    shutouts: dict[str, int],
    individual_corsi_for_events: dict[str, int],
    on_shot_ice_for_events: dict[str, int],
    on_shot_ice_against_events: dict[str, int],
    corsi_for_percentage: dict[str, float],
    relative_corsi_for_percentage: dict[str, float],
    offensive_zone_starts: dict[str, int],
    defensive_zone_starts: dict[str, int],
    offensive_zone_start_percentage: dict[str, float],
    hits: dict[str, int],
    true_shooting_percentage: dict[str, float],
    at_bats: dict[str, int],
    runs_scored: dict[str, int],
    runs_batted_in: dict[str, int],
    bases_on_balls: dict[str, int],
    strikeouts: dict[str, int],
    plate_appearances: dict[str, int],
    hits_at_bats: dict[str, float],
    obp: dict[str, float],
    slg: dict[str, float],
    ops: dict[str, float],
    pitches: dict[str, int],
    strikes: dict[str, int],
    win_probability_added: dict[str, float],
    average_leverage_index: dict[str, float],
    wpa_plus: dict[str, float],
    wpa_minus: dict[str, float],
    cwpa: dict[str, float],
    acli: dict[str, float],
    re24: dict[str, float],
    putouts: dict[str, int],
    innings_pitched: dict[str, int],
    earned_runs: dict[str, int],
    home_runs: dict[str, int],
    era: dict[str, float],
    batters_faced: dict[str, int],
    strikes_by_contact: dict[str, int],
    strikes_swinging: dict[str, int],
    strikes_looking: dict[str, int],
    ground_balls: dict[str, int],
    fly_balls: dict[str, int],
    line_drives: dict[str, int],
    inherited_runners: dict[str, int],
    inherited_scores: dict[str, int],
    effective_field_goal_percentage: dict[str, float],
    penalty_kicks_made: dict[str, int],
    penalty_kicks_attempted: dict[str, int],
    shots_total: dict[str, int],
    shots_on_target: dict[str, int],
    yellow_cards: dict[str, int],
    red_cards: dict[str, int],
    touches: dict[str, int],
    expected_goals: dict[str, float],
    non_penalty_expected_goals: dict[str, float],
    expected_assisted_goals: dict[str, float],
    shot_creating_actions: dict[str, int],
    goal_creating_actions: dict[str, int],
    passes_completed: dict[str, int],
    passes_attempted: dict[str, int],
    pass_completion: dict[str, int],
    progressive_passes: dict[str, int],
    carries: dict[str, int],
    progressive_carries: dict[str, int],
    take_ons_attempted: dict[str, int],
    successful_take_ons: dict[str, int],
    total_passing_distance: dict[str, int],
    progressive_passing_distance: dict[str, int],
    passes_completed_short: dict[str, int],
    passes_attempted_short: dict[str, int],
    pass_completion_short: dict[str, int],
    passes_completed_medium: dict[str, int],
    passes_attempted_medium: dict[str, int],
    pass_completion_medium: dict[str, int],
    passes_completed_long: dict[str, int],
    passes_attempted_long: dict[str, int],
    pass_completion_long: dict[str, int],
    expected_assists: dict[str, float],
    key_passes: dict[str, int],
    passes_into_final_third: dict[str, int],
    passes_into_penalty_area: dict[str, int],
    crosses_into_penalty_area: dict[str, int],
    live_ball_passes: dict[str, int],
    dead_ball_passes: dict[str, int],
    passes_from_free_kicks: dict[str, int],
    through_balls: dict[str, int],
    switches: dict[str, int],
    crosses: dict[str, int],
    throw_ins_taken: dict[str, int],
    corner_kicks: dict[str, int],
    inswinging_corner_kicks: dict[str, int],
    outswinging_corner_kicks: dict[str, int],
    straight_corner_kicks: dict[str, int],
    passes_offside: dict[str, int],
    passes_blocked: dict[str, int],
    tackles_won: dict[str, int],
    tackles_in_defensive_third: dict[str, int],
    tackles_in_middle_third: dict[str, int],
    tackles_in_attacking_third: dict[str, int],
    dribblers_tackled: dict[str, int],
    dribbles_challenged: dict[str, int],
    percent_of_dribblers_tackled: dict[str, float],
    challenges_lost: dict[str, int],
    shots_blocked: dict[str, int],
    tackles_plus_interceptions: dict[str, int],
    errors: dict[str, int],
    touches_in_defensive_penalty_area: dict[str, int],
    touches_in_defensive_third: dict[str, int],
    touches_in_middle_third: dict[str, int],
    touches_in_attacking_third: dict[str, int],
    touches_in_attacking_penalty_area: dict[str, int],
    live_ball_touches: dict[str, int],
    successful_take_on_percentage: dict[str, float],
    times_tackled_during_take_ons: dict[str, int],
    tackled_during_take_ons_percentage: dict[str, int],
    total_carrying_distance: dict[str, int],
    progressive_carrying_distance: dict[str, int],
    carries_into_final_third: dict[str, int],
    carries_into_penalty_area: dict[str, int],
    miscontrols: dict[str, int],
    dispossessed: dict[str, int],
    passes_received: dict[str, int],
    progressive_passes_received: dict[str, int],
    second_yellow_card: dict[str, int],
    fouls_committed: dict[str, int],
    fouls_drawn: dict[str, int],
    offsides: dict[str, int],
    penalty_kicks_won: dict[str, int],
    penalty_kicks_conceded: dict[str, int],
    own_goals: dict[str, int],
    ball_recoveries: dict[str, int],
    aerials_won: dict[str, int],
    aerials_lost: dict[str, int],
    percentage_of_aerials_won: dict[str, float],
    shots_on_target_against: dict[str, int],
    post_shot_expected_goals: dict[str, int],
    passes_attempted_minus_goal_kicks: dict[str, int],
    throws_attempted: dict[str, int],
    percentage_of_passes_that_were_launched: dict[str, float],
    average_pass_length: dict[str, float],
    goal_kicks_attempted: dict[str, int],
    percentage_of_goal_kicks_that_were_launched: dict[str, float],
    average_goal_kick_length: dict[str, float],
    crosses_faced: dict[str, int],
    crosses_stopped: dict[str, int],
    percentage_crosses_stopped: dict[str, float],
    defensive_actions_outside_penalty_area: dict[str, int],
    average_distance_of_defensive_actions: dict[str, float],
    three_point_attempt_rate: dict[str, float],
    tackles: dict[str, int],
    interceptions: dict[str, int],
    clearances: dict[str, int],
    free_throw_attempt_rate: dict[str, float],
    offensive_rebound_percentage: dict[str, float],
    defensive_rebound_percentage: dict[str, float],
    total_rebound_percentage: dict[str, float],
    assist_percentage: dict[str, float],
    steal_percentage: dict[str, float],
    block_percentage: dict[str, float],
    turnover_percentage: dict[str, float],
    usage_percentage: dict[str, float],
    offensive_rating: dict[str, int],
    defensive_rating: dict[str, int],
    box_plus_minus: dict[str, float],
) -> tuple[datetime.datetime, list[TeamModel], str]:
    in_divs = scorebox_meta_div.find_all("div")
    current_in_div_idx = 0
    in_div = in_divs[current_in_div_idx]
    in_div_text = in_div.get_text().strip()
    current_in_div_idx += 1
    if "Tournament" in in_div_text:
        in_div_text = in_divs[1].get_text().strip()
        current_in_div_idx += 1
    dt = None
    try:
        dt = parse(in_div_text)
    except dateutil.parser._parser.ParserError as exc:  # type: ignore
        matches = datefinder.find_dates(scorebox_meta_div.get_text(separator="\n"))
        for match in matches:
            if isinstance(match, datetime.datetime):
                dt = match
                break
        if dt is None:
            logging.error("Failed to parse date for URL: %s", url)
            raise exc
    venue_div = in_divs[current_in_div_idx]
    venue_name = venue_div.get_text().strip()
    if league == League.NCAAF:
        filepath = url.split("/")[-1]
        filename, _ = os.path.splitext(filepath)
        venue_name = "-".join(filename.split("-")[3:])
    else:
        for in_div in in_divs:
            in_div_text = in_div.get_text()
            if "Arena:" in in_div_text:
                venue_name = in_div_text.replace("Arena: ", "").strip()
            elif "Stadium:" in in_div_text:
                venue_name = in_div_text.replace("Stadium: ", "").strip()
            elif "Venue:" in in_div_text:
                venue_name = in_div_text.replace("Venue: ", "").strip()

    scorebox_div = soup.find("div", class_="scorebox")
    if not isinstance(scorebox_div, Tag):
        raise ValueError("scorebox_div is not a Tag.")

    teams: list[TeamModel] = []
    for a in scorebox_div.find_all("a"):
        team_url = urllib.parse.urljoin(url, a.get("href"))
        if "/schools/" in team_url or "/teams/" in team_url:
            teams.append(
                create_sportsreference_team_model(
                    session=session,
                    url=team_url,
                    dt=dt,
                    league=league,
                    player_urls=player_urls,
                    points=scores[len(teams)],
                    fg=fg,
                    fga=fga,
                    offensive_rebounds=offensive_rebounds,
                    assists=assists,
                    turnovers=turnovers,
                    team_name=a.get_text().strip(),
                    positions_validator=positions_validator,
                    minutes_played=minutes_played,
                    three_point_field_goals=three_point_field_goals,
                    three_point_field_goals_attempted=three_point_field_goals_attempted,
                    free_throws=free_throws,
                    free_throws_attempted=free_throws_attempted,
                    defensive_rebounds=defensive_rebounds,
                    steals=steals,
                    blocks=blocks,
                    personal_fouls=personal_fouls,
                    player_points=player_points,
                    game_scores=game_scores,
                    point_differentials=point_differentials,
                    goals=goals,
                    penalties_in_minutes=penalties_in_minutes,
                    even_strength_goals=even_strength_goals,
                    power_play_goals=power_play_goals,
                    short_handed_goals=short_handed_goals,
                    game_winning_goals=game_winning_goals,
                    even_strength_assists=even_strength_assists,
                    power_play_assists=power_play_assists,
                    short_handed_assists=short_handed_assists,
                    shots_on_goal=shots_on_goal,
                    shooting_percentage=shooting_percentage,
                    shifts=shifts,
                    time_on_ice=time_on_ice,
                    decision=decision,
                    goals_against=goals_against,
                    shots_against=shots_against,
                    saves=saves,
                    save_percentage=save_percentage,
                    shutouts=shutouts,
                    individual_corsi_for_events=individual_corsi_for_events,
                    on_shot_ice_for_events=on_shot_ice_for_events,
                    on_shot_ice_against_events=on_shot_ice_against_events,
                    corsi_for_percentage=corsi_for_percentage,
                    relative_corsi_for_percentage=relative_corsi_for_percentage,
                    offensive_zone_starts=offensive_zone_starts,
                    defensive_zone_starts=defensive_zone_starts,
                    offensive_zone_start_percentage=offensive_zone_start_percentage,
                    hits=hits,
                    true_shooting_percentage=true_shooting_percentage,
                    at_bats=at_bats,
                    runs_scored=runs_scored,
                    runs_batted_in=runs_batted_in,
                    bases_on_balls=bases_on_balls,
                    strikeouts=strikeouts,
                    plate_appearances=plate_appearances,
                    hits_at_bats=hits_at_bats,
                    obp=obp,
                    slg=slg,
                    ops=ops,
                    pitches=pitches,
                    strikes=strikes,
                    win_probability_added=win_probability_added,
                    average_leverage_index=average_leverage_index,
                    wpa_plus=wpa_plus,
                    wpa_minus=wpa_minus,
                    cwpa=cwpa,
                    acli=acli,
                    re24=re24,
                    putouts=putouts,
                    innings_pitched=innings_pitched,
                    earned_runs=earned_runs,
                    home_runs=home_runs,
                    era=era,
                    batters_faced=batters_faced,
                    strikes_by_contact=strikes_by_contact,
                    strikes_swinging=strikes_swinging,
                    strikes_looking=strikes_looking,
                    ground_balls=ground_balls,
                    fly_balls=fly_balls,
                    line_drives=line_drives,
                    inherited_runners=inherited_runners,
                    inherited_scores=inherited_scores,
                    effective_field_goal_percentage=effective_field_goal_percentage,
                    penalty_kicks_made=penalty_kicks_made,
                    penalty_kicks_attempted=penalty_kicks_attempted,
                    shots_total=shots_total,
                    shots_on_target=shots_on_target,
                    yellow_cards=yellow_cards,
                    red_cards=red_cards,
                    touches=touches,
                    expected_goals=expected_goals,
                    non_penalty_expected_goals=non_penalty_expected_goals,
                    expected_assisted_goals=expected_assisted_goals,
                    shot_creating_actions=shot_creating_actions,
                    goal_creating_actions=goal_creating_actions,
                    passes_completed=passes_completed,
                    passes_attempted=passes_attempted,
                    pass_completion=pass_completion,
                    progressive_passes=progressive_passes,
                    carries=carries,
                    progressive_carries=progressive_carries,
                    take_ons_attempted=take_ons_attempted,
                    successful_take_ons=successful_take_ons,
                    total_passing_distance=total_passing_distance,
                    progressive_passing_distance=progressive_passing_distance,
                    passes_completed_short=passes_completed_short,
                    passes_attempted_short=passes_attempted_short,
                    pass_completion_short=pass_completion_short,
                    passes_completed_medium=passes_completed_medium,
                    passes_attempted_medium=passes_attempted_medium,
                    pass_completion_medium=pass_completion_medium,
                    passes_completed_long=passes_completed_long,
                    passes_attempted_long=passes_attempted_long,
                    pass_completion_long=pass_completion_long,
                    expected_assists=expected_assists,
                    key_passes=key_passes,
                    passes_into_final_third=passes_into_final_third,
                    passes_into_penalty_area=passes_into_penalty_area,
                    crosses_into_penalty_area=crosses_into_penalty_area,
                    live_ball_passes=live_ball_passes,
                    dead_ball_passes=dead_ball_passes,
                    passes_from_free_kicks=passes_from_free_kicks,
                    through_balls=through_balls,
                    switches=switches,
                    crosses=crosses,
                    throw_ins_taken=throw_ins_taken,
                    corner_kicks=corner_kicks,
                    inswinging_corner_kicks=inswinging_corner_kicks,
                    outswinging_corner_kicks=outswinging_corner_kicks,
                    straight_corner_kicks=straight_corner_kicks,
                    passes_offside=passes_offside,
                    passes_blocked=passes_blocked,
                    tackles_won=tackles_won,
                    tackles_in_defensive_third=tackles_in_defensive_third,
                    tackles_in_middle_third=tackles_in_middle_third,
                    tackles_in_attacking_third=tackles_in_attacking_third,
                    dribblers_tackled=dribblers_tackled,
                    dribbles_challenged=dribbles_challenged,
                    percent_of_dribblers_tackled=percent_of_dribblers_tackled,
                    challenges_lost=challenges_lost,
                    shots_blocked=shots_blocked,
                    tackles_plus_interceptions=tackles_plus_interceptions,
                    errors=errors,
                    touches_in_defensive_penalty_area=touches_in_defensive_penalty_area,
                    touches_in_defensive_third=touches_in_defensive_third,
                    touches_in_middle_third=touches_in_middle_third,
                    touches_in_attacking_third=touches_in_attacking_third,
                    touches_in_attacking_penalty_area=touches_in_attacking_penalty_area,
                    live_ball_touches=live_ball_touches,
                    successful_take_on_percentage=successful_take_on_percentage,
                    times_tackled_during_take_ons=times_tackled_during_take_ons,
                    tackled_during_take_ons_percentage=tackled_during_take_ons_percentage,
                    total_carrying_distance=total_carrying_distance,
                    progressive_carrying_distance=progressive_carrying_distance,
                    carries_into_final_third=carries_into_final_third,
                    carries_into_penalty_area=carries_into_penalty_area,
                    miscontrols=miscontrols,
                    dispossessed=dispossessed,
                    passes_received=passes_received,
                    progressive_passes_received=progressive_passes_received,
                    second_yellow_card=second_yellow_card,
                    fouls_committed=fouls_committed,
                    fouls_drawn=fouls_drawn,
                    offsides=offsides,
                    penalty_kicks_won=penalty_kicks_won,
                    penalty_kicks_conceded=penalty_kicks_conceded,
                    own_goals=own_goals,
                    ball_recoveries=ball_recoveries,
                    aerials_won=aerials_won,
                    aerials_lost=aerials_lost,
                    percentage_of_aerials_won=percentage_of_aerials_won,
                    shots_on_target_against=shots_on_target_against,
                    post_shot_expected_goals=post_shot_expected_goals,
                    passes_attempted_minus_goal_kicks=passes_attempted_minus_goal_kicks,
                    throws_attempted=throws_attempted,
                    percentage_of_passes_that_were_launched=percentage_of_passes_that_were_launched,
                    average_pass_length=average_pass_length,
                    goal_kicks_attempted=goal_kicks_attempted,
                    percentage_of_goal_kicks_that_were_launched=percentage_of_goal_kicks_that_were_launched,
                    average_goal_kick_length=average_goal_kick_length,
                    crosses_faced=crosses_faced,
                    crosses_stopped=crosses_stopped,
                    percentage_crosses_stopped=percentage_crosses_stopped,
                    defensive_actions_outside_penalty_area=defensive_actions_outside_penalty_area,
                    average_distance_of_defensive_actions=average_distance_of_defensive_actions,
                    three_point_attempt_rate=three_point_attempt_rate,
                    tackles=tackles,
                    interceptions=interceptions,
                    clearances=clearances,
                    free_throw_attempt_rate=free_throw_attempt_rate,
                    offensive_rebound_percentage=offensive_rebound_percentage,
                    defensive_rebound_percentage=defensive_rebound_percentage,
                    total_rebound_percentage=total_rebound_percentage,
                    assist_percentage=assist_percentage,
                    steal_percentage=steal_percentage,
                    block_percentage=block_percentage,
                    turnover_percentage=turnover_percentage,
                    usage_percentage=usage_percentage,
                    offensive_rating=offensive_rating,
                    defensive_rating=defensive_rating,
                    box_plus_minus=box_plus_minus,
                )
            )

    return (dt, teams, venue_name)


def _create_sportsreference_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    positions_validator: dict[str, str],
    version: str,
) -> GameModel | None:
    # pylint: disable=too-many-branches
    if url in _NON_WAYBACK_URLS:
        with session.wayback_disabled():
            response = session.get(url)
    else:
        response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    page_title = soup.find("h1", class_="page_title")

    # If the page_title is bad, try fetching from a non wayback source
    if page_title is not None:
        if "file not found" in page_title.get_text().strip().lower():
            session.cache.delete(urls=[url, response.url])
            with session.wayback_disabled():
                response = session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")

    comp_ids = []
    for a in soup.find_all("a"):
        comp_url = urllib.parse.urljoin(url, a.get("href"))
        o = urlparse(comp_url)
        path_components = o.path.split("/")
        if len(path_components) >= 4 and path_components[2] == "comps":
            comp_id = path_components[3]
            if comp_id:
                try:
                    comp_ids.append(int(comp_id))
                except ValueError:
                    pass
    data = Counter(comp_ids)
    mode_comp_id = data.most_common()

    match league:
        case League.EPL:
            if mode_comp_id != 9:
                return None
        case League.FIFA:
            if mode_comp_id != 1:
                return None

    player_urls = set()
    for a in soup.find_all("a"):
        player_url = urllib.parse.urljoin(url, a.get("href"))
        if "/players/" in player_url and not player_url.endswith("/players/"):
            player_urls.add(player_url)

    scores = []
    for score_div in soup.find_all("div", class_="score"):
        try:
            scores.append(float(score_div.get_text().strip()))
        except ValueError as exc:
            session.cache.delete(urls=[url, response.url])
            logging.error(response.text)
            logging.error(url)
            raise exc

    def _normalize_value(value: Any) -> Any:
        if isinstance(value, str):
            if "%" in value:
                return float(value.replace("%", ""))
        if isinstance(value, float) and math.isnan(value):
            return None
        return value

    handle = io.StringIO()
    handle.write(response.text)
    handle.seek(0)
    fg = {}
    fga = {}
    offensive_rebounds = {}
    assists = {}
    turnovers = {}
    minutes_played = {}
    three_point_field_goals = {}
    three_point_field_goals_attempted = {}
    free_throws = {}
    free_throws_attempted = {}
    defensive_rebounds = {}
    steals = {}
    blocks = {}
    personal_fouls = {}
    player_points = {}
    game_scores = {}
    point_differentials = {}
    goals = {}
    penalties_in_minutes: dict[str, datetime.timedelta] = {}
    even_strength_goals = {}
    power_play_goals = {}
    short_handed_goals = {}
    game_winning_goals = {}
    even_strength_assists: dict[str, int] = {}
    power_play_assists: dict[str, int] = {}
    short_handed_assists: dict[str, int] = {}
    shots_on_goal = {}
    shooting_percentage = {}
    shifts = {}
    time_on_ice = {}
    decision = {}
    goals_against = {}
    shots_against = {}
    saves = {}
    save_percentage = {}
    shutouts = {}
    individual_corsi_for_events = {}
    on_shot_ice_for_events = {}
    on_shot_ice_against_events = {}
    corsi_for_percentage = {}
    relative_corsi_for_percentage = {}
    offensive_zone_starts = {}
    defensive_zone_starts = {}
    offensive_zone_start_percentage = {}
    hits = {}
    true_shooting_percentage = {}
    at_bats = {}
    runs_scored = {}
    runs_batted_in = {}
    bases_on_balls = {}
    strikeouts = {}
    plate_appearances = {}
    hits_at_bats = {}
    obp = {}
    slg = {}
    ops = {}
    pitches = {}
    strikes = {}
    win_probability_added = {}
    average_leverage_index = {}
    wpa_plus = {}
    wpa_minus = {}
    cwpa = {}
    acli = {}
    re24 = {}
    putouts = {}
    innings_pitched = {}
    earned_runs = {}
    home_runs = {}
    era = {}
    batters_faced = {}
    strikes_by_contact = {}
    strikes_swinging = {}
    strikes_looking = {}
    ground_balls = {}
    fly_balls = {}
    line_drives = {}
    inherited_runners = {}
    inherited_scores = {}
    effective_field_goal_percentage = {}
    penalty_kicks_made = {}
    penalty_kicks_attempted = {}
    shots_total = {}
    shots_on_target = {}
    yellow_cards = {}
    red_cards = {}
    touches = {}
    expected_goals = {}
    non_penalty_expected_goals = {}
    expected_assisted_goals = {}
    shot_creating_actions = {}
    goal_creating_actions = {}
    passes_completed = {}
    passes_attempted = {}
    pass_completion = {}
    progressive_passes = {}
    carries = {}
    progressive_carries = {}
    take_ons_attempted = {}
    successful_take_ons = {}
    total_passing_distance = {}
    progressive_passing_distance = {}
    passes_completed_short = {}
    passes_attempted_short = {}
    pass_completion_short = {}
    passes_completed_medium = {}
    passes_attempted_medium = {}
    pass_completion_medium = {}
    passes_completed_long = {}
    passes_attempted_long = {}
    pass_completion_long = {}
    expected_assists = {}
    key_passes = {}
    passes_into_final_third = {}
    passes_into_penalty_area = {}
    crosses_into_penalty_area = {}
    live_ball_passes = {}
    dead_ball_passes = {}
    passes_from_free_kicks = {}
    through_balls = {}
    switches = {}
    crosses = {}
    throw_ins_taken = {}
    corner_kicks = {}
    inswinging_corner_kicks = {}
    outswinging_corner_kicks = {}
    straight_corner_kicks = {}
    passes_offside = {}
    passes_blocked = {}
    tackles_won = {}
    tackles_in_defensive_third = {}
    tackles_in_middle_third = {}
    tackles_in_attacking_third = {}
    dribblers_tackled = {}
    dribbles_challenged = {}
    percent_of_dribblers_tackled = {}
    challenges_lost = {}
    shots_blocked = {}
    tackles_plus_interceptions = {}
    errors = {}
    touches_in_defensive_penalty_area = {}
    touches_in_defensive_third = {}
    touches_in_middle_third = {}
    touches_in_attacking_third = {}
    touches_in_attacking_penalty_area = {}
    live_ball_touches = {}
    successful_take_on_percentage = {}
    times_tackled_during_take_ons = {}
    tackled_during_take_ons_percentage = {}
    total_carrying_distance = {}
    progressive_carrying_distance = {}
    carries_into_final_third = {}
    carries_into_penalty_area = {}
    miscontrols = {}
    dispossessed = {}
    passes_received = {}
    progressive_passes_received = {}
    second_yellow_card = {}
    fouls_committed = {}
    fouls_drawn = {}
    offsides = {}
    penalty_kicks_won = {}
    penalty_kicks_conceded = {}
    own_goals = {}
    ball_recoveries = {}
    aerials_won = {}
    aerials_lost = {}
    percentage_of_aerials_won = {}
    shots_on_target_against = {}
    post_shot_expected_goals = {}
    passes_attempted_minus_goal_kicks = {}
    throws_attempted = {}
    percentage_of_passes_that_were_launched = {}
    average_pass_length = {}
    goal_kicks_attempted = {}
    percentage_of_goal_kicks_that_were_launched = {}
    average_goal_kick_length = {}
    crosses_faced = {}
    crosses_stopped = {}
    percentage_crosses_stopped = {}
    defensive_actions_outside_penalty_area = {}
    average_distance_of_defensive_actions = {}
    three_point_attempt_rate = {}
    tackles = {}
    interceptions = {}
    clearances = {}
    free_throw_attempt_rate = {}
    offensive_rebound_percentage = {}
    defensive_rebound_percentage = {}
    total_rebound_percentage = {}
    assist_percentage = {}
    steal_percentage = {}
    block_percentage = {}
    turnover_percentage = {}
    usage_percentage = {}
    offensive_rating = {}
    defensive_rating = {}
    box_plus_minus = {}
    try:
        dfs = pd.read_html(handle)
        for df in dfs:
            if df.index.nlevels > 1:
                df.columns = df.columns.get_level_values(1)
            cols = set(df.columns.values.tolist())
            players = []
            if "Starters" in cols:
                players = df["Starters"].tolist()
            elif "Batting" in cols:
                players = df["Batting"].tolist()
            elif "Pitching" in cols:
                players = df["Pitching"].tolist()
            elif "Player" in cols:
                players = df["Player"].tolist()
            elif "Reserves" in cols:
                players = df["Reserves"].tolist()

            if players:
                if "FG" in cols:
                    fgs = df["FG"].tolist()
                    for idx, player in enumerate(players):
                        fg[player] = _normalize_value(fgs[idx])
                if "FGA" in cols:
                    fgas = df["FGA"].tolist()
                    for idx, player in enumerate(players):
                        fga[player] = _normalize_value(fgas[idx])
                if "OREB" in cols:
                    orebs = df["OREB"].tolist()
                    for idx, player in enumerate(players):
                        offensive_rebounds[player] = _normalize_value(orebs[idx])
                if "AST" in cols:
                    asts = df["AST"].tolist()
                    for idx, player in enumerate(players):
                        assists[player] = _normalize_value(asts[idx])
                if "TOV" in cols:
                    tovs = df["TOV"].tolist()
                    for idx, player in enumerate(players):
                        turnovers[player] = _normalize_value(tovs[idx])
                if "MP" in cols:
                    mps = df["MP"].tolist()
                    for idx, player in enumerate(players):
                        mp = mps[idx]
                        mp_minutes, mp_seconds = mp.split(":")
                        minutes_played[player] = datetime.timedelta(
                            minutes=int(mp_minutes), seconds=int(mp_seconds)
                        )
                if "3P" in cols:
                    threeps = df["3P"].tolist()
                    for idx, player in enumerate(players):
                        three_point_field_goals[player] = _normalize_value(threeps[idx])
                if "3PA" in cols:
                    threepsattempted = df["3PA"].tolist()
                    for idx, player in enumerate(players):
                        three_point_field_goals_attempted[player] = _normalize_value(
                            threepsattempted[idx]
                        )
                if "FT" in cols:
                    fts = df["FT"].tolist()
                    for idx, player in enumerate(players):
                        free_throws[player] = _normalize_value(fts[idx])
                if "FTA" in cols:
                    ftas = df["FTA"].tolist()
                    for idx, player in enumerate(players):
                        free_throws_attempted[player] = _normalize_value(ftas[idx])
                if "DRB" in cols:
                    drbs = df["DRB"].tolist()
                    for idx, player in enumerate(players):
                        defensive_rebounds[player] = _normalize_value(drbs[idx])
                if "STL" in cols:
                    stls = df["STL"].tolist()
                    for idx, player in enumerate(players):
                        steals[player] = _normalize_value(stls[idx])
                if "BLK" in cols:
                    blks = df["BLK"].tolist()
                    for idx, player in enumerate(players):
                        blocks[player] = _normalize_value(blks[idx])
                if "PF" in cols:
                    pfs = df["PF"].tolist()
                    for idx, player in enumerate(players):
                        personal_fouls[player] = _normalize_value(pfs[idx])
                if "PTS" in cols:
                    ptss = df["PTS"].tolist()
                    for idx, player in enumerate(players):
                        player_points[player] = _normalize_value(ptss[idx])
                if "GmSc" in cols:
                    gmscs = df["GmSc"].tolist()
                    for idx, player in enumerate(players):
                        game_scores[player] = _normalize_value(gmscs[idx])
                if "+/-" in cols:
                    plusminuses = df["GmSc"].tolist()
                    for idx, player in enumerate(players):
                        point_differentials[player] = _normalize_value(plusminuses[idx])
                if "G" in cols:
                    gs = df["G"].tolist()
                    for idx, player in enumerate(players):
                        goals[player] = _normalize_value(gs[idx])
                if "A" in cols:
                    ass = df["A"].tolist()
                    for idx, player in enumerate(players):
                        assists[player] = _normalize_value(ass[idx])
                if "PIM" in cols:
                    pims = df["PIM"].tolist()
                    for idx, player in enumerate(players):
                        pim = pims[idx]
                        pim_minutes, pim_seconds = pim.split(":")
                        penalties_in_minutes[player] = datetime.timedelta(
                            minutes=int(pim_minutes), seconds=int(pim_seconds)
                        )
                if "EV" in cols:
                    evs = df["EV"].tolist()
                    for idx, player in enumerate(players):
                        even_strength_goals[player] = _normalize_value(evs[idx])
                if "PP" in cols:
                    pps = df["PP"].tolist()
                    for idx, player in enumerate(players):
                        power_play_goals[player] = _normalize_value(pps[idx])
                if "SH" in cols:
                    shs = df["SH"].tolist()
                    for idx, player in enumerate(players):
                        short_handed_goals[player] = _normalize_value(shs[idx])
                if "GW" in cols:
                    gws = df["GW"].tolist()
                    for idx, player in enumerate(players):
                        game_winning_goals[player] = _normalize_value(gws[idx])
                if "S" in cols:
                    ss = df["S"].tolist()
                    for idx, player in enumerate(players):
                        shots_on_goal[player] = _normalize_value(ss[idx])
                if "S%" in cols:
                    sps = df["S%"].tolist()
                    for idx, player in enumerate(players):
                        shooting_percentage[player] = _normalize_value(sps[idx])
                if "SHFT" in cols:
                    shfts = df["SHFT"].tolist()
                    for idx, player in enumerate(players):
                        shifts[player] = _normalize_value(shfts[idx])
                if "TOI" in cols:
                    tois = df["TOI"].tolist()
                    for idx, player in enumerate(players):
                        toi = tois[idx]
                        toi_minutes, toi_seconds = toi.split(":")
                        time_on_ice[player] = datetime.timedelta(
                            minutes=int(toi_minutes), seconds=int(toi_seconds)
                        )
                if "DEC" in cols:
                    decs = df["DEC"].tolist()
                    for idx, player in enumerate(players):
                        decision[player] = _normalize_value(decs[idx])
                if "GA" in cols:
                    gas = df["GA"].tolist()
                    for idx, player in enumerate(players):
                        goals_against[player] = _normalize_value(gas[idx])
                if "SA" in cols:
                    sas = df["SA"].tolist()
                    for idx, player in enumerate(players):
                        shots_against[player] = _normalize_value(sas[idx])
                if "SV" in cols:
                    svs = df["SV"].tolist()
                    for idx, player in enumerate(players):
                        saves[player] = _normalize_value(svs[idx])
                if "SV%" in cols:
                    svps = df["SV%"].tolist()
                    for idx, player in enumerate(players):
                        save_percentage[player] = _normalize_value(svps[idx])
                if "SO" in cols:
                    sos = df["SO"].tolist()
                    for idx, player in enumerate(players):
                        shutouts[player] = _normalize_value(sos[idx])
                if "iCF" in cols:
                    icfs = df["iCF"].tolist()
                    for idx, player in enumerate(players):
                        individual_corsi_for_events[player] = _normalize_value(
                            icfs[idx]
                        )
                if "SAT-F" in cols:
                    satfs = df["SAT-F"].tolist()
                    for idx, player in enumerate(players):
                        on_shot_ice_for_events[player] = _normalize_value(satfs[idx])
                if "SAT-A" in cols:
                    satas = df["SAT-A"].tolist()
                    for idx, player in enumerate(players):
                        on_shot_ice_against_events[player] = _normalize_value(
                            satas[idx]
                        )
                if "CF%" in cols:
                    cfps = df["CF%"].tolist()
                    for idx, player in enumerate(players):
                        corsi_for_percentage[player] = _normalize_value(cfps[idx])
                if "CRel%" in cols:
                    crelps = df["CRel%"].tolist()
                    for idx, player in enumerate(players):
                        relative_corsi_for_percentage[player] = _normalize_value(
                            crelps[idx]
                        )
                if "ZSO" in cols:
                    zsos = df["ZSO"].tolist()
                    for idx, player in enumerate(players):
                        offensive_zone_starts[player] = _normalize_value(zsos[idx])
                if "ZSD" in cols:
                    zsds = df["ZSD"].tolist()
                    for idx, player in enumerate(players):
                        defensive_zone_starts[player] = _normalize_value(zsds[idx])
                if "oZS%" in cols:
                    ozsps = df["oZS%"].tolist()
                    for idx, player in enumerate(players):
                        offensive_zone_start_percentage[player] = _normalize_value(
                            ozsps[idx]
                        )
                if "HIT" in cols:
                    hitss = df["HIT"].tolist()
                    for idx, player in enumerate(players):
                        hits[player] = _normalize_value(hitss[idx])
                if "TS%" in cols:
                    tsps = df["TS%"].tolist()
                    for idx, player in enumerate(players):
                        true_shooting_percentage[player] = _normalize_value(tsps[idx])
                if "AB" in cols:
                    abss = df["AB"].tolist()
                    for idx, player in enumerate(players):
                        at_bats[player] = _normalize_value(abss[idx])
                if "R" in cols:
                    rs = df["R"].tolist()
                    for idx, player in enumerate(players):
                        runs_scored[player] = _normalize_value(rs[idx])
                if "RBI" in cols:
                    rbis = df["RBI"].tolist()
                    for idx, player in enumerate(players):
                        runs_batted_in[player] = _normalize_value(rbis[idx])
                if "BB" in cols:
                    bbs = df["BB"].tolist()
                    for idx, player in enumerate(players):
                        bases_on_balls[player] = _normalize_value(bbs[idx])
                if "SO" in cols:
                    sos = df["SO"].tolist()
                    for idx, player in enumerate(players):
                        strikeouts[player] = _normalize_value(sos[idx])
                if "PA" in cols:
                    pas = df["PA"].tolist()
                    for idx, player in enumerate(players):
                        plate_appearances[player] = _normalize_value(pas[idx])
                if "BA" in cols:
                    bas = df["BA"].tolist()
                    for idx, player in enumerate(players):
                        hits_at_bats[player] = _normalize_value(bas[idx])
                if "OBP" in cols:
                    obps = df["OBP"].tolist()
                    for idx, player in enumerate(players):
                        obp[player] = _normalize_value(obps[idx])
                if "SLG" in cols:
                    slgs = df["SLG"].tolist()
                    for idx, player in enumerate(players):
                        slg[player] = _normalize_value(slgs[idx])
                if "OPS" in cols:
                    opss = df["OPS"].tolist()
                    for idx, player in enumerate(players):
                        ops[player] = _normalize_value(opss[idx])
                if "Pit" in cols:
                    pits = df["Pit"].tolist()
                    for idx, player in enumerate(players):
                        pitches[player] = _normalize_value(pits[idx])
                if "Str" in cols:
                    strs = df["Str"].tolist()
                    for idx, player in enumerate(players):
                        strikes[player] = _normalize_value(strs[idx])
                if "WPA" in cols:
                    wpas = df["WPA"].tolist()
                    for idx, player in enumerate(players):
                        win_probability_added[player] = _normalize_value(wpas[idx])
                if "aLI" in cols:
                    alis = df["aLI"].tolist()
                    for idx, player in enumerate(players):
                        average_leverage_index[player] = _normalize_value(alis[idx])
                if "WPA+" in cols:
                    wpapluss = df["WPA+"].tolist()
                    for idx, player in enumerate(players):
                        wpa_plus[player] = _normalize_value(wpapluss[idx])
                if "WPA-" in cols:
                    wpaminuss = df["WPA-"].tolist()
                    for idx, player in enumerate(players):
                        wpa_minus[player] = _normalize_value(wpaminuss[idx])
                if "cWPA" in cols:
                    cwpas = df["cWPA"].tolist()
                    for idx, player in enumerate(players):
                        cwpa[player] = _normalize_value(cwpas[idx])
                if "acLI" in cols:
                    aclis = df["acLI"].tolist()
                    for idx, player in enumerate(players):
                        acli[player] = _normalize_value(aclis[idx])
                if "RE24" in cols:
                    re24s = df["RE24"].tolist()
                    for idx, player in enumerate(players):
                        re24[player] = _normalize_value(re24s[idx])
                if "PO" in cols:
                    pos = df["PO"].tolist()
                    for idx, player in enumerate(players):
                        putouts[player] = _normalize_value(pos[idx])
                if "IP" in cols:
                    ips = df["IP"].tolist()
                    for idx, player in enumerate(players):
                        innings_pitched[player] = int(_normalize_value(ips[idx]))
                if "ER" in cols:
                    ers = df["ER"].tolist()
                    for idx, player in enumerate(players):
                        earned_runs[player] = _normalize_value(ers[idx])
                if "HR" in cols:
                    hrs = df["HR"].tolist()
                    for idx, player in enumerate(players):
                        home_runs[player] = _normalize_value(hrs[idx])
                if "ERA" in cols:
                    eras = df["ERA"].tolist()
                    for idx, player in enumerate(players):
                        era[player] = _normalize_value(eras[idx])
                if "BF" in cols:
                    bfs = df["BF"].tolist()
                    for idx, player in enumerate(players):
                        batters_faced[player] = _normalize_value(bfs[idx])
                if "Ctct" in cols:
                    ctcts = df["Ctct"].tolist()
                    for idx, player in enumerate(players):
                        strikes_by_contact[player] = _normalize_value(ctcts[idx])
                if "StS" in cols:
                    stss = df["StS"].tolist()
                    for idx, player in enumerate(players):
                        strikes_swinging[player] = _normalize_value(stss[idx])
                if "StL" in cols:
                    stls = df["StL"].tolist()
                    for idx, player in enumerate(players):
                        strikes_looking[player] = _normalize_value(stls[idx])
                if "GB" in cols:
                    gbs = df["GB"].tolist()
                    for idx, player in enumerate(players):
                        ground_balls[player] = _normalize_value(gbs[idx])
                if "FB" in cols:
                    fbs = df["FB"].tolist()
                    for idx, player in enumerate(players):
                        fly_balls[player] = _normalize_value(fbs[idx])
                if "LD" in cols:
                    lds = df["LD"].tolist()
                    for idx, player in enumerate(players):
                        line_drives[player] = _normalize_value(lds[idx])
                if "IR" in cols:
                    irs = df["IR"].tolist()
                    for idx, player in enumerate(players):
                        inherited_runners[player] = _normalize_value(irs[idx])
                if "IS" in cols:
                    iss = df["IS"].tolist()
                    for idx, player in enumerate(players):
                        inherited_scores[player] = _normalize_value(iss[idx])
                if "eFG%" in cols:
                    efgps = df["eFG%"].tolist()
                    for idx, player in enumerate(players):
                        effective_field_goal_percentage[player] = _normalize_value(
                            efgps[idx]
                        )
                if "Gls" in cols:
                    glss = df["Gls"].tolist()
                    for idx, player in enumerate(players):
                        goals[player] = _normalize_value(glss[idx])
                if "Ast" in cols:
                    asts = df["Ast"].tolist()
                    for idx, player in enumerate(players):
                        assists[player] = _normalize_value(asts[idx])
                if "PK" in cols:
                    pks = df["PK"].tolist()
                    for idx, player in enumerate(players):
                        penalty_kicks_made[player] = _normalize_value(pks[idx])
                if "PKatt" in cols:
                    pkatts = df["PKatt"].tolist()
                    for idx, player in enumerate(players):
                        penalty_kicks_attempted[player] = _normalize_value(pkatts[idx])
                if "Sh" in cols:
                    shs = df["Sh"].tolist()
                    for idx, player in enumerate(players):
                        shots_total[player] = _normalize_value(shs[idx])
                if "SoT" in cols:
                    sots = df["SoT"].tolist()
                    for idx, player in enumerate(players):
                        shots_on_target[player] = _normalize_value(sots[idx])
                if "CrdY" in cols:
                    crdys = df["CrdY"].tolist()
                    for idx, player in enumerate(players):
                        yellow_cards[player] = _normalize_value(crdys[idx])
                if "CrdR" in cols:
                    crdrs = df["CrdR"].tolist()
                    for idx, player in enumerate(players):
                        red_cards[player] = _normalize_value(crdrs[idx])
                if "Touches" in cols:
                    touchess = df["Touches"].tolist()
                    for idx, player in enumerate(players):
                        touches[player] = _normalize_value(touchess[idx])
                if "Tkl" in cols:
                    tkls = df["Tkl"].tolist()
                    for idx, player in enumerate(players):
                        tackles[player] = _normalize_value(tkls[idx])
                if "Int" in cols:
                    ints = df["Int"].tolist()
                    for idx, player in enumerate(players):
                        interceptions[player] = _normalize_value(ints[idx])
                if "Blocks" in cols:
                    blockss = df["Blocks"].tolist()
                    for idx, player in enumerate(players):
                        blocks[player] = _normalize_value(blockss[idx])
                if "xG" in cols:
                    xgs = df["xG"].tolist()
                    for idx, player in enumerate(players):
                        expected_goals[player] = _normalize_value(xgs[idx])
                if "npxG" in cols:
                    npxgs = df["npxG"].tolist()
                    for idx, player in enumerate(players):
                        non_penalty_expected_goals[player] = _normalize_value(
                            npxgs[idx]
                        )
                if "xAG" in cols:
                    xags = df["xAG"].tolist()
                    for idx, player in enumerate(players):
                        expected_assisted_goals[player] = _normalize_value(xags[idx])
                if "SCA" in cols:
                    scas = df["SCA"].tolist()
                    for idx, player in enumerate(players):
                        shot_creating_actions[player] = _normalize_value(scas[idx])
                if "GCA" in cols:
                    gcas = df["GCA"].tolist()
                    for idx, player in enumerate(players):
                        goal_creating_actions[player] = _normalize_value(gcas[idx])
                if "Cmp" in cols:
                    cmps = df["Cmp"].tolist()
                    for idx, player in enumerate(players):
                        passes_completed[player] = _normalize_value(cmps[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        passes_attempted[player] = _normalize_value(atts[idx])
                if "Cmp%" in cols:
                    cmpps = df["Cmp%"].tolist()
                    for idx, player in enumerate(players):
                        pass_completion[player] = _normalize_value(cmpps[idx])
                if "PrgP" in cols:
                    prgps = df["PrgP"].tolist()
                    for idx, player in enumerate(players):
                        progressive_passes[player] = _normalize_value(prgps[idx])
                if "Carries" in cols:
                    carriess = df["Carries"].tolist()
                    for idx, player in enumerate(players):
                        carries[player] = _normalize_value(carriess[idx])
                if "PrgC" in cols:
                    prgcs = df["PrgC"].tolist()
                    for idx, player in enumerate(players):
                        progressive_carries[player] = _normalize_value(prgcs[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        take_ons_attempted[player] = _normalize_value(atts[idx])
                if "Succ" in cols:
                    succs = df["Succ"].tolist()
                    for idx, player in enumerate(players):
                        successful_take_ons[player] = _normalize_value(succs[idx])
                if "TotDist" in cols:
                    totdists = df["TotDist"].tolist()
                    for idx, player in enumerate(players):
                        total_passing_distance[player] = _normalize_value(totdists[idx])
                if "PrgDist" in cols:
                    prgdists = df["PrgDist"].tolist()
                    for idx, player in enumerate(players):
                        progressive_passing_distance[player] = _normalize_value(
                            prgdists[idx]
                        )
                if "Cmp" in cols:
                    cmps = df["Cmp"].tolist()
                    for idx, player in enumerate(players):
                        passes_completed_short[player] = _normalize_value(cmps[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        passes_attempted_short[player] = _normalize_value(atts[idx])
                if "Cmp%" in cols:
                    cmpps = df["Cmp%"].tolist()
                    for idx, player in enumerate(players):
                        pass_completion_short[player] = _normalize_value(cmpps[idx])
                if "Cmp" in cols:
                    cmps = df["Cmp"].tolist()
                    for idx, player in enumerate(players):
                        passes_completed_medium[player] = _normalize_value(cmps[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        passes_attempted_medium[player] = _normalize_value(atts[idx])
                if "Cmp%" in cols:
                    cmpps = df["Cmp%"].tolist()
                    for idx, player in enumerate(players):
                        pass_completion_medium[player] = _normalize_value(cmpps[idx])
                if "Cmp" in cols:
                    cmps = df["Cmp"].tolist()
                    for idx, player in enumerate(players):
                        passes_completed_long[player] = _normalize_value(cmps[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        passes_attempted_long[player] = _normalize_value(atts[idx])
                if "Cmp%" in cols:
                    cmpps = df["Cmp%"].tolist()
                    for idx, player in enumerate(players):
                        pass_completion_long[player] = _normalize_value(cmpps[idx])
                if "xA" in cols:
                    xas = df["xA"].tolist()
                    for idx, player in enumerate(players):
                        expected_assists[player] = _normalize_value(xas[idx])
                if "KP" in cols:
                    kps = df["KP"].tolist()
                    for idx, player in enumerate(players):
                        key_passes[player] = _normalize_value(kps[idx])
                if "1/3" in cols:
                    onethrees = df["1/3"].tolist()
                    for idx, player in enumerate(players):
                        passes_into_final_third[player] = _normalize_value(
                            onethrees[idx]
                        )
                if "PPA" in cols:
                    ppas = df["PPA"].tolist()
                    for idx, player in enumerate(players):
                        passes_into_penalty_area[player] = _normalize_value(ppas[idx])
                if "CrsPA" in cols:
                    crspas = df["CrsPA"].tolist()
                    for idx, player in enumerate(players):
                        crosses_into_penalty_area[player] = _normalize_value(
                            crspas[idx]
                        )
                if "Live" in cols:
                    lives = df["Live"].tolist()
                    for idx, player in enumerate(players):
                        live_ball_passes[player] = _normalize_value(lives[idx])
                if "Dead" in cols:
                    deads = df["Dead"].tolist()
                    for idx, player in enumerate(players):
                        dead_ball_passes[player] = _normalize_value(deads[idx])
                if "FK" in cols:
                    fks = df["FK"].tolist()
                    for idx, player in enumerate(players):
                        passes_from_free_kicks[player] = _normalize_value(fks[idx])
                if "TB" in cols:
                    tbs = df["TB"].tolist()
                    for idx, player in enumerate(players):
                        through_balls[player] = _normalize_value(tbs[idx])
                if "Sw" in cols:
                    sws = df["Sw"].tolist()
                    for idx, player in enumerate(players):
                        switches[player] = _normalize_value(sws[idx])
                if "Crs" in cols:
                    crss = df["Crs"].tolist()
                    for idx, player in enumerate(players):
                        crosses[player] = _normalize_value(crss[idx])
                if "TI" in cols:
                    tis = df["TI"].tolist()
                    for idx, player in enumerate(players):
                        throw_ins_taken[player] = _normalize_value(tis[idx])
                if "CK" in cols:
                    cks = df["CK"].tolist()
                    for idx, player in enumerate(players):
                        corner_kicks[player] = _normalize_value(cks[idx])
                if "In" in cols:
                    ins = df["In"].tolist()
                    for idx, player in enumerate(players):
                        inswinging_corner_kicks[player] = _normalize_value(ins[idx])
                if "Out" in cols:
                    outs = df["Out"].tolist()
                    for idx, player in enumerate(players):
                        outswinging_corner_kicks[player] = _normalize_value(outs[idx])
                if "Str" in cols:
                    strs = df["Str"].tolist()
                    for idx, player in enumerate(players):
                        straight_corner_kicks[player] = _normalize_value(strs[idx])
                if "Off" in cols:
                    offs = df["Off"].tolist()
                    for idx, player in enumerate(players):
                        passes_offside[player] = _normalize_value(offs[idx])
                if "Blocks" in cols:
                    blockss = df["Blocks"].tolist()
                    for idx, player in enumerate(players):
                        passes_blocked[player] = _normalize_value(blockss[idx])
                if "TklW" in cols:
                    tklws = df["TklW"].tolist()
                    for idx, player in enumerate(players):
                        tackles_won[player] = _normalize_value(tklws[idx])
                if "Def 3rd" in cols:
                    defthirds = df["Def 3rd"].tolist()
                    for idx, player in enumerate(players):
                        tackles_in_defensive_third[player] = _normalize_value(
                            defthirds[idx]
                        )
                if "Mid 3rd" in cols:
                    midthirds = df["Mid 3rd"].tolist()
                    for idx, player in enumerate(players):
                        tackles_in_middle_third[player] = _normalize_value(
                            midthirds[idx]
                        )
                if "Att 3rd" in cols:
                    attthirds = df["Att 3rd"].tolist()
                    for idx, player in enumerate(players):
                        tackles_in_attacking_third[player] = _normalize_value(
                            attthirds[idx]
                        )
                if "Tkl" in cols:
                    tkls = df["Tkl"].tolist()
                    for idx, player in enumerate(players):
                        dribblers_tackled[player] = _normalize_value(tkls[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        dribbles_challenged[player] = _normalize_value(atts[idx])
                if "Tkl%" in cols:
                    tklps = df["Tkl%"].tolist()
                    for idx, player in enumerate(players):
                        percent_of_dribblers_tackled[player] = _normalize_value(
                            tklps[idx]
                        )
                if "Lost" in cols:
                    losts = df["Lost"].tolist()
                    for idx, player in enumerate(players):
                        challenges_lost[player] = _normalize_value(losts[idx])
                if "Sh" in cols:
                    shs = df["Sh"].tolist()
                    for idx, player in enumerate(players):
                        shots_blocked[player] = _normalize_value(shs[idx])
                if "Tkl+Int" in cols:
                    tklplusints = df["Tkl+Int"].tolist()
                    for idx, player in enumerate(players):
                        tackles_plus_interceptions[player] = _normalize_value(
                            tklplusints[idx]
                        )
                if "Clr" in cols:
                    clrs = df["Clr"].tolist()
                    for idx, player in enumerate(players):
                        clearances[player] = _normalize_value(clrs[idx])
                if "Err" in cols:
                    errs = df["Err"].tolist()
                    for idx, player in enumerate(players):
                        errors[player] = _normalize_value(errs[idx])
                if "Def Pen" in cols:
                    defpens = df["Def Pen"].tolist()
                    for idx, player in enumerate(players):
                        touches_in_defensive_penalty_area[player] = _normalize_value(
                            defpens[idx]
                        )
                if "Def 3rd" in cols:
                    defthirds = df["Mid 3rd"].tolist()
                    for idx, player in enumerate(players):
                        touches_in_defensive_third[player] = _normalize_value(
                            defthirds[idx]
                        )
                if "Mid 3rd" in cols:
                    midthirds = df["Mid 3rd"].tolist()
                    for idx, player in enumerate(players):
                        touches_in_middle_third[player] = _normalize_value(
                            midthirds[idx]
                        )
                if "Att 3rd" in cols:
                    attthirds = df["Att 3rd"].tolist()
                    for idx, player in enumerate(players):
                        touches_in_attacking_third[player] = _normalize_value(
                            attthirds[idx]
                        )
                if "Att Pen" in cols:
                    attpens = df["Att Pen"].tolist()
                    for idx, player in enumerate(players):
                        touches_in_attacking_penalty_area[player] = _normalize_value(
                            attpens[idx]
                        )
                if "Live" in cols:
                    lives = df["Live"].tolist()
                    for idx, player in enumerate(players):
                        live_ball_touches[player] = _normalize_value(lives[idx])
                if "Succ%" in cols:
                    succps = df["Succ%"].tolist()
                    for idx, player in enumerate(players):
                        successful_take_on_percentage[player] = _normalize_value(
                            succps[idx]
                        )
                if "Tkld" in cols:
                    tklds = df["Tkld"].tolist()
                    for idx, player in enumerate(players):
                        times_tackled_during_take_ons[player] = _normalize_value(
                            tklds[idx]
                        )
                if "Tkld%" in cols:
                    tkldps = df["Tkld%"].tolist()
                    for idx, player in enumerate(players):
                        tackled_during_take_ons_percentage[player] = _normalize_value(
                            tkldps[idx]
                        )
                if "TotDist" in cols:
                    totdists = df["TotDist"].tolist()
                    for idx, player in enumerate(players):
                        total_carrying_distance[player] = _normalize_value(
                            totdists[idx]
                        )
                if "PrgDist" in cols:
                    prgdists = df["PrgDist"].tolist()
                    for idx, player in enumerate(players):
                        progressive_carrying_distance[player] = _normalize_value(
                            prgdists[idx]
                        )
                if "1/3" in cols:
                    onethrees = df["1/3"].tolist()
                    for idx, player in enumerate(players):
                        carries_into_final_third[player] = _normalize_value(
                            onethrees[idx]
                        )
                if "CPA" in cols:
                    cpas = df["CPA"].tolist()
                    for idx, player in enumerate(players):
                        carries_into_penalty_area[player] = _normalize_value(cpas[idx])
                if "Mis" in cols:
                    miss = df["Mis"].tolist()
                    for idx, player in enumerate(players):
                        miscontrols[player] = _normalize_value(miss[idx])
                if "Dis" in cols:
                    diss = df["Dis"].tolist()
                    for idx, player in enumerate(players):
                        dispossessed[player] = _normalize_value(diss[idx])
                if "Rec" in cols:
                    recs = df["Rec"].tolist()
                    for idx, player in enumerate(players):
                        passes_received[player] = _normalize_value(recs[idx])
                if "PrgR" in cols:
                    prgrs = df["PrgR"].tolist()
                    for idx, player in enumerate(players):
                        progressive_passes_received[player] = _normalize_value(
                            prgrs[idx]
                        )
                if "2CrdY" in cols:
                    twocrdys = df["2CrdY"].tolist()
                    for idx, player in enumerate(players):
                        second_yellow_card[player] = _normalize_value(twocrdys[idx])
                if "Fls" in cols:
                    flss = df["Fls"].tolist()
                    for idx, player in enumerate(players):
                        fouls_committed[player] = _normalize_value(flss[idx])
                if "Fld" in cols:
                    flds = df["Fld"].tolist()
                    for idx, player in enumerate(players):
                        fouls_drawn[player] = _normalize_value(flds[idx])
                if "Off" in cols:
                    offs = df["Off"].tolist()
                    for idx, player in enumerate(players):
                        offsides[player] = _normalize_value(offs[idx])
                if "PKwon" in cols:
                    pkwons = df["PKwon"].tolist()
                    for idx, player in enumerate(players):
                        penalty_kicks_won[player] = _normalize_value(pkwons[idx])
                if "PKcon" in cols:
                    pkcons = df["PKcon"].tolist()
                    for idx, player in enumerate(players):
                        penalty_kicks_conceded[player] = _normalize_value(pkcons[idx])
                if "OG" in cols:
                    ogs = df["OG"].tolist()
                    for idx, player in enumerate(players):
                        own_goals[player] = _normalize_value(ogs[idx])
                if "Recov" in cols:
                    recovs = df["Recov"].tolist()
                    for idx, player in enumerate(players):
                        ball_recoveries[player] = _normalize_value(recovs[idx])
                if "Won" in cols:
                    wons = df["Won"].tolist()
                    for idx, player in enumerate(players):
                        aerials_won[player] = _normalize_value(wons[idx])
                if "Lost" in cols:
                    losts = df["Lost"].tolist()
                    for idx, player in enumerate(players):
                        aerials_lost[player] = _normalize_value(losts[idx])
                if "Won%" in cols:
                    wonps = df["Won%"].tolist()
                    for idx, player in enumerate(players):
                        percentage_of_aerials_won[player] = _normalize_value(wonps[idx])
                if "SoTA" in cols:
                    sotas = df["SoTA"].tolist()
                    for idx, player in enumerate(players):
                        shots_on_target_against[player] = _normalize_value(sotas[idx])
                if "Saves" in cols:
                    savess = df["Saves"].tolist()
                    for idx, player in enumerate(players):
                        saves[player] = _normalize_value(savess[idx])
                if "Save%" in cols:
                    saveps = df["Save%"].tolist()
                    for idx, player in enumerate(players):
                        save_percentage[player] = _normalize_value(saveps[idx])
                if "PSxG" in cols:
                    psxgs = df["PSxG"].tolist()
                    for idx, player in enumerate(players):
                        post_shot_expected_goals[player] = _normalize_value(psxgs[idx])
                if "Att (GK)" in cols:
                    attgks = df["Att (GK)"].tolist()
                    for idx, player in enumerate(players):
                        passes_attempted_minus_goal_kicks[player] = _normalize_value(
                            attgks[idx]
                        )
                if "Thr" in cols:
                    thrs = df["Thr"].tolist()
                    for idx, player in enumerate(players):
                        throws_attempted[player] = _normalize_value(thrs[idx])
                if "Launch%" in cols:
                    launchps = df["Launch%"].tolist()
                    for idx, player in enumerate(players):
                        percentage_of_passes_that_were_launched[player] = (
                            _normalize_value(launchps[idx])
                        )
                if "AvgLen" in cols:
                    avglens = df["AvgLen"].tolist()
                    for idx, player in enumerate(players):
                        average_pass_length[player] = _normalize_value(avglens[idx])
                if "Att" in cols:
                    atts = df["Att"].tolist()
                    for idx, player in enumerate(players):
                        goal_kicks_attempted[player] = _normalize_value(atts[idx])
                if "Launch%" in cols:
                    launchps = df["Launch%"].tolist()
                    for idx, player in enumerate(players):
                        percentage_of_goal_kicks_that_were_launched[player] = (
                            _normalize_value(launchps[idx])
                        )
                if "AvgLen" in cols:
                    avglens = df["AvgLen"].tolist()
                    for idx, player in enumerate(players):
                        average_goal_kick_length[player] = _normalize_value(
                            avglens[idx]
                        )
                if "Opp" in cols:
                    opps = df["Opp"].tolist()
                    for idx, player in enumerate(players):
                        crosses_faced[player] = _normalize_value(opps[idx])
                if "Stp" in cols:
                    stps = df["Stp"].tolist()
                    for idx, player in enumerate(players):
                        crosses_stopped[player] = _normalize_value(stps[idx])
                if "Stp%" in cols:
                    stpps = df["Stp%"].tolist()
                    for idx, player in enumerate(players):
                        percentage_crosses_stopped[player] = _normalize_value(
                            stpps[idx]
                        )
                if "#OPA" in cols:
                    hopas = df["#OPA"].tolist()
                    for idx, player in enumerate(players):
                        defensive_actions_outside_penalty_area[player] = (
                            _normalize_value(hopas[idx])
                        )
                if "AvgDist" in cols:
                    avgdists = df["AvgDist"].tolist()
                    for idx, player in enumerate(players):
                        average_distance_of_defensive_actions[player] = (
                            _normalize_value(avgdists[idx])
                        )
                if "3PAr" in cols:
                    threepars = df["3PAr"].tolist()
                    for idx, player in enumerate(players):
                        three_point_attempt_rate[player] = _normalize_value(
                            threepars[idx]
                        )
                if "FTr" in cols:
                    ftrs = df["FTr"].tolist()
                    for idx, player in enumerate(players):
                        free_throw_attempt_rate[player] = _normalize_value(ftrs[idx])
                if "ORB%" in cols:
                    orbps = df["ORB%"].tolist()
                    for idx, player in enumerate(players):
                        offensive_rebound_percentage[player] = _normalize_value(
                            orbps[idx]
                        )
                if "DRB%" in cols:
                    drbps = df["DRB%"].tolist()
                    for idx, player in enumerate(players):
                        defensive_rebound_percentage[player] = _normalize_value(
                            drbps[idx]
                        )
                if "TRB%" in cols:
                    trbps = df["TRB%"].tolist()
                    for idx, player in enumerate(players):
                        total_rebound_percentage[player] = _normalize_value(trbps[idx])
                if "AST%" in cols:
                    astps = df["AST%"].tolist()
                    for idx, player in enumerate(players):
                        assist_percentage[player] = _normalize_value(astps[idx])
                if "STL%" in cols:
                    stlps = df["STL%"].tolist()
                    for idx, player in enumerate(players):
                        steal_percentage[player] = _normalize_value(stlps[idx])
                if "BLK%" in cols:
                    blkps = df["BLK%"].tolist()
                    for idx, player in enumerate(players):
                        block_percentage[player] = _normalize_value(blkps[idx])
                if "TOV%" in cols:
                    tovps = df["TOV%"].tolist()
                    for idx, player in enumerate(players):
                        turnover_percentage[player] = _normalize_value(tovps[idx])
                if "USG%" in cols:
                    usgps = df["USG%"].tolist()
                    for idx, player in enumerate(players):
                        usage_percentage[player] = _normalize_value(usgps[idx])
                if "ORtg" in cols:
                    ortgs = df["ORtg"].tolist()
                    for idx, player in enumerate(players):
                        offensive_rating[player] = _normalize_value(ortgs[idx])
                if "DRtg" in cols:
                    drtgs = df["DRtg"].tolist()
                    for idx, player in enumerate(players):
                        defensive_rating[player] = _normalize_value(drtgs[idx])
                if "BPM" in cols:
                    bpms = df["BPM"].tolist()
                    for idx, player in enumerate(players):
                        box_plus_minus[player] = _normalize_value(bpms[idx])

    except Exception as exc:
        logging.error(url)
        logging.error(response.text)
        logging.error(str(exc))
        return None

    scorebox_meta_div = soup.find("div", class_="scorebox_meta")
    if not isinstance(scorebox_meta_div, Tag):
        dt, teams, venue_name = _find_old_dt(
            dfs=dfs,
            session=session,
            soup=soup,
            url=url,
            league=league,
            player_urls=player_urls,
            fg=fg,
            fga=fga,
            offensive_rebounds=offensive_rebounds,
            assists=assists,
            turnovers=turnovers,
            response=response,
            positions_validator=positions_validator,
            minutes_played=minutes_played,
            three_point_field_goals=three_point_field_goals,
            three_point_field_goals_attempted=three_point_field_goals_attempted,
            free_throws=free_throws,
            free_throws_attempted=free_throws_attempted,
            defensive_rebounds=defensive_rebounds,
            steals=steals,
            blocks=blocks,
            personal_fouls=personal_fouls,
            player_points=player_points,
            game_scores=game_scores,
            point_differentials=point_differentials,
            goals=goals,
            penalties_in_minutes=penalties_in_minutes,
            even_strength_goals=even_strength_goals,
            power_play_goals=power_play_goals,
            short_handed_goals=short_handed_goals,
            game_winning_goals=game_winning_goals,
            even_strength_assists=even_strength_assists,
            power_play_assists=power_play_assists,
            short_handed_assists=short_handed_assists,
            shots_on_goal=shots_on_goal,
            shooting_percentage=shooting_percentage,
            shifts=shifts,
            time_on_ice=time_on_ice,
            decision=decision,
            goals_against=goals_against,
            shots_against=shots_against,
            saves=saves,
            save_percentage=save_percentage,
            shutouts=shutouts,
            individual_corsi_for_events=individual_corsi_for_events,
            on_shot_ice_for_events=on_shot_ice_for_events,
            on_shot_ice_against_events=on_shot_ice_against_events,
            corsi_for_percentage=corsi_for_percentage,
            relative_corsi_for_percentage=relative_corsi_for_percentage,
            offensive_zone_starts=offensive_zone_starts,
            defensive_zone_starts=defensive_zone_starts,
            offensive_zone_start_percentage=offensive_zone_start_percentage,
            hits=hits,
            true_shooting_percentage=true_shooting_percentage,
            at_bats=at_bats,
            runs_scored=runs_scored,
            runs_batted_in=runs_batted_in,
            bases_on_balls=bases_on_balls,
            strikeouts=strikeouts,
            plate_appearances=plate_appearances,
            hits_at_bats=hits_at_bats,
            obp=obp,
            slg=slg,
            ops=ops,
            pitches=pitches,
            strikes=strikes,
            win_probability_added=win_probability_added,
            average_leverage_index=average_leverage_index,
            wpa_plus=wpa_plus,
            wpa_minus=wpa_minus,
            cwpa=cwpa,
            acli=acli,
            re24=re24,
            putouts=putouts,
            innings_pitched=innings_pitched,
            earned_runs=earned_runs,
            home_runs=home_runs,
            era=era,
            batters_faced=batters_faced,
            strikes_by_contact=strikes_by_contact,
            strikes_swinging=strikes_swinging,
            strikes_looking=strikes_looking,
            ground_balls=ground_balls,
            fly_balls=fly_balls,
            line_drives=line_drives,
            inherited_runners=inherited_runners,
            inherited_scores=inherited_scores,
            effective_field_goal_percentage=effective_field_goal_percentage,
            penalty_kicks_made=penalty_kicks_made,
            penalty_kicks_attempted=penalty_kicks_attempted,
            shots_total=shots_total,
            shots_on_target=shots_on_target,
            yellow_cards=yellow_cards,
            red_cards=red_cards,
            touches=touches,
            expected_goals=expected_goals,
            non_penalty_expected_goals=non_penalty_expected_goals,
            expected_assisted_goals=expected_assisted_goals,
            shot_creating_actions=shot_creating_actions,
            goal_creating_actions=goal_creating_actions,
            passes_completed=passes_completed,
            passes_attempted=passes_attempted,
            pass_completion=pass_completion,
            progressive_passes=progressive_passes,
            carries=carries,
            progressive_carries=progressive_carries,
            take_ons_attempted=take_ons_attempted,
            successful_take_ons=successful_take_ons,
            total_passing_distance=total_passing_distance,
            progressive_passing_distance=progressive_passing_distance,
            passes_completed_short=passes_completed_short,
            passes_attempted_short=passes_attempted_short,
            pass_completion_short=pass_completion_short,
            passes_completed_medium=passes_completed_medium,
            passes_attempted_medium=passes_attempted_medium,
            pass_completion_medium=pass_completion_medium,
            passes_completed_long=passes_completed_long,
            passes_attempted_long=passes_attempted_long,
            pass_completion_long=pass_completion_long,
            expected_assists=expected_assists,
            key_passes=key_passes,
            passes_into_final_third=passes_into_final_third,
            passes_into_penalty_area=passes_into_penalty_area,
            crosses_into_penalty_area=crosses_into_penalty_area,
            live_ball_passes=live_ball_passes,
            dead_ball_passes=dead_ball_passes,
            passes_from_free_kicks=passes_from_free_kicks,
            through_balls=through_balls,
            switches=switches,
            crosses=crosses,
            throw_ins_taken=throw_ins_taken,
            corner_kicks=corner_kicks,
            inswinging_corner_kicks=inswinging_corner_kicks,
            outswinging_corner_kicks=outswinging_corner_kicks,
            straight_corner_kicks=straight_corner_kicks,
            passes_offside=passes_offside,
            passes_blocked=passes_blocked,
            tackles_won=tackles_won,
            tackles_in_defensive_third=tackles_in_defensive_third,
            tackles_in_middle_third=tackles_in_middle_third,
            tackles_in_attacking_third=tackles_in_attacking_third,
            dribblers_tackled=dribblers_tackled,
            dribbles_challenged=dribbles_challenged,
            percent_of_dribblers_tackled=percent_of_dribblers_tackled,
            challenges_lost=challenges_lost,
            shots_blocked=shots_blocked,
            tackles_plus_interceptions=tackles_plus_interceptions,
            errors=errors,
            touches_in_defensive_penalty_area=touches_in_defensive_penalty_area,
            touches_in_defensive_third=touches_in_defensive_third,
            touches_in_middle_third=touches_in_middle_third,
            touches_in_attacking_third=touches_in_attacking_third,
            touches_in_attacking_penalty_area=touches_in_attacking_penalty_area,
            live_ball_touches=live_ball_touches,
            successful_take_on_percentage=successful_take_on_percentage,
            times_tackled_during_take_ons=times_tackled_during_take_ons,
            tackled_during_take_ons_percentage=tackled_during_take_ons_percentage,
            total_carrying_distance=total_carrying_distance,
            progressive_carrying_distance=progressive_carrying_distance,
            carries_into_final_third=carries_into_final_third,
            carries_into_penalty_area=carries_into_penalty_area,
            miscontrols=miscontrols,
            dispossessed=dispossessed,
            passes_received=passes_received,
            progressive_passes_received=progressive_passes_received,
            second_yellow_card=second_yellow_card,
            fouls_committed=fouls_committed,
            fouls_drawn=fouls_drawn,
            offsides=offsides,
            penalty_kicks_won=penalty_kicks_won,
            penalty_kicks_conceded=penalty_kicks_conceded,
            own_goals=own_goals,
            ball_recoveries=ball_recoveries,
            aerials_won=aerials_won,
            aerials_lost=aerials_lost,
            percentage_of_aerials_won=percentage_of_aerials_won,
            shots_on_target_against=shots_on_target_against,
            post_shot_expected_goals=post_shot_expected_goals,
            passes_attempted_minus_goal_kicks=passes_attempted_minus_goal_kicks,
            throws_attempted=throws_attempted,
            percentage_of_passes_that_were_launched=percentage_of_passes_that_were_launched,
            average_pass_length=average_pass_length,
            goal_kicks_attempted=goal_kicks_attempted,
            percentage_of_goal_kicks_that_were_launched=percentage_of_goal_kicks_that_were_launched,
            average_goal_kick_length=average_goal_kick_length,
            crosses_faced=crosses_faced,
            crosses_stopped=crosses_stopped,
            percentage_crosses_stopped=percentage_crosses_stopped,
            defensive_actions_outside_penalty_area=defensive_actions_outside_penalty_area,
            average_distance_of_defensive_actions=average_distance_of_defensive_actions,
            three_point_attempt_rate=three_point_attempt_rate,
            tackles=tackles,
            interceptions=interceptions,
            clearances=clearances,
            free_throw_attempt_rate=free_throw_attempt_rate,
            offensive_rebound_percentage=offensive_rebound_percentage,
            defensive_rebound_percentage=defensive_rebound_percentage,
            total_rebound_percentage=total_rebound_percentage,
            assist_percentage=assist_percentage,
            steal_percentage=steal_percentage,
            block_percentage=block_percentage,
            turnover_percentage=turnover_percentage,
            usage_percentage=usage_percentage,
            offensive_rating=offensive_rating,
            defensive_rating=defensive_rating,
            box_plus_minus=box_plus_minus,
        )
    else:
        dt, teams, venue_name = _find_new_dt(
            soup=soup,
            scorebox_meta_div=scorebox_meta_div,
            url=url,
            session=session,
            league=league,
            player_urls=player_urls,
            scores=scores,
            fg=fg,
            fga=fga,
            offensive_rebounds=offensive_rebounds,
            assists=assists,
            turnovers=turnovers,
            positions_validator=positions_validator,
            minutes_played=minutes_played,
            three_point_field_goals=three_point_field_goals,
            three_point_field_goals_attempted=three_point_field_goals_attempted,
            free_throws=free_throws,
            free_throws_attempted=free_throws_attempted,
            defensive_rebounds=defensive_rebounds,
            steals=steals,
            blocks=blocks,
            personal_fouls=personal_fouls,
            player_points=player_points,
            game_scores=game_scores,
            point_differentials=point_differentials,
            goals=goals,
            penalties_in_minutes=penalties_in_minutes,
            even_strength_goals=even_strength_goals,
            power_play_goals=power_play_goals,
            short_handed_goals=short_handed_goals,
            game_winning_goals=game_winning_goals,
            even_strength_assists=even_strength_assists,
            power_play_assists=power_play_assists,
            short_handed_assists=short_handed_assists,
            shots_on_goal=shots_on_goal,
            shooting_percentage=shooting_percentage,
            shifts=shifts,
            time_on_ice=time_on_ice,
            decision=decision,
            goals_against=goals_against,
            shots_against=shots_against,
            saves=saves,
            save_percentage=save_percentage,
            shutouts=shutouts,
            individual_corsi_for_events=individual_corsi_for_events,
            on_shot_ice_for_events=on_shot_ice_for_events,
            on_shot_ice_against_events=on_shot_ice_against_events,
            corsi_for_percentage=corsi_for_percentage,
            relative_corsi_for_percentage=relative_corsi_for_percentage,
            offensive_zone_starts=offensive_zone_starts,
            defensive_zone_starts=defensive_zone_starts,
            offensive_zone_start_percentage=offensive_zone_start_percentage,
            hits=hits,
            true_shooting_percentage=true_shooting_percentage,
            at_bats=at_bats,
            runs_scored=runs_scored,
            runs_batted_in=runs_batted_in,
            bases_on_balls=bases_on_balls,
            strikeouts=strikeouts,
            plate_appearances=plate_appearances,
            hits_at_bats=hits_at_bats,
            obp=obp,
            slg=slg,
            ops=ops,
            pitches=pitches,
            strikes=strikes,
            win_probability_added=win_probability_added,
            average_leverage_index=average_leverage_index,
            wpa_plus=wpa_plus,
            wpa_minus=wpa_minus,
            cwpa=cwpa,
            acli=acli,
            re24=re24,
            putouts=putouts,
            innings_pitched=innings_pitched,
            earned_runs=earned_runs,
            home_runs=home_runs,
            era=era,
            batters_faced=batters_faced,
            strikes_by_contact=strikes_by_contact,
            strikes_swinging=strikes_swinging,
            strikes_looking=strikes_looking,
            ground_balls=ground_balls,
            fly_balls=fly_balls,
            line_drives=line_drives,
            inherited_runners=inherited_runners,
            inherited_scores=inherited_scores,
            effective_field_goal_percentage=effective_field_goal_percentage,
            penalty_kicks_made=penalty_kicks_made,
            penalty_kicks_attempted=penalty_kicks_attempted,
            shots_total=shots_total,
            shots_on_target=shots_on_target,
            yellow_cards=yellow_cards,
            red_cards=red_cards,
            touches=touches,
            expected_goals=expected_goals,
            non_penalty_expected_goals=non_penalty_expected_goals,
            expected_assisted_goals=expected_assisted_goals,
            shot_creating_actions=shot_creating_actions,
            goal_creating_actions=goal_creating_actions,
            passes_completed=passes_completed,
            passes_attempted=passes_attempted,
            pass_completion=pass_completion,
            progressive_passes=progressive_passes,
            carries=carries,
            progressive_carries=progressive_carries,
            take_ons_attempted=take_ons_attempted,
            successful_take_ons=successful_take_ons,
            total_passing_distance=total_passing_distance,
            progressive_passing_distance=progressive_passing_distance,
            passes_completed_short=passes_completed_short,
            passes_attempted_short=passes_attempted_short,
            pass_completion_short=pass_completion_short,
            passes_completed_medium=passes_completed_medium,
            passes_attempted_medium=passes_attempted_medium,
            pass_completion_medium=pass_completion_medium,
            passes_completed_long=passes_completed_long,
            passes_attempted_long=passes_attempted_long,
            pass_completion_long=pass_completion_long,
            expected_assists=expected_assists,
            key_passes=key_passes,
            passes_into_final_third=passes_into_final_third,
            passes_into_penalty_area=passes_into_penalty_area,
            crosses_into_penalty_area=crosses_into_penalty_area,
            live_ball_passes=live_ball_passes,
            dead_ball_passes=dead_ball_passes,
            passes_from_free_kicks=passes_from_free_kicks,
            through_balls=through_balls,
            switches=switches,
            crosses=crosses,
            throw_ins_taken=throw_ins_taken,
            corner_kicks=corner_kicks,
            inswinging_corner_kicks=inswinging_corner_kicks,
            outswinging_corner_kicks=outswinging_corner_kicks,
            straight_corner_kicks=straight_corner_kicks,
            passes_offside=passes_offside,
            passes_blocked=passes_blocked,
            tackles_won=tackles_won,
            tackles_in_defensive_third=tackles_in_defensive_third,
            tackles_in_middle_third=tackles_in_middle_third,
            tackles_in_attacking_third=tackles_in_attacking_third,
            dribblers_tackled=dribblers_tackled,
            dribbles_challenged=dribbles_challenged,
            percent_of_dribblers_tackled=percent_of_dribblers_tackled,
            challenges_lost=challenges_lost,
            shots_blocked=shots_blocked,
            tackles_plus_interceptions=tackles_plus_interceptions,
            errors=errors,
            touches_in_defensive_penalty_area=touches_in_defensive_penalty_area,
            touches_in_defensive_third=touches_in_defensive_third,
            touches_in_middle_third=touches_in_middle_third,
            touches_in_attacking_third=touches_in_attacking_third,
            touches_in_attacking_penalty_area=touches_in_attacking_penalty_area,
            live_ball_touches=live_ball_touches,
            successful_take_on_percentage=successful_take_on_percentage,
            times_tackled_during_take_ons=times_tackled_during_take_ons,
            tackled_during_take_ons_percentage=tackled_during_take_ons_percentage,
            total_carrying_distance=total_carrying_distance,
            progressive_carrying_distance=progressive_carrying_distance,
            carries_into_final_third=carries_into_final_third,
            carries_into_penalty_area=carries_into_penalty_area,
            miscontrols=miscontrols,
            dispossessed=dispossessed,
            passes_received=passes_received,
            progressive_passes_received=progressive_passes_received,
            second_yellow_card=second_yellow_card,
            fouls_committed=fouls_committed,
            fouls_drawn=fouls_drawn,
            offsides=offsides,
            penalty_kicks_won=penalty_kicks_won,
            penalty_kicks_conceded=penalty_kicks_conceded,
            own_goals=own_goals,
            ball_recoveries=ball_recoveries,
            aerials_won=aerials_won,
            aerials_lost=aerials_lost,
            percentage_of_aerials_won=percentage_of_aerials_won,
            shots_on_target_against=shots_on_target_against,
            post_shot_expected_goals=post_shot_expected_goals,
            passes_attempted_minus_goal_kicks=passes_attempted_minus_goal_kicks,
            throws_attempted=throws_attempted,
            percentage_of_passes_that_were_launched=percentage_of_passes_that_were_launched,
            average_pass_length=average_pass_length,
            goal_kicks_attempted=goal_kicks_attempted,
            percentage_of_goal_kicks_that_were_launched=percentage_of_goal_kicks_that_were_launched,
            average_goal_kick_length=average_goal_kick_length,
            crosses_faced=crosses_faced,
            crosses_stopped=crosses_stopped,
            percentage_crosses_stopped=percentage_crosses_stopped,
            defensive_actions_outside_penalty_area=defensive_actions_outside_penalty_area,
            average_distance_of_defensive_actions=average_distance_of_defensive_actions,
            three_point_attempt_rate=three_point_attempt_rate,
            tackles=tackles,
            interceptions=interceptions,
            clearances=clearances,
            free_throw_attempt_rate=free_throw_attempt_rate,
            offensive_rebound_percentage=offensive_rebound_percentage,
            defensive_rebound_percentage=defensive_rebound_percentage,
            total_rebound_percentage=total_rebound_percentage,
            assist_percentage=assist_percentage,
            steal_percentage=steal_percentage,
            block_percentage=block_percentage,
            turnover_percentage=turnover_percentage,
            usage_percentage=usage_percentage,
            offensive_rating=offensive_rating,
            defensive_rating=defensive_rating,
            box_plus_minus=box_plus_minus,
        )
    for team in teams:
        if team.name == "File Not Found":
            raise ValueError("team name is File Not Found (invalid)")

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
            case "Pacific-10 Conference":
                season_type = SeasonType.REGULAR
            case "Great West Conference":
                season_type = SeasonType.REGULAR
            case _:
                logging.warning("Unrecognised Season Text: %s", season_text)
        break

    game_text = soup.get_text().replace("\n", "")
    attendance = None
    if "Attendance:" in game_text:
        attendance_text = (
            game_text.split("Attendance:")[1]
            .strip()
            .split()[0]
            .strip()
            .replace(",", "")
            .replace("Time", "")
            .replace("Show/Hide", "")
            .replace("Team", "")
            .replace("Arena:", "")
            .replace("Copyright", "")
            .replace("Venue:", "")
            .replace("Game", "")
        )
        if attendance_text != "Not":
            attendance = int(attendance_text)

    umpire_urls = []
    for div in soup.find_all("div"):
        for strong in div.find_all("strong"):
            strong_text = strong.get_text().strip().lower()
            if strong_text == "officials:":
                for umpire_a in div.find_all("a", href=True):
                    umpire_url = urllib.parse.urljoin(url, str(umpire_a.get("href")))
                    if "/referees/" in umpire_url and not umpire_url.endswith(
                        "/referees/"
                    ):
                        umpire_urls.append(umpire_url)

    try:
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
            attendance=attendance,
            postponed=None,
            play_off=None,
            distance=None,
            dividends=[],
            pot=None,
            version=version,
            umpires=[
                create_sportsreference_umpire_model(url=x, session=session, dt=dt)
                for x in umpire_urls
            ],
            best_of=None,
        )
    except ValueError as exc:
        logging.error(response.text)
        logging.error(url)
        raise exc


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsreference_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    positions_validator: dict[str, str],
    version: str,
) -> GameModel | None:
    return _create_sportsreference_game_model(
        session=session,
        url=url,
        league=league,
        positions_validator=positions_validator,
        version=version,
    )


def create_sportsreference_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    positions_validator: dict[str, str],
) -> GameModel | None:
    """Create a sports reference game model."""
    if not pytest_is_running.is_running():
        return _cached_create_sportsreference_game_model(
            session=session,
            url=url,
            league=league,
            positions_validator=positions_validator,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_sportsreference_game_model(
            session=session,
            url=url,
            league=league,
            positions_validator=positions_validator,
            version=VERSION,
        )
