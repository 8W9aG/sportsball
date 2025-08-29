"""ESPN team model."""

# pylint: skip-file

# pylint: disable=too-many-arguments,too-many-locals,duplicate-code,too-many-branches,too-many-positional-arguments,too-many-statements

import datetime
import json
import logging
from typing import Any

import pytest_is_running
import requests_cache

from ...cache import MEMORY
from ..combined.most_interesting import more_interesting
from ..google.google_news_model import create_google_news_models
from ..league import League
from ..odds_model import OddsModel
from ..team_model import VERSION, TeamModel
from ..x.x_social_model import create_x_social_model
from .espn_coach_model import create_espn_coach_model
from .espn_player_model import create_espn_player_model

ID_KEY = "id"


def _create_espn_team_model(
    session: requests_cache.CachedSession,
    team: dict[str, Any],
    roster_dict: dict[str, Any],
    odds: list[OddsModel],
    score_dict: dict[str, Any],
    dt: datetime.datetime,
    league: League,
    positions_validator: dict[str, str],
    statistics_dict: dict[str, Any],
    version: str,
) -> TeamModel:
    identifier = team[ID_KEY]
    name = team.get("name", team.get("fullName", team.get("displayName")))
    if name is None:
        raise ValueError("name is null")
    location = team.get("location")
    players = []
    for entity in roster_dict.get("entries", []):
        player = create_espn_player_model(session, entity, dt, positions_validator)
        players.append(player)
    points = None
    try:
        points = score_dict["value"]
    except KeyError:
        points = float(int(team["winner"]))
    coaches_urls = []
    if "coaches" in team:
        try:
            coaches_response = session.get(team["coaches"]["$ref"])
        except KeyError:
            logging.warning("coaches missing for team %s", json.dumps(team))
            raise
        coaches_response.raise_for_status()
        coaches_urls = [x["$ref"] for x in coaches_response.json()["items"]]

    kicks = None
    handballs = None
    disposals = None
    marks = None
    bounces = None
    tackles = None
    tackles_inside_50 = None
    contested_possessions = None
    uncontested_possessions = None
    total_possessions = None
    inside_50s = None
    marks_inside_50 = None
    contested_marks = None
    uncontested_marks = None
    hitouts = None
    one_percenters = None
    disposal_efficiency = None
    clangers = None
    goals = None
    behinds = None
    frees_for = None
    frees_against = None
    total_clearances = None
    centre_clearances = None
    stoppage_clearances = None
    goal_assists = None
    goal_accuracy = None
    rushed_behinds = None
    touched_behinds = None
    left_behinds = None
    left_posters = None
    right_behinds = None
    right_posters = None
    total_interchange_count = None
    interchange_count_q1 = None
    interchange_count_q2 = None
    interchange_count_q3 = None
    interchange_count_q4 = None
    blocked_shots = None
    effective_clearances = None
    effective_tackles = None
    ineffective_tackles = None
    interceptions = None
    tackle_percentage = None
    appearances = None
    average_rating_from_correspondent = None
    average_rating_from_data_feed = None
    average_rating_from_editor = None
    average_rating_from_user = None
    did_not_play = None
    draws = None
    fouls_committed = None
    fouls_suffered = None
    goal_difference = None
    losses = None
    lost_corners = None
    minutes = None
    own_goals = None
    pass_percentage = None
    red_cards = None
    starts = None
    sub_ins = None
    sub_outs = None
    suspensions = None
    time_ended = None
    time_started = None
    win_percentage = None
    wins = None
    won_corners = None
    yellow_cards = None
    clean_sheet = None
    crosses_caught = None
    goals_conceded = None
    partial_clean_sheet = None
    penalty_kick_conceded = None
    penalty_kick_save_percentage = None
    penalty_kicks_faced = None
    penalty_kicks_saved = None
    punches = None
    saves = None
    shoot_out_kicks_faced = None
    shoot_out_kicks_saved = None
    shoot_out_save_percentage = None
    shots_faced = None
    smothers = None
    unclaimed_crosses = None
    accurate_crosses = None
    accurate_long_balls = None
    accurate_passes = None
    accurate_through_balls = None
    cross_percentage = None
    free_kick_goals = None
    free_kick_percentage = None
    free_kick_shots = None
    game_winning_assists = None
    game_winning_goals = None
    goal_assists = None
    headed_goals = None
    inaccurate_crosses = None
    inaccurate_long_balls = None
    inaccurate_passes = None
    inaccurate_through_balls = None
    left_footed_shots = None
    longball_percentage = None
    offsides = None
    penalty_kick_goals = None
    penalty_kick_percentage = None
    penalty_kick_shots = None
    penalty_kicks_missed = None
    possession_percentage = None
    possession_time = None
    right_footed_shots = None
    shoot_out_goals = None
    shoot_out_misses = None
    shoot_out_percentage = None
    shot_assists = None
    shot_percentage = None
    shots_headed = None
    shots_off_target = None
    shots_on_post = None
    shots_on_target = None
    through_ball_percentage = None
    total_crosses = None
    total_goals = None
    total_long_balls = None
    total_passes = None
    total_shots = None
    total_through_balls = None
    hit_by_pitch = None
    ground_balls = None
    strikeouts = None
    rbis = None
    sac_hits = None
    hits = None
    stolen_bases = None
    walks = None
    catcher_interference = None
    runs = None
    gidps = None
    sacrifice_flies = None
    at_bats = None
    home_runs = None
    grand_slam_home_runs = None
    runners_left_on_base = None
    triples = None
    game_winning_rbis = None
    intentional_walks = None
    doubles = None
    fly_balls = None
    caught_stealing = None
    pitches = None
    games_started = None
    pinch_at_bats = None
    pinch_hits = None
    player_rating = None
    is_qualified = None
    is_qualified_steals = None
    total_bases = None
    plate_appearances = None
    projected_home_runs = None
    extra_base_hits = None
    runs_created = None
    batting_average = None
    pinch_average = None
    slug_average = None
    secondary_average = None
    on_base_percentage = None
    ops = None
    ground_to_fly_ratio = None
    runs_created_per_27_outs = None
    batter_rating = None
    at_bats_per_home_run = None
    stolen_base_percentage = None
    pitches_per_plate_appearance = None
    isolated_power = None
    walk_to_strikeout_ratio = None
    walks_per_plate_appearance = None
    secondary_average_minus_batting_average = None
    runs_produced = None
    runs_ratio = None
    patience_ratio = None
    balls_in_play_average = None
    mlb_rating = None
    offensive_wins_above_replacement = None
    wins_above_replacement = None
    earned_runs = None
    batters_hit = None
    sacrifice_bunts = None
    save_opportunities = None
    finishes = None
    balks = None
    batters_faced = None
    holds = None
    complete_games = None
    perfect_games = None
    wild_pitches = None
    third_innings = None
    team_earned_runs = None
    shutouts = None
    pickoff_attempts = None
    pitches = None
    run_support = None
    catcher_interference = None
    pitches_as_starter = None
    average_game_score = None
    quality_starts = None
    inherited_runners = None
    inherited_runners_scored = None
    opponent_total_bases = None
    is_qualified_saves = None
    full_innings = None
    part_innings = None
    blown_saves = None
    era = None
    whip = None
    caught_stealing_percentage = None
    pitches_per_start = None
    pitches_per_inning = None
    pitches_per_plate_appearance = None
    run_support_average = None
    opponent_average = None
    opponent_slug_average = None
    opponent_on_base_percentage = None
    opponent_ops = None
    save_percentage = None
    strikeouts_per_nine_innings = None
    strikeout_to_walk_ratio = None
    tough_losses = None
    cheap_wins = None
    save_opportunities_per_win = None
    pitch_count = None
    strikes = None
    strike_pitch_ratio = None
    games_played = None
    team_games_played = None
    double_plays = None
    opportunities = None
    errors = None
    passed_balls = None
    outfield_assists = None
    pickoffs = None
    putouts = None
    outs_on_field = None
    triple_plays = None
    balls_in_zone = None
    outs_made = None
    catcher_third_innings_played = None
    catcher_caught_stealing = None
    catcher_stolen_bases_allowed = None
    catcher_earned_runs = None
    is_qualified_catcher = None
    is_qualified_pitcher = None
    successful_chances = None
    total_chances = None
    full_innings_played = None
    part_innings_played = None
    fielding_percentage = None
    range_factor = None
    zone_rating = None
    catcher_caught_stealing_percentage = None
    catcher_era = None
    def_warbr = None
    innings = None
    assists = None
    extra_bases = None
    blocks = None
    defensive_rebounds = None
    steals = None
    turnover_points = None
    average_defensive_rebounds = None
    average_blocks = None
    average_steals = None
    average_48_defensive_rebounds = None
    average_48_blocks = None
    average_48_steals = None
    largest_lead = None
    disqualifications = None
    flagrant_fouls = None
    fouls = None
    ejections = None
    technical_fouls = None
    rebounds = None
    vorp = None
    average_minutes = None
    nba_rating = None
    average_rebounds = None
    average_fouls = None
    average_flagrant_fouls = None
    average_technical_fouls = None
    average_ejections = None
    average_disqualifications = None
    assist_turnover_ratio = None
    steal_foul_ratio = None
    block_foul_ratio = None
    average_team_rebounds = None
    total_rebounds = None
    total_technical_fouls = None
    team_assist_turnover_ratio = None
    steal_turnover_ratio = None
    average_48_rebounds = None
    average_48_fouls = None
    average_48_flagrant_fouls = None
    average_48_technical_fouls = None
    average_48_ejections = None
    average_48_disqualifications = None
    double_double = None
    triple_double = None
    field_goals = None
    field_goals_attempted = None
    field_goals_made = None
    field_goal_percentage = None
    free_throws = None
    free_throw_percentage = None
    free_throws_attempted = None
    free_throws_made = None
    offensive_rebounds = None
    turnovers = None
    three_point_percentage = None
    three_point_field_goals_attempted = None
    three_point_field_goals_made = None
    team_turnovers = None
    total_turnovers = None
    points_in_paint = None
    brick_index = None
    fast_break_points = None
    average_field_goals_made = None
    average_field_goals_attempted = None
    average_three_point_field_goals_made = None
    average_three_point_field_goals_attempted = None
    average_free_throws_made = None
    average_free_throws_attempted = None
    average_points = None
    average_offensive_rebounds = None
    average_assists = None
    average_turnovers = None
    offensive_rebound_percentage = None
    estimated_possessions = None
    average_estimated_possessions = None
    points_per_estimated_possessions = None
    average_team_turnovers = None
    average_total_turnovers = None
    three_point_field_goal_percentage = None
    two_point_field_goals_made = None
    two_point_field_goals_attempted = None
    average_two_point_field_goals_made = None
    average_two_point_field_goals_attempted = None
    two_point_field_goal_percentage = None
    shooting_efficiency = None
    scoring_efficiency = None
    average_48_field_goals_made = None
    average_48_field_goals_attempted = None
    average_48_three_point_field_goals_made = None
    average_48_three_point_field_goals_attempted = None
    average_48_free_throws_made = None
    average_48_free_throws_attempted = None
    average_48_points = None
    average_48_offensive_rebounds = None
    average_48_assists = None
    average_48_turnovers = None
    if "splits" in statistics_dict:
        for category in statistics_dict["splits"]["categories"]:
            for stat in category["stats"]:
                if stat["name"] == "kicks":
                    kicks = more_interesting(kicks, stat["value"])
                elif stat["name"] == "handballs":
                    handballs = more_interesting(handballs, stat["value"])
                elif stat["name"] == "disposals":
                    disposals = more_interesting(disposals, stat["value"])
                elif stat["name"] == "marks":
                    marks = more_interesting(marks, stat["value"])
                elif stat["name"] == "bounces":
                    bounces = more_interesting(bounces, stat["value"])
                elif stat["name"] == "tackles":
                    tackles = more_interesting(tackles, stat["value"])
                elif stat["name"] == "tacklesInside50":
                    tackles_inside_50 = more_interesting(
                        tackles_inside_50, stat["value"]
                    )
                elif stat["name"] == "contestedPossessions":
                    contested_possessions = more_interesting(
                        contested_possessions, stat["value"]
                    )
                elif stat["name"] == "uncontestedPossessions":
                    uncontested_possessions = more_interesting(
                        uncontested_possessions, stat["value"]
                    )
                elif stat["name"] == "totalPossessions":
                    total_possessions = more_interesting(
                        total_possessions, stat["value"]
                    )
                elif stat["name"] == "inside50s":
                    inside_50s = more_interesting(inside_50s, stat["value"])
                elif stat["name"] == "marksInside50":
                    marks_inside_50 = more_interesting(marks_inside_50, stat["value"])
                elif stat["name"] == "contestedMarks":
                    contested_marks = more_interesting(contested_marks, stat["value"])
                elif stat["name"] == "uncontestedMarks":
                    uncontested_marks = more_interesting(
                        uncontested_marks, stat["value"]
                    )
                elif stat["name"] == "hitouts":
                    hitouts = more_interesting(hitouts, stat["value"])
                elif stat["name"] == "onePercenters":
                    one_percenters = more_interesting(one_percenters, stat["value"])
                elif stat["name"] == "disposalEfficiency":
                    disposal_efficiency = more_interesting(
                        disposal_efficiency, stat["value"]
                    )
                elif stat["name"] == "clangers":
                    clangers = more_interesting(clangers, stat["value"])
                elif stat["name"] == "goals":
                    goals = more_interesting(goals, stat["value"])
                elif stat["name"] == "behinds":
                    behinds = more_interesting(behinds, stat["value"])
                elif stat["name"] == "freesFor":
                    frees_for = more_interesting(frees_for, stat["value"])
                elif stat["name"] == "freesAgainst":
                    frees_against = more_interesting(frees_against, stat["value"])
                elif stat["name"] == "totalClearances":
                    total_clearances = more_interesting(total_clearances, stat["value"])
                elif stat["name"] == "centreClearances":
                    centre_clearances = more_interesting(
                        centre_clearances, stat["value"]
                    )
                elif stat["name"] == "stoppageClearances":
                    stoppage_clearances = more_interesting(
                        stoppage_clearances, stat["value"]
                    )
                elif stat["name"] == "rebound50s":
                    rebounds = more_interesting(rebounds, stat["value"])
                elif stat["name"] == "goalAssists":
                    goal_assists = more_interesting(goal_assists, stat["value"])
                elif stat["name"] == "goalAccuracy":
                    goal_accuracy = more_interesting(goal_accuracy, stat["value"])
                elif stat["name"] == "rushedBehinds":
                    rushed_behinds = more_interesting(rushed_behinds, stat["value"])
                elif stat["name"] == "touchedBehinds":
                    touched_behinds = more_interesting(touched_behinds, stat["value"])
                elif stat["name"] == "leftBehinds":
                    left_behinds = more_interesting(left_behinds, stat["value"])
                elif stat["name"] == "leftPosters":
                    left_posters = more_interesting(left_posters, stat["value"])
                elif stat["name"] == "rightBehinds":
                    right_behinds = more_interesting(right_behinds, stat["value"])
                elif stat["name"] == "rightPosters":
                    right_posters = more_interesting(right_posters, stat["value"])
                elif stat["name"] == "totalInterchangeCount":
                    total_interchange_count = more_interesting(
                        total_interchange_count, stat["value"]
                    )
                elif stat["name"] == "interchangeCountQ1":
                    interchange_count_q1 = more_interesting(
                        interchange_count_q1, stat["value"]
                    )
                elif stat["name"] == "interchangeCountQ2":
                    interchange_count_q2 = more_interesting(
                        interchange_count_q2, stat["value"]
                    )
                elif stat["name"] == "interchangeCountQ3":
                    interchange_count_q3 = more_interesting(
                        interchange_count_q3, stat["value"]
                    )
                elif stat["name"] == "interchangeCountQ4":
                    interchange_count_q4 = more_interesting(
                        interchange_count_q4, stat["value"]
                    )
                elif stat["name"] == "blockedShots":
                    blocked_shots = more_interesting(blocked_shots, stat["value"])
                elif stat["name"] == "effectiveClearance":
                    effective_clearances = more_interesting(
                        effective_clearances, stat["value"]
                    )
                elif stat["name"] == "effectiveTackles":
                    effective_tackles = more_interesting(
                        effective_tackles, stat["value"]
                    )
                elif stat["name"] == "inneffectiveTackles":
                    ineffective_tackles = more_interesting(
                        ineffective_tackles, stat["value"]
                    )
                elif stat["name"] == "interceptions":
                    interceptions = more_interesting(interceptions, stat["value"])
                elif stat["name"] == "tacklePct":
                    tackle_percentage = more_interesting(
                        tackle_percentage, stat["value"]
                    )
                elif stat["name"] == "totalClearance":
                    total_clearances = more_interesting(total_clearances, stat["value"])
                elif stat["name"] == "totalTackles":
                    tackles = more_interesting(tackles, stat["value"])
                elif stat["name"] == "appearances":
                    appearances = more_interesting(appearances, stat["value"])
                elif stat["name"] == "avgRatingFromCorrespondent":
                    average_rating_from_correspondent = more_interesting(
                        average_rating_from_correspondent, stat["value"]
                    )
                elif stat["name"] == "avgRatingFromDataFeed":
                    average_rating_from_data_feed = more_interesting(
                        average_rating_from_data_feed, stat["value"]
                    )
                elif stat["name"] == "avgRatingFromEditor":
                    average_rating_from_editor = more_interesting(
                        average_rating_from_editor, stat["value"]
                    )
                elif stat["name"] == "avgRatingFromUser":
                    average_rating_from_user = more_interesting(
                        average_rating_from_user, stat["value"]
                    )
                elif stat["name"] == "dnp":
                    did_not_play = more_interesting(did_not_play, stat["value"])
                elif stat["name"] == "draws":
                    draws = more_interesting(draws, stat["value"])
                elif stat["name"] == "foulsCommitted":
                    fouls_committed = more_interesting(fouls_committed, stat["value"])
                elif stat["name"] == "foulsSuffered":
                    fouls_suffered = more_interesting(fouls_suffered, stat["value"])
                elif stat["name"] == "goalDifference":
                    goal_difference = more_interesting(goal_difference, stat["value"])
                elif stat["name"] == "handBalls":
                    handballs = more_interesting(handballs, stat["value"])
                elif stat["name"] == "losses":
                    losses = more_interesting(losses, stat["value"])
                elif stat["name"] == "lostCorners":
                    lost_corners = more_interesting(lost_corners, stat["value"])
                elif stat["name"] == "minutes":
                    minutes = more_interesting(minutes, stat["value"])
                elif stat["name"] == "ownGoals":
                    own_goals = more_interesting(own_goals, stat["value"])
                elif stat["name"] == "passPct":
                    pass_percentage = more_interesting(pass_percentage, stat["value"])
                elif stat["name"] == "redCards":
                    red_cards = more_interesting(red_cards, stat["value"])
                elif stat["name"] == "starts":
                    starts = more_interesting(starts, stat["value"])
                elif stat["name"] == "subIns":
                    sub_ins = more_interesting(sub_ins, stat["value"])
                elif stat["name"] == "subOuts":
                    sub_outs = more_interesting(sub_outs, stat["value"])
                elif stat["name"] == "suspensions":
                    suspensions = more_interesting(suspensions, stat["value"])
                elif stat["name"] == "timeEnded":
                    time_ended = more_interesting(time_ended, stat["value"])
                elif stat["name"] == "timeStarted":
                    time_started = more_interesting(time_started, stat["value"])
                elif stat["name"] == "winPct":
                    win_percentage = more_interesting(win_percentage, stat["value"])
                elif stat["name"] == "wins":
                    wins = more_interesting(wins, stat["value"])
                elif stat["name"] == "wonCorners":
                    won_corners = more_interesting(won_corners, stat["value"])
                elif stat["name"] == "yellowCards":
                    yellow_cards = more_interesting(yellow_cards, stat["value"])
                elif stat["name"] == "cleanSheet":
                    clean_sheet = more_interesting(clean_sheet, stat["value"])
                elif stat["name"] == "crossesCaught":
                    crosses_caught = more_interesting(crosses_caught, stat["value"])
                elif stat["name"] == "goalsConceded":
                    goals_conceded = more_interesting(goals_conceded, stat["value"])
                elif stat["name"] == "partialCleenSheet":
                    partial_clean_sheet = more_interesting(
                        partial_clean_sheet, stat["value"]
                    )
                elif stat["name"] == "penaltyKickConceded":
                    penalty_kick_conceded = more_interesting(
                        penalty_kick_conceded, stat["value"]
                    )
                elif stat["name"] == "penaltyKickSavePct":
                    penalty_kick_save_percentage = more_interesting(
                        penalty_kick_save_percentage, stat["value"]
                    )
                elif stat["name"] == "penaltyKicksFaced":
                    penalty_kicks_faced = more_interesting(
                        penalty_kicks_faced, stat["value"]
                    )
                elif stat["name"] == "penaltyKicksSaved":
                    penalty_kicks_saved = more_interesting(
                        penalty_kicks_saved, stat["value"]
                    )
                elif stat["name"] == "punches":
                    punches = more_interesting(punches, stat["value"])
                elif stat["name"] == "saves":
                    saves = more_interesting(saves, stat["value"])
                elif stat["name"] == "shootOutKicksFaced":
                    shoot_out_kicks_faced = more_interesting(
                        shoot_out_kicks_faced, stat["value"]
                    )
                elif stat["name"] == "shootOutKicksSaved":
                    shoot_out_kicks_saved = more_interesting(
                        shoot_out_kicks_saved, stat["value"]
                    )
                elif stat["name"] == "shootOutSavePct":
                    shoot_out_save_percentage = more_interesting(
                        shoot_out_save_percentage, stat["value"]
                    )
                elif stat["name"] == "shotsFaced":
                    shots_faced = more_interesting(shots_faced, stat["value"])
                elif stat["name"] == "smothers":
                    smothers = more_interesting(smothers, stat["value"])
                elif stat["name"] == "unclaimedCrosses":
                    unclaimed_crosses = more_interesting(
                        unclaimed_crosses, stat["value"]
                    )
                elif stat["name"] == "accurateCrosses":
                    accurate_crosses = more_interesting(accurate_crosses, stat["value"])
                elif stat["name"] == "accurateLongBalls":
                    accurate_long_balls = more_interesting(
                        accurate_long_balls, stat["value"]
                    )
                elif stat["name"] == "accuratePasses":
                    accurate_passes = more_interesting(accurate_passes, stat["value"])
                elif stat["name"] == "accurateThroughBalls":
                    accurate_through_balls = more_interesting(
                        accurate_through_balls, stat["value"]
                    )
                elif stat["name"] == "crossPct":
                    cross_percentage = more_interesting(cross_percentage, stat["value"])
                elif stat["name"] == "freeKickGoals":
                    free_kick_goals = more_interesting(free_kick_goals, stat["value"])
                elif stat["name"] == "freeKickPct":
                    free_kick_percentage = more_interesting(
                        free_kick_percentage, stat["value"]
                    )
                elif stat["name"] == "freeKickShots":
                    free_kick_shots = more_interesting(free_kick_shots, stat["value"])
                elif stat["name"] == "gameWinningAssists":
                    game_winning_assists = more_interesting(
                        game_winning_assists, stat["value"]
                    )
                elif stat["name"] == "gameWinningGoals":
                    game_winning_goals = more_interesting(
                        game_winning_goals, stat["value"]
                    )
                elif stat["name"] == "headedGoals":
                    headed_goals = more_interesting(headed_goals, stat["value"])
                elif stat["name"] == "inaccurateCrosses":
                    inaccurate_crosses = more_interesting(
                        inaccurate_crosses, stat["value"]
                    )
                elif stat["name"] == "inaccurateLongBalls":
                    inaccurate_long_balls = more_interesting(
                        inaccurate_long_balls, stat["value"]
                    )
                elif stat["name"] == "inaccuratePasses":
                    inaccurate_passes = more_interesting(
                        inaccurate_passes, stat["value"]
                    )
                elif stat["name"] == "inaccurateThroughBalls":
                    inaccurate_through_balls = more_interesting(
                        inaccurate_through_balls, stat["value"]
                    )
                elif stat["name"] == "leftFootedShots":
                    left_footed_shots = more_interesting(
                        left_footed_shots, stat["value"]
                    )
                elif stat["name"] == "longballPct":
                    longball_percentage = more_interesting(
                        longball_percentage, stat["value"]
                    )
                elif stat["name"] == "offsides":
                    offsides = more_interesting(offsides, stat["value"])
                elif stat["name"] == "penaltyKickGoals":
                    penalty_kick_goals = more_interesting(
                        penalty_kick_goals, stat["value"]
                    )
                elif stat["name"] == "penaltyKickPct":
                    penalty_kick_percentage = more_interesting(
                        penalty_kick_percentage, stat["value"]
                    )
                elif stat["name"] == "penaltyKickShots":
                    penalty_kick_shots = more_interesting(
                        penalty_kick_shots, stat["value"]
                    )
                elif stat["name"] == "penaltyKicksMissed":
                    penalty_kicks_missed = more_interesting(
                        penalty_kicks_missed, stat["value"]
                    )
                elif stat["name"] == "possessionPct":
                    possession_percentage = more_interesting(
                        possession_percentage, stat["value"]
                    )
                elif stat["name"] == "possessionTime":
                    possession_time = more_interesting(possession_time, stat["value"])
                elif stat["name"] == "rightFootedShots":
                    right_footed_shots = more_interesting(
                        right_footed_shots, stat["value"]
                    )
                elif stat["name"] == "shootOutGoals":
                    shoot_out_goals = more_interesting(shoot_out_goals, stat["value"])
                elif stat["name"] == "shootOutMisses":
                    shoot_out_misses = more_interesting(shoot_out_misses, stat["value"])
                elif stat["name"] == "shootOutPct":
                    shoot_out_percentage = more_interesting(
                        shoot_out_percentage, stat["value"]
                    )
                elif stat["name"] == "shotAssists":
                    shot_assists = more_interesting(shot_assists, stat["value"])
                elif stat["name"] == "shotPct":
                    shot_percentage = more_interesting(shot_percentage, stat["value"])
                elif stat["name"] == "shotsHeaded":
                    shots_headed = more_interesting(shots_headed, stat["value"])
                elif stat["name"] == "shotsOffTarget":
                    shots_off_target = more_interesting(shots_off_target, stat["value"])
                elif stat["name"] == "shotsOnPost":
                    shots_on_post = more_interesting(shots_on_post, stat["value"])
                elif stat["name"] == "shotsOnTarget":
                    shots_on_target = more_interesting(shots_on_target, stat["value"])
                elif stat["name"] == "throughBallPct":
                    through_ball_percentage = more_interesting(
                        through_ball_percentage, stat["value"]
                    )
                elif stat["name"] == "totalCrosses":
                    total_crosses = more_interesting(total_crosses, stat["value"])
                elif stat["name"] == "totalGoals":
                    total_goals = more_interesting(total_goals, stat["value"])
                elif stat["name"] == "totalLongBalls":
                    total_long_balls = more_interesting(total_long_balls, stat["value"])
                elif stat["name"] == "totalPasses":
                    total_passes = more_interesting(total_passes, stat["value"])
                elif stat["name"] == "totalShots":
                    total_shots = more_interesting(total_shots, stat["value"])
                elif stat["name"] == "totalThroughBalls":
                    total_through_balls = more_interesting(
                        total_through_balls, stat["value"]
                    )
                elif stat["name"] == "hitByPitch":
                    hit_by_pitch = more_interesting(hit_by_pitch, stat["value"])
                elif stat["name"] == "groundBalls":
                    ground_balls = more_interesting(ground_balls, stat["value"])
                elif stat["name"] == "strikeouts":
                    strikeouts = more_interesting(strikeouts, stat["value"])
                elif stat["name"] == "RBIs":
                    rbis = more_interesting(rbis, stat["value"])
                elif stat["name"] == "sacHits":
                    sac_hits = more_interesting(sac_hits, stat["value"])
                elif stat["name"] == "hits":
                    hits = more_interesting(hits, stat["value"])
                elif stat["name"] == "stolenBases":
                    stolen_bases = more_interesting(stolen_bases, stat["value"])
                elif stat["name"] == "walks":
                    walks = more_interesting(walks, stat["value"])
                elif stat["name"] == "catcherInterference":
                    catcher_interference = more_interesting(
                        catcher_interference, stat["value"]
                    )
                elif stat["name"] == "runs":
                    runs = more_interesting(runs, stat["value"])
                elif stat["name"] == "GIDPs":
                    gidps = more_interesting(gidps, stat["value"])
                elif stat["name"] == "sacFlies":
                    sacrifice_flies = more_interesting(sacrifice_flies, stat["value"])
                elif stat["name"] == "atBats":
                    at_bats = more_interesting(at_bats, stat["value"])
                elif stat["name"] == "homeRuns":
                    home_runs = more_interesting(home_runs, stat["value"])
                elif stat["name"] == "grandSlamHomeRuns":
                    grand_slam_home_runs = more_interesting(
                        grand_slam_home_runs, stat["value"]
                    )
                elif stat["name"] == "runnersLeftOnBase":
                    runners_left_on_base = more_interesting(
                        runners_left_on_base, stat["value"]
                    )
                elif stat["name"] == "triples":
                    triples = more_interesting(triples, stat["value"])
                elif stat["name"] == "gameWinningRBIs":
                    game_winning_rbis = more_interesting(
                        game_winning_rbis, stat["value"]
                    )
                elif stat["name"] == "intentionalWalks":
                    intentional_walks = more_interesting(
                        intentional_walks, stat["value"]
                    )
                elif stat["name"] == "doubles":
                    doubles = more_interesting(doubles, stat["value"])
                elif stat["name"] == "flyBalls":
                    fly_balls = more_interesting(fly_balls, stat["value"])
                elif stat["name"] == "caughtStealing":
                    caught_stealing = more_interesting(caught_stealing, stat["value"])
                elif stat["name"] == "pitches":
                    pitches = more_interesting(pitches, stat["value"])
                elif stat["name"] == "gamesStarted":
                    games_started = more_interesting(games_started, stat["value"])
                elif stat["name"] == "pinchAtBats":
                    pinch_at_bats = more_interesting(pinch_at_bats, stat["value"])
                elif stat["name"] == "pinchHits":
                    pinch_hits = more_interesting(pinch_hits, stat["value"])
                elif stat["name"] == "playerRating":
                    player_rating = more_interesting(player_rating, stat["value"])
                elif stat["name"] == "isQualified":
                    is_qualified = more_interesting(is_qualified, stat["value"])
                elif stat["name"] == "isQualifiedSteals":
                    is_qualified_steals = more_interesting(
                        is_qualified_steals, stat["value"]
                    )
                elif stat["name"] == "totalBases":
                    total_bases = more_interesting(total_bases, stat["value"])
                elif stat["name"] == "plateAppearances":
                    plate_appearances = more_interesting(
                        plate_appearances, stat["value"]
                    )
                elif stat["name"] == "projectedHomeRuns":
                    projected_home_runs = more_interesting(
                        projected_home_runs, stat["value"]
                    )
                elif stat["name"] == "extraBaseHits":
                    extra_base_hits = more_interesting(extra_base_hits, stat["value"])
                elif stat["name"] == "runsCreated":
                    runs_created = more_interesting(runs_created, stat["value"])
                elif stat["name"] == "avg":
                    batting_average = more_interesting(batting_average, stat["value"])
                elif stat["name"] == "pinchAvg":
                    pinch_average = more_interesting(pinch_average, stat["value"])
                elif stat["name"] == "slugAvg":
                    slug_average = more_interesting(slug_average, stat["value"])
                elif stat["name"] == "secondaryAvg":
                    secondary_average = more_interesting(
                        secondary_average, stat["value"]
                    )
                elif stat["name"] == "onBasePct":
                    on_base_percentage = more_interesting(
                        on_base_percentage, stat["value"]
                    )
                elif stat["name"] == "OPS":
                    ops = more_interesting(ops, stat["value"])
                elif stat["name"] == "groundToFlyRatio":
                    ground_to_fly_ratio = more_interesting(
                        ground_to_fly_ratio, stat["value"]
                    )
                elif stat["name"] == "runsCreatedPer27Outs":
                    runs_created_per_27_outs = more_interesting(
                        runs_created_per_27_outs, stat["value"]
                    )
                elif stat["name"] == "batterRating":
                    batter_rating = more_interesting(batter_rating, stat["value"])
                elif stat["name"] == "atBatsPerHomeRun":
                    at_bats_per_home_run = more_interesting(
                        at_bats_per_home_run, stat["value"]
                    )
                elif stat["name"] == "stolenBasePct":
                    stolen_base_percentage = more_interesting(
                        stolen_base_percentage, stat["value"]
                    )
                elif stat["name"] == "pitchesPerPlateAppearance":
                    pitches_per_plate_appearance = more_interesting(
                        pitches_per_plate_appearance, stat["value"]
                    )
                elif stat["name"] == "isolatedPower":
                    isolated_power = more_interesting(isolated_power, stat["value"])
                elif stat["name"] == "walkToStrikeoutRatio":
                    walk_to_strikeout_ratio = more_interesting(
                        walk_to_strikeout_ratio, stat["value"]
                    )
                elif stat["name"] == "walksPerPlateAppearance":
                    walks_per_plate_appearance = more_interesting(
                        walks_per_plate_appearance, stat["value"]
                    )
                elif stat["name"] == "secondaryAvgMinusBA":
                    secondary_average_minus_batting_average = more_interesting(
                        secondary_average_minus_batting_average, stat["value"]
                    )
                elif stat["name"] == "runsProduced":
                    runs_produced = more_interesting(runs_produced, stat["value"])
                elif stat["name"] == "runsRatio":
                    runs_ratio = more_interesting(runs_ratio, stat["value"])
                elif stat["name"] == "patienceRatio":
                    patience_ratio = more_interesting(patience_ratio, stat["value"])
                elif stat["name"] == "BIPA":
                    balls_in_play_average = more_interesting(
                        balls_in_play_average, stat["value"]
                    )
                elif stat["name"] == "MLBRating":
                    mlb_rating = more_interesting(mlb_rating, stat["value"])
                elif stat["name"] == "offWARBR":
                    offensive_wins_above_replacement = more_interesting(
                        offensive_wins_above_replacement, stat["value"]
                    )
                elif stat["name"] == "WARBR":
                    wins_above_replacement = more_interesting(
                        wins_above_replacement, stat["value"]
                    )
                elif stat["name"] == "earnedRuns":
                    earned_runs = more_interesting(earned_runs, stat["value"])
                elif stat["name"] == "battersHit":
                    batters_hit = more_interesting(batters_hit, stat["value"])
                elif stat["name"] == "sacBunts":
                    sacrifice_bunts = more_interesting(sacrifice_bunts, stat["value"])
                elif stat["name"] == "saveOpportunities":
                    save_opportunities = more_interesting(
                        save_opportunities, stat["value"]
                    )
                elif stat["name"] == "finishes":
                    finishes = more_interesting(finishes, stat["value"])
                elif stat["name"] == "balks":
                    balks = more_interesting(balks, stat["value"])
                elif stat["name"] == "battersFaced":
                    batters_faced = more_interesting(batters_faced, stat["value"])
                elif stat["name"] == "holds":
                    holds = more_interesting(holds, stat["value"])
                elif stat["name"] == "completeGames":
                    complete_games = more_interesting(complete_games, stat["value"])
                elif stat["name"] == "perfectGames":
                    perfect_games = more_interesting(perfect_games, stat["value"])
                elif stat["name"] == "wildPitches":
                    wild_pitches = more_interesting(wild_pitches, stat["value"])
                elif stat["name"] == "thirdInnings":
                    third_innings = more_interesting(third_innings, stat["value"])
                elif stat["name"] == "teamEarnedRuns":
                    team_earned_runs = more_interesting(team_earned_runs, stat["value"])
                elif stat["name"] == "shutouts":
                    shutouts = more_interesting(shutouts, stat["value"])
                elif stat["name"] == "pickoffAttempts":
                    pickoff_attempts = more_interesting(pickoff_attempts, stat["value"])
                elif stat["name"] == "pitches":
                    pitches = more_interesting(pitches, stat["value"])
                elif stat["name"] == "runSupport":
                    run_support = more_interesting(run_support, stat["value"])
                elif stat["name"] == "catcherInterference":
                    catcher_interference = more_interesting(
                        catcher_interference, stat["value"]
                    )
                elif stat["name"] == "pitchesAsStarter":
                    pitches_as_starter = more_interesting(
                        pitches_as_starter, stat["value"]
                    )
                elif stat["name"] == "avgGameScore":
                    average_game_score = more_interesting(
                        average_game_score, stat["value"]
                    )
                elif stat["name"] == "qualityStarts":
                    quality_starts = more_interesting(quality_starts, stat["value"])
                elif stat["name"] == "inheritedRunners":
                    inherited_runners = more_interesting(
                        inherited_runners, stat["value"]
                    )
                elif stat["name"] == "inheritedRunnersScored":
                    inherited_runners_scored = more_interesting(
                        inherited_runners_scored, stat["value"]
                    )
                elif stat["name"] == "opponentTotalBases":
                    opponent_total_bases = more_interesting(
                        opponent_total_bases, stat["value"]
                    )
                elif stat["name"] == "isQualifiedSaves":
                    is_qualified_saves = more_interesting(
                        is_qualified_saves, stat["value"]
                    )
                elif stat["name"] == "fullInnings":
                    full_innings = more_interesting(full_innings, stat["value"])
                elif stat["name"] == "partInnings":
                    part_innings = more_interesting(part_innings, stat["value"])
                elif stat["name"] == "blownSaves":
                    blown_saves = more_interesting(blown_saves, stat["value"])
                elif stat["name"] == "innings":
                    innings = more_interesting(innings, stat["value"])
                elif stat["name"] == "ERA":
                    era = more_interesting(era, stat["value"])
                elif stat["name"] == "WHIP":
                    whip = more_interesting(whip, stat["value"])
                elif stat["name"] == "caughtStealingPct":
                    caught_stealing_percentage = more_interesting(
                        caught_stealing_percentage, stat["value"]
                    )
                elif stat["name"] == "pitchesPerStart":
                    pitches_per_start = more_interesting(
                        pitches_per_start, stat["value"]
                    )
                elif stat["name"] == "pitchesPerInning":
                    pitches_per_inning = more_interesting(
                        pitches_per_inning, stat["value"]
                    )
                elif stat["name"] == "pitchesPerPlateAppearance":
                    pitches_per_plate_appearance = more_interesting(
                        pitches_per_plate_appearance, stat["value"]
                    )
                elif stat["name"] == "runSupportAvg":
                    run_support_average = more_interesting(
                        run_support_average, stat["value"]
                    )
                elif stat["name"] == "opponentAvg":
                    opponent_average = more_interesting(opponent_average, stat["value"])
                elif stat["name"] == "opponentSlugAvg":
                    opponent_slug_average = more_interesting(
                        opponent_slug_average, stat["value"]
                    )
                elif stat["name"] == "opponentOnBasePct":
                    opponent_on_base_percentage = more_interesting(
                        opponent_on_base_percentage, stat["value"]
                    )
                elif stat["name"] == "opponentOPS":
                    opponent_ops = more_interesting(opponent_ops, stat["value"])
                elif stat["name"] == "savePct":
                    save_percentage = more_interesting(save_percentage, stat["value"])
                elif stat["name"] == "strikeoutsPerNineInnings":
                    strikeouts_per_nine_innings = more_interesting(
                        strikeouts_per_nine_innings, stat["value"]
                    )
                elif stat["name"] == "strikeoutToWalkRatio":
                    strikeout_to_walk_ratio = more_interesting(
                        strikeout_to_walk_ratio, stat["value"]
                    )
                elif stat["name"] == "toughLosses":
                    tough_losses = more_interesting(tough_losses, stat["value"])
                elif stat["name"] == "cheapWins":
                    cheap_wins = more_interesting(cheap_wins, stat["value"])
                elif stat["name"] == "saveOpportunitiesPerWin":
                    save_opportunities_per_win = more_interesting(
                        save_opportunities_per_win, stat["value"]
                    )
                elif stat["name"] == "pitchCount":
                    pitch_count = more_interesting(pitch_count, stat["value"])
                elif stat["name"] == "strikes":
                    strikes = more_interesting(strikes, stat["value"])
                elif stat["name"] == "strikePitchRatio":
                    strike_pitch_ratio = more_interesting(
                        strike_pitch_ratio, stat["value"]
                    )
                elif stat["name"] == "gamesPlayed":
                    games_played = more_interesting(games_played, stat["value"])
                elif stat["name"] == "teamGamesPlayed":
                    team_games_played = more_interesting(
                        team_games_played, stat["value"]
                    )
                elif stat["name"] == "doublePlays":
                    double_plays = more_interesting(double_plays, stat["value"])
                elif stat["name"] == "opportunities":
                    opportunities = more_interesting(opportunities, stat["value"])
                elif stat["name"] == "errors":
                    errors = more_interesting(errors, stat["value"])
                elif stat["name"] == "passedBalls":
                    passed_balls = more_interesting(passed_balls, stat["value"])
                elif stat["name"] == "assists":
                    assists = more_interesting(assists, stat["value"])
                elif stat["name"] == "outfieldAssists":
                    outfield_assists = more_interesting(outfield_assists, stat["value"])
                elif stat["name"] == "pickoffs":
                    pickoffs = more_interesting(pickoffs, stat["value"])
                elif stat["name"] == "putouts":
                    putouts = more_interesting(putouts, stat["value"])
                elif stat["name"] == "outsOnField":
                    outs_on_field = more_interesting(outs_on_field, stat["value"])
                elif stat["name"] == "triplePlays":
                    triple_plays = more_interesting(triple_plays, stat["value"])
                elif stat["name"] == "ballsInZone":
                    balls_in_zone = more_interesting(balls_in_zone, stat["value"])
                elif stat["name"] == "extraBases":
                    extra_bases = more_interesting(extra_bases, stat["value"])
                elif stat["name"] == "outsMade":
                    outs_made = more_interesting(outs_made, stat["value"])
                elif stat["name"] == "catcherThirdInningsPlayed":
                    catcher_third_innings_played = more_interesting(
                        catcher_third_innings_played, stat["value"]
                    )
                elif stat["name"] == "catcherCaughtStealing":
                    catcher_caught_stealing = more_interesting(
                        catcher_caught_stealing, stat["value"]
                    )
                elif stat["name"] == "catcherStolenBasesAllowed":
                    catcher_stolen_bases_allowed = more_interesting(
                        catcher_stolen_bases_allowed, stat["value"]
                    )
                elif stat["name"] == "catcherEarnedRuns":
                    catcher_earned_runs = more_interesting(
                        catcher_earned_runs, stat["value"]
                    )
                elif stat["name"] == "isQualifiedCatcher":
                    is_qualified_catcher = more_interesting(
                        is_qualified_catcher, stat["value"]
                    )
                elif stat["name"] == "isQualifiedPitcher":
                    is_qualified_pitcher = more_interesting(
                        is_qualified_pitcher, stat["value"]
                    )
                elif stat["name"] == "successfulChances":
                    successful_chances = more_interesting(
                        successful_chances, stat["value"]
                    )
                elif stat["name"] == "totalChances":
                    total_chances = more_interesting(total_chances, stat["value"])
                elif stat["name"] == "fullInningsPlayed":
                    full_innings_played = more_interesting(
                        full_innings_played, stat["value"]
                    )
                elif stat["name"] == "partInningsPlayed":
                    part_innings_played = more_interesting(
                        part_innings_played, stat["value"]
                    )
                elif stat["name"] == "fieldingPct":
                    fielding_percentage = more_interesting(
                        fielding_percentage, stat["value"]
                    )
                elif stat["name"] == "rangeFactor":
                    range_factor = more_interesting(range_factor, stat["value"])
                elif stat["name"] == "zoneRating":
                    zone_rating = more_interesting(zone_rating, stat["value"])
                elif stat["name"] == "catcherCaughtStealingPct":
                    catcher_caught_stealing_percentage = more_interesting(
                        catcher_caught_stealing_percentage, stat["value"]
                    )
                elif stat["name"] == "catcherERA":
                    catcher_era = more_interesting(catcher_era, stat["value"])
                elif stat["name"] == "defWARBR":
                    def_warbr = more_interesting(def_warbr, stat["value"])
                elif stat["name"] == "blocks":
                    blocks = more_interesting(blocks, stat["value"])
                elif stat["name"] == "defensiveRebounds":
                    defensive_rebounds = more_interesting(
                        defensive_rebounds, stat["value"]
                    )
                elif stat["name"] == "steals":
                    steals = more_interesting(steals, stat["value"])
                elif stat["name"] == "turnoverPoints":
                    turnover_points = more_interesting(turnover_points, stat["value"])
                elif stat["name"] == "avgDefensiveRebounds":
                    average_defensive_rebounds = more_interesting(
                        average_defensive_rebounds, stat["value"]
                    )
                elif stat["name"] == "avgBlocks":
                    average_blocks = more_interesting(average_blocks, stat["value"])
                elif stat["name"] == "avgSteals":
                    average_steals = more_interesting(average_steals, stat["value"])
                elif stat["name"] == "avg48DefensiveRebounds":
                    average_48_defensive_rebounds = more_interesting(
                        average_48_defensive_rebounds, stat["value"]
                    )
                elif stat["name"] == "avg48Blocks":
                    average_48_blocks = more_interesting(
                        average_48_blocks, stat["value"]
                    )
                elif stat["name"] == "avg48Steals":
                    average_48_steals = more_interesting(
                        average_48_steals, stat["value"]
                    )
                elif stat["name"] == "largestLead":
                    largest_lead = more_interesting(largest_lead, stat["value"])
                elif stat["name"] == "disqualifications":
                    disqualifications = more_interesting(
                        disqualifications, stat["value"]
                    )
                elif stat["name"] == "flagrantFouls":
                    flagrant_fouls = more_interesting(flagrant_fouls, stat["value"])
                elif stat["name"] == "fouls":
                    fouls = more_interesting(fouls, stat["value"])
                elif stat["name"] == "ejections":
                    ejections = more_interesting(ejections, stat["value"])
                elif stat["name"] == "technicalFouls":
                    technical_fouls = more_interesting(technical_fouls, stat["value"])
                elif stat["name"] == "rebounds":
                    rebounds = more_interesting(rebounds, stat["value"])
                elif stat["name"] == "VORP":
                    vorp = more_interesting(vorp, stat["value"])
                elif stat["name"] == "avgMinutes":
                    average_minutes = more_interesting(average_minutes, stat["value"])
                elif stat["name"] == "NBARating":
                    nba_rating = more_interesting(nba_rating, stat["value"])
                elif stat["name"] == "avgRebounds":
                    average_rebounds = more_interesting(average_rebounds, stat["value"])
                elif stat["name"] == "avgFouls":
                    average_fouls = more_interesting(average_fouls, stat["value"])
                elif stat["name"] == "avgFlagrantFouls":
                    average_flagrant_fouls = more_interesting(
                        average_flagrant_fouls, stat["value"]
                    )
                elif stat["name"] == "avgTechnicalFouls":
                    average_technical_fouls = more_interesting(
                        average_technical_fouls, stat["value"]
                    )
                elif stat["name"] == "avgEjections":
                    average_ejections = more_interesting(
                        average_ejections, stat["value"]
                    )
                elif stat["name"] == "avgDisqualifications":
                    average_disqualifications = more_interesting(
                        average_disqualifications, stat["value"]
                    )
                elif stat["name"] == "assistTurnoverRatio":
                    assist_turnover_ratio = more_interesting(
                        assist_turnover_ratio, stat["value"]
                    )
                elif stat["name"] == "stealFoulRatio":
                    steal_foul_ratio = more_interesting(steal_foul_ratio, stat["value"])
                elif stat["name"] == "blockFoulRatio":
                    block_foul_ratio = more_interesting(block_foul_ratio, stat["value"])
                elif stat["name"] == "avgTeamRebounds":
                    average_team_rebounds = more_interesting(
                        average_team_rebounds, stat["value"]
                    )
                elif stat["name"] == "totalRebounds":
                    total_rebounds = more_interesting(total_rebounds, stat["value"])
                elif stat["name"] == "totalTechnicalFouls":
                    total_technical_fouls = more_interesting(
                        total_technical_fouls, stat["value"]
                    )
                elif stat["name"] == "teamAssistTurnoverRatio":
                    team_assist_turnover_ratio = more_interesting(
                        team_assist_turnover_ratio, stat["value"]
                    )
                elif stat["name"] == "stealTurnoverRatio":
                    steal_turnover_ratio = more_interesting(
                        steal_turnover_ratio, stat["value"]
                    )
                elif stat["name"] == "avg48Rebounds":
                    average_48_rebounds = more_interesting(
                        average_48_rebounds, stat["value"]
                    )
                elif stat["name"] == "avg48Fouls":
                    average_48_fouls = more_interesting(average_48_fouls, stat["value"])
                elif stat["name"] == "avg48FlagrantFouls":
                    average_48_flagrant_fouls = more_interesting(
                        average_48_flagrant_fouls, stat["value"]
                    )
                elif stat["name"] == "avg48TechnicalFouls":
                    average_48_technical_fouls = more_interesting(
                        average_48_technical_fouls, stat["value"]
                    )
                elif stat["name"] == "avg48Ejections":
                    average_48_ejections = more_interesting(
                        average_48_ejections, stat["value"]
                    )
                elif stat["name"] == "avg48Disqualifications":
                    average_48_disqualifications = more_interesting(
                        average_48_disqualifications, stat["value"]
                    )
                elif stat["name"] == "doubleDouble":
                    double_double = more_interesting(double_double, stat["value"])
                elif stat["name"] == "tripleDouble":
                    triple_double = more_interesting(triple_double, stat["value"])
                elif stat["name"] == "fieldGoals":
                    field_goals = more_interesting(field_goals, stat["value"])
                elif stat["name"] == "fieldGoalsAttempted":
                    field_goals_attempted = more_interesting(
                        field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "fieldGoalsMade":
                    field_goals_made = more_interesting(field_goals_made, stat["value"])
                elif stat["name"] == "fieldGoalPct":
                    field_goal_percentage = more_interesting(
                        field_goal_percentage, stat["value"]
                    )
                elif stat["name"] == "freeThrows":
                    free_throws = more_interesting(free_throws, stat["value"])
                elif stat["name"] == "freeThrowPct":
                    free_throw_percentage = more_interesting(
                        free_throw_percentage, stat["value"]
                    )
                elif stat["name"] == "freeThrowsAttempted":
                    free_throws_attempted = more_interesting(
                        free_throws_attempted, stat["value"]
                    )
                elif stat["name"] == "freeThrowsMade":
                    free_throws_made = more_interesting(free_throws_made, stat["value"])
                elif stat["name"] == "offensiveRebounds":
                    offensive_rebounds = more_interesting(
                        offensive_rebounds, stat["value"]
                    )
                elif stat["name"] == "turnovers":
                    turnovers = more_interesting(turnovers, stat["value"])
                elif stat["name"] == "threePointPct":
                    three_point_percentage = more_interesting(
                        three_point_percentage, stat["value"]
                    )
                elif stat["name"] == "threePointFieldGoalsAttempted":
                    three_point_field_goals_attempted = more_interesting(
                        three_point_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "threePointFieldGoalsMade":
                    three_point_field_goals_made = more_interesting(
                        three_point_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "teamTurnovers":
                    team_turnovers = more_interesting(team_turnovers, stat["value"])
                elif stat["name"] == "totalTurnovers":
                    total_turnovers = more_interesting(total_turnovers, stat["value"])
                elif stat["name"] == "pointsInPaint":
                    points_in_paint = more_interesting(points_in_paint, stat["value"])
                elif stat["name"] == "brickIndex":
                    brick_index = more_interesting(brick_index, stat["value"])
                elif stat["name"] == "fastBreakPoints":
                    fast_break_points = more_interesting(
                        fast_break_points, stat["value"]
                    )
                elif stat["name"] == "avgFieldGoalsMade":
                    average_field_goals_made = more_interesting(
                        average_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "avgFieldGoalsAttempted":
                    average_field_goals_attempted = more_interesting(
                        average_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "avgThreePointFieldGoalsMade":
                    average_three_point_field_goals_made = more_interesting(
                        average_three_point_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "avgThreePointFieldGoalsAttempted":
                    average_three_point_field_goals_attempted = more_interesting(
                        average_three_point_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "avgFreeThrowsMade":
                    average_free_throws_made = more_interesting(
                        average_free_throws_made, stat["value"]
                    )
                elif stat["name"] == "avgFreeThrowsAttempted":
                    average_free_throws_attempted = more_interesting(
                        average_free_throws_attempted, stat["value"]
                    )
                elif stat["name"] == "avgPoints":
                    average_points = more_interesting(average_points, stat["value"])
                elif stat["name"] == "avgOffensiveRebounds":
                    average_offensive_rebounds = more_interesting(
                        average_offensive_rebounds, stat["value"]
                    )
                elif stat["name"] == "avgAssists":
                    average_assists = more_interesting(average_assists, stat["value"])
                elif stat["name"] == "avgTurnovers":
                    average_turnovers = more_interesting(
                        average_turnovers, stat["value"]
                    )
                elif stat["name"] == "offensiveReboundPct":
                    offensive_rebound_percentage = more_interesting(
                        offensive_rebound_percentage, stat["value"]
                    )
                elif stat["name"] == "estimatedPossessions":
                    estimated_possessions = more_interesting(
                        estimated_possessions, stat["value"]
                    )
                elif stat["name"] == "avgEstimatedPossessions":
                    average_estimated_possessions = more_interesting(
                        average_estimated_possessions, stat["value"]
                    )
                elif stat["name"] == "pointsPerEstimatedPossessions":
                    points_per_estimated_possessions = more_interesting(
                        points_per_estimated_possessions, stat["value"]
                    )
                elif stat["name"] == "avgTeamTurnovers":
                    average_team_turnovers = more_interesting(
                        average_team_turnovers, stat["value"]
                    )
                elif stat["name"] == "avgTotalTurnovers":
                    average_total_turnovers = more_interesting(
                        average_total_turnovers, stat["value"]
                    )
                elif stat["name"] == "threePointFieldGoalPct":
                    three_point_field_goal_percentage = more_interesting(
                        three_point_field_goal_percentage, stat["value"]
                    )
                elif stat["name"] == "twoPointFieldGoalsMade":
                    two_point_field_goals_made = more_interesting(
                        two_point_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "twoPointFieldGoalsAttempted":
                    two_point_field_goals_attempted = more_interesting(
                        two_point_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "avgTwoPointFieldGoalsMade":
                    average_two_point_field_goals_made = more_interesting(
                        average_two_point_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "avgTwoPointFieldGoalsAttempted":
                    average_two_point_field_goals_attempted = more_interesting(
                        average_two_point_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "twoPointFieldGoalPct":
                    two_point_field_goal_percentage = more_interesting(
                        two_point_field_goal_percentage, stat["value"]
                    )
                elif stat["name"] == "shootingEfficiency":
                    shooting_efficiency = more_interesting(
                        shooting_efficiency, stat["value"]
                    )
                elif stat["name"] == "scoringEfficiency":
                    scoring_efficiency = more_interesting(
                        scoring_efficiency, stat["value"]
                    )
                elif stat["name"] == "avg48FieldGoalsMade":
                    average_48_field_goals_made = more_interesting(
                        average_48_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "avg48FieldGoalsAttempted":
                    average_48_field_goals_attempted = more_interesting(
                        average_48_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "avg48ThreePointFieldGoalsMade":
                    average_48_three_point_field_goals_made = more_interesting(
                        average_48_three_point_field_goals_made, stat["value"]
                    )
                elif stat["name"] == "avg48ThreePointFieldGoalsAttempted":
                    average_48_three_point_field_goals_attempted = more_interesting(
                        average_48_three_point_field_goals_attempted, stat["value"]
                    )
                elif stat["name"] == "avg48FreeThrowsMade":
                    average_48_free_throws_made = more_interesting(
                        average_48_free_throws_made, stat["value"]
                    )
                elif stat["name"] == "avg48FreeThrowsAttempted":
                    average_48_free_throws_attempted = more_interesting(
                        average_48_free_throws_attempted, stat["value"]
                    )
                elif stat["name"] == "avg48Points":
                    average_48_points = more_interesting(
                        average_48_points, stat["value"]
                    )
                elif stat["name"] == "avg48OffensiveRebounds":
                    average_48_offensive_rebounds = more_interesting(
                        average_48_offensive_rebounds, stat["value"]
                    )
                elif stat["name"] == "avg48Assists":
                    average_48_assists = more_interesting(
                        average_48_assists, stat["value"]
                    )
                elif stat["name"] == "avg48Turnovers":
                    average_48_turnovers = more_interesting(
                        average_48_turnovers, stat["value"]
                    )

    return TeamModel(
        identifier=identifier,
        name=name,
        location=location,
        players=players,
        odds=odds,
        points=points,
        ladder_rank=None,
        news=create_google_news_models(name, session, dt, league),
        social=create_x_social_model(identifier, session, dt),
        field_goals=field_goals,
        coaches=[create_espn_coach_model(session, dt, x) for x in coaches_urls],
        lbw=None,
        end_dt=None,
        runs=runs,
        wickets=None,
        overs=None,
        balls=None,
        byes=None,
        leg_byes=None,
        wides=None,
        no_balls=None,
        penalties=None,
        balls_per_over=None,
        fours=None,
        sixes=None,
        catches=None,
        catches_dropped=None,
        version=version,
        kicks=kicks,
        handballs=handballs,
        disposals=disposals,
        marks=marks,
        bounces=bounces,
        tackles=tackles,
        tackles_inside_50=tackles_inside_50,
        contested_possessions=contested_possessions,
        uncontested_possessions=uncontested_possessions,
        total_possessions=total_possessions,
        marks_inside=marks_inside_50,
        contested_marks=contested_marks,
        uncontested_marks=uncontested_marks,
        hit_outs=hitouts,
        one_percenters=one_percenters,
        disposal_efficiency=disposal_efficiency,
        clangers=clangers,
        goals=goals,
        behinds=behinds,
        free_kicks_for=frees_for,
        free_kicks_against=frees_against,
        clearances=total_clearances,
        centre_clearances=centre_clearances,
        stoppage_clearances=stoppage_clearances,
        rebounds=rebounds,
        goal_assists=goal_assists,
        goal_accuracy=goal_accuracy,
        rushed_behinds=rushed_behinds,
        touched_behinds=touched_behinds,
        left_behinds=left_behinds,
        left_posters=left_posters,
        right_behinds=right_behinds,
        right_posters=right_posters,
        total_interchange_count=total_interchange_count,
        interchange_count_q1=interchange_count_q1,
        interchange_count_q2=interchange_count_q2,
        interchange_count_q3=interchange_count_q3,
        interchange_count_q4=interchange_count_q4,
        insides=inside_50s,
        blocked_shots=blocked_shots,
        effective_clearances=effective_clearances,
        effective_tackles=effective_tackles,
        ineffective_tackles=ineffective_tackles,
        interceptions=interceptions,
        tackle_percentage=tackle_percentage,
        appearances=appearances,
        average_rating_from_correspondent=average_rating_from_correspondent,
        average_rating_from_data_feed=average_rating_from_data_feed,
        average_rating_from_editor=average_rating_from_editor,
        average_rating_from_user=average_rating_from_user,
        did_not_play=did_not_play,
        fouls_committed=fouls_committed,
        fouls_suffered=fouls_suffered,
        goal_difference=goal_difference,
        losses=losses,
        lost_corners=lost_corners,
        minutes=minutes,
        own_goals=own_goals,
        pass_percentage=pass_percentage,
        red_cards=red_cards,
        starts=starts,
        sub_ins=sub_ins,
        sub_outs=sub_outs,
        suspensions=suspensions,
        time_ended=time_ended,
        time_started=time_started,
        win_percentage=win_percentage,
        wins=wins,
        won_corners=won_corners,
        yellow_cards=yellow_cards,
        clean_sheet=clean_sheet,
        crosses_caught=crosses_caught,
        goals_conceded=goals_conceded,
        partial_clean_sheet=partial_clean_sheet,
        penalty_kick_conceded=penalty_kick_conceded,
        penalty_kick_save_percentage=penalty_kick_save_percentage,
        penalty_kicks_faced=penalty_kicks_faced,
        penalty_kicks_saved=penalty_kicks_saved,
        punches=punches,
        saves=saves,
        shoot_out_kicks_faced=shoot_out_kicks_faced,
        shoot_out_kicks_saved=shoot_out_kicks_saved,
        shoot_out_save_percentage=shoot_out_save_percentage,
        shots_faced=shots_faced,
        smothers=smothers,
        unclaimed_crosses=unclaimed_crosses,
        accurate_crosses=accurate_crosses,
        accurate_long_balls=accurate_long_balls,
        accurate_passes=accurate_passes,
        accurate_through_balls=accurate_through_balls,
        cross_percentage=cross_percentage,
        free_kick_goals=free_kick_goals,
        free_kick_percentage=free_kick_percentage,
        free_kick_shots=free_kick_shots,
        game_winning_assists=game_winning_assists,
        game_winning_goals=game_winning_goals,
        headed_goals=headed_goals,
        inaccurate_crosses=inaccurate_crosses,
        inaccurate_long_balls=inaccurate_long_balls,
        inaccurate_passes=inaccurate_passes,
        inaccurate_through_balls=inaccurate_through_balls,
        left_footed_shots=left_footed_shots,
        longball_percentage=longball_percentage,
        offsides=offsides,
        penalty_kick_goals=penalty_kick_goals,
        penalty_kick_percentage=penalty_kick_percentage,
        penalty_kick_shots=penalty_kick_shots,
        penalty_kicks_missed=penalty_kicks_missed,
        possession_percentage=possession_percentage,
        possession_time=possession_time,
        right_footed_shots=right_footed_shots,
        shoot_out_goals=shoot_out_goals,
        shoot_out_misses=shoot_out_misses,
        shoot_out_percentage=shoot_out_percentage,
        shot_assists=shot_assists,
        shot_percentage=shot_percentage,
        shots_headed=shots_headed,
        shots_off_target=shots_off_target,
        shots_on_post=shots_on_post,
        shots_on_target=shots_on_target,
        through_ball_percentage=through_ball_percentage,
        total_crosses=total_crosses,
        total_goals=total_goals,
        total_long_balls=total_long_balls,
        total_passes=total_passes,
        total_shots=total_shots,
        total_through_balls=total_through_balls,
        draws=draws,
        hit_by_pitch=hit_by_pitch,
        ground_balls=ground_balls,
        strikeouts=strikeouts,
        rbis=rbis,
        sac_hits=sac_hits,
        hits=hits,
        stolen_bases=stolen_bases,
        walks=walks,
        catcher_interference=catcher_interference,
        gidps=gidps,
        sacrifice_flies=sacrifice_flies,
        at_bats=at_bats,
        home_runs=home_runs,
        grand_slam_home_runs=grand_slam_home_runs,
        runners_left_on_base=runners_left_on_base,
        triples=triples,
        game_winning_rbis=game_winning_rbis,
        intentional_walks=intentional_walks,
        doubles=doubles,
        fly_balls=fly_balls,
        caught_stealing=caught_stealing,
        pitches=pitches,
        games_started=games_started,
        pinch_at_bats=pinch_at_bats,
        pinch_hits=pinch_hits,
        player_rating=player_rating,
        is_qualified=is_qualified,
        is_qualified_steals=is_qualified_steals,
        total_bases=total_bases,
        plate_appearances=plate_appearances,
        projected_home_runs=projected_home_runs,
        extra_base_hits=extra_base_hits,
        runs_created=runs_created,
        batting_average=batting_average,
        pinch_average=pinch_average,
        slug_average=slug_average,
        secondary_average=secondary_average,
        on_base_percentage=on_base_percentage,
        ops=ops,
        ground_to_fly_ratio=ground_to_fly_ratio,
        runs_created_per_27_outs=runs_created_per_27_outs,
        batter_rating=batter_rating,
        at_bats_per_home_run=at_bats_per_home_run,
        stolen_base_percentage=stolen_base_percentage,
        pitches_per_plate_appearance=pitches_per_plate_appearance,
        isolated_power=isolated_power,
        walk_to_strikeout_ratio=walk_to_strikeout_ratio,
        walks_per_plate_appearance=walks_per_plate_appearance,
        secondary_average_minus_batting_average=secondary_average_minus_batting_average,
        runs_produced=runs_produced,
        runs_ratio=runs_ratio,
        patience_ratio=patience_ratio,
        balls_in_play_average=balls_in_play_average,
        mlb_rating=mlb_rating,
        offensive_wins_above_replacement=offensive_wins_above_replacement,
        wins_above_replacement=wins_above_replacement,
        earned_runs=earned_runs,
        batters_hit=batters_hit,
        sacrifice_bunts=sacrifice_bunts,
        save_opportunities=save_opportunities,
        finishes=finishes,
        balks=balks,
        batters_faced=batters_faced,
        holds=holds,
        complete_games=complete_games,
        perfect_games=perfect_games,
        wild_pitches=wild_pitches,
        third_innings=third_innings,
        team_earned_runs=team_earned_runs,
        shutouts=shutouts,
        pickoff_attempts=pickoff_attempts,
        run_support=run_support,
        pitches_as_starter=pitches_as_starter,
        quality_starts=quality_starts,
        inherited_runners=inherited_runners,
        inherited_runners_scored=inherited_runners_scored,
        opponent_total_bases=opponent_total_bases,
        is_qualified_saves=is_qualified_saves,
        full_innings=full_innings,
        part_innings=part_innings,
        blown_saves=blown_saves,
        innings=innings,
        era=era,
        whip=whip,
        caught_stealing_percentage=caught_stealing_percentage,
        pitches_per_start=pitches_per_start,
        pitches_per_inning=pitches_per_inning,
        run_support_average=run_support_average,
        opponent_average=opponent_average,
        opponent_slug_average=opponent_slug_average,
        opponent_on_base_percentage=opponent_on_base_percentage,
        opponent_ops=opponent_ops,
        save_percentage=save_percentage,
        strikeouts_per_nine_innings=strikeouts_per_nine_innings,
        strikeout_to_walk_ratio=strikeout_to_walk_ratio,
        tough_losses=tough_losses,
        cheap_wins=cheap_wins,
        save_opportunities_per_win=save_opportunities_per_win,
        pitch_count=pitch_count,
        strikes=strikes,
        strike_pitch_ratio=strike_pitch_ratio,
        games_played=games_played,
        team_games_played=team_games_played,
        double_plays=double_plays,
        opportunities=opportunities,
        errors=errors,
        passed_balls=passed_balls,
        assists=assists,
        outfield_assists=outfield_assists,
        pickoffs=pickoffs,
        putouts=putouts,
        outs_on_field=outs_on_field,
        triple_plays=triple_plays,
        balls_in_zone=balls_in_zone,
        extra_bases=extra_bases,
        outs_made=outs_made,
        catcher_third_innings_played=catcher_third_innings_played,
        catcher_caught_stealing=catcher_caught_stealing,
        catcher_stolen_bases_allowed=catcher_stolen_bases_allowed,
        catcher_earned_runs=catcher_earned_runs,
        is_qualified_catcher=is_qualified_catcher,
        is_qualified_pitcher=is_qualified_pitcher,
        successful_chances=successful_chances,
        total_chances=total_chances,
        full_innings_played=full_innings_played,
        part_innings_played=part_innings_played,
        fielding_percentage=fielding_percentage,
        range_factor=range_factor,
        zone_rating=zone_rating,
        catcher_caught_stealing_percentage=catcher_caught_stealing_percentage,
        catcher_era=catcher_era,
        def_warbr=def_warbr,
        average_game_score=average_game_score,
        blocks=blocks,
        defensive_rebounds=defensive_rebounds,
        steals=steals,
        turnover_points=turnover_points,
        average_defensive_rebounds=average_defensive_rebounds,
        average_blocks=average_blocks,
        average_steals=average_steals,
        average_48_defensive_rebounds=average_48_defensive_rebounds,
        average_48_blocks=average_48_blocks,
        average_48_steals=average_48_steals,
        largest_lead=largest_lead,
        disqualifications=disqualifications,
        flagrant_fouls=flagrant_fouls,
        fouls=fouls,
        ejections=ejections,
        technical_fouls=technical_fouls,
        vorp=vorp,
        average_minutes=average_minutes,
        nba_rating=nba_rating,
        average_rebounds=average_rebounds,
        average_fouls=average_fouls,
        average_flagrant_fouls=average_flagrant_fouls,
        average_technical_fouls=average_technical_fouls,
        average_ejections=average_ejections,
        average_disqualifications=average_disqualifications,
        assist_turnover_ratio=assist_turnover_ratio,
        steal_foul_ratio=steal_foul_ratio,
        block_foul_ratio=block_foul_ratio,
        average_team_rebounds=average_team_rebounds,
        total_rebounds=total_rebounds,
        total_technical_fouls=total_technical_fouls,
        team_assist_turnover_ratio=team_assist_turnover_ratio,
        steal_turnover_ratio=steal_turnover_ratio,
        average_48_rebounds=average_48_rebounds,
        average_48_fouls=average_48_fouls,
        average_48_flagrant_fouls=average_48_flagrant_fouls,
        average_48_technical_fouls=average_48_technical_fouls,
        average_48_ejections=average_48_ejections,
        average_48_disqualifications=average_48_disqualifications,
        double_double=double_double,
        triple_double=triple_double,
        field_goals_attempted=field_goals_attempted,
        field_goals_made=field_goals_made,
        field_goals_percentage=field_goal_percentage,
        free_throws=free_throws,
        free_throws_percentage=free_throw_percentage,
        free_throws_attempted=free_throws_attempted,
        free_throws_made=free_throws_made,
        offensive_rebounds=offensive_rebounds,
        turnovers=turnovers,
        three_point_percentage=three_point_percentage,
        three_point_field_goals_attempted=three_point_field_goals_attempted,
        three_point_field_goals_made=three_point_field_goals_made,
        team_turnovers=team_turnovers,
        total_turnovers=total_turnovers,
        points_in_paint=points_in_paint,
        brick_index=brick_index,
        fast_break_points=fast_break_points,
        average_field_goals_made=average_field_goals_made,
        average_field_goals_attempted=average_field_goals_attempted,
        average_three_point_field_goals_made=average_three_point_field_goals_made,
        average_three_point_field_goals_attempted=average_three_point_field_goals_attempted,
        average_free_throws_made=average_free_throws_made,
        average_free_throws_attempted=average_free_throws_attempted,
        average_points=average_points,
        average_offensive_rebounds=average_offensive_rebounds,
        average_assists=average_assists,
        average_turnovers=average_turnovers,
        offensive_rebound_percentage=offensive_rebound_percentage,
        estimated_possessions=estimated_possessions,
        average_estimated_possessions=average_estimated_possessions,
        points_per_estimated_possessions=points_per_estimated_possessions,
        average_team_turnovers=average_team_turnovers,
        average_total_turnovers=average_total_turnovers,
        three_point_field_goals_percentage=three_point_field_goal_percentage,
        two_point_field_goals_made=two_point_field_goals_made,
        two_point_field_goals_attempted=two_point_field_goals_attempted,
        average_two_point_field_goals_made=average_two_point_field_goals_made,
        average_two_point_field_goals_attempted=average_two_point_field_goals_attempted,
        two_point_field_goal_percentage=two_point_field_goal_percentage,
        shooting_efficiency=shooting_efficiency,
        scoring_efficiency=scoring_efficiency,
        average_48_field_goals_made=average_48_field_goals_made,
        average_48_field_goals_attempted=average_48_field_goals_attempted,
        average_48_three_point_field_goals_made=average_48_three_point_field_goals_made,
        average_48_three_point_field_goals_attempted=average_48_three_point_field_goals_attempted,
        average_48_free_throws_made=average_48_free_throws_made,
        average_48_free_throws_attempted=average_48_free_throws_attempted,
        average_48_points=average_48_points,
        average_48_offensive_rebounds=average_48_offensive_rebounds,
        average_48_assists=average_48_assists,
        average_48_turnovers=average_48_turnovers,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_espn_team_model(
    session: requests_cache.CachedSession,
    team: dict[str, Any],
    roster_dict: dict[str, Any],
    odds: list[OddsModel],
    score_dict: dict[str, Any],
    dt: datetime.datetime,
    league: League,
    positions_validator: dict[str, str],
    statistics_dict: dict[str, Any],
    version: str,
) -> TeamModel:
    return _create_espn_team_model(
        session=session,
        team=team,
        roster_dict=roster_dict,
        odds=odds,
        score_dict=score_dict,
        dt=dt,
        league=league,
        positions_validator=positions_validator,
        statistics_dict=statistics_dict,
        version=version,
    )


def create_espn_team_model(
    session: requests_cache.CachedSession,
    team: dict[str, Any],
    roster_dict: dict[str, Any],
    odds: list[OddsModel],
    score_dict: dict[str, Any],
    dt: datetime.datetime,
    league: League,
    positions_validator: dict[str, str],
    statistics_dict: dict[str, Any],
) -> TeamModel:
    """Create team model from ESPN."""
    if (
        not pytest_is_running.is_running()
        and dt.date() < datetime.datetime.today().date() - datetime.timedelta(days=7)
    ):
        return _cached_create_espn_team_model(
            session=session,
            team=team,
            roster_dict=roster_dict,
            odds=odds,
            score_dict=score_dict,
            dt=dt,
            league=league,
            positions_validator=positions_validator,
            version=VERSION,
            statistics_dict=statistics_dict,
        )
    with session.cache_disabled():
        return _create_espn_team_model(
            session=session,
            team=team,
            roster_dict=roster_dict,
            odds=odds,
            score_dict=score_dict,
            dt=dt,
            league=league,
            positions_validator=positions_validator,
            statistics_dict=statistics_dict,
            version=VERSION,
        )
