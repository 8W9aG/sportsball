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
    fumbles = None
    fumbles_lost = None
    fumbles_forced = None
    fumbles_recovered = None
    fumbles_recovered_yards = None
    fumbles_touchdowns = None
    offensive_two_point_returns = None
    offensive_fumbles_touchdowns = None
    defensive_fumbles_touchdowns = None
    average_gain = None
    completion_percentage = None
    completions = None
    espn_qb_rating = None
    interception_percentage = None
    long_passing = None
    misc_yards = None
    net_passing_yards = None
    net_passing_yards_per_game = None
    net_total_yards = None
    net_yards_per_game = None
    passing_attempts = None
    passing_big_plays = None
    passing_first_downs = None
    passing_fumbles = None
    passing_fumbles_lost = None
    passing_touchdown_percentage = None
    passing_touchdowns = None
    passing_yards = None
    passing_yards_after_catch = None
    passing_yards_at_catch = None
    passing_yards_per_game = None
    qb_rating = None
    sacks = None
    sack_yards_lost = None
    net_passing_attempts = None
    total_offensive_plays = None
    total_points = None
    total_points_per_game = None
    total_touchdowns = None
    total_yards = None
    total_yards_from_scrimmage = None
    two_point_pass_convs = None
    two_point_pass = None
    two_point_pass_attempts = None
    yards_from_scrimmage_per_game = None
    yards_per_completion = None
    yards_per_game = None
    yards_per_pass_attempt = None
    net_yards_per_pass_attempt = None
    quarterback_rating = None
    espn_rb_rating = None
    long_rushing = None
    rushing_attempts = None
    rushing_big_plays = None
    rushing_first_downs = None
    rushing_fumbles = None
    rushing_fumbles_lost = None
    rushing_touchdowns = None
    rushing_yards = None
    rushing_yards_per_game = None
    stuffs = None
    stuff_yards_lost = None
    two_point_rush_conversions = None
    two_point_rush = None
    two_point_rush_attempts = None
    yards_per_rush_attempt = None
    espn_wr_rating = None
    long_reception = None
    receiving_big_plays = None
    receiving_first_downs = None
    receiving_fumbles = None
    receiving_fumbles_lost = None
    receiving_targets = None
    receiving_touchdowns = None
    receiving_yards = None
    receiving_yards_after_catch = None
    receiving_yards_at_catch = None
    receiving_yards_per_game = None
    receptions = None
    two_point_rec_conversions = None
    two_point_reception = None
    two_point_reception_attempts = None
    yards_per_reception = None
    assist_tackles = None
    average_interception_yards = None
    average_sack_yards = None
    average_stuff_yards = None
    blocked_field_goal_touchdowns = None
    blocked_punt_touchdowns = None
    defensive_touchdowns = None
    hurries = None
    kicks_blocked = None
    long_interception = None
    misc_touchdowns = None
    passes_batted_down = None
    passes_defended = None
    qb_hits = None
    two_point_returns = None
    sacks_assisted = None
    sacks_unassisted = None
    sack_yards = None
    safeties = None
    solo_tackles = None
    stuff_yards = None
    tackles_for_loss = None
    tackles_yards_lost = None
    yards_allowed = None
    points_allowed = None
    one_point_safeties_made = None
    missed_field_goal_return_td = None
    blocked_punt_ez_rec_td = None
    interception_touchdowns = None
    interception_yards = None
    average_kickoff_return_yards = None
    average_kickoff_yards = None
    extra_point_attempts = None
    extra_point_percentage = None
    extra_points_blocked = None
    extra_points_blocked_percentage = None
    extra_points_made = None
    fair_catches = None
    fair_catch_percentage = None
    field_goal_attempts = None
    field_goal_attempts_1_19 = None
    field_goal_attempts_20_29 = None
    field_goal_attempts_30_39 = None
    field_goal_attempts_40_49 = None
    field_goal_attempts_50_59 = None
    field_goal_attempts_60_99 = None
    field_goal_attempts_50 = None
    field_goal_attempt_yards = None
    field_goals_blocked = None
    field_goals_blocked_percentage = None
    field_goals_made_1_19 = None
    field_goals_made_20_29 = None
    field_goals_made_30_39 = None
    field_goals_made_40_49 = None
    field_goals_made_50_59 = None
    field_goals_made_60_99 = None
    field_goals_made_50 = None
    field_goals_made_yards = None
    field_goals_missed_yards = None
    kickoff_ob = None
    kickoff_returns = None
    kickoff_return_touchdowns = None
    kickoff_return_yards = None
    kickoffs = None
    kickoff_yards = None
    long_field_goal_attempt = None
    long_field_goal_made = None
    long_kickoff = None
    total_kicking_points = None
    touchback_percentage = None
    touchbacks = None
    def_fumble_returns = None
    def_fumble_return_yards = None
    fumble_recoveries = None
    fumble_recovery_yards = None
    kick_return_fair_catches = None
    kick_return_fair_catch_percentage = None
    kick_return_fumbles = None
    kick_return_fumbles_lost = None
    kick_returns = None
    kick_return_touchdowns = None
    kick_return_yards = None
    long_kick_return = None
    long_punt_return = None
    misc_fumble_returns = None
    misc_fumble_return_yards = None
    opp_fumble_recoveries = None
    opp_fumble_recovery_yards = None
    opp_special_team_fumble_returns = None
    opp_special_team_fumble_return_yards = None
    punt_return_fair_catches = None
    punt_return_fair_catch_percentage = None
    punt_return_fumbles = None
    punt_return_fumbles_lost = None
    punt_returns = None
    punt_returns_started_inside_the_10 = None
    punt_returns_started_inside_the_20 = None
    punt_return_touchdowns = None
    punt_return_yards = None
    special_team_fumble_returns = None
    special_team_fumble_return_yards = None
    yards_per_kick_return = None
    yards_per_punt_return = None
    yards_per_return = None
    average_punt_return_yards = None
    gross_average_punt_yards = None
    long_punt = None
    net_average_punt_yards = None
    punts = None
    punts_blocked = None
    punts_blocked_percentage = None
    punts_inside_10 = None
    punts_inside_10_percentage = None
    punts_inside_20 = None
    punts_inside_20_percentage = None
    punts_over_50 = None
    punt_yards = None
    defensive_points = None
    kick_extra_points = None
    kick_extra_points_made = None
    misc_points = None
    return_touchdowns = None
    total_two_point_conversions = None
    first_downs = None
    first_downs_passing = None
    first_downs_penalty = None
    first_downs_per_game = None
    first_downs_rushing = None
    fourth_down_attempts = None
    fourth_down_conversion_percentage = None
    fourth_down_conversions = None
    possession_time_seconds = None
    redzone_attempt_points = None
    redzone_attempts = None
    redzone_conversions = None
    redzone_efficiency_percentage = None
    redzone_end_downs = None
    redzone_end_game = None
    redzone_end_half = None
    redzone_field_goal_percentage = None
    redzone_field_goal_points = None
    redzone_field_goals = None
    redzone_field_goals_missed = None
    redzone_fumble = None
    redzone_interception = None
    redzone_scoring_percentage = None
    redzone_total_points = None
    redzone_touchdown_pass = None
    redzone_touchdown_percentage = None
    redzone_touchdown_points = None
    redzone_touchdown_rush = None
    redzone_touchdowns = None
    third_down_attempts = None
    third_down_conversion_percentage = None
    third_down_conversions = None
    timeouts_used = None
    total_penalties = None
    total_penalty_yards = None
    total_plays = None
    total_drives = None
    turn_over_differential = None
    goals_against = None
    shots_against = None
    penalty_kill_percentage = None
    power_play_goals_against = None
    short_handed_goals_against = None
    shootout_saves = None
    shootout_shots_against = None
    times_short_handed = None
    empty_net_goals_against = None
    takeaways = None
    even_strength_saves = None
    power_play_saves = None
    short_handed_saves = None
    time_on_ice = None
    power_play_time_on_ice = None
    short_handed_time_on_ice = None
    even_strength_time_on_ice = None
    shifts = None
    shot_differential = None
    goal_differential = None
    pim_differential = None
    rating = None
    ytd_goals = None
    shots_in_first_period = None
    shots_in_second_period = None
    shots_in_third_period = None
    shots_ot = None
    shots_total = None
    shots_missed = None
    points_per_game = None
    power_play_goals = None
    power_play_assists = None
    power_play_opportunities = None
    power_play_percentage = None
    short_handed_goals = None
    short_handed_assists = None
    shootout_attempts = None
    shootout_shot_percentage = None
    empty_net_goals_for = None
    shooting_percentage = None
    total_face_offs = None
    faceoffs_won = None
    faceoffs_lost = None
    faceoff_percentage = None
    unassisted_goals = None
    giveaways = None
    penalties = None
    penalty_minutes = None
    total_giveaways = None
    total_takeaways = None
    fantasy_rating = None
    second_chance_points = None
    plus_minus = None
    if "splits" in statistics_dict:
        try:
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
                        marks_inside_50 = more_interesting(
                            marks_inside_50, stat["value"]
                        )
                    elif stat["name"] == "contestedMarks":
                        contested_marks = more_interesting(
                            contested_marks, stat["value"]
                        )
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
                        total_clearances = more_interesting(
                            total_clearances, stat["value"]
                        )
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
                        touched_behinds = more_interesting(
                            touched_behinds, stat["value"]
                        )
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
                        total_clearances = more_interesting(
                            total_clearances, stat["value"]
                        )
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
                        fouls_committed = more_interesting(
                            fouls_committed, stat["value"]
                        )
                    elif stat["name"] == "foulsSuffered":
                        fouls_suffered = more_interesting(fouls_suffered, stat["value"])
                    elif stat["name"] == "goalDifference":
                        goal_difference = more_interesting(
                            goal_difference, stat["value"]
                        )
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
                        pass_percentage = more_interesting(
                            pass_percentage, stat["value"]
                        )
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
                        accurate_crosses = more_interesting(
                            accurate_crosses, stat["value"]
                        )
                    elif stat["name"] == "accurateLongBalls":
                        accurate_long_balls = more_interesting(
                            accurate_long_balls, stat["value"]
                        )
                    elif stat["name"] == "accuratePasses":
                        accurate_passes = more_interesting(
                            accurate_passes, stat["value"]
                        )
                    elif stat["name"] == "accurateThroughBalls":
                        accurate_through_balls = more_interesting(
                            accurate_through_balls, stat["value"]
                        )
                    elif stat["name"] == "crossPct":
                        cross_percentage = more_interesting(
                            cross_percentage, stat["value"]
                        )
                    elif stat["name"] == "freeKickGoals":
                        free_kick_goals = more_interesting(
                            free_kick_goals, stat["value"]
                        )
                    elif stat["name"] == "freeKickPct":
                        free_kick_percentage = more_interesting(
                            free_kick_percentage, stat["value"]
                        )
                    elif stat["name"] == "freeKickShots":
                        free_kick_shots = more_interesting(
                            free_kick_shots, stat["value"]
                        )
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
                        possession_time = more_interesting(
                            possession_time, stat["value"]
                        )
                    elif stat["name"] == "rightFootedShots":
                        right_footed_shots = more_interesting(
                            right_footed_shots, stat["value"]
                        )
                    elif stat["name"] == "shootOutGoals":
                        shoot_out_goals = more_interesting(
                            shoot_out_goals, stat["value"]
                        )
                    elif stat["name"] == "shootOutMisses":
                        shoot_out_misses = more_interesting(
                            shoot_out_misses, stat["value"]
                        )
                    elif stat["name"] == "shootOutPct":
                        shoot_out_percentage = more_interesting(
                            shoot_out_percentage, stat["value"]
                        )
                    elif stat["name"] == "shotAssists":
                        shot_assists = more_interesting(shot_assists, stat["value"])
                    elif stat["name"] == "shotPct":
                        shot_percentage = more_interesting(
                            shot_percentage, stat["value"]
                        )
                    elif stat["name"] == "shotsHeaded":
                        shots_headed = more_interesting(shots_headed, stat["value"])
                    elif stat["name"] == "shotsOffTarget":
                        shots_off_target = more_interesting(
                            shots_off_target, stat["value"]
                        )
                    elif stat["name"] == "shotsOnPost":
                        shots_on_post = more_interesting(shots_on_post, stat["value"])
                    elif stat["name"] == "shotsOnTarget":
                        shots_on_target = more_interesting(
                            shots_on_target, stat["value"]
                        )
                    elif stat["name"] == "throughBallPct":
                        through_ball_percentage = more_interesting(
                            through_ball_percentage, stat["value"]
                        )
                    elif stat["name"] == "totalCrosses":
                        total_crosses = more_interesting(total_crosses, stat["value"])
                    elif stat["name"] == "totalGoals":
                        total_goals = more_interesting(total_goals, stat["value"])
                    elif stat["name"] == "totalLongBalls":
                        total_long_balls = more_interesting(
                            total_long_balls, stat["value"]
                        )
                    elif stat["name"] == "totalPasses":
                        total_passes = more_interesting(total_passes, stat["value"])
                    elif stat["name"] == "totalShots":
                        total_shots = more_interesting(total_shots, stat["value"])
                    elif stat["name"] == "totalThroughBalls":
                        total_through_balls = more_interesting(
                            total_through_balls, stat["value"]
                        )
                    elif stat["name"] == "hitByPitch":
                        if "value" in stat:
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
                        if "value" in stat:
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
                        sacrifice_flies = more_interesting(
                            sacrifice_flies, stat["value"]
                        )
                    elif stat["name"] == "atBats":
                        at_bats = more_interesting(at_bats, stat["value"])
                    elif stat["name"] == "homeRuns":
                        home_runs = more_interesting(home_runs, stat["value"])
                    elif stat["name"] == "homeruns":
                        pass
                    elif stat["name"] == "grandSlamHomeRuns":
                        grand_slam_home_runs = more_interesting(
                            grand_slam_home_runs, stat["value"]
                        )
                    elif stat["name"] == "runnersLeftOnBase":
                        runners_left_on_base = more_interesting(
                            runners_left_on_base, stat["value"]
                        )
                    elif stat["name"] == "triples":
                        if "value" in stat:
                            triples = more_interesting(triples, stat["value"])
                    elif stat["name"] == "gameWinningRBIs":
                        game_winning_rbis = more_interesting(
                            game_winning_rbis, stat["value"]
                        )
                    elif stat["name"] == "intentionalWalks":
                        if "value" in stat:
                            intentional_walks = more_interesting(
                                intentional_walks, stat["value"]
                            )
                    elif stat["name"] == "doubles":
                        if "value" in stat:
                            doubles = more_interesting(doubles, stat["value"])
                    elif stat["name"] == "flyBalls":
                        fly_balls = more_interesting(fly_balls, stat["value"])
                    elif stat["name"] == "caughtStealing":
                        if "value" in stat:
                            caught_stealing = more_interesting(
                                caught_stealing, stat["value"]
                            )
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
                        extra_base_hits = more_interesting(
                            extra_base_hits, stat["value"]
                        )
                    elif stat["name"] == "runsCreated":
                        runs_created = more_interesting(runs_created, stat["value"])
                    elif stat["name"] == "avg":
                        batting_average = more_interesting(
                            batting_average, stat["value"]
                        )
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
                        sacrifice_bunts = more_interesting(
                            sacrifice_bunts, stat["value"]
                        )
                    elif stat["name"] == "saveOpportunities":
                        save_opportunities = more_interesting(
                            save_opportunities, stat["value"]
                        )
                    elif stat["name"] == "finishes":
                        finishes = more_interesting(finishes, stat["value"])
                    elif stat["name"] == "balks":
                        if "value" in stat:
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
                        if "value" in stat:
                            wild_pitches = more_interesting(wild_pitches, stat["value"])
                    elif stat["name"] == "thirdInnings":
                        third_innings = more_interesting(third_innings, stat["value"])
                    elif stat["name"] == "teamEarnedRuns":
                        team_earned_runs = more_interesting(
                            team_earned_runs, stat["value"]
                        )
                    elif stat["name"] == "shutouts":
                        shutouts = more_interesting(shutouts, stat["value"])
                    elif stat["name"] == "pickoffAttempts":
                        pickoff_attempts = more_interesting(
                            pickoff_attempts, stat["value"]
                        )
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
                        opponent_average = more_interesting(
                            opponent_average, stat["value"]
                        )
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
                        save_percentage = more_interesting(
                            save_percentage, stat["value"]
                        )
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
                            team_games_played,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "doublePlays":
                        if "value" in stat:
                            double_plays = more_interesting(double_plays, stat["value"])
                    elif stat["name"] == "opportunities":
                        opportunities = more_interesting(opportunities, stat["value"])
                    elif stat["name"] == "errors":
                        if "value" in stat:
                            errors = more_interesting(errors, stat["value"])
                    elif stat["name"] == "passedBalls":
                        if "value" in stat:
                            passed_balls = more_interesting(passed_balls, stat["value"])
                    elif stat["name"] == "assists":
                        assists = more_interesting(assists, stat["value"])
                    elif stat["name"] == "outfieldAssists":
                        if "value" in stat:
                            outfield_assists = more_interesting(
                                outfield_assists, stat["value"]
                            )
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
                        turnover_points = more_interesting(
                            turnover_points, stat["value"]
                        )
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
                        technical_fouls = more_interesting(
                            technical_fouls, stat["value"]
                        )
                    elif stat["name"] == "rebounds":
                        rebounds = more_interesting(rebounds, stat["value"])
                    elif stat["name"] == "VORP":
                        vorp = more_interesting(vorp, stat["value"])
                    elif stat["name"] == "avgMinutes":
                        average_minutes = more_interesting(
                            average_minutes, stat["value"]
                        )
                    elif stat["name"] == "NBARating":
                        nba_rating = more_interesting(nba_rating, stat["value"])
                    elif stat["name"] == "avgRebounds":
                        average_rebounds = more_interesting(
                            average_rebounds, stat["value"]
                        )
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
                        steal_foul_ratio = more_interesting(
                            steal_foul_ratio, stat["value"]
                        )
                    elif stat["name"] == "blockFoulRatio":
                        block_foul_ratio = more_interesting(
                            block_foul_ratio, stat["value"]
                        )
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
                        average_48_fouls = more_interesting(
                            average_48_fouls, stat["value"]
                        )
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
                        field_goals_made = more_interesting(
                            field_goals_made, stat["value"]
                        )
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
                        free_throws_made = more_interesting(
                            free_throws_made, stat["value"]
                        )
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
                        total_turnovers = more_interesting(
                            total_turnovers, stat["value"]
                        )
                    elif stat["name"] == "pointsInPaint":
                        points_in_paint = more_interesting(
                            points_in_paint, stat["value"]
                        )
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
                        average_assists = more_interesting(
                            average_assists, stat["value"]
                        )
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
                    elif stat["name"] == "fumbles":
                        fumbles = more_interesting(fumbles, stat["value"])
                    elif stat["name"] == "fumblesLost":
                        fumbles_lost = more_interesting(fumbles_lost, stat["value"])
                    elif stat["name"] == "fumblesForced":
                        fumbles_forced = more_interesting(fumbles_forced, stat["value"])
                    elif stat["name"] == "fumblesRecovered":
                        fumbles_recovered = more_interesting(
                            fumbles_recovered, stat["value"]
                        )
                    elif stat["name"] == "fumblesRecoveredYards":
                        fumbles_recovered_yards = more_interesting(
                            fumbles_recovered_yards, stat["value"]
                        )
                    elif stat["name"] == "fumblesTouchdowns":
                        fumbles_touchdowns = more_interesting(
                            fumbles_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "offensiveTwoPtReturns":
                        offensive_two_point_returns = more_interesting(
                            offensive_two_point_returns, stat["value"]
                        )
                    elif stat["name"] == "offensiveFumblesTouchdowns":
                        offensive_fumbles_touchdowns = more_interesting(
                            offensive_fumbles_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "defensiveFumblesTouchdowns":
                        defensive_fumbles_touchdowns = more_interesting(
                            defensive_fumbles_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "avgGain":
                        average_gain = more_interesting(average_gain, stat["value"])
                    elif stat["name"] == "completionPct":
                        completion_percentage = more_interesting(
                            completion_percentage, stat["value"]
                        )
                    elif stat["name"] == "completions":
                        completions = more_interesting(completions, stat["value"])
                    elif stat["name"] == "ESPNQBRating":
                        espn_qb_rating = more_interesting(espn_qb_rating, stat["value"])
                    elif stat["name"] == "interceptionPct":
                        interception_percentage = more_interesting(
                            interception_percentage, stat["value"]
                        )
                    elif stat["name"] == "longPassing":
                        long_passing = more_interesting(long_passing, stat["value"])
                    elif stat["name"] == "miscYards":
                        misc_yards = more_interesting(misc_yards, stat["value"])
                    elif stat["name"] == "netPassingYards":
                        net_passing_yards = more_interesting(
                            net_passing_yards, stat["value"]
                        )
                    elif stat["name"] == "netPassingYardsPerGame":
                        net_passing_yards_per_game = more_interesting(
                            net_passing_yards_per_game, stat["value"]
                        )
                    elif stat["name"] == "netTotalYards":
                        net_total_yards = more_interesting(
                            net_total_yards, stat["value"]
                        )
                    elif stat["name"] == "netYardsPerGame":
                        net_yards_per_game = more_interesting(
                            net_yards_per_game, stat["value"]
                        )
                    elif stat["name"] == "passingAttempts":
                        passing_attempts = more_interesting(
                            passing_attempts, stat["value"]
                        )
                    elif stat["name"] == "passingBigPlays":
                        passing_big_plays = more_interesting(
                            passing_big_plays, stat["value"]
                        )
                    elif stat["name"] == "passingFirstDowns":
                        passing_first_downs = more_interesting(
                            passing_first_downs, stat["value"]
                        )
                    elif stat["name"] == "passingFumbles":
                        passing_fumbles = more_interesting(
                            passing_fumbles, stat["value"]
                        )
                    elif stat["name"] == "passingFumblesLost":
                        passing_fumbles_lost = more_interesting(
                            passing_fumbles_lost, stat["value"]
                        )
                    elif stat["name"] == "passingTouchdownPct":
                        passing_touchdown_percentage = more_interesting(
                            passing_touchdown_percentage, stat["value"]
                        )
                    elif stat["name"] == "passingTouchdowns":
                        passing_touchdowns = more_interesting(
                            passing_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "passingYards":
                        passing_yards = more_interesting(passing_yards, stat["value"])
                    elif stat["name"] == "passingYardsAfterCatch":
                        passing_yards_after_catch = more_interesting(
                            passing_yards_after_catch, stat["value"]
                        )
                    elif stat["name"] == "passingYardsAtCatch":
                        passing_yards_at_catch = more_interesting(
                            passing_yards_at_catch, stat["value"]
                        )
                    elif stat["name"] == "passingYardsPerGame":
                        passing_yards_per_game = more_interesting(
                            passing_yards_per_game, stat["value"]
                        )
                    elif stat["name"] == "QBRating":
                        qb_rating = more_interesting(qb_rating, stat["value"])
                    elif stat["name"] == "sacks":
                        sacks = more_interesting(sacks, stat["value"])
                    elif stat["name"] == "sackYardsLost":
                        sack_yards_lost = more_interesting(
                            sack_yards_lost, stat["value"]
                        )
                    elif stat["name"] == "netPassingAttempts":
                        net_passing_attempts = more_interesting(
                            net_passing_attempts, stat["value"]
                        )
                    elif stat["name"] == "totalOffensivePlays":
                        total_offensive_plays = more_interesting(
                            total_offensive_plays, stat["value"]
                        )
                    elif stat["name"] == "totalPoints":
                        total_points = more_interesting(total_points, stat["value"])
                    elif stat["name"] == "totalPointsPerGame":
                        total_points_per_game = more_interesting(
                            total_points_per_game, stat["value"]
                        )
                    elif stat["name"] == "totalTouchdowns":
                        total_touchdowns = more_interesting(
                            total_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "totalYards":
                        total_yards = more_interesting(total_yards, stat["value"])
                    elif stat["name"] == "totalYardsFromScrimmage":
                        total_yards_from_scrimmage = more_interesting(
                            total_yards_from_scrimmage, stat["value"]
                        )
                    elif stat["name"] == "twoPointPassConvs":
                        two_point_pass_convs = more_interesting(
                            two_point_pass_convs, stat["value"]
                        )
                    elif stat["name"] == "twoPtPass":
                        two_point_pass = more_interesting(two_point_pass, stat["value"])
                    elif stat["name"] == "twoPtPassAttempts":
                        two_point_pass_attempts = more_interesting(
                            two_point_pass_attempts, stat["value"]
                        )
                    elif stat["name"] == "yardsFromScrimmagePerGame":
                        yards_from_scrimmage_per_game = more_interesting(
                            yards_from_scrimmage_per_game, stat["value"]
                        )
                    elif stat["name"] == "yardsPerCompletion":
                        yards_per_completion = more_interesting(
                            yards_per_completion, stat["value"]
                        )
                    elif stat["name"] == "yardsPerGame":
                        yards_per_game = more_interesting(yards_per_game, stat["value"])
                    elif stat["name"] == "yardsPerPassAttempt":
                        yards_per_pass_attempt = more_interesting(
                            yards_per_pass_attempt, stat["value"]
                        )
                    elif stat["name"] == "netYardsPerPassAttempt":
                        net_yards_per_pass_attempt = more_interesting(
                            net_yards_per_pass_attempt, stat["value"]
                        )
                    elif stat["name"] == "quarterbackRating":
                        quarterback_rating = more_interesting(
                            quarterback_rating, stat["value"]
                        )
                    elif stat["name"] == "ESPNRBRating":
                        espn_rb_rating = more_interesting(espn_rb_rating, stat["value"])
                    elif stat["name"] == "longRushing":
                        long_rushing = more_interesting(long_rushing, stat["value"])
                    elif stat["name"] == "rushingAttempts":
                        rushing_attempts = more_interesting(
                            rushing_attempts, stat["value"]
                        )
                    elif stat["name"] == "rushingBigPlays":
                        rushing_big_plays = more_interesting(
                            rushing_big_plays, stat["value"]
                        )
                    elif stat["name"] == "rushingFirstDowns":
                        rushing_first_downs = more_interesting(
                            rushing_first_downs, stat["value"]
                        )
                    elif stat["name"] == "rushingFumbles":
                        rushing_fumbles = more_interesting(
                            rushing_fumbles, stat["value"]
                        )
                    elif stat["name"] == "rushingFumblesLost":
                        rushing_fumbles_lost = more_interesting(
                            rushing_fumbles_lost, stat["value"]
                        )
                    elif stat["name"] == "rushingTouchdowns":
                        rushing_touchdowns = more_interesting(
                            rushing_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "rushingYards":
                        rushing_yards = more_interesting(rushing_yards, stat["value"])
                    elif stat["name"] == "rushingYardsPerGame":
                        rushing_yards_per_game = more_interesting(
                            rushing_yards_per_game, stat["value"]
                        )
                    elif stat["name"] == "stuffs":
                        stuffs = more_interesting(stuffs, stat["value"])
                    elif stat["name"] == "stuffYardsLost":
                        stuff_yards_lost = more_interesting(
                            stuff_yards_lost, stat["value"]
                        )
                    elif stat["name"] == "twoPointRushConvs":
                        two_point_rush_conversions = more_interesting(
                            two_point_rush_conversions, stat["value"]
                        )
                    elif stat["name"] == "twoPtRush":
                        two_point_rush = more_interesting(two_point_rush, stat["value"])
                    elif stat["name"] == "twoPtRushAttempts":
                        two_point_rush_attempts = more_interesting(
                            two_point_rush_attempts, stat["value"]
                        )
                    elif stat["name"] == "yardsPerRushAttempt":
                        yards_per_rush_attempt = more_interesting(
                            yards_per_rush_attempt, stat["value"]
                        )
                    elif stat["name"] == "ESPNWRRating":
                        espn_wr_rating = more_interesting(espn_wr_rating, stat["value"])
                    elif stat["name"] == "longReception":
                        long_reception = more_interesting(long_reception, stat["value"])
                    elif stat["name"] == "receivingBigPlays":
                        receiving_big_plays = more_interesting(
                            receiving_big_plays, stat["value"]
                        )
                    elif stat["name"] == "receivingFirstDowns":
                        receiving_first_downs = more_interesting(
                            receiving_first_downs, stat["value"]
                        )
                    elif stat["name"] == "receivingFumbles":
                        receiving_fumbles = more_interesting(
                            receiving_fumbles, stat["value"]
                        )
                    elif stat["name"] == "receivingFumblesLost":
                        receiving_fumbles_lost = more_interesting(
                            receiving_fumbles_lost, stat["value"]
                        )
                    elif stat["name"] == "receivingTargets":
                        receiving_targets = more_interesting(
                            receiving_targets, stat["value"]
                        )
                    elif stat["name"] == "receivingTouchdowns":
                        receiving_touchdowns = more_interesting(
                            receiving_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "receivingYards":
                        receiving_yards = more_interesting(
                            receiving_yards, stat["value"]
                        )
                    elif stat["name"] == "receivingYardsAfterCatch":
                        receiving_yards_after_catch = more_interesting(
                            receiving_yards_after_catch, stat["value"]
                        )
                    elif stat["name"] == "receivingYardsAtCatch":
                        receiving_yards_at_catch = more_interesting(
                            receiving_yards_at_catch, stat["value"]
                        )
                    elif stat["name"] == "receivingYardsPerGame":
                        receiving_yards_per_game = more_interesting(
                            receiving_yards_per_game, stat["value"]
                        )
                    elif stat["name"] == "receptions":
                        receptions = more_interesting(receptions, stat["value"])
                    elif stat["name"] == "twoPointRecConvs":
                        two_point_rec_conversions = more_interesting(
                            two_point_rec_conversions, stat["value"]
                        )
                    elif stat["name"] == "twoPtReception":
                        two_point_reception = more_interesting(
                            two_point_reception, stat["value"]
                        )
                    elif stat["name"] == "twoPtReceptionAttempts":
                        two_point_reception_attempts = more_interesting(
                            two_point_reception_attempts, stat["value"]
                        )
                    elif stat["name"] == "yardsPerReception":
                        yards_per_reception = more_interesting(
                            yards_per_reception, stat["value"]
                        )
                    elif stat["name"] == "assistTackles":
                        assist_tackles = more_interesting(assist_tackles, stat["value"])
                    elif stat["name"] == "avgInterceptionYards":
                        average_interception_yards = more_interesting(
                            average_interception_yards, stat["value"]
                        )
                    elif stat["name"] == "avgSackYards":
                        average_sack_yards = more_interesting(
                            average_sack_yards, stat["value"]
                        )
                    elif stat["name"] == "avgStuffYards":
                        average_stuff_yards = more_interesting(
                            average_stuff_yards, stat["value"]
                        )
                    elif stat["name"] == "blockedFieldGoalTouchdowns":
                        blocked_field_goal_touchdowns = more_interesting(
                            blocked_field_goal_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "blockedPuntTouchdowns":
                        blocked_punt_touchdowns = more_interesting(
                            blocked_punt_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "defensiveTouchdowns":
                        defensive_touchdowns = more_interesting(
                            defensive_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "hurries":
                        hurries = more_interesting(hurries, stat["value"])
                    elif stat["name"] == "kicksBlocked":
                        kicks_blocked = more_interesting(kicks_blocked, stat["value"])
                    elif stat["name"] == "longInterception":
                        long_interception = more_interesting(
                            long_interception, stat["value"]
                        )
                    elif stat["name"] == "miscTouchdowns":
                        misc_touchdowns = more_interesting(
                            misc_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "passesBattedDown":
                        passes_batted_down = more_interesting(
                            passes_batted_down, stat["value"]
                        )
                    elif stat["name"] == "passesDefended":
                        passes_defended = more_interesting(
                            passes_defended, stat["value"]
                        )
                    elif stat["name"] == "QBHits":
                        qb_hits = more_interesting(qb_hits, stat["value"])
                    elif stat["name"] == "twoPtReturns":
                        two_point_returns = more_interesting(
                            two_point_returns, stat["value"]
                        )
                    elif stat["name"] == "sacksAssisted":
                        sacks_assisted = more_interesting(sacks_assisted, stat["value"])
                    elif stat["name"] == "sacksUnassisted":
                        sacks_unassisted = more_interesting(
                            sacks_unassisted, stat["value"]
                        )
                    elif stat["name"] == "sackYards":
                        sack_yards = more_interesting(sack_yards, stat["value"])
                    elif stat["name"] == "safeties":
                        safeties = more_interesting(safeties, stat["value"])
                    elif stat["name"] == "soloTackles":
                        solo_tackles = more_interesting(solo_tackles, stat["value"])
                    elif stat["name"] == "stuffYards":
                        stuff_yards = more_interesting(stuff_yards, stat["value"])
                    elif stat["name"] == "tacklesForLoss":
                        tackles_for_loss = more_interesting(
                            tackles_for_loss, stat["value"]
                        )
                    elif stat["name"] == "tacklesYardsLost":
                        tackles_yards_lost = more_interesting(
                            tackles_yards_lost, stat["value"]
                        )
                    elif stat["name"] == "yardsAllowed":
                        yards_allowed = more_interesting(yards_allowed, stat["value"])
                    elif stat["name"] == "pointsAllowed":
                        points_allowed = more_interesting(points_allowed, stat["value"])
                    elif stat["name"] == "onePtSafetiesMade":
                        one_point_safeties_made = more_interesting(
                            one_point_safeties_made, stat["value"]
                        )
                    elif stat["name"] == "missedFieldGoalReturnTd":
                        missed_field_goal_return_td = more_interesting(
                            missed_field_goal_return_td, stat["value"]
                        )
                    elif stat["name"] == "blockedPuntEzRecTd":
                        blocked_punt_ez_rec_td = more_interesting(
                            blocked_punt_ez_rec_td, stat["value"]
                        )
                    elif stat["name"] == "interceptionTouchdowns":
                        interception_touchdowns = more_interesting(
                            interception_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "interceptionYards":
                        interception_yards = more_interesting(
                            interception_yards, stat["value"]
                        )
                    elif stat["name"] == "avgKickoffReturnYards":
                        average_kickoff_return_yards = more_interesting(
                            average_kickoff_return_yards, stat["value"]
                        )
                    elif stat["name"] == "avgKickoffYards":
                        average_kickoff_yards = more_interesting(
                            average_kickoff_yards, stat["value"]
                        )
                    elif stat["name"] == "extraPointAttempts":
                        extra_point_attempts = more_interesting(
                            extra_point_attempts, stat["value"]
                        )
                    elif stat["name"] == "extraPointPct":
                        extra_point_percentage = more_interesting(
                            extra_point_percentage, stat["value"]
                        )
                    elif stat["name"] == "extraPointsBlocked":
                        extra_points_blocked = more_interesting(
                            extra_points_blocked, stat["value"]
                        )
                    elif stat["name"] == "extraPointsBlockedPct":
                        extra_points_blocked_percentage = more_interesting(
                            extra_points_blocked_percentage, stat["value"]
                        )
                    elif stat["name"] == "extraPointsMade":
                        extra_points_made = more_interesting(
                            extra_points_made, stat["value"]
                        )
                    elif stat["name"] == "fairCatches":
                        fair_catches = more_interesting(fair_catches, stat["value"])
                    elif stat["name"] == "fairCatchPct":
                        fair_catch_percentage = more_interesting(
                            fair_catch_percentage, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts":
                        field_goal_attempts = more_interesting(
                            field_goal_attempts, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts1_19":
                        field_goal_attempts_1_19 = more_interesting(
                            field_goal_attempts_1_19, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts20_29":
                        field_goal_attempts_20_29 = more_interesting(
                            field_goal_attempts_20_29, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts30_39":
                        field_goal_attempts_30_39 = more_interesting(
                            field_goal_attempts_30_39, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts40_49":
                        field_goal_attempts_40_49 = more_interesting(
                            field_goal_attempts_40_49, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts50_59":
                        field_goal_attempts_50_59 = more_interesting(
                            field_goal_attempts_50_59, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts60_99":
                        field_goal_attempts_60_99 = more_interesting(
                            field_goal_attempts_60_99, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttempts50":
                        field_goal_attempts_50 = more_interesting(
                            field_goal_attempts_50, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalAttemptYards":
                        field_goal_attempt_yards = more_interesting(
                            field_goal_attempt_yards, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsBlocked":
                        field_goals_blocked = more_interesting(
                            field_goals_blocked, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsBlockedPct":
                        field_goals_blocked_percentage = more_interesting(
                            field_goals_blocked_percentage, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade1_19":
                        field_goals_made_1_19 = more_interesting(
                            field_goals_made_1_19, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade20_29":
                        field_goals_made_20_29 = more_interesting(
                            field_goals_made_20_29, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade30_39":
                        field_goals_made_30_39 = more_interesting(
                            field_goals_made_30_39, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade40_49":
                        field_goals_made_40_49 = more_interesting(
                            field_goals_made_40_49, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade50_59":
                        field_goals_made_50_59 = more_interesting(
                            field_goals_made_50_59, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade60_99":
                        field_goals_made_60_99 = more_interesting(
                            field_goals_made_60_99, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMade50":
                        field_goals_made_50 = more_interesting(
                            field_goals_made_50, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMadeYards":
                        field_goals_made_yards = more_interesting(
                            field_goals_made_yards, stat["value"]
                        )
                    elif stat["name"] == "fieldGoalsMissedYards":
                        field_goals_missed_yards = more_interesting(
                            field_goals_missed_yards, stat["value"]
                        )
                    elif stat["name"] == "kickoffOB":
                        kickoff_ob = more_interesting(kickoff_ob, stat["value"])
                    elif stat["name"] == "kickoffReturns":
                        kickoff_returns = more_interesting(
                            kickoff_returns, stat["value"]
                        )
                    elif stat["name"] == "kickoffReturnTouchdowns":
                        kickoff_return_touchdowns = more_interesting(
                            kickoff_return_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "kickoffReturnYards":
                        kickoff_return_yards = more_interesting(
                            kickoff_return_yards, stat["value"]
                        )
                    elif stat["name"] == "kickoffs":
                        kickoffs = more_interesting(kickoffs, stat["value"])
                    elif stat["name"] == "kickoffYards":
                        kickoff_yards = more_interesting(kickoff_yards, stat["value"])
                    elif stat["name"] == "longFieldGoalAttempt":
                        long_field_goal_attempt = more_interesting(
                            long_field_goal_attempt, stat["value"]
                        )
                    elif stat["name"] == "longFieldGoalMade":
                        long_field_goal_made = more_interesting(
                            long_field_goal_made, stat["value"]
                        )
                    elif stat["name"] == "longKickoff":
                        long_kickoff = more_interesting(long_kickoff, stat["value"])
                    elif stat["name"] == "totalKickingPoints":
                        total_kicking_points = more_interesting(
                            total_kicking_points, stat["value"]
                        )
                    elif stat["name"] == "touchbackPct":
                        touchback_percentage = more_interesting(
                            touchback_percentage, stat["value"]
                        )
                    elif stat["name"] == "touchbacks":
                        touchbacks = more_interesting(touchbacks, stat["value"])
                    elif stat["name"] == "defFumbleReturns":
                        def_fumble_returns = more_interesting(
                            def_fumble_returns, stat["value"]
                        )
                    elif stat["name"] == "defFumbleReturnYards":
                        def_fumble_return_yards = more_interesting(
                            def_fumble_return_yards, stat["value"]
                        )
                    elif stat["name"] == "fumbleRecoveries":
                        fumble_recoveries = more_interesting(
                            fumble_recoveries, stat["value"]
                        )
                    elif stat["name"] == "fumbleRecoveryYards":
                        fumble_recovery_yards = more_interesting(
                            fumble_recovery_yards, stat["value"]
                        )
                    elif stat["name"] == "kickReturnFairCatches":
                        kick_return_fair_catches = more_interesting(
                            kick_return_fair_catches, stat["value"]
                        )
                    elif stat["name"] == "kickReturnFairCatchPct":
                        kick_return_fair_catch_percentage = more_interesting(
                            kick_return_fair_catch_percentage, stat["value"]
                        )
                    elif stat["name"] == "kickReturnFumbles":
                        kick_return_fumbles = more_interesting(
                            kick_return_fumbles, stat["value"]
                        )
                    elif stat["name"] == "kickReturnFumblesLost":
                        kick_return_fumbles_lost = more_interesting(
                            kick_return_fumbles_lost, stat["value"]
                        )
                    elif stat["name"] == "kickReturns":
                        kick_returns = more_interesting(kick_returns, stat["value"])
                    elif stat["name"] == "kickReturnTouchdowns":
                        kick_return_touchdowns = more_interesting(
                            kick_return_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "kickReturnYards":
                        kick_return_yards = more_interesting(
                            kick_return_yards, stat["value"]
                        )
                    elif stat["name"] == "longKickReturn":
                        long_kick_return = more_interesting(
                            long_kick_return, stat["value"]
                        )
                    elif stat["name"] == "longPuntReturn":
                        long_punt_return = more_interesting(
                            long_punt_return, stat["value"]
                        )
                    elif stat["name"] == "miscFumbleReturns":
                        misc_fumble_returns = more_interesting(
                            misc_fumble_returns, stat["value"]
                        )
                    elif stat["name"] == "miscFumbleReturnYards":
                        misc_fumble_return_yards = more_interesting(
                            misc_fumble_return_yards, stat["value"]
                        )
                    elif stat["name"] == "oppFumbleRecoveries":
                        opp_fumble_recoveries = more_interesting(
                            opp_fumble_recoveries, stat["value"]
                        )
                    elif stat["name"] == "oppFumbleRecoveryYards":
                        opp_fumble_recovery_yards = more_interesting(
                            opp_fumble_recovery_yards, stat["value"]
                        )
                    elif stat["name"] == "oppSpecialTeamFumbleReturns":
                        opp_special_team_fumble_returns = more_interesting(
                            opp_special_team_fumble_returns, stat["value"]
                        )
                    elif stat["name"] == "oppSpecialTeamFumbleReturnYards":
                        opp_special_team_fumble_return_yards = more_interesting(
                            opp_special_team_fumble_return_yards, stat["value"]
                        )
                    elif stat["name"] == "puntReturnFairCatches":
                        punt_return_fair_catches = more_interesting(
                            punt_return_fair_catches, stat["value"]
                        )
                    elif stat["name"] == "puntReturnFairCatchPct":
                        punt_return_fair_catch_percentage = more_interesting(
                            punt_return_fair_catch_percentage, stat["value"]
                        )
                    elif stat["name"] == "puntReturnFumbles":
                        punt_return_fumbles = more_interesting(
                            punt_return_fumbles, stat["value"]
                        )
                    elif stat["name"] == "puntReturnFumblesLost":
                        punt_return_fumbles_lost = more_interesting(
                            punt_return_fumbles_lost, stat["value"]
                        )
                    elif stat["name"] == "puntReturns":
                        punt_returns = more_interesting(punt_returns, stat["value"])
                    elif stat["name"] == "puntReturnsStartedInsideThe10":
                        punt_returns_started_inside_the_10 = more_interesting(
                            punt_returns_started_inside_the_10, stat["value"]
                        )
                    elif stat["name"] == "puntReturnsStartedInsideThe20":
                        punt_returns_started_inside_the_20 = more_interesting(
                            punt_returns_started_inside_the_20, stat["value"]
                        )
                    elif stat["name"] == "puntReturnTouchdowns":
                        punt_return_touchdowns = more_interesting(
                            punt_return_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "puntReturnYards":
                        punt_return_yards = more_interesting(
                            punt_return_yards, stat["value"]
                        )
                    elif stat["name"] == "specialTeamFumbleReturns":
                        special_team_fumble_returns = more_interesting(
                            special_team_fumble_returns, stat["value"]
                        )
                    elif stat["name"] == "specialTeamFumbleReturnYards":
                        special_team_fumble_return_yards = more_interesting(
                            special_team_fumble_return_yards, stat["value"]
                        )
                    elif stat["name"] == "yardsPerKickReturn":
                        yards_per_kick_return = more_interesting(
                            yards_per_kick_return, stat["value"]
                        )
                    elif stat["name"] == "yardsPerPuntReturn":
                        yards_per_punt_return = more_interesting(
                            yards_per_punt_return, stat["value"]
                        )
                    elif stat["name"] == "yardsPerReturn":
                        yards_per_return = more_interesting(
                            yards_per_return, stat["value"]
                        )
                    elif stat["name"] == "avgPuntReturnYards":
                        average_punt_return_yards = more_interesting(
                            average_punt_return_yards, stat["value"]
                        )
                    elif stat["name"] == "grossAvgPuntYards":
                        gross_average_punt_yards = more_interesting(
                            gross_average_punt_yards, stat["value"]
                        )
                    elif stat["name"] == "longPunt":
                        long_punt = more_interesting(long_punt, stat["value"])
                    elif stat["name"] == "netAvgPuntYards":
                        net_average_punt_yards = more_interesting(
                            net_average_punt_yards, stat["value"]
                        )
                    elif stat["name"] == "punts":
                        punts = more_interesting(punts, stat["value"])
                    elif stat["name"] == "puntsBlocked":
                        punts_blocked = more_interesting(punts_blocked, stat["value"])
                    elif stat["name"] == "puntsBlockedPct":
                        punts_blocked_percentage = more_interesting(
                            punts_blocked_percentage, stat["value"]
                        )
                    elif stat["name"] == "puntsInside10":
                        punts_inside_10 = more_interesting(
                            punts_inside_10, stat["value"]
                        )
                    elif stat["name"] == "puntsInside10Pct":
                        punts_inside_10_percentage = more_interesting(
                            punts_inside_10_percentage, stat["value"]
                        )
                    elif stat["name"] == "puntsInside20":
                        punts_inside_20 = more_interesting(
                            punts_inside_20, stat["value"]
                        )
                    elif stat["name"] == "puntsInside20Pct":
                        punts_inside_20_percentage = more_interesting(
                            punts_inside_20_percentage, stat["value"]
                        )
                    elif stat["name"] == "puntsOver50":
                        punts_over_50 = more_interesting(punts_over_50, stat["value"])
                    elif stat["name"] == "puntYards":
                        punt_yards = more_interesting(punt_yards, stat["value"])
                    elif stat["name"] == "defensivePoints":
                        defensive_points = more_interesting(
                            defensive_points, stat["value"]
                        )
                    elif stat["name"] == "kickExtraPoints":
                        kick_extra_points = more_interesting(
                            kick_extra_points, stat["value"]
                        )
                    elif stat["name"] == "kickExtraPointsMade":
                        kick_extra_points_made = more_interesting(
                            kick_extra_points_made, stat["value"]
                        )
                    elif stat["name"] == "miscPoints":
                        misc_points = more_interesting(misc_points, stat["value"])
                    elif stat["name"] == "returnTouchdowns":
                        return_touchdowns = more_interesting(
                            return_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "totalTwoPointConvs":
                        total_two_point_conversions = more_interesting(
                            total_two_point_conversions, stat["value"]
                        )
                    elif stat["name"] == "firstDowns":
                        first_downs = more_interesting(first_downs, stat["value"])
                    elif stat["name"] == "firstDownsPassing":
                        first_downs_passing = more_interesting(
                            first_downs_passing, stat["value"]
                        )
                    elif stat["name"] == "firstDownsPenalty":
                        first_downs_penalty = more_interesting(
                            first_downs_penalty, stat["value"]
                        )
                    elif stat["name"] == "firstDownsPerGame":
                        first_downs_per_game = more_interesting(
                            first_downs_per_game, stat["value"]
                        )
                    elif stat["name"] == "firstDownsRushing":
                        first_downs_rushing = more_interesting(
                            first_downs_rushing, stat["value"]
                        )
                    elif stat["name"] == "fourthDownAttempts":
                        fourth_down_attempts = more_interesting(
                            fourth_down_attempts, stat["value"]
                        )
                    elif stat["name"] == "fourthDownConvPct":
                        fourth_down_conversion_percentage = more_interesting(
                            fourth_down_conversion_percentage, stat["value"]
                        )
                    elif stat["name"] == "fourthDownConvs":
                        fourth_down_conversions = more_interesting(
                            fourth_down_conversions, stat["value"]
                        )
                    elif stat["name"] == "possessionTimeSeconds":
                        possession_time_seconds = more_interesting(
                            possession_time_seconds, stat["value"]
                        )
                    elif stat["name"] == "redzoneAttemptPoints":
                        redzone_attempt_points = more_interesting(
                            redzone_attempt_points, stat["value"]
                        )
                    elif stat["name"] == "redzoneAttempts":
                        redzone_attempts = more_interesting(
                            redzone_attempts, stat["value"]
                        )
                    elif stat["name"] == "redzoneConversion":
                        redzone_conversions = more_interesting(
                            redzone_conversions, stat["value"]
                        )
                    elif stat["name"] == "redzoneEfficiencyPct":
                        redzone_efficiency_percentage = more_interesting(
                            redzone_efficiency_percentage, stat["value"]
                        )
                    elif stat["name"] == "redzoneEndDowns":
                        redzone_end_downs = more_interesting(
                            redzone_end_downs, stat["value"]
                        )
                    elif stat["name"] == "redzoneEndGame":
                        redzone_end_game = more_interesting(
                            redzone_end_game, stat["value"]
                        )
                    elif stat["name"] == "redzoneEndHalf":
                        redzone_end_half = more_interesting(
                            redzone_end_half, stat["value"]
                        )
                    elif stat["name"] == "redzoneFieldGoalPct":
                        redzone_field_goal_percentage = more_interesting(
                            redzone_field_goal_percentage, stat["value"]
                        )
                    elif stat["name"] == "redzoneFieldGoalPoints":
                        redzone_field_goal_points = more_interesting(
                            redzone_field_goal_points, stat["value"]
                        )
                    elif stat["name"] == "redzoneFieldGoals":
                        redzone_field_goals = more_interesting(
                            redzone_field_goals, stat["value"]
                        )
                    elif stat["name"] == "redzoneFieldGoalsMissed":
                        redzone_field_goals_missed = more_interesting(
                            redzone_field_goals_missed, stat["value"]
                        )
                    elif stat["name"] == "redzoneFumble":
                        redzone_fumble = more_interesting(redzone_fumble, stat["value"])
                    elif stat["name"] == "redzoneInterception":
                        redzone_interception = more_interesting(
                            redzone_interception, stat["value"]
                        )
                    elif stat["name"] == "redzoneScoringPct":
                        redzone_scoring_percentage = more_interesting(
                            redzone_scoring_percentage, stat["value"]
                        )
                    elif stat["name"] == "redzoneTotalPoints":
                        redzone_total_points = more_interesting(
                            redzone_total_points, stat["value"]
                        )
                    elif stat["name"] == "redzoneTouchdownPass":
                        redzone_touchdown_pass = more_interesting(
                            redzone_touchdown_pass, stat["value"]
                        )
                    elif stat["name"] == "redzoneTouchdownPct":
                        redzone_touchdown_percentage = more_interesting(
                            redzone_touchdown_percentage, stat["value"]
                        )
                    elif stat["name"] == "redzoneTouchdownPoints":
                        redzone_touchdown_points = more_interesting(
                            redzone_touchdown_points, stat["value"]
                        )
                    elif stat["name"] == "redzoneTouchdownRush":
                        redzone_touchdown_rush = more_interesting(
                            redzone_touchdown_rush, stat["value"]
                        )
                    elif stat["name"] == "redzoneTouchdowns":
                        redzone_touchdowns = more_interesting(
                            redzone_touchdowns, stat["value"]
                        )
                    elif stat["name"] == "thirdDownAttempts":
                        third_down_attempts = more_interesting(
                            third_down_attempts, stat["value"]
                        )
                    elif stat["name"] == "thirdDownConvPct":
                        third_down_conversion_percentage = more_interesting(
                            third_down_conversion_percentage, stat["value"]
                        )
                    elif stat["name"] == "thirdDownConvs":
                        third_down_conversions = more_interesting(
                            third_down_conversions, stat["value"]
                        )
                    elif stat["name"] == "timeoutsUsed":
                        timeouts_used = more_interesting(timeouts_used, stat["value"])
                    elif stat["name"] == "totalPenalties":
                        total_penalties = more_interesting(
                            total_penalties, stat["value"]
                        )
                    elif stat["name"] == "totalPenaltyYards":
                        total_penalty_yards = more_interesting(
                            total_penalty_yards, stat["value"]
                        )
                    elif stat["name"] == "totalPlays":
                        total_plays = more_interesting(total_plays, stat["value"])
                    elif stat["name"] == "totalDrives":
                        total_drives = more_interesting(total_drives, stat["value"])
                    elif stat["name"] == "turnOverDifferential":
                        turn_over_differential = more_interesting(
                            turn_over_differential, stat["value"]
                        )
                    elif stat["name"] == "goalsAgainst":
                        goals_against = more_interesting(goals_against, stat["value"])
                    elif stat["name"] == "shotsAgainst":
                        shots_against = more_interesting(shots_against, stat["value"])
                    elif stat["name"] == "penaltyKillPct":
                        penalty_kill_percentage = more_interesting(
                            penalty_kill_percentage, stat["value"]
                        )
                    elif stat["name"] == "powerPlayGoalsAgainst":
                        power_play_goals_against = more_interesting(
                            power_play_goals_against, stat["value"]
                        )
                    elif stat["name"] == "shortHandedGoalsAgainst":
                        short_handed_goals_against = more_interesting(
                            short_handed_goals_against, stat["value"]
                        )
                    elif stat["name"] == "shootoutSaves":
                        shootout_saves = more_interesting(shootout_saves, stat["value"])
                    elif stat["name"] == "shootoutShotsAgainst":
                        shootout_shots_against = more_interesting(
                            shootout_shots_against, stat["value"]
                        )
                    elif stat["name"] == "shootoutSavePct":
                        shoot_out_save_percentage = more_interesting(
                            shoot_out_save_percentage, stat["value"]
                        )
                    elif stat["name"] == "timesShortHanded":
                        times_short_handed = more_interesting(
                            times_short_handed, stat["value"]
                        )
                    elif stat["name"] == "emptyNetGoalsAgainst":
                        empty_net_goals_against = more_interesting(
                            empty_net_goals_against, stat["value"]
                        )
                    elif stat["name"] == "takeaways":
                        takeaways = more_interesting(takeaways, stat["value"])
                    elif stat["name"] == "evenStrengthSaves":
                        even_strength_saves = more_interesting(
                            even_strength_saves,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "powerPlaySaves":
                        power_play_saves = more_interesting(
                            power_play_saves,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "shortHandedSaves":
                        short_handed_saves = more_interesting(
                            short_handed_saves,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "timeOnIce":
                        time_on_ice = more_interesting(time_on_ice, stat["value"])
                    elif stat["name"] == "powerPlayTimeOnIce":
                        power_play_time_on_ice = more_interesting(
                            power_play_time_on_ice, stat["value"]
                        )
                    elif stat["name"] == "shortHandedTimeOnIce":
                        short_handed_time_on_ice = more_interesting(
                            short_handed_time_on_ice, stat["value"]
                        )
                    elif stat["name"] == "evenStrengthTimeOnIce":
                        even_strength_time_on_ice = more_interesting(
                            even_strength_time_on_ice, stat["value"]
                        )
                    elif stat["name"] == "shifts":
                        shifts = more_interesting(shifts, stat["value"])
                    elif stat["name"] == "shotDifferential":
                        shot_differential = more_interesting(
                            shot_differential, stat["value"]
                        )
                    elif stat["name"] == "goalDifferential":
                        goal_differential = more_interesting(
                            goal_differential, stat["value"]
                        )
                    elif stat["name"] == "PIMDifferential":
                        pim_differential = more_interesting(
                            pim_differential, stat["value"]
                        )
                    elif stat["name"] == "rating":
                        rating = more_interesting(
                            rating, stat.get("value", float(stat["displayValue"]))
                        )
                    elif stat["name"] == "ytdGoals":
                        ytd_goals = more_interesting(
                            ytd_goals, stat.get("value", int(stat["displayValue"]))
                        )
                    elif stat["name"] == "shotsIn1stPeriod":
                        shots_in_first_period = more_interesting(
                            shots_in_first_period,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "shotsIn2ndPeriod":
                        shots_in_second_period = more_interesting(
                            shots_in_second_period,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "shotsIn3rdPeriod":
                        shots_in_third_period = more_interesting(
                            shots_in_third_period,
                            stat.get("value", int(stat["displayValue"])),
                        )
                    elif stat["name"] == "shotsOT":
                        shots_ot = more_interesting(
                            shots_ot, stat.get("value", int(stat["displayValue"]))
                        )
                    elif stat["name"] == "shotsTotal":
                        shots_total = more_interesting(shots_total, stat["value"])
                    elif stat["name"] == "shotsMissed":
                        shots_missed = more_interesting(shots_missed, stat["value"])
                    elif stat["name"] == "pointsPerGame":
                        points_per_game = more_interesting(
                            points_per_game,
                            stat.get("value", float(stat["displayValue"])),
                        )
                    elif stat["name"] == "powerPlayGoals":
                        power_play_goals = more_interesting(
                            power_play_goals, stat["value"]
                        )
                    elif stat["name"] == "powerPlayAssists":
                        power_play_assists = more_interesting(
                            power_play_assists, stat["value"]
                        )
                    elif stat["name"] == "powerPlayOpportunities":
                        power_play_opportunities = more_interesting(
                            power_play_opportunities, stat["value"]
                        )
                    elif stat["name"] == "powerPlayPct":
                        power_play_percentage = more_interesting(
                            power_play_percentage, stat["value"]
                        )
                    elif stat["name"] == "shortHandedGoals":
                        short_handed_goals = more_interesting(
                            short_handed_goals, stat["value"]
                        )
                    elif stat["name"] == "shortHandedAssists":
                        short_handed_assists = more_interesting(
                            short_handed_assists, stat["value"]
                        )
                    elif stat["name"] == "shootoutAttempts":
                        shootout_attempts = more_interesting(
                            shootout_attempts, stat["value"]
                        )
                    elif stat["name"] == "shootoutGoals":
                        shoot_out_goals = more_interesting(
                            shoot_out_goals, stat["value"]
                        )
                    elif stat["name"] == "shootoutShotPct":
                        shootout_shot_percentage = more_interesting(
                            shootout_shot_percentage, stat["value"]
                        )
                    elif stat["name"] == "emptyNetGoalsFor":
                        empty_net_goals_for = more_interesting(
                            empty_net_goals_for, stat["value"]
                        )
                    elif stat["name"] == "shootingPct":
                        shooting_percentage = more_interesting(
                            shooting_percentage, stat["value"]
                        )
                    elif stat["name"] == "totalFaceOffs":
                        total_face_offs = more_interesting(
                            total_face_offs, stat["value"]
                        )
                    elif stat["name"] == "faceoffsWon":
                        faceoffs_won = more_interesting(faceoffs_won, stat["value"])
                    elif stat["name"] == "faceoffsLost":
                        faceoffs_lost = more_interesting(faceoffs_lost, stat["value"])
                    elif stat["name"] == "faceoffPercent":
                        faceoff_percentage = more_interesting(
                            faceoff_percentage, stat["value"]
                        )
                    elif stat["name"] == "unassistedGoals":
                        unassisted_goals = more_interesting(
                            unassisted_goals, stat["value"]
                        )
                    elif stat["name"] == "giveaways":
                        giveaways = more_interesting(giveaways, stat["value"])
                    elif stat["name"] == "penalties":
                        penalties = more_interesting(penalties, stat["value"])
                    elif stat["name"] == "penaltyMinutes":
                        penalty_minutes = more_interesting(
                            penalty_minutes, stat["value"]
                        )
                    elif stat["name"] == "score":
                        pass
                    elif stat["name"] == "points":
                        pass
                    elif stat["name"] == "totalGiveaways":
                        total_giveaways = more_interesting(
                            total_giveaways,
                            stat["value"],
                        )
                    elif stat["name"] == "totalTakeaways":
                        total_takeaways = more_interesting(
                            total_takeaways, stat["value"]
                        )
                    elif stat["name"] == "fantasyRating":
                        fantasy_rating = more_interesting(fantasy_rating, stat["value"])
                    elif stat["name"] == "rbi":
                        pass
                    elif stat["name"] == "2outRBI":
                        pass
                    elif stat["name"] == "gidp":
                        pass
                    elif stat["name"] == "teamLOB":
                        pass
                    elif stat["name"] == "teamRISP":
                        pass
                    elif stat["name"] == "runnersLeftScoringPosition2Outs":
                        pass
                    elif stat["name"] == "secondChancePoints":
                        second_chance_points = more_interesting(
                            second_chance_points, stat["value"]
                        )
                    elif stat["name"] == "pitcherNotes":
                        pass
                    elif stat["name"] == "sacFly":
                        pass
                    elif stat["name"] == "pickedOff":
                        pass
                    elif stat["name"] == "plusMinus":
                        plus_minus = more_interesting(plus_minus, stat["value"])
                    elif stat["name"] == "firstPitchStrikesBattersFaced":
                        pass
                    elif stat["name"] == "sacHit":
                        pass
                    elif stat["name"] == "strikeRatio":
                        pass
                    elif stat["name"] == "groundballFlyballRatio":
                        pass
                    elif stat["name"] == "gameScores":
                        pass
                    else:
                        raise ValueError(
                            f"Failed to account for statistic: {stat['name']} on {statistics_dict['$ref']}"
                        )
        except KeyError as exc:
            logging.warning(
                "Key error for team ESPN stats URL: %s", statistics_dict["$ref"]
            )
            raise exc

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
        penalties=penalties,
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
        fumbles=fumbles,
        fumbles_lost=fumbles_lost,
        fumbles_forced=fumbles_forced,
        fumbles_recovered=fumbles_recovered,
        fumbles_recovered_yards=fumbles_recovered_yards,
        fumbles_touchdowns=fumbles_touchdowns,
        offensive_two_point_returns=offensive_two_point_returns,
        offensive_fumbles_touchdowns=offensive_fumbles_touchdowns,
        defensive_fumbles_touchdowns=defensive_fumbles_touchdowns,
        average_gain=average_gain,
        completion_percentage=completion_percentage,
        completions=completions,
        espn_qb_rating=espn_qb_rating,
        interception_percentage=interception_percentage,
        long_passing=long_passing,
        misc_yards=misc_yards,
        net_passing_yards=net_passing_yards,
        net_passing_yards_per_game=net_passing_yards_per_game,
        net_total_yards=net_total_yards,
        net_yards_per_game=net_yards_per_game,
        passing_attempts=passing_attempts,
        passing_big_plays=passing_big_plays,
        passing_first_downs=passing_first_downs,
        passing_fumbles=passing_fumbles,
        passing_fumbles_lost=passing_fumbles_lost,
        passing_touchdown_percentage=passing_touchdown_percentage,
        passing_touchdowns=passing_touchdowns,
        passing_yards=passing_yards,
        passing_yards_after_catch=passing_yards_after_catch,
        passing_yards_at_catch=passing_yards_at_catch,
        passing_yards_per_game=passing_yards_per_game,
        qb_rating=qb_rating,
        sacks=sacks,
        sack_yards_lost=sack_yards_lost,
        net_passing_attempts=net_passing_attempts,
        total_offensive_plays=total_offensive_plays,
        total_points=total_points,
        total_points_per_game=total_points_per_game,
        total_touchdowns=total_touchdowns,
        total_yards=total_yards,
        total_yards_from_scrimmage=total_yards_from_scrimmage,
        two_point_pass_convs=two_point_pass_convs,
        two_point_pass=two_point_pass,
        two_point_pass_attempts=two_point_pass_attempts,
        yards_from_scrimmage_per_game=yards_from_scrimmage_per_game,
        yards_per_completion=yards_per_completion,
        yards_per_game=yards_per_game,
        yards_per_pass_attempt=yards_per_pass_attempt,
        net_yards_per_pass_attempt=net_yards_per_pass_attempt,
        quarterback_rating=quarterback_rating,
        espn_rb_rating=espn_rb_rating,
        long_rushing=long_rushing,
        rushing_attempts=rushing_attempts,
        rushing_big_plays=rushing_big_plays,
        rushing_first_downs=rushing_first_downs,
        rushing_fumbles=rushing_fumbles,
        rushing_fumbles_lost=rushing_fumbles_lost,
        rushing_touchdowns=rushing_touchdowns,
        rushing_yards=rushing_yards,
        rushing_yards_per_game=rushing_yards_per_game,
        stuffs=stuffs,
        stuff_yards_lost=stuff_yards_lost,
        two_point_rush_conversions=two_point_rush_conversions,
        two_point_rush=two_point_rush,
        two_point_rush_attempts=two_point_rush_attempts,
        yards_per_rush_attempt=yards_per_rush_attempt,
        espn_wr_rating=espn_wr_rating,
        long_reception=long_reception,
        receiving_big_plays=receiving_big_plays,
        receiving_first_downs=receiving_first_downs,
        receiving_fumbles=receiving_fumbles,
        receiving_fumbles_lost=receiving_fumbles_lost,
        receiving_targets=receiving_targets,
        receiving_touchdowns=receiving_touchdowns,
        receiving_yards=receiving_yards,
        receiving_yards_after_catch=receiving_yards_after_catch,
        receiving_yards_at_catch=receiving_yards_at_catch,
        receiving_yards_per_game=receiving_yards_per_game,
        receptions=receptions,
        two_point_rec_conversions=two_point_rec_conversions,
        two_point_reception=two_point_reception,
        two_point_reception_attempts=two_point_reception_attempts,
        yards_per_reception=yards_per_reception,
        assist_tackles=assist_tackles,
        average_interception_yards=average_interception_yards,
        average_sack_yards=average_sack_yards,
        average_stuff_yards=average_stuff_yards,
        blocked_field_goal_touchdowns=blocked_field_goal_touchdowns,
        blocked_punt_touchdowns=blocked_punt_touchdowns,
        defensive_touchdowns=defensive_touchdowns,
        hurries=hurries,
        kicks_blocked=kicks_blocked,
        long_interception=long_interception,
        misc_touchdowns=misc_touchdowns,
        passes_batted_down=passes_batted_down,
        passes_defended=passes_defended,
        qb_hits=qb_hits,
        two_point_returns=two_point_returns,
        sacks_assisted=sacks_assisted,
        sacks_unassisted=sacks_unassisted,
        sack_yards=sack_yards,
        safeties=safeties,
        solo_tackles=solo_tackles,
        stuff_yards=stuff_yards,
        tackles_for_loss=tackles_for_loss,
        tackles_yards_lost=tackles_yards_lost,
        yards_allowed=yards_allowed,
        points_allowed=points_allowed,
        one_point_safeties_made=one_point_safeties_made,
        missed_field_goal_return_td=missed_field_goal_return_td,
        blocked_punt_ez_rec_td=blocked_punt_ez_rec_td,
        interception_touchdowns=interception_touchdowns,
        interception_yards=interception_yards,
        average_kickoff_return_yards=average_kickoff_return_yards,
        average_kickoff_yards=average_kickoff_yards,
        extra_point_attempts=extra_point_attempts,
        extra_point_percentage=extra_point_percentage,
        extra_points_blocked=extra_points_blocked,
        extra_points_blocked_percentage=extra_points_blocked_percentage,
        extra_points_made=extra_points_made,
        fair_catches=fair_catches,
        fair_catch_percentage=fair_catch_percentage,
        field_goal_attempts=field_goal_attempts,
        field_goal_attempts_1_19=field_goal_attempts_1_19,
        field_goal_attempts_20_29=field_goal_attempts_20_29,
        field_goal_attempts_30_39=field_goal_attempts_30_39,
        field_goal_attempts_40_49=field_goal_attempts_40_49,
        field_goal_attempts_50_59=field_goal_attempts_50_59,
        field_goal_attempts_60_99=field_goal_attempts_60_99,
        field_goal_attempts_50=field_goal_attempts_50,
        field_goal_attempt_yards=field_goal_attempt_yards,
        field_goals_blocked=field_goals_blocked,
        field_goals_blocked_percentage=field_goals_blocked_percentage,
        field_goals_made_1_19=field_goals_made_1_19,
        field_goals_made_20_29=field_goals_made_20_29,
        field_goals_made_30_39=field_goals_made_30_39,
        field_goals_made_40_49=field_goals_made_40_49,
        field_goals_made_50_59=field_goals_made_50_59,
        field_goals_made_60_99=field_goals_made_60_99,
        field_goals_made_50=field_goals_made_50,
        field_goals_made_yards=field_goals_made_yards,
        field_goals_missed_yards=field_goals_missed_yards,
        kickoff_ob=kickoff_ob,
        kickoff_returns=kickoff_returns,
        kickoff_return_touchdowns=kickoff_return_touchdowns,
        kickoff_return_yards=kickoff_return_yards,
        kickoffs=kickoffs,
        kickoff_yards=kickoff_yards,
        long_field_goal_attempt=long_field_goal_attempt,
        long_field_goal_made=long_field_goal_made,
        long_kickoff=long_kickoff,
        total_kicking_points=total_kicking_points,
        touchback_percentage=touchback_percentage,
        touchbacks=touchbacks,
        def_fumble_returns=def_fumble_returns,
        def_fumble_return_yards=def_fumble_return_yards,
        fumble_recoveries=fumble_recoveries,
        fumble_recovery_yards=fumble_recovery_yards,
        kick_return_fair_catches=kick_return_fair_catches,
        kick_return_fair_catch_percentage=kick_return_fair_catch_percentage,
        kick_return_fumbles=kick_return_fumbles,
        kick_return_fumbles_lost=kick_return_fumbles_lost,
        kick_returns=kick_returns,
        kick_return_touchdowns=kick_return_touchdowns,
        kick_return_yards=kick_return_yards,
        long_kick_return=long_kick_return,
        long_punt_return=long_punt_return,
        misc_fumble_returns=misc_fumble_returns,
        misc_fumble_return_yards=misc_fumble_return_yards,
        opp_fumble_recoveries=opp_fumble_recoveries,
        opp_fumble_recovery_yards=opp_fumble_recovery_yards,
        opp_special_team_fumble_returns=opp_special_team_fumble_returns,
        opp_special_team_fumble_return_yards=opp_special_team_fumble_return_yards,
        punt_return_fair_catches=punt_return_fair_catches,
        punt_return_fair_catch_percentage=punt_return_fair_catch_percentage,
        punt_return_fumbles=punt_return_fumbles,
        punt_return_fumbles_lost=punt_return_fumbles_lost,
        punt_returns=punt_returns,
        punt_returns_started_inside_the_10=punt_returns_started_inside_the_10,
        punt_returns_started_inside_the_20=punt_returns_started_inside_the_20,
        punt_return_touchdowns=punt_return_touchdowns,
        punt_return_yards=punt_return_yards,
        special_team_fumble_returns=special_team_fumble_returns,
        special_team_fumble_return_yards=special_team_fumble_return_yards,
        yards_per_kick_return=yards_per_kick_return,
        yards_per_punt_return=yards_per_punt_return,
        yards_per_return=yards_per_return,
        average_punt_return_yards=average_punt_return_yards,
        gross_average_punt_yards=gross_average_punt_yards,
        long_punt=long_punt,
        net_average_punt_yards=net_average_punt_yards,
        punts=punts,
        punts_blocked=punts_blocked,
        punts_blocked_percentage=punts_blocked_percentage,
        punts_inside_10=punts_inside_10,
        punts_inside_10_percentage=punts_inside_10_percentage,
        punts_inside_20=punts_inside_20,
        punts_inside_20_percentage=punts_inside_20_percentage,
        punts_over_50=punts_over_50,
        punt_yards=punt_yards,
        defensive_points=defensive_points,
        kick_extra_points=kick_extra_points,
        kick_extra_points_made=kick_extra_points_made,
        misc_points=misc_points,
        return_touchdowns=return_touchdowns,
        total_two_point_conversions=total_two_point_conversions,
        first_downs=first_downs,
        first_downs_passing=first_downs_passing,
        first_downs_penalty=first_downs_penalty,
        first_downs_per_game=first_downs_per_game,
        first_downs_rushing=first_downs_rushing,
        fourth_down_attempts=fourth_down_attempts,
        fourth_down_conversion_percentage=fourth_down_conversion_percentage,
        fourth_down_conversions=fourth_down_conversions,
        possession_time_seconds=possession_time_seconds,
        redzone_attempt_points=redzone_attempt_points,
        redzone_attempts=redzone_attempts,
        redzone_conversions=redzone_conversions,
        redzone_efficiency_percentage=redzone_efficiency_percentage,
        redzone_end_downs=redzone_end_downs,
        redzone_end_game=redzone_end_game,
        redzone_end_half=redzone_end_half,
        redzone_field_goal_percentage=redzone_field_goal_percentage,
        redzone_field_goal_points=redzone_field_goal_points,
        redzone_field_goals=redzone_field_goals,
        redzone_field_goals_missed=redzone_field_goals_missed,
        redzone_fumble=redzone_fumble,
        redzone_interception=redzone_interception,
        redzone_scoring_percentage=redzone_scoring_percentage,
        redzone_total_points=redzone_total_points,
        redzone_touchdown_pass=redzone_touchdown_pass,
        redzone_touchdown_percentage=redzone_touchdown_percentage,
        redzone_touchdown_points=redzone_touchdown_points,
        redzone_touchdown_rush=redzone_touchdown_rush,
        redzone_touchdowns=redzone_touchdowns,
        third_down_attempts=third_down_attempts,
        third_down_conversion_percentage=third_down_conversion_percentage,
        third_down_conversions=third_down_conversions,
        timeouts_used=timeouts_used,
        total_penalties=total_penalties,
        total_penalty_yards=total_penalty_yards,
        total_plays=total_plays,
        total_drives=total_drives,
        turn_over_differential=turn_over_differential,
        goals_against=goals_against,
        shots_against=shots_against,
        penalty_kill_percentage=penalty_kill_percentage,
        power_play_goals_against=power_play_goals_against,
        short_handed_goals_against=short_handed_goals_against,
        shootout_saves=shootout_saves,
        shootout_shots_against=shootout_shots_against,
        times_short_handed=times_short_handed,
        empty_net_goals_against=empty_net_goals_against,
        takeaways=takeaways,
        even_strength_saves=even_strength_saves,
        power_play_saves=power_play_saves,
        short_handed_saves=short_handed_saves,
        time_on_ice=time_on_ice,
        power_play_time_on_ice=power_play_time_on_ice,
        short_handed_time_on_ice=short_handed_time_on_ice,
        even_strength_time_on_ice=even_strength_time_on_ice,
        shifts=shifts,
        shot_differential=shot_differential,
        goal_differential=goal_differential,
        pim_differential=pim_differential,
        rating=rating,
        ytd_goals=ytd_goals,
        shots_in_first_period=shots_in_first_period,
        shots_in_second_period=shots_in_second_period,
        shots_in_third_period=shots_in_third_period,
        shots_ot=shots_ot,
        shots_total=shots_total,
        shots_missed=shots_missed,
        points_per_game=points_per_game,
        power_play_goals=power_play_goals,
        power_play_assists=power_play_assists,
        power_play_opportunities=power_play_opportunities,
        power_play_percentage=power_play_percentage,
        short_handed_goals=short_handed_goals,
        short_handed_assists=short_handed_assists,
        shootout_attempts=shootout_attempts,
        shootout_shot_percentage=shootout_shot_percentage,
        empty_net_goals_for=empty_net_goals_for,
        shooting_percentage=shooting_percentage,
        total_face_offs=total_face_offs,
        faceoffs_won=faceoffs_won,
        faceoffs_lost=faceoffs_lost,
        faceoff_percentage=faceoff_percentage,
        unassisted_goals=unassisted_goals,
        giveaways=giveaways,
        penalty_minutes=penalty_minutes,
        total_giveaways=total_giveaways,
        total_takeaways=total_takeaways,
        fantasy_rating=fantasy_rating,
        second_chance_points=second_chance_points,
        plus_minus=plus_minus,
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
