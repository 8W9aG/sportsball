"""ESPN player model."""

# pylint: disable=duplicate-code,too-many-locals,too-many-branches,line-too-long,too-many-lines,too-many-statements
import datetime
import logging
from typing import Any

import pytest_is_running
import requests_cache
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

from ...cache import MEMORY
from ..combined.most_interesting import more_interesting
from ..google.address_exception import AddressException
from ..google.google_address_model import create_google_address_model
from ..player_model import VERSION, PlayerModel
from ..sex import Sex
from ..species import Species
from ..venue_model import VERSION as VENUE_VERSION
from .espn_venue_model import create_espn_venue_model

_BAD_URLS = {
    "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/athletes/4689686?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/athletes/2333612?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2021/athletes/4426888?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4896615?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2025/athletes/5226349?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4869785?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2025/athletes/4693647?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4433138?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4703879?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4702946?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4898186?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4897774?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/5241346?lang=en&region=us",
    "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4431764?lang=en&region=us",
}


def _create_espn_player_model(
    session: requests_cache.CachedSession,
    player: dict[str, Any],
    positions_validator: dict[str, str],
    dt: datetime.datetime,
    version: str,
) -> PlayerModel:
    identifier = None
    try:
        identifier = str(player["playerId"])
    except KeyError:
        identifier = str(player["id"])
    jersey = player.get("jersey")
    fumbles = None
    fumbles_lost = None
    forced_fumbles = None
    fumbles_recovered = None
    fumbles_recovered_yards = None
    fumbles_touchdowns = None
    offensive_two_point_returns = None
    offensive_fumbles_touchdowns = None
    defensive_fumbles_touchdowns = None
    average_gain = None
    completion_percentage = None
    completions = None
    espn_quarterback_rating = None
    interception_percentage = None
    interceptions = None
    long_passing = None
    misc_yards = None
    net_passing_yards = None
    net_total_yards = None
    passing_attempts = None
    passing_big_plays = None
    passing_first_downs = None
    passing_fumbles = None
    passing_fumbles_lost = None
    passing_touchdown_percentage = None
    passing_touchdowns = None
    passing_yards = None
    passing_yards_after_catch = None
    quarterback_rating = None
    sacks = None
    passing_yards_at_catch = None
    sacks_yards_lost = None
    net_passing_attempts = None
    total_offensive_plays = None
    total_points = None
    total_touchdowns = None
    total_yards = None
    total_yards_from_scrimmage = None
    two_point_pass = None
    two_point_pass_attempt = None
    yards_per_completion = None
    yards_per_pass_attempt = None
    net_yards_per_pass_attempt = None
    long_rushing = None
    rushing_attempts = None
    rushing_big_plays = None
    rushing_first_downs = None
    rushing_fumbles = None
    rushing_fumbles_lost = None
    rushing_touchdowns = None
    rushing_yards = None
    stuffs = None
    stuff_yards_lost = None
    two_point_rush = None
    two_point_rush_attempts = None
    yards_per_rush_attempt = None
    espn_widereceiver = None
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
    receptions = None
    two_point_receptions = None
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
    quarterback_hits = None
    sacks_assisted = None
    sacks_unassisted = None
    sacks_yards = None
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
    extra_point_blocked = None
    extra_points_blocked_percentage = None
    extra_points_made = None
    fair_catches = None
    fair_catch_percentage = None
    field_goal_attempts_max_19_yards = None
    field_goal_attempts_max_29_yards = None
    field_goal_attempts_max_39_yards = None
    field_goal_attempts_max_49_yards = None
    field_goal_attempts_max_59_yards = None
    field_goal_attempts_max_99_yards = None
    field_goal_attempts_above_50_yards = None
    field_goal_attempt_yards = None
    field_goals_blocked = None
    field_goals_blocked_percentage = None
    field_goals_made = None
    field_goals_made_max_19_yards = None
    field_goals_made_max_29_yards = None
    field_goals_made_max_39_yards = None
    field_goals_made_max_49_yards = None
    field_goals_made_max_59_yards = None
    field_goals_made_max_99_yards = None
    field_goals_made_above_50_yards = None
    field_goals_made_yards = None
    field_goals_missed_yards = None
    kickoff_out_of_bounds = None
    kickoff_returns = None
    kickoff_returns_touchdowns = None
    kickoff_return_yards = None
    kickoffs = None
    kickoff_yards = None
    long_field_goal_attempt = None
    long_field_goal_made = None
    long_kickoff = None
    total_kicking_points = None
    touchback_percentage = None
    touchbacks = None
    defensive_fumble_returns = None
    defensive_fumble_return_yards = None
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
    opposition_fumble_recoveries = None
    opposition_fumble_recovery_yards = None
    opposition_special_team_fumble_returns = None
    opposition_special_team_fumble_return_yards = None
    punt_return_fair_catches = None
    punt_return_fair_catch_percentage = None
    punt_return_fumbles = None
    punt_return_fumbles_lost = None
    punt_returns = None
    punt_returns_started_inside_the_10 = None
    punt_returns_started_inside_the_20 = None
    punt_return_touchdowns = None
    special_team_fumble_returns = None
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
    misc_points = None
    return_touchdowns = None
    total_two_point_conversions = None
    passing_touchdowns_9_yards = None
    passing_touchdowns_19_yards = None
    passing_touchdowns_29_yards = None
    passing_touchdowns_39_yards = None
    passing_touchdowns_49_yards = None
    passing_touchdowns_above_50_yards = None
    receiving_touchdowns_9_yards = None
    receiving_touchdowns_19_yards = None
    receiving_touchdowns_29_yards = None
    receiving_touchdowns_39_yards = None
    punt_return_yards = None
    receiving_touchdowns_49_yards = None
    receiving_touchdowns_above_50_yards = None
    rushing_touchdowns_9_yards = None
    rushing_touchdowns_19_yards = None
    rushing_touchdowns_29_yards = None
    rushing_touchdowns_39_yards = None
    rushing_touchdowns_49_yards = None
    rushing_touchdowns_above_50_yards = None
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
    rebounds = None
    goal_assists = None
    goal_accuracy = None
    score_involvements = None
    score = None
    shots_blocked = None
    effective_clearances = None
    effective_tackles = None
    ineffective_tackles = None
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
    clean_sheets = None
    crosses_caught = None
    goals_conceded = None
    partial_clean_sheet = None
    penalty_kick_conceded = None
    penalty_kick_save_percentage = None
    penalty_kicks_faced = None
    penalty_kicks_saved = None
    punches = None
    save_percentage = None
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
    headed_goals = None
    inaccurate_crosses = None
    inaccurate_long_balls = None
    inaccurate_passes = None
    inaccurate_through_balls = None
    left_footed_shots = None
    long_ball_percentage = None
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
    long_balls = None
    total_passes = None
    total_shots = None
    through_balls = None
    games_played = None
    team_games_played = None
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
    sac_flies = None
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
    runs_batted_in = None
    third_innings = None
    team_earned_runs = None
    shutouts = None
    pickoff_attempts = None
    run_support = None
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
    innings = None
    era = None
    whip = None
    caught_stealing_percentage = None
    pitches_per_start = None
    pitches_per_inning = None
    run_support_average = None
    opponent_average = None
    opponent_slug_average = None
    opponent_on_base_percentage = None
    opponent_ops = None
    strikeouts_per_nine_innings = None
    strikeout_to_walk_ratio = None
    tough_losses = None
    cheap_wins = None
    save_opportunities_per_win = None
    pitch_count = None
    strike_pitch_ratio = None
    double_plays = None
    opportunities = None
    errors = None
    passed_balls = None
    assists = None
    outfield_assists = None
    pickoffs = None
    putouts = None
    outs_on_field = None
    triple_plays = None
    balls_in_zone = None
    extra_bases = None
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
    blocks = None
    defensive_rebounds = None
    steals = None
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
    average_minutes = None
    nba_rating = None
    plus_minus = None
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
    r40 = None
    double_double = None
    triple_double = None
    field_goals = None
    field_goals_attempted = None
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
    total_turnovers = None
    points_in_paint = None
    brick_index = None
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
    p40 = None
    a40 = None
    goals_against = None
    average_goals_against = None
    shots_against = None
    average_shots_against = None
    penalty_kill_percentage = None
    power_play_goals_against = None
    short_handed_goals_against = None
    shootout_saves = None
    shootout_shots_against = None
    times_short_handed = None
    empty_net_goals_against = None
    overtime_losses = None
    takeaways = None
    even_strength_saves = None
    power_play_saves = None
    short_handed_saves = None
    games = None
    game_started = None
    ties = None
    time_on_ice = None
    time_on_ice_per_game = None
    power_play_time_on_ice = None
    short_handed_time_on_ice = None
    even_strength_time_on_ice = None
    shifts = None
    shifts_per_game = None
    production = None
    shot_differential = None
    goal_differential = None
    pim_differential = None
    rating = None
    average_goals = None
    ytd_goals = None
    shots_in_first_period = None
    shots_in_second_period = None
    shots_in_third_period = None
    shots_overtime = None
    shots_missed = None
    average_shots = None
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
    shutouts_against = None
    shooting_percentage = None
    total_face_offs = None
    faceoffs_won = None
    faceoffs_lost = None
    faceoff_percentage = None
    unassisted_goals = None
    game_tying_goals = None
    giveaways = None
    penalties = None
    penalty_minutes = None
    penalty_minutes_against = None
    major_penalties = None
    minor_penalties = None
    match_penalties = None
    misconducts = None
    game_misconducts = None
    boarding_penalties = None
    unsportsmanlike_penalties = None
    fighting_penalties = None
    average_fights = None
    time_between_fights = None
    instigator_penalties = None
    charging_penalties = None
    hooking_penalties = None
    tripping_penalties = None
    roughing_penalties = None
    holding_penalties = None
    interference_penalties = None
    slashing_penalties = None
    high_sticking_penalties = None
    cross_checking_penalties = None
    stick_holding_penalties = None
    goalie_interference_penalties = None
    elbowing_penalties = None
    diving_penalties = None
    net_passing_yards_per_game = None
    net_yards_per_game = None
    passing_yards_per_game = None
    total_points_per_game = None
    yards_from_scrimmage_per_game = None
    yards_per_game = None
    quarterback_rating = None
    espn_rb_rating = None
    rushing_yards_per_game = None
    receiving_yards_per_game = None
    two_point_returns = None
    field_goal_attempts = None
    special_team_fumble_return_yards = None
    kick_extra_point = None
    kick_extra_points_made = None
    attempts_in_box = None
    second_assists = None
    qbr = None
    attempts_out_box = None
    adjusted_qbr = None
    turnover_points = None
    fantasy_rating = None
    team_turnovers = None
    second_chance_points = None
    fast_break_points = None
    team_rebounds = None
    strikes = None
    if "statistics" in player:
        stats_url = player["statistics"]["$ref"]
        statistics_response = session.get(stats_url)
        if statistics_response.ok:
            try:
                statistics_dict = statistics_response.json()
                fumbles = None
                for category in statistics_dict["splits"]["categories"]:
                    for stat in category["stats"]:
                        if stat["name"] == "fumbles":
                            fumbles = more_interesting(fumbles, stat["value"])
                        elif stat["name"] == "fumblesLost":
                            fumbles_lost = more_interesting(fumbles_lost, stat["value"])
                        elif stat["name"] == "fumblesForced":
                            forced_fumbles = more_interesting(
                                forced_fumbles, stat["value"]
                            )
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
                            espn_quarterback_rating = more_interesting(
                                espn_quarterback_rating, stat["value"]
                            )
                        elif stat["name"] == "interceptionPct":
                            interception_percentage = more_interesting(
                                interception_percentage, stat["value"]
                            )
                        elif stat["name"] == "interceptions":
                            interceptions = more_interesting(
                                interceptions, stat["value"]
                            )
                        elif stat["name"] == "longPassing":
                            long_passing = more_interesting(long_passing, stat["value"])
                        elif stat["name"] == "miscYards":
                            misc_yards = more_interesting(misc_yards, stat["value"])
                        elif stat["name"] == "netPassingYards":
                            net_passing_yards = more_interesting(
                                net_passing_yards, stat["value"]
                            )
                        elif stat["name"] == "netTotalYards":
                            net_total_yards = more_interesting(
                                net_total_yards, stat["value"]
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
                            passing_yards = more_interesting(
                                passing_yards, stat["value"]
                            )
                        elif stat["name"] == "passingYardsAfterCatch":
                            passing_yards_after_catch = more_interesting(
                                passing_yards_after_catch, stat["value"]
                            )
                        elif stat["name"] == "QBRating":
                            quarterback_rating = more_interesting(
                                quarterback_rating, stat["value"]
                            )
                        elif stat["name"] == "sacks":
                            sacks = more_interesting(sacks, stat["value"])
                        elif stat["name"] == "passingYardsAtCatch":
                            passing_yards_at_catch = more_interesting(
                                passing_yards_at_catch, stat["value"]
                            )
                        elif stat["name"] == "sackYardsLost":
                            sacks_yards_lost = more_interesting(
                                sacks_yards_lost, stat["value"]
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
                        elif stat["name"] == "twoPtPass":
                            two_point_pass = more_interesting(
                                two_point_pass, stat["value"]
                            )
                        elif stat["name"] == "twoPtPassAttempts":
                            two_point_pass_attempt = more_interesting(
                                two_point_pass_attempt, stat["value"]
                            )
                        elif stat["name"] == "yardsPerCompletion":
                            yards_per_completion = more_interesting(
                                yards_per_completion, stat["value"]
                            )
                        elif stat["name"] == "yardsPerPassAttempt":
                            yards_per_pass_attempt = more_interesting(
                                yards_per_pass_attempt, stat["value"]
                            )
                        elif stat["name"] == "netYardsPerPassAttempt":
                            net_yards_per_pass_attempt = more_interesting(
                                net_yards_per_pass_attempt, stat["value"]
                            )
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
                            rushing_yards = more_interesting(
                                rushing_yards, stat["value"]
                            )
                        elif stat["name"] == "stuffs":
                            stuffs = more_interesting(stuffs, stat["value"])
                        elif stat["name"] == "stuffYardsLost":
                            stuff_yards_lost = more_interesting(
                                stuff_yards_lost, stat["value"]
                            )
                        elif stat["name"] == "twoPtRush":
                            two_point_rush = more_interesting(
                                two_point_rush, stat["value"]
                            )
                        elif stat["name"] == "twoPtRushAttempts":
                            two_point_rush_attempts = more_interesting(
                                two_point_rush_attempts, stat["value"]
                            )
                        elif stat["name"] == "yardsPerRushAttempt":
                            yards_per_rush_attempt = more_interesting(
                                yards_per_rush_attempt, stat["value"]
                            )
                        elif stat["name"] == "ESPNWRRating":
                            espn_widereceiver = more_interesting(
                                espn_widereceiver, stat["value"]
                            )
                        elif stat["name"] == "longReception":
                            long_reception = more_interesting(
                                long_reception, stat["value"]
                            )
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
                        elif stat["name"] == "receptions":
                            receptions = more_interesting(receptions, stat["value"])
                        elif stat["name"] == "twoPtReception":
                            two_point_receptions = more_interesting(
                                two_point_receptions, stat["value"]
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
                            assist_tackles = more_interesting(
                                assist_tackles, stat["value"]
                            )
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
                            kicks_blocked = more_interesting(
                                kicks_blocked, stat["value"]
                            )
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
                            quarterback_hits = more_interesting(
                                quarterback_hits, stat["value"]
                            )
                        elif stat["name"] == "sacksAssisted":
                            sacks_assisted = more_interesting(
                                sacks_assisted, stat["value"]
                            )
                        elif stat["name"] == "sacksUnassisted":
                            sacks_unassisted = more_interesting(
                                sacks_unassisted, stat["value"]
                            )
                        elif stat["name"] == "sackYards":
                            sacks_yards = more_interesting(sacks_yards, stat["value"])
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
                            yards_allowed = more_interesting(
                                yards_allowed, stat["value"]
                            )
                        elif stat["name"] == "pointsAllowed":
                            points_allowed = more_interesting(
                                points_allowed, stat["value"]
                            )
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
                            extra_point_blocked = more_interesting(
                                extra_point_blocked, stat["value"]
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
                        elif stat["name"] == "fieldGoalAttempts1_19":
                            field_goal_attempts_max_19_yards = more_interesting(
                                field_goal_attempts_max_19_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts20_29":
                            field_goal_attempts_max_29_yards = more_interesting(
                                field_goal_attempts_max_29_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts30_39":
                            field_goal_attempts_max_39_yards = more_interesting(
                                field_goal_attempts_max_39_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts40_49":
                            field_goal_attempts_max_49_yards = more_interesting(
                                field_goal_attempts_max_49_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts50_59":
                            field_goal_attempts_max_59_yards = more_interesting(
                                field_goal_attempts_max_59_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts60_99":
                            field_goal_attempts_max_99_yards = more_interesting(
                                field_goal_attempts_max_99_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts50":
                            field_goal_attempts_above_50_yards = more_interesting(
                                field_goal_attempts_above_50_yards, stat["value"]
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
                        elif stat["name"] == "fieldGoalsMade":
                            field_goals_made = more_interesting(
                                field_goals_made, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade1_19":
                            field_goals_made_max_19_yards = more_interesting(
                                field_goals_made_max_19_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade20_29":
                            field_goals_made_max_29_yards = more_interesting(
                                field_goals_made_max_29_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade30_39":
                            field_goals_made_max_39_yards = more_interesting(
                                field_goals_made_max_39_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade40_49":
                            field_goals_made_max_49_yards = more_interesting(
                                field_goals_made_max_49_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade50_59":
                            field_goals_made_max_59_yards = more_interesting(
                                field_goals_made_max_59_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade60_99":
                            field_goals_made_max_99_yards = more_interesting(
                                field_goals_made_max_99_yards, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalsMade50":
                            field_goals_made_above_50_yards = more_interesting(
                                field_goals_made_above_50_yards, stat["value"]
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
                            kickoff_out_of_bounds = more_interesting(
                                kickoff_out_of_bounds, stat["value"]
                            )
                        elif stat["name"] == "kickoffReturns":
                            kickoff_returns = more_interesting(
                                kickoff_returns, stat["value"]
                            )
                        elif stat["name"] == "kickoffReturnTouchdowns":
                            kickoff_returns_touchdowns = more_interesting(
                                kickoff_returns_touchdowns, stat["value"]
                            )
                        elif stat["name"] == "kickoffReturnYards":
                            kickoff_return_yards = more_interesting(
                                kickoff_return_yards, stat["value"]
                            )
                        elif stat["name"] == "kickoffs":
                            kickoffs = more_interesting(kickoffs, stat["value"])
                        elif stat["name"] == "kickoffYards":
                            kickoff_yards = more_interesting(
                                kickoff_yards, stat["value"]
                            )
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
                            defensive_fumble_returns = more_interesting(
                                defensive_fumble_returns, stat["value"]
                            )
                        elif stat["name"] == "defFumbleReturnYards":
                            defensive_fumble_return_yards = more_interesting(
                                defensive_fumble_return_yards, stat["value"]
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
                            opposition_fumble_recoveries = more_interesting(
                                opposition_fumble_recoveries, stat["value"]
                            )
                        elif stat["name"] == "oppFumbleRecoveryYards":
                            opposition_fumble_recovery_yards = more_interesting(
                                opposition_fumble_recovery_yards, stat["value"]
                            )
                        elif stat["name"] == "oppSpecialTeamFumbleReturns":
                            opposition_special_team_fumble_returns = more_interesting(
                                opposition_special_team_fumble_returns, stat["value"]
                            )
                        elif stat["name"] == "oppSpecialTeamFumbleReturnYards":
                            opposition_special_team_fumble_return_yards = (
                                more_interesting(
                                    opposition_special_team_fumble_return_yards,
                                    stat["value"],
                                )
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
                        elif stat["name"] == "specialTeamFumbleReturns":
                            special_team_fumble_returns = more_interesting(
                                special_team_fumble_returns, stat["value"]
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
                            punts_blocked = more_interesting(
                                punts_blocked, stat["value"]
                            )
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
                            punts_over_50 = more_interesting(
                                punts_over_50, stat["value"]
                            )
                        elif stat["name"] == "puntYards":
                            punt_yards = more_interesting(punt_yards, stat["value"])
                        elif stat["name"] == "defensivePoints":
                            defensive_points = more_interesting(
                                defensive_points, stat["value"]
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
                        elif stat["name"] == "passingTouchdownsOf0to9Yds":
                            passing_touchdowns_9_yards = more_interesting(
                                passing_touchdowns_9_yards, stat["value"]
                            )
                        elif stat["name"] == "passingTouchdownsOf10to19Yds":
                            passing_touchdowns_19_yards = more_interesting(
                                passing_touchdowns_19_yards, stat["value"]
                            )
                        elif stat["name"] == "passingTouchdownsOf20to29Yds":
                            passing_touchdowns_29_yards = more_interesting(
                                passing_touchdowns_29_yards, stat["value"]
                            )
                        elif stat["name"] == "passingTouchdownsOf30to39Yds":
                            passing_touchdowns_39_yards = more_interesting(
                                passing_touchdowns_39_yards, stat["value"]
                            )
                        elif stat["name"] == "passingTouchdownsOf40to49Yds":
                            passing_touchdowns_49_yards = more_interesting(
                                passing_touchdowns_49_yards, stat["value"]
                            )
                        elif stat["name"] == "passingTouchdownsOf50PlusYds":
                            passing_touchdowns_above_50_yards = more_interesting(
                                passing_touchdowns_above_50_yards, stat["value"]
                            )
                        elif stat["name"] == "receivingTouchdownsOf0to9Yds":
                            receiving_touchdowns_9_yards = more_interesting(
                                receiving_touchdowns_9_yards, stat["value"]
                            )
                        elif stat["name"] == "receivingTouchdownsOf10to19Yds":
                            receiving_touchdowns_19_yards = more_interesting(
                                receiving_touchdowns_19_yards, stat["value"]
                            )
                        elif stat["name"] == "receivingTouchdownsOf20to29Yds":
                            receiving_touchdowns_29_yards = more_interesting(
                                receiving_touchdowns_29_yards, stat["value"]
                            )
                        elif stat["name"] == "receivingTouchdownsOf30to39Yds":
                            receiving_touchdowns_39_yards = more_interesting(
                                receiving_touchdowns_39_yards, stat["value"]
                            )
                        elif stat["name"] == "puntReturnYards":
                            punt_return_yards = more_interesting(
                                punt_return_yards, stat["value"]
                            )
                        elif stat["name"] == "receivingTouchdownsOf40to49Yds":
                            receiving_touchdowns_49_yards = more_interesting(
                                receiving_touchdowns_49_yards, stat["value"]
                            )
                        elif stat["name"] == "receivingTouchdownsOf50PlusYds":
                            receiving_touchdowns_above_50_yards = more_interesting(
                                receiving_touchdowns_above_50_yards, stat["value"]
                            )
                        elif stat["name"] == "rushingTouchdownsOf0to9Yds":
                            rushing_touchdowns_9_yards = more_interesting(
                                rushing_touchdowns_9_yards, stat["value"]
                            )
                        elif stat["name"] == "rushingTouchdownsOf10to19Yds":
                            rushing_touchdowns_19_yards = more_interesting(
                                rushing_touchdowns_19_yards, stat["value"]
                            )
                        elif stat["name"] == "rushingTouchdownsOf20to29Yds":
                            rushing_touchdowns_29_yards = more_interesting(
                                rushing_touchdowns_29_yards, stat["value"]
                            )
                        elif stat["name"] == "rushingTouchdownsOf30to39Yds":
                            rushing_touchdowns_39_yards = more_interesting(
                                rushing_touchdowns_39_yards, stat["value"]
                            )
                        elif stat["name"] == "rushingTouchdownsOf40to49Yds":
                            rushing_touchdowns_49_yards = more_interesting(
                                rushing_touchdowns_49_yards, stat["value"]
                            )
                        elif stat["name"] == "rushingTouchdownsOf50PlusYds":
                            rushing_touchdowns_above_50_yards = more_interesting(
                                rushing_touchdowns_above_50_yards, stat["value"]
                            )
                        elif stat["name"] == "kicks":
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
                            one_percenters = more_interesting(
                                one_percenters, stat["value"]
                            )
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
                            frees_against = more_interesting(
                                frees_against, stat["value"]
                            )
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
                            goal_accuracy = more_interesting(
                                goal_accuracy, stat["value"]
                            )
                        elif stat["name"] == "scoreInvolvements":
                            score_involvements = more_interesting(
                                score_involvements, stat["value"]
                            )
                        elif stat["name"] == "score":
                            score = more_interesting(score, stat["value"])
                        elif stat["name"] == "blockedShots":
                            shots_blocked = more_interesting(
                                shots_blocked, stat["value"]
                            )
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
                        elif stat["name"] == "tacklePct":
                            tackle_percentage = more_interesting(
                                tackle_percentage, stat["value"]
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
                            fouls_suffered = more_interesting(
                                fouls_suffered, stat["value"]
                            )
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
                            win_percentage = more_interesting(
                                win_percentage, stat["value"]
                            )
                        elif stat["name"] == "wins":
                            wins = more_interesting(wins, stat["value"])
                        elif stat["name"] == "wonCorners":
                            won_corners = more_interesting(won_corners, stat["value"])
                        elif stat["name"] == "yellowCards":
                            yellow_cards = more_interesting(yellow_cards, stat["value"])
                        elif stat["name"] == "cleanSheet":
                            clean_sheets = more_interesting(clean_sheets, stat["value"])
                        elif stat["name"] == "crossesCaught":
                            crosses_caught = more_interesting(
                                crosses_caught, stat["value"]
                            )
                        elif stat["name"] == "goalsConceded":
                            goals_conceded = more_interesting(
                                goals_conceded, stat["value"]
                            )
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
                        elif stat["name"] == "savePct":
                            save_percentage = more_interesting(
                                save_percentage, stat["value"]
                            )
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
                            long_ball_percentage = more_interesting(
                                long_ball_percentage, stat["value"]
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
                            shots_on_post = more_interesting(
                                shots_on_post, stat["value"]
                            )
                        elif stat["name"] == "shotsOnTarget":
                            shots_on_target = more_interesting(
                                shots_on_target, stat["value"]
                            )
                        elif stat["name"] == "throughBallPct":
                            through_ball_percentage = more_interesting(
                                through_ball_percentage, stat["value"]
                            )
                        elif stat["name"] == "totalCrosses":
                            total_crosses = more_interesting(
                                total_crosses, stat["value"]
                            )
                        elif stat["name"] == "totalGoals":
                            goals = more_interesting(goals, stat["value"])
                        elif stat["name"] == "totalLongBalls":
                            long_balls = more_interesting(long_balls, stat["value"])
                        elif stat["name"] == "totalPasses":
                            total_passes = more_interesting(total_passes, stat["value"])
                        elif stat["name"] == "totalShots":
                            total_shots = more_interesting(total_shots, stat["value"])
                        elif stat["name"] == "totalThroughBalls":
                            through_balls = more_interesting(
                                through_balls, stat["value"]
                            )
                        elif stat["name"] == "gamesPlayed":
                            games_played = more_interesting(games_played, stat["value"])
                        elif stat["name"] == "teamGamesPlayed":
                            team_games_played = more_interesting(
                                team_games_played, stat["value"]
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
                            sac_flies = more_interesting(sac_flies, stat["value"])
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
                            caught_stealing = more_interesting(
                                caught_stealing, stat["value"]
                            )
                        elif stat["name"] == "pitches":
                            pitches = more_interesting(pitches, stat["value"])
                        elif stat["name"] == "gamesStarted":
                            games_started = more_interesting(
                                games_started, stat["value"]
                            )
                        elif stat["name"] == "pinchAtBats":
                            pinch_at_bats = more_interesting(
                                pinch_at_bats, stat["value"]
                            )
                        elif stat["name"] == "pinchHits":
                            pinch_hits = more_interesting(pinch_hits, stat["value"])
                        elif stat["name"] == "playerRating":
                            player_rating = more_interesting(
                                player_rating, stat["value"]
                            )
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
                            pinch_average = more_interesting(
                                pinch_average, stat["value"]
                            )
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
                            batter_rating = more_interesting(
                                batter_rating, stat["value"]
                            )
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
                            isolated_power = more_interesting(
                                isolated_power, stat["value"]
                            )
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
                            runs_produced = more_interesting(
                                runs_produced, stat["value"]
                            )
                        elif stat["name"] == "runsRatio":
                            runs_ratio = more_interesting(runs_ratio, stat["value"])
                        elif stat["name"] == "patienceRatio":
                            patience_ratio = more_interesting(
                                patience_ratio, stat["value"]
                            )
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
                            balks = more_interesting(balks, stat["value"])
                        elif stat["name"] == "battersFaced":
                            batters_faced = more_interesting(
                                batters_faced, stat["value"]
                            )
                        elif stat["name"] == "holds":
                            holds = more_interesting(holds, stat["value"])
                        elif stat["name"] == "completeGames":
                            complete_games = more_interesting(
                                complete_games, stat["value"]
                            )
                        elif stat["name"] == "perfectGames":
                            perfect_games = more_interesting(
                                perfect_games, stat["value"]
                            )
                        elif stat["name"] == "wildPitches":
                            wild_pitches = more_interesting(wild_pitches, stat["value"])
                        elif stat["name"] == "RBIs":
                            runs_batted_in = more_interesting(
                                runs_batted_in, stat["value"]
                            )
                        elif stat["name"] == "thirdInnings":
                            third_innings = more_interesting(
                                third_innings, stat["value"]
                            )
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
                        elif stat["name"] == "runSupport":
                            run_support = more_interesting(run_support, stat["value"])
                        elif stat["name"] == "pitchesAsStarter":
                            pitches_as_starter = more_interesting(
                                pitches_as_starter, stat["value"]
                            )
                        elif stat["name"] == "avgGameScore":
                            average_game_score = more_interesting(
                                average_game_score, stat["value"]
                            )
                        elif stat["name"] == "qualityStarts":
                            quality_starts = more_interesting(
                                quality_starts, stat["value"]
                            )
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
                        elif stat["name"] == "strikePitchRatio":
                            strike_pitch_ratio = more_interesting(
                                strike_pitch_ratio, stat["value"]
                            )
                        elif stat["name"] == "doublePlays":
                            double_plays = more_interesting(double_plays, stat["value"])
                        elif stat["name"] == "opportunities":
                            opportunities = more_interesting(
                                opportunities, stat["value"]
                            )
                        elif stat["name"] == "errors":
                            errors = more_interesting(errors, stat["value"])
                        elif stat["name"] == "passedBalls":
                            passed_balls = more_interesting(passed_balls, stat["value"])
                        elif stat["name"] == "assists":
                            assists = more_interesting(assists, stat["value"])
                        elif stat["name"] == "outfieldAssists":
                            outfield_assists = more_interesting(
                                outfield_assists, stat["value"]
                            )
                        elif stat["name"] == "pickoffs":
                            pickoffs = more_interesting(pickoffs, stat["value"])
                        elif stat["name"] == "putouts":
                            putouts = more_interesting(putouts, stat["value"])
                        elif stat["name"] == "outsOnField":
                            outs_on_field = more_interesting(
                                outs_on_field, stat["value"]
                            )
                        elif stat["name"] == "triplePlays":
                            triple_plays = more_interesting(triple_plays, stat["value"])
                        elif stat["name"] == "ballsInZone":
                            balls_in_zone = more_interesting(
                                balls_in_zone, stat["value"]
                            )
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
                            total_chances = more_interesting(
                                total_chances, stat["value"]
                            )
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
                        elif stat["name"] == "avgDefensiveRebounds":
                            average_defensive_rebounds = more_interesting(
                                average_defensive_rebounds, stat["value"]
                            )
                        elif stat["name"] == "avgBlocks":
                            average_blocks = more_interesting(
                                average_blocks, stat["value"]
                            )
                        elif stat["name"] == "avgSteals":
                            average_steals = more_interesting(
                                average_steals, stat["value"]
                            )
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
                            flagrant_fouls = more_interesting(
                                flagrant_fouls, stat["value"]
                            )
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
                        elif stat["name"] == "avgMinutes":
                            average_minutes = more_interesting(
                                average_minutes, stat["value"]
                            )
                        elif stat["name"] == "NBARating":
                            nba_rating = more_interesting(nba_rating, stat["value"])
                        elif stat["name"] == "plusMinus":
                            plus_minus = more_interesting(plus_minus, stat["value"])
                        elif stat["name"] == "avgRebounds":
                            average_rebounds = more_interesting(
                                average_rebounds, stat["value"]
                            )
                        elif stat["name"] == "avgFouls":
                            average_fouls = more_interesting(
                                average_fouls, stat["value"]
                            )
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
                            total_rebounds = more_interesting(
                                total_rebounds, stat["value"]
                            )
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
                        elif stat["name"] == "r40":
                            r40 = more_interesting(r40, stat["value"])
                        elif stat["name"] == "doubleDouble":
                            double_double = more_interesting(
                                double_double, stat["value"]
                            )
                        elif stat["name"] == "tripleDouble":
                            triple_double = more_interesting(
                                triple_double, stat["value"]
                            )
                        elif stat["name"] == "fieldGoals":
                            field_goals = more_interesting(field_goals, stat["value"])
                        elif stat["name"] == "fieldGoalsAttempted":
                            field_goals_attempted = more_interesting(
                                field_goals_attempted, stat["value"]
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
                        elif stat["name"] == "points":
                            score = more_interesting(score, stat["value"])
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
                            average_three_point_field_goals_attempted = (
                                more_interesting(
                                    average_three_point_field_goals_attempted,
                                    stat["value"],
                                )
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
                            average_points = more_interesting(
                                average_points, stat["value"]
                            )
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
                            average_48_three_point_field_goals_attempted = (
                                more_interesting(
                                    average_48_three_point_field_goals_attempted,
                                    stat["value"],
                                )
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
                        elif stat["name"] == "p40":
                            p40 = more_interesting(p40, stat["value"])
                        elif stat["name"] == "a40":
                            a40 = more_interesting(a40, stat["value"])
                        elif stat["name"] == "goalsAgainst":
                            goals_against = more_interesting(
                                goals_against, stat["value"]
                            )
                        elif stat["name"] == "avgGoalsAgainst":
                            average_goals_against = more_interesting(
                                average_goals_against, stat["value"]
                            )
                        elif stat["name"] == "shotsAgainst":
                            shots_against = more_interesting(
                                shots_against, stat["value"]
                            )
                        elif stat["name"] == "avgShotsAgainst":
                            average_shots_against = more_interesting(
                                average_shots_against, stat["value"]
                            )
                        elif stat["name"] == "penaltyKillPct":
                            penalty_kill_percentage = more_interesting(
                                penalty_kill_percentage,
                                stat.get("value", float(stat["displayValue"])),
                            )
                        elif stat["name"] == "powerPlayGoalsAgainst":
                            power_play_goals_against = more_interesting(
                                power_play_goals_against,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "shortHandedGoalsAgainst":
                            short_handed_goals_against = more_interesting(
                                short_handed_goals_against,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "shootoutSaves":
                            shootout_saves = more_interesting(
                                shootout_saves, stat["value"]
                            )
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
                                times_short_handed,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "emptyNetGoalsAgainst":
                            empty_net_goals_against = more_interesting(
                                empty_net_goals_against,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "overtimeLosses":
                            overtime_losses = more_interesting(
                                overtime_losses, stat["value"]
                            )
                        elif stat["name"] == "takeaways":
                            takeaways = more_interesting(takeaways, stat["value"])
                        elif stat["name"] == "evenStrengthSaves":
                            even_strength_saves = more_interesting(
                                even_strength_saves, stat["value"]
                            )
                        elif stat["name"] == "powerPlaySaves":
                            power_play_saves = more_interesting(
                                power_play_saves, stat["value"]
                            )
                        elif stat["name"] == "shortHandedSaves":
                            short_handed_saves = more_interesting(
                                short_handed_saves, stat["value"]
                            )
                        elif stat["name"] == "games":
                            games = more_interesting(games, stat["value"])
                        elif stat["name"] == "gameStarted":
                            game_started = more_interesting(game_started, stat["value"])
                        elif stat["name"] == "ties":
                            ties = more_interesting(ties, stat["value"])
                        elif stat["name"] == "timeOnIce":
                            time_on_ice = more_interesting(time_on_ice, stat["value"])
                        elif stat["name"] == "timeOnIcePerGame":
                            time_on_ice_per_game = more_interesting(
                                time_on_ice_per_game, stat["value"]
                            )
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
                        elif stat["name"] == "shiftsPerGame":
                            shifts_per_game = more_interesting(
                                shifts_per_game, stat["value"]
                            )
                        elif stat["name"] == "production":
                            production = more_interesting(production, stat["value"])
                        elif stat["name"] == "shotDifferential":
                            shot_differential = more_interesting(
                                shot_differential,
                                stat.get("value", float(stat["displayValue"])),
                            )
                        elif stat["name"] == "goalDifferential":
                            goal_differential = more_interesting(
                                goal_differential,
                                stat.get("value", float(stat["displayValue"])),
                            )
                        elif stat["name"] == "PIMDifferential":
                            pim_differential = more_interesting(
                                pim_differential,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "rating":
                            rating = more_interesting(rating, stat["value"])
                        elif stat["name"] == "avgGoals":
                            average_goals = more_interesting(
                                average_goals, stat["value"]
                            )
                        elif stat["name"] == "ytdGoals":
                            ytd_goals = more_interesting(ytd_goals, stat["value"])
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
                            shots_overtime = more_interesting(
                                shots_overtime,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "shotsTotal":
                            total_shots = more_interesting(total_shots, stat["value"])
                        elif stat["name"] == "shotsMissed":
                            shots_missed = more_interesting(shots_missed, stat["value"])
                        elif stat["name"] == "avgShots":
                            average_shots = more_interesting(
                                average_shots, stat["value"]
                            )
                        elif stat["name"] == "pointsPerGame":
                            points_per_game = more_interesting(
                                points_per_game, stat["value"]
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
                                power_play_opportunities,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "powerPlayPct":
                            power_play_percentage = more_interesting(
                                power_play_percentage,
                                stat.get("value", float(stat["displayValue"])),
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
                                empty_net_goals_for,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "shutoutsAgainst":
                            shutouts_against = more_interesting(
                                shutouts_against,
                                stat.get("value", int(stat["displayValue"])),
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
                            faceoffs_lost = more_interesting(
                                faceoffs_lost, stat["value"]
                            )
                        elif stat["name"] == "faceoffPercent":
                            faceoff_percentage = more_interesting(
                                faceoff_percentage, stat["value"]
                            )
                        elif stat["name"] == "unassistedGoals":
                            unassisted_goals = more_interesting(
                                unassisted_goals, stat["value"]
                            )
                        elif stat["name"] == "gameTyingGoals":
                            game_tying_goals = more_interesting(
                                game_tying_goals, stat["value"]
                            )
                        elif stat["name"] == "giveaways":
                            giveaways = more_interesting(giveaways, stat["value"])
                        elif stat["name"] == "penalties":
                            penalties = more_interesting(penalties, stat["value"])
                        elif stat["name"] == "penaltyMinutes":
                            penalty_minutes = more_interesting(
                                penalty_minutes, stat["value"]
                            )
                        elif stat["name"] == "penaltyMinutesAgainst":
                            penalty_minutes_against = more_interesting(
                                penalty_minutes_against,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "majorPenalties":
                            major_penalties = more_interesting(
                                major_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "minorPenalties":
                            minor_penalties = more_interesting(
                                minor_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "matchPenalties":
                            match_penalties = more_interesting(
                                match_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "misconducts":
                            misconducts = more_interesting(
                                misconducts,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "gameMisconducts":
                            game_misconducts = more_interesting(
                                game_misconducts,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "boardingPenalties":
                            boarding_penalties = more_interesting(
                                boarding_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "unsportsmanlikePenalties":
                            unsportsmanlike_penalties = more_interesting(
                                unsportsmanlike_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "fightingPenalties":
                            fighting_penalties = more_interesting(
                                fighting_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "avgFights":
                            average_fights = more_interesting(
                                average_fights,
                                stat.get("value", float(stat["displayValue"])),
                            )
                        elif stat["name"] == "timeBetweenFights":
                            if "value" in stat:
                                time_between_fights = more_interesting(
                                    time_between_fights, stat["value"]
                                )
                            else:
                                minutes, seconds = stat["displayValue"].split(":")
                                time_between_fights = more_interesting(
                                    time_between_fights,
                                    (float(minutes) * 60.0) + float(seconds),
                                )
                        elif stat["name"] == "instigatorPenalties":
                            instigator_penalties = more_interesting(
                                instigator_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "chargingPenalties":
                            charging_penalties = more_interesting(
                                charging_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "hookingPenalties":
                            hooking_penalties = more_interesting(
                                hooking_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "trippingPenalties":
                            tripping_penalties = more_interesting(
                                tripping_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "roughingPenalties":
                            roughing_penalties = more_interesting(
                                roughing_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "holdingPenalties":
                            holding_penalties = more_interesting(
                                holding_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "interferencePenalties":
                            interference_penalties = more_interesting(
                                interference_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "slashingPenalties":
                            slashing_penalties = more_interesting(
                                slashing_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "highStickingPenalties":
                            high_sticking_penalties = more_interesting(
                                high_sticking_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "crossCheckingPenalties":
                            cross_checking_penalties = more_interesting(
                                cross_checking_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "stickHoldingPenalties":
                            stick_holding_penalties = more_interesting(
                                stick_holding_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "goalieInterferencePenalties":
                            goalie_interference_penalties = more_interesting(
                                goalie_interference_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "elbowingPenalties":
                            elbowing_penalties = more_interesting(
                                elbowing_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "divingPenalties":
                            diving_penalties = more_interesting(
                                diving_penalties,
                                stat.get("value", int(stat["displayValue"])),
                            )
                        elif stat["name"] == "netPassingYardsPerGame":
                            net_passing_yards_per_game = more_interesting(
                                net_passing_yards_per_game, stat["value"]
                            )
                        elif stat["name"] == "netYardsPerGame":
                            net_yards_per_game = more_interesting(
                                net_yards_per_game, stat["value"]
                            )
                        elif stat["name"] == "passingYardsPerGame":
                            passing_yards_per_game = more_interesting(
                                passing_yards_per_game, stat["value"]
                            )
                        elif stat["name"] == "totalPointsPerGame":
                            total_points_per_game = more_interesting(
                                total_points_per_game, stat["value"]
                            )
                        elif stat["name"] == "yardsFromScrimmagePerGame":
                            yards_from_scrimmage_per_game = more_interesting(
                                yards_from_scrimmage_per_game, stat["value"]
                            )
                        elif stat["name"] == "yardsPerGame":
                            yards_per_game = more_interesting(
                                yards_per_game, stat["value"]
                            )
                        elif stat["name"] == "quarterbackRating":
                            quarterback_rating = more_interesting(
                                quarterback_rating, stat["value"]
                            )
                        elif stat["name"] == "ESPNRBRating":
                            espn_rb_rating = more_interesting(
                                espn_rb_rating, stat["value"]
                            )
                        elif stat["name"] == "rushingYardsPerGame":
                            rushing_yards_per_game = more_interesting(
                                rushing_yards_per_game, stat["value"]
                            )
                        elif stat["name"] == "receivingYardsPerGame":
                            receiving_yards_per_game = more_interesting(
                                receiving_yards_per_game, stat["value"]
                            )
                        elif stat["name"] == "twoPtReturns":
                            two_point_returns = more_interesting(
                                two_point_returns, stat["value"]
                            )
                        elif stat["name"] == "fieldGoalAttempts":
                            field_goal_attempts = more_interesting(
                                field_goal_attempts, stat["value"]
                            )
                        elif stat["name"] == "specialTeamFumbleReturnYards":
                            special_team_fumble_return_yards = more_interesting(
                                special_team_fumble_return_yards, stat["value"]
                            )
                        elif stat["name"] == "score":
                            pass
                        elif stat["name"] == "totalClearance":
                            total_clearances = more_interesting(
                                total_clearances, stat["value"]
                            )
                        elif stat["name"] == "kickExtraPoints":
                            kick_extra_point = more_interesting(
                                kick_extra_point, stat["value"]
                            )
                        elif stat["name"] == "kickExtraPointsMade":
                            kick_extra_points_made = more_interesting(
                                kick_extra_points_made, stat["value"]
                            )
                        elif stat["name"] == "attemptsInBox":
                            attempts_in_box = more_interesting(
                                attempts_in_box, stat["value"]
                            )
                        elif stat["name"] == "secondAssists":
                            second_assists = more_interesting(
                                second_assists, stat["value"]
                            )
                        elif stat["name"] == "QBR":
                            qbr = more_interesting(qbr, stat["value"])
                        elif stat["name"] == "attemptsOutBox":
                            attempts_out_box = more_interesting(
                                attempts_out_box, stat["value"]
                            )
                        elif stat["name"] == "adjQBR":
                            adjusted_qbr = more_interesting(adjusted_qbr, stat["value"])
                        elif stat["name"] == "turnoverPoints":
                            turnover_points = more_interesting(
                                turnover_points, stat["value"]
                            )
                        elif stat["name"] == "fantasyRating":
                            fantasy_rating = more_interesting(
                                fantasy_rating, stat["value"]
                            )
                        elif stat["name"] == "teamTurnovers":
                            team_turnovers = more_interesting(
                                team_turnovers, stat["value"]
                            )
                        elif stat["name"] == "secondChancePoints":
                            second_chance_points = more_interesting(
                                second_chance_points, stat["value"]
                            )
                        elif stat["name"] == "fastBreakPoints":
                            fast_break_points = more_interesting(
                                fast_break_points, stat["value"]
                            )
                        elif stat["name"] == "teamRebounds":
                            team_rebounds = more_interesting(
                                team_rebounds, stat["value"]
                            )
                        elif stat["name"] == "strikes":
                            strikes = more_interesting(strikes, stat["value"])
                        else:
                            raise ValueError(
                                f"Failed to account for statistic: {stat['name']} on {stats_url}"
                            )
            except KeyError as exc:
                logging.error("Key error for %s", stats_url)
                raise exc

    athlete_dict = {}
    athelete_url = player["athlete"]["$ref"]
    if athelete_url not in _BAD_URLS:
        athlete_response = session.get(athelete_url)
        athlete_response.raise_for_status()
        athelete_url = athlete_response.url
        athlete_dict = athlete_response.json()
    position_dict = {}
    if "position" in player:
        position_response = session.get(player["position"]["$ref"])
        position_response.raise_for_status()
        position_dict = position_response.json()
    college_dict = {}
    if "college" in athlete_dict:
        college_url = athlete_dict["college"]["$ref"]
        if (
            college_url
            != "http://sports.core.api.espn.com/v2/colleges/429?lang=en&region=us"
        ):
            college_response = session.get(college_url)
            college_response.raise_for_status()
            college_dict = college_response.json()
    name = athlete_dict.get("fullName", identifier)

    birth_date = None
    try:
        birth_date = parse(athlete_dict["dateOfBirth"]).date()
    except KeyError:
        logging.debug("Failed to get birth date for %s", athelete_url)

    birth_place = athlete_dict.get("birthPlace", {})
    birth_address_components = []
    city = birth_place.get("city")
    if city is not None:
        birth_address_components.append(city)
    state = birth_place.get("state")
    if state is not None:
        birth_address_components.append(state)
    country = birth_place.get("country")
    if country is not None:
        birth_address_components.append(country)

    birth_address = None
    if not birth_address_components:
        query = ", ".join(birth_address_components).strip()
        if query:
            try:
                birth_address = create_google_address_model(
                    query=query,
                    session=session,
                    dt=None,
                )
            except ValueError:
                logging.warning("Failed to get birth address for: %s", query)

    position_abbreviation = position_dict.get("abbreviation")
    college = None
    try:
        if "id" in college_dict:
            college = create_espn_venue_model(
                venue=college_dict, session=session, dt=dt, version=VENUE_VERSION
            )
    except (KeyError, AddressException) as exc:
        logging.warning("Failed to get college: %s", str(exc))

    headshot = None
    if "headshot" in athlete_dict:
        headshot = athlete_dict["headshot"]["href"]

    return PlayerModel(
        identifier=identifier,
        jersey=jersey,
        kicks=kicks,
        fumbles=fumbles,
        fumbles_lost=fumbles_lost,
        field_goals=field_goals,
        field_goals_attempted=field_goals_attempted,
        offensive_rebounds=offensive_rebounds,
        assists=assists,
        turnovers=turnovers,
        name=name,
        marks=marks,
        handballs=handballs,
        disposals=disposals,
        goals=goals,
        behinds=behinds,
        hit_outs=hitouts,
        tackles=tackles,
        rebounds=rebounds,
        insides=inside_50s,
        clearances=total_clearances,
        clangers=clangers,
        free_kicks_for=frees_for,
        free_kicks_against=frees_against,
        brownlow_votes=None,
        contested_possessions=contested_possessions,
        uncontested_possessions=uncontested_possessions,
        contested_marks=contested_marks,
        marks_inside=marks_inside_50,
        one_percenters=one_percenters,
        bounces=bounces,
        goal_assists=goal_assists,
        percentage_played=None,
        birth_date=birth_date,
        species=str(Species.HUMAN),
        handicap_weight=None,
        father=None,
        sex=str(Sex.MALE),
        age=None if birth_date is None else relativedelta(birth_date, dt.date()).years,
        starting_position=positions_validator[position_abbreviation]
        if position_abbreviation != "-" and position_abbreviation is not None
        else None,
        weight=athlete_dict["weight"] * 0.453592 if "weight" in athlete_dict else None,
        birth_address=birth_address,
        owner=None,
        seconds_played=None,
        three_point_field_goals=None,
        three_point_field_goals_attempted=three_point_field_goals_attempted,
        free_throws=free_throws,
        free_throws_attempted=free_throws_attempted,
        defensive_rebounds=defensive_rebounds,
        steals=steals,
        blocks=blocks,
        personal_fouls=None,
        points=score,
        game_score=None,
        point_differential=None,
        version=version,
        height=athlete_dict["height"] * 2.54 if "height" in athlete_dict else None,
        colleges=[college] if college is not None else [],
        headshot=headshot,
        forced_fumbles=forced_fumbles,
        fumbles_recovered=fumbles_recovered,
        fumbles_recovered_yards=fumbles_recovered_yards,
        fumbles_touchdowns=fumbles_touchdowns,
        offensive_two_point_returns=offensive_two_point_returns,
        offensive_fumbles_touchdowns=offensive_fumbles_touchdowns,
        defensive_fumbles_touchdowns=defensive_fumbles_touchdowns,
        average_gain=average_gain,
        completion_percentage=completion_percentage,
        completions=completions,
        espn_quarterback_rating=espn_quarterback_rating,
        interception_percentage=interception_percentage,
        interceptions=interceptions,
        long_passing=long_passing,
        misc_yards=misc_yards,
        net_passing_yards=net_passing_yards,
        net_total_yards=net_total_yards,
        passing_attempts=passing_attempts,
        passing_big_plays=passing_big_plays,
        passing_first_downs=passing_first_downs,
        passing_fumbles=passing_fumbles,
        passing_fumbles_lost=passing_fumbles_lost,
        passing_touchdown_percentage=passing_touchdown_percentage,
        passing_touchdowns=passing_touchdowns,
        passing_yards=passing_yards,
        passing_yards_after_catch=passing_yards_after_catch,
        quarterback_rating=quarterback_rating,
        sacks=sacks,
        passing_yards_at_catch=passing_yards_at_catch,
        sacks_yards_lost=sacks_yards_lost,
        net_passing_attempts=net_passing_attempts,
        total_offensive_plays=total_offensive_plays,
        total_points=total_points,
        total_touchdowns=total_touchdowns,
        total_yards=total_yards,
        total_yards_from_scrimmage=total_yards_from_scrimmage,
        two_point_pass=two_point_pass,
        two_point_pass_attempt=two_point_pass_attempt,
        yards_per_completion=yards_per_completion,
        yards_per_pass_attempt=yards_per_pass_attempt,
        net_yards_per_pass_attempt=net_yards_per_pass_attempt,
        long_rushing=long_rushing,
        rushing_attempts=rushing_attempts,
        rushing_big_plays=rushing_big_plays,
        rushing_first_downs=rushing_first_downs,
        rushing_fumbles=rushing_fumbles,
        rushing_fumbles_lost=rushing_fumbles_lost,
        rushing_touchdowns=rushing_touchdowns,
        rushing_yards=rushing_yards,
        stuffs=stuffs,
        stuff_yards_lost=stuff_yards_lost,
        two_point_rush=two_point_rush,
        two_point_rush_attempts=two_point_rush_attempts,
        yards_per_rush_attempt=yards_per_rush_attempt,
        espn_widereceiver=espn_widereceiver,
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
        receptions=receptions,
        two_point_receptions=two_point_receptions,
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
        quarterback_hits=quarterback_hits,
        sacks_assisted=sacks_assisted,
        sacks_unassisted=sacks_unassisted,
        sacks_yards=sacks_yards,
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
        extra_point_blocked=extra_point_blocked,
        extra_points_blocked_percentage=extra_points_blocked_percentage,
        extra_points_made=extra_points_made,
        fair_catches=fair_catches,
        fair_catch_percentage=fair_catch_percentage,
        field_goal_attempts_max_19_yards=field_goal_attempts_max_19_yards,
        field_goal_attempts_max_29_yards=field_goal_attempts_max_29_yards,
        field_goal_attempts_max_39_yards=field_goal_attempts_max_39_yards,
        field_goal_attempts_max_49_yards=field_goal_attempts_max_49_yards,
        field_goal_attempts_max_59_yards=field_goal_attempts_max_59_yards,
        field_goal_attempts_max_99_yards=field_goal_attempts_max_99_yards,
        field_goal_attempts_above_50_yards=field_goal_attempts_above_50_yards,
        field_goal_attempt_yards=field_goal_attempt_yards,
        field_goals_blocked=field_goals_blocked,
        field_goals_blocked_percentage=field_goals_blocked_percentage,
        field_goals_made=field_goals_made,
        field_goals_made_max_19_yards=field_goals_made_max_19_yards,
        field_goals_made_max_29_yards=field_goals_made_max_29_yards,
        field_goals_made_max_39_yards=field_goals_made_max_39_yards,
        field_goals_made_max_49_yards=field_goals_made_max_49_yards,
        field_goals_made_max_59_yards=field_goals_made_max_59_yards,
        field_goals_made_max_99_yards=field_goals_made_max_99_yards,
        field_goals_made_above_50_yards=field_goals_made_above_50_yards,
        field_goals_made_yards=field_goals_made_yards,
        field_goals_missed_yards=field_goals_missed_yards,
        kickoff_out_of_bounds=kickoff_out_of_bounds,
        kickoff_returns=kickoff_returns,
        kickoff_returns_touchdowns=kickoff_returns_touchdowns,
        kickoff_return_yards=kickoff_return_yards,
        kickoffs=kickoffs,
        kickoff_yards=kickoff_yards,
        long_field_goal_attempt=long_field_goal_attempt,
        long_field_goal_made=long_field_goal_made,
        long_kickoff=long_kickoff,
        total_kicking_points=total_kicking_points,
        touchback_percentage=touchback_percentage,
        touchbacks=touchbacks,
        defensive_fumble_returns=defensive_fumble_returns,
        defensive_fumble_return_yards=defensive_fumble_return_yards,
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
        opposition_fumble_recoveries=opposition_fumble_recoveries,
        opposition_fumble_recovery_yards=opposition_fumble_recovery_yards,
        opposition_special_team_fumble_returns=opposition_special_team_fumble_returns,
        opposition_special_team_fumble_return_yards=opposition_special_team_fumble_return_yards,
        punt_return_fair_catches=punt_return_fair_catches,
        punt_return_fair_catch_percentage=punt_return_fair_catch_percentage,
        punt_return_fumbles=punt_return_fumbles,
        punt_return_fumbles_lost=punt_return_fumbles_lost,
        punt_returns=punt_returns,
        punt_returns_started_inside_the_10=punt_returns_started_inside_the_10,
        punt_returns_started_inside_the_20=punt_returns_started_inside_the_20,
        punt_return_touchdowns=punt_return_touchdowns,
        special_team_fumble_returns=special_team_fumble_returns,
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
        misc_points=misc_points,
        return_touchdowns=return_touchdowns,
        total_two_point_conversions=total_two_point_conversions,
        passing_touchdowns_9_yards=passing_touchdowns_9_yards,
        passing_touchdowns_19_yards=passing_touchdowns_19_yards,
        passing_touchdowns_29_yards=passing_touchdowns_29_yards,
        passing_touchdowns_39_yards=passing_touchdowns_39_yards,
        passing_touchdowns_49_yards=passing_touchdowns_49_yards,
        passing_touchdowns_above_50_yards=passing_touchdowns_above_50_yards,
        receiving_touchdowns_9_yards=receiving_touchdowns_9_yards,
        receiving_touchdowns_19_yards=receiving_touchdowns_19_yards,
        receiving_touchdowns_29_yards=receiving_touchdowns_29_yards,
        receiving_touchdowns_39_yards=receiving_touchdowns_39_yards,
        punt_return_yards=punt_return_yards,
        receiving_touchdowns_49_yards=receiving_touchdowns_49_yards,
        receiving_touchdowns_above_50_yards=receiving_touchdowns_above_50_yards,
        rushing_touchdowns_9_yards=rushing_touchdowns_9_yards,
        rushing_touchdowns_19_yards=rushing_touchdowns_19_yards,
        rushing_touchdowns_29_yards=rushing_touchdowns_29_yards,
        rushing_touchdowns_39_yards=rushing_touchdowns_39_yards,
        rushing_touchdowns_49_yards=rushing_touchdowns_49_yards,
        rushing_touchdowns_above_50_yards=rushing_touchdowns_above_50_yards,
        penalties_in_minutes=None,
        even_strength_goals=None,
        power_play_goals=power_play_goals,
        short_handed_goals=short_handed_goals,
        game_winning_goals=game_winning_goals,
        even_strength_assists=None,
        power_play_assists=power_play_assists,
        short_handed_assists=short_handed_assists,
        shots_on_goal=None,
        shooting_percentage=shooting_percentage,
        shifts=shifts,
        time_on_ice=time_on_ice,
        decision=None,
        goals_against=goals_against,
        shots_against=shots_against,
        saves=saves,
        save_percentage=save_percentage,
        shutouts=shutouts,
        individual_corsi_for_events=None,
        on_shot_ice_for_events=None,
        on_shot_ice_against_events=None,
        corsi_for_percentage=None,
        relative_corsi_for_percentage=None,
        offensive_zone_starts=None,
        defensive_zone_starts=None,
        offensive_zone_start_percentage=None,
        hits=None,
        true_shooting_percentage=None,
        at_bats=at_bats,
        runs_scored=None,
        runs_batted_in=runs_batted_in,
        bases_on_balls=None,
        strikeouts=strikeouts,
        plate_appearances=plate_appearances,
        hits_at_bats=None,
        obp=None,
        slg=None,
        ops=ops,
        pitches=pitches,
        strikes=strikes,
        win_probability_added=None,
        average_leverage_index=None,
        wpa_plus=None,
        wpa_minus=None,
        cwpa=None,
        acli=None,
        re24=None,
        putouts=putouts,
        innings_pitched=None,
        earned_runs=None,
        home_runs=home_runs,
        era=era,
        batters_faced=batters_faced,
        strikes_by_contact=None,
        strikes_swinging=None,
        strikes_looking=None,
        ground_balls=ground_balls,
        fly_balls=fly_balls,
        line_drives=None,
        inherited_runners=inherited_runners,
        inherited_scores=None,
        effective_field_goal_percentage=None,
        penalty_kicks_made=None,
        penalty_kicks_attempted=penalty_kick_shots,
        shots_total=total_shots,
        shots_on_target=shots_on_target,
        yellow_cards=yellow_cards,
        red_cards=red_cards,
        touches=None,
        expected_goals=None,
        non_penalty_expected_goals=None,
        expected_assisted_goals=None,
        shot_creating_actions=None,
        goal_creating_actions=None,
        passes_completed=None,
        passes_attempted=None,
        pass_completion=None,
        progressive_passes=None,
        carries=None,
        progressive_carries=None,
        take_ons_attempted=None,
        successful_take_ons=None,
        total_passing_distance=None,
        progressive_passing_distance=None,
        passes_completed_short=None,
        passes_attempted_short=None,
        pass_completion_short=None,
        passes_completed_medium=None,
        passes_attempted_medium=None,
        pass_completion_medium=None,
        passes_completed_long=None,
        passes_attempted_long=None,
        pass_completion_long=None,
        expected_assists=None,
        key_passes=None,
        passes_into_final_third=None,
        passes_into_penalty_area=None,
        crosses_into_penalty_area=None,
        live_ball_passes=None,
        dead_ball_passes=None,
        passes_from_free_kicks=None,
        through_balls=through_balls,
        switches=None,
        crosses=total_crosses,
        throw_ins_taken=None,
        corner_kicks=None,
        inswinging_corner_kicks=None,
        outswinging_corner_kicks=None,
        straight_corner_kicks=None,
        passes_offside=None,
        passes_blocked=None,
        tackles_won=None,
        tackles_in_defensive_third=None,
        tackles_in_middle_third=None,
        tackles_in_attacking_third=None,
        dribblers_tackled=None,
        dribbles_challenged=None,
        percent_of_dribblers_tackled=None,
        challenges_lost=None,
        shots_blocked=shots_blocked,
        tackles_plus_interceptions=None,
        errors=errors,
        touches_in_defensive_penalty_area=None,
        touches_in_defensive_third=None,
        touches_in_middle_third=None,
        touches_in_attacking_third=None,
        touches_in_attacking_penalty_area=None,
        live_ball_touches=None,
        successful_take_on_percentage=None,
        times_tackled_during_take_ons=None,
        tackled_during_take_on_percentage=None,
        total_carrying_distance=None,
        progressive_carrying_distance=None,
        carries_into_final_third=None,
        carries_into_penalty_area=None,
        miscontrols=None,
        dispossessed=None,
        passes_received=None,
        progressive_passes_received=None,
        second_yellow_card=None,
        fouls_committed=fouls_committed,
        fouls_drawn=fouls_suffered,
        offsides=offsides,
        penalty_kicks_won=None,
        penalty_kicks_conceded=None,
        own_goals=own_goals,
        ball_recoveries=None,
        aerials_won=None,
        aerials_lost=None,
        percentage_of_aerials_won=None,
        shots_on_target_against=None,
        post_shot_expected_goals=None,
        passes_attempted_minus_goal_kicks=None,
        throws_attempted=None,
        percentage_of_passes_that_were_launched=None,
        average_pass_length=None,
        goal_kicks_attempted=None,
        percentage_of_goal_kicks_that_were_launched=None,
        average_goal_kick_length=None,
        crosses_faced=None,
        crosses_stopped=None,
        percentage_crosses_stopped=None,
        defensive_actions_outside_penalty_area=None,
        average_distance_of_defensive_actions=None,
        three_point_attempt_rate=None,
        batting_style=None,
        bowling_style=None,
        playing_roles=None,
        runs=runs,
        balls=None,
        fours=None,
        sixes=None,
        strikerate=None,
        fall_of_wicket_order=None,
        fall_of_wicket_num=None,
        fall_of_wicket_runs=None,
        fall_of_wicket_balls=None,
        fall_of_wicket_overs=None,
        fall_of_wicket_over_number=None,
        ball_over_actual=None,
        ball_over_unique=None,
        ball_total_runs=None,
        ball_batsman_runs=None,
        overs=None,
        maidens=None,
        conceded=None,
        wickets=None,
        economy=None,
        runs_per_ball=None,
        dots=None,
        wides=None,
        no_balls=None,
        free_throw_attempt_rate=None,
        offensive_rebound_percentage=offensive_rebound_percentage,
        defensive_rebound_percentage=None,
        total_rebound_percentage=None,
        assist_percentage=None,
        steal_percentage=None,
        block_percentage=None,
        turnover_percentage=None,
        usage_percentage=None,
        offensive_rating=None,
        defensive_rating=None,
        box_plus_minus=None,
        ace_percentage=None,
        double_fault_percentage=None,
        first_serves_in=None,
        first_serve_percentage=None,
        second_serve_percentage=None,
        break_points_saved=None,
        return_points_won_percentage=None,
        winners=None,
        winners_fronthand=None,
        winners_backhand=None,
        unforced_errors=None,
        unforced_errors_fronthand=None,
        unforced_errors_backhand=None,
        serve_points=None,
        serves_won=None,
        serves_aces=None,
        serves_unreturned=None,
        serves_forced_error_percentage=None,
        serves_won_in_three_shots_or_less=None,
        serves_wide_percentage=None,
        serves_body_percentage=None,
        serves_t_percentage=None,
        serves_wide_deuce_percentage=None,
        serves_body_deuce_percentage=None,
        serves_t_deuce_percentage=None,
        serves_wide_ad_percentage=None,
        serves_body_ad_percentage=None,
        serves_t_ad_percentage=None,
        serves_net_percentage=None,
        serves_wide_direction_percentage=None,
        shots_deep_percentage=None,
        shots_deep_wide_percentage=None,
        shots_foot_errors_percentage=None,
        shots_unknown_percentage=None,
        points_won_percentage=None,
        tackles_inside_50=tackles_inside_50,
        total_possessions=total_possessions,
        uncontested_marks=uncontested_marks,
        disposal_efficiency=disposal_efficiency,
        centre_clearances=centre_clearances,
        stoppage_clearances=stoppage_clearances,
        goal_accuracy=goal_accuracy,
        score_involvements=score_involvements,
        effective_clearances=effective_clearances,
        effective_tackles=effective_tackles,
        ineffective_tackles=ineffective_tackles,
        tackle_percentage=tackle_percentage,
        appearances=appearances,
        average_rating_from_correspondent=average_rating_from_correspondent,
        average_rating_from_data_feed=average_rating_from_data_feed,
        average_rating_from_editor=average_rating_from_editor,
        average_rating_from_user=average_rating_from_user,
        did_not_play=did_not_play,
        draws=draws,
        goal_difference=goal_difference,
        losses=losses,
        lost_corners=lost_corners,
        minutes=minutes,
        pass_percentage=pass_percentage,
        starts=starts,
        sub_ins=sub_ins,
        sub_outs=sub_outs,
        suspensions=suspensions,
        time_ended=time_ended,
        time_started=time_started,
        win_percentage=win_percentage,
        wins=wins,
        won_corners=won_corners,
        clean_sheet=clean_sheets,
        crosses_caught=crosses_caught,
        goals_conceded=goals_conceded,
        partial_clean_sheet=partial_clean_sheet,
        penalty_kick_conceded=penalty_kick_conceded,
        penalty_kick_save_percentage=penalty_kick_save_percentage,
        penalty_kicks_faced=penalty_kicks_faced,
        penalty_kicks_saved=penalty_kicks_saved,
        punches=punches,
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
        headed_goals=headed_goals,
        inaccurate_crosses=inaccurate_crosses,
        inaccurate_long_balls=inaccurate_long_balls,
        inaccurate_passes=inaccurate_passes,
        inaccurate_through_balls=inaccurate_through_balls,
        left_footed_shots=left_footed_shots,
        long_ball_percentage=long_ball_percentage,
        penalty_kick_goals=penalty_kick_goals,
        penalty_kick_percentage=penalty_kick_percentage,
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
        through_ball_percentage=through_ball_percentage,
        long_balls=long_balls,
        total_passes=total_passes,
        games_played=games_played,
        team_games_played=team_games_played,
        hit_by_pitch=hit_by_pitch,
        rbis=rbis,
        sac_hits=sac_hits,
        stolen_bases=stolen_bases,
        walks=walks,
        catcher_interference=catcher_interference,
        gidps=gidps,
        sac_flies=sac_flies,
        grand_slam_home_runs=grand_slam_home_runs,
        runners_left_on_base=runners_left_on_base,
        triples=triples,
        game_winning_rbis=game_winning_rbis,
        intentional_walks=intentional_walks,
        doubles=doubles,
        caught_stealing=caught_stealing,
        games_started=games_started,
        pinch_at_bats=pinch_at_bats,
        pinch_hits=pinch_hits,
        player_rating=player_rating,
        is_qualified=is_qualified,
        is_qualified_steals=is_qualified_steals,
        total_bases=total_bases,
        projected_home_runs=projected_home_runs,
        extra_base_hits=extra_base_hits,
        runs_created=runs_created,
        batting_average=batting_average,
        pinch_average=pinch_average,
        slug_average=slug_average,
        secondary_average=secondary_average,
        on_base_percentage=on_base_percentage,
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
        batters_hit=batters_hit,
        sacrifice_bunts=sacrifice_bunts,
        save_opportunities=save_opportunities,
        finishes=finishes,
        balks=balks,
        holds=holds,
        complete_games=complete_games,
        perfect_games=perfect_games,
        wild_pitches=wild_pitches,
        third_innings=third_innings,
        team_earned_runs=team_earned_runs,
        pickoff_attempts=pickoff_attempts,
        run_support=run_support,
        pitches_as_starter=pitches_as_starter,
        average_game_score=average_game_score,
        quality_starts=quality_starts,
        inherited_runners_scored=inherited_runners_scored,
        opponent_total_bases=opponent_total_bases,
        is_qualified_saves=is_qualified_saves,
        full_innings=full_innings,
        part_innings=part_innings,
        blown_saves=blown_saves,
        innings=innings,
        whip=whip,
        caught_stealing_percentage=caught_stealing_percentage,
        pitches_per_start=pitches_per_start,
        pitches_per_inning=pitches_per_inning,
        run_support_average=run_support_average,
        opponent_average=opponent_average,
        opponent_slug_average=opponent_slug_average,
        opponent_on_base_percentage=opponent_on_base_percentage,
        opponent_ops=opponent_ops,
        strikeouts_per_nine_innings=strikeouts_per_nine_innings,
        strikeout_to_walk_ratio=strikeout_to_walk_ratio,
        tough_losses=tough_losses,
        cheap_wins=cheap_wins,
        save_opportunities_per_win=save_opportunities_per_win,
        pitch_count=pitch_count,
        strike_pitch_ratio=strike_pitch_ratio,
        double_plays=double_plays,
        opportunities=opportunities,
        passed_balls=passed_balls,
        outfield_assists=outfield_assists,
        pickoffs=pickoffs,
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
        average_minutes=average_minutes,
        nba_rating=nba_rating,
        plus_minus=plus_minus,
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
        r40=r40,
        double_double=double_double,
        triple_double=triple_double,
        field_goals_percentage=field_goal_percentage,
        free_throws_percentage=free_throw_percentage,
        free_throws_made=free_throws_made,
        three_point_percentage=three_point_percentage,
        three_point_field_goals_made=three_point_field_goals_made,
        total_turnovers=total_turnovers,
        points_in_paint=points_in_paint,
        brick_index=brick_index,
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
        estimated_possessions=estimated_possessions,
        average_estimated_possessions=average_estimated_possessions,
        points_per_estimated_possessions=points_per_estimated_possessions,
        average_team_turnovers=average_team_turnovers,
        average_total_turnovers=average_total_turnovers,
        three_point_field_goal_percentage=three_point_field_goal_percentage,
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
        p40=p40,
        a40=a40,
        average_goals_against=average_goals_against,
        average_shots_against=average_shots_against,
        penalty_kill_percentage=penalty_kill_percentage,
        power_play_goals_against=power_play_goals_against,
        short_handed_goals_against=short_handed_goals_against,
        shootout_saves=shootout_saves,
        shootout_shots_against=shootout_shots_against,
        times_short_handed=times_short_handed,
        empty_net_goals_against=empty_net_goals_against,
        overtime_losses=overtime_losses,
        takeaways=takeaways,
        even_strength_saves=even_strength_saves,
        power_play_saves=power_play_saves,
        short_handed_saves=short_handed_saves,
        games=games,
        game_started=game_started,
        ties=ties,
        time_on_ice_per_game=time_on_ice_per_game,
        power_play_time_on_ice=power_play_time_on_ice,
        short_handed_time_on_ice=short_handed_time_on_ice,
        even_strength_time_on_ice=even_strength_time_on_ice,
        shifts_per_game=shifts_per_game,
        production=production,
        shot_differential=shot_differential,
        goal_differential=goal_differential,
        pim_differential=pim_differential,
        rating=rating,
        average_goals=average_goals,
        ytd_goals=ytd_goals,
        shots_in_first_period=shots_in_first_period,
        shots_in_second_period=shots_in_second_period,
        shots_in_third_period=shots_in_third_period,
        shots_overtime=shots_overtime,
        shots_missed=shots_missed,
        average_shots=average_shots,
        points_per_game=points_per_game,
        power_play_opportunities=power_play_opportunities,
        power_play_percentage=power_play_percentage,
        shootout_attempts=shootout_attempts,
        shootout_shot_percentage=shootout_shot_percentage,
        empty_net_goals_for=empty_net_goals_for,
        shutouts_against=shutouts_against,
        total_face_offs=total_face_offs,
        faceoffs_won=faceoffs_won,
        faceoffs_lost=faceoffs_lost,
        faceoff_percentage=faceoff_percentage,
        unassisted_goals=unassisted_goals,
        game_tying_goals=game_tying_goals,
        giveaways=giveaways,
        penalties=penalties,
        penalty_minutes=penalty_minutes,
        penalty_minutes_against=penalty_minutes_against,
        major_penalties=major_penalties,
        minor_penalties=minor_penalties,
        match_penalties=match_penalties,
        misconducts=misconducts,
        game_misconducts=game_misconducts,
        boarding_penalties=boarding_penalties,
        unsportsmanlike_penalties=unsportsmanlike_penalties,
        fighting_penalties=fighting_penalties,
        average_fights=average_fights,
        time_between_fights=time_between_fights,
        instigator_penalties=instigator_penalties,
        charging_penalties=charging_penalties,
        hooking_penalties=hooking_penalties,
        tripping_penalties=tripping_penalties,
        roughing_penalties=roughing_penalties,
        holding_penalties=holding_penalties,
        interference_penalties=interference_penalties,
        slashing_penalties=slashing_penalties,
        high_sticking_penalties=high_sticking_penalties,
        cross_checking_penalties=cross_checking_penalties,
        stick_holding_penalties=stick_holding_penalties,
        goalie_interference_penalties=goalie_interference_penalties,
        elbowing_penalties=elbowing_penalties,
        diving_penalties=diving_penalties,
        net_passing_yards_per_game=net_passing_yards_per_game,
        net_yards_per_game=net_yards_per_game,
        passing_yards_per_game=passing_yards_per_game,
        total_points_per_game=total_points_per_game,
        yards_from_scrimmage_per_game=yards_from_scrimmage_per_game,
        yards_per_game=yards_per_game,
        espn_rb_rating=espn_rb_rating,
        rushing_yards_per_game=rushing_yards_per_game,
        receiving_yards_per_game=receiving_yards_per_game,
        two_point_returns=two_point_returns,
        field_goal_attempts=field_goal_attempts,
        special_team_fumble_return_yards=special_team_fumble_return_yards,
        kick_extra_points=kick_extra_point,
        kick_extra_points_made=kick_extra_points_made,
        attempts_in_box=attempts_in_box,
        second_assists=second_assists,
        qbr=qbr,
        attempts_out_box=attempts_out_box,
        adjusted_qbr=adjusted_qbr,
        turnover_points=turnover_points,
        fantasy_rating=fantasy_rating,
        team_turnovers=team_turnovers,
        second_chance_points=second_chance_points,
        fast_break_points=fast_break_points,
        team_rebounds=team_rebounds,
        gained=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_espn_player_model(
    session: requests_cache.CachedSession,
    player: dict[str, Any],
    positions_validator: dict[str, str],
    dt: datetime.datetime,
    version: str,
) -> PlayerModel:
    return _create_espn_player_model(
        session=session,
        player=player,
        positions_validator=positions_validator,
        dt=dt,
        version=version,
    )


def create_espn_player_model(
    session: requests_cache.CachedSession,
    player: dict[str, Any],
    dt: datetime.datetime,
    positions_validator: dict[str, str],
) -> PlayerModel:
    """Create a player model based off ESPN."""
    if (
        not pytest_is_running.is_running()
        and dt.date() < datetime.datetime.today().date() - datetime.timedelta(days=7)
    ):
        return _cached_create_espn_player_model(
            session=session,
            player=player,
            positions_validator=positions_validator,
            dt=dt,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_espn_player_model(
            session=session,
            player=player,
            positions_validator=positions_validator,
            dt=dt,
            version=VERSION,
        )
