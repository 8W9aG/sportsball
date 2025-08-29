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
    rebound_50s = None
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
    if "splits" in statistics_dict:
        for category in statistics_dict["splits"]["categories"]:
            for stat in category["stats"]:
                if stat["name"] == "kicks":
                    kicks = stat["value"]
                elif stat["name"] == "handballs":
                    handballs = stat["value"]
                elif stat["name"] == "disposals":
                    disposals = stat["value"]
                elif stat["name"] == "marks":
                    marks = stat["value"]
                elif stat["name"] == "bounces":
                    bounces = stat["value"]
                elif stat["name"] == "tackles":
                    tackles = stat["value"]
                elif stat["name"] == "tacklesInside50":
                    tackles_inside_50 = stat["value"]
                elif stat["name"] == "contestedPossessions":
                    contested_possessions = stat["value"]
                elif stat["name"] == "uncontestedPossessions":
                    uncontested_possessions = stat["value"]
                elif stat["name"] == "totalPossessions":
                    total_possessions = stat["value"]
                elif stat["name"] == "inside50s":
                    inside_50s = stat["value"]
                elif stat["name"] == "marksInside50":
                    marks_inside_50 = stat["value"]
                elif stat["name"] == "contestedMarks":
                    contested_marks = stat["value"]
                elif stat["name"] == "uncontestedMarks":
                    uncontested_marks = stat["value"]
                elif stat["name"] == "hitouts":
                    hitouts = stat["value"]
                elif stat["name"] == "onePercenters":
                    one_percenters = stat["value"]
                elif stat["name"] == "disposalEfficiency":
                    disposal_efficiency = stat["value"]
                elif stat["name"] == "clangers":
                    clangers = stat["value"]
                elif stat["name"] == "goals":
                    goals = stat["value"]
                elif stat["name"] == "behinds":
                    behinds = stat["value"]
                elif stat["name"] == "freesFor":
                    frees_for = stat["value"]
                elif stat["name"] == "freesAgainst":
                    frees_against = stat["value"]
                elif stat["name"] == "totalClearances":
                    total_clearances = stat["value"]
                elif stat["name"] == "centreClearances":
                    centre_clearances = stat["value"]
                elif stat["name"] == "stoppageClearances":
                    stoppage_clearances = stat["value"]
                elif stat["name"] == "rebound50s":
                    rebound_50s = stat["value"]
                elif stat["name"] == "goalAssists":
                    goal_assists = stat["value"]
                elif stat["name"] == "goalAccuracy":
                    goal_accuracy = stat["value"]
                elif stat["name"] == "rushedBehinds":
                    rushed_behinds = stat["value"]
                elif stat["name"] == "touchedBehinds":
                    touched_behinds = stat["value"]
                elif stat["name"] == "leftBehinds":
                    left_behinds = stat["value"]
                elif stat["name"] == "leftPosters":
                    left_posters = stat["value"]
                elif stat["name"] == "rightBehinds":
                    right_behinds = stat["value"]
                elif stat["name"] == "rightPosters":
                    right_posters = stat["value"]
                elif stat["name"] == "totalInterchangeCount":
                    total_interchange_count = stat["value"]
                elif stat["name"] == "interchangeCountQ1":
                    interchange_count_q1 = stat["value"]
                elif stat["name"] == "interchangeCountQ2":
                    interchange_count_q2 = stat["value"]
                elif stat["name"] == "interchangeCountQ3":
                    interchange_count_q3 = stat["value"]
                elif stat["name"] == "interchangeCountQ4":
                    interchange_count_q4 = stat["value"]
                elif stat["name"] == "blockedShots":
                    blocked_shots = stat["value"]
                elif stat["name"] == "effectiveClearance":
                    effective_clearances = stat["value"]
                elif stat["name"] == "effectiveTackles":
                    effective_tackles = stat["value"]
                elif stat["name"] == "inneffectiveTackles":
                    ineffective_tackles = stat["value"]
                elif stat["name"] == "interceptions":
                    interceptions = stat["value"]
                elif stat["name"] == "tacklePct":
                    tackle_percentage = stat["value"]
                elif stat["name"] == "totalClearance":
                    total_clearances = stat["value"]
                elif stat["name"] == "totalTackles":
                    tackles = stat["value"]
                elif stat["name"] == "appearances":
                    appearances = stat["value"]
                elif stat["name"] == "avgRatingFromCorrespondent":
                    average_rating_from_correspondent = stat["value"]
                elif stat["name"] == "avgRatingFromDataFeed":
                    average_rating_from_data_feed = stat["value"]
                elif stat["name"] == "avgRatingFromEditor":
                    average_rating_from_editor = stat["value"]
                elif stat["name"] == "avgRatingFromUser":
                    average_rating_from_user = stat["value"]
                elif stat["name"] == "dnp":
                    did_not_play = stat["value"]
                elif stat["name"] == "draws":
                    draws = stat["value"]
                elif stat["name"] == "foulsCommitted":
                    fouls_committed = stat["value"]
                elif stat["name"] == "foulsSuffered":
                    fouls_suffered = stat["value"]
                elif stat["name"] == "goalDifference":
                    goal_difference = stat["value"]
                elif stat["name"] == "handBalls":
                    handballs = stat["value"]
                elif stat["name"] == "losses":
                    losses = stat["value"]
                elif stat["name"] == "lostCorners":
                    lost_corners = stat["value"]
                elif stat["name"] == "minutes":
                    minutes = stat["value"]
                elif stat["name"] == "ownGoals":
                    own_goals = stat["value"]
                elif stat["name"] == "passPct":
                    pass_percentage = stat["value"]
                elif stat["name"] == "redCards":
                    red_cards = stat["value"]
                elif stat["name"] == "starts":
                    starts = stat["value"]
                elif stat["name"] == "subIns":
                    sub_ins = stat["value"]
                elif stat["name"] == "subOuts":
                    sub_outs = stat["value"]
                elif stat["name"] == "suspensions":
                    suspensions = stat["value"]
                elif stat["name"] == "timeEnded":
                    time_ended = stat["value"]
                elif stat["name"] == "timeStarted":
                    time_started = stat["value"]
                elif stat["name"] == "winPct":
                    win_percentage = stat["value"]
                elif stat["name"] == "wins":
                    wins = stat["value"]
                elif stat["name"] == "wonCorners":
                    won_corners = stat["value"]
                elif stat["name"] == "yellowCards":
                    yellow_cards = stat["value"]
                elif stat["name"] == "cleanSheet":
                    clean_sheet = stat["value"]
                elif stat["name"] == "crossesCaught":
                    crosses_caught = stat["value"]
                elif stat["name"] == "goalsConceded":
                    goals_conceded = stat["value"]
                elif stat["name"] == "partialCleenSheet":
                    partial_clean_sheet = stat["value"]
                elif stat["name"] == "penaltyKickConceded":
                    penalty_kick_conceded = stat["value"]
                elif stat["name"] == "penaltyKickSavePct":
                    penalty_kick_save_percentage = stat["value"]
                elif stat["name"] == "penaltyKicksFaced":
                    penalty_kicks_faced = stat["value"]
                elif stat["name"] == "penaltyKicksSaved":
                    penalty_kicks_saved = stat["value"]
                elif stat["name"] == "punches":
                    punches = stat["value"]
                elif stat["name"] == "saves":
                    saves = stat["value"]
                elif stat["name"] == "shootOutKicksFaced":
                    shoot_out_kicks_faced = stat["value"]
                elif stat["name"] == "shootOutKicksSaved":
                    shoot_out_kicks_saved = stat["value"]
                elif stat["name"] == "shootOutSavePct":
                    shoot_out_save_percentage = stat["value"]
                elif stat["name"] == "shotsFaced":
                    shots_faced = stat["value"]
                elif stat["name"] == "smothers":
                    smothers = stat["value"]
                elif stat["name"] == "unclaimedCrosses":
                    unclaimed_crosses = stat["value"]
                elif stat["name"] == "accurateCrosses":
                    accurate_crosses = stat["value"]
                elif stat["name"] == "accurateLongBalls":
                    accurate_long_balls = stat["value"]
                elif stat["name"] == "accuratePasses":
                    accurate_passes = stat["value"]
                elif stat["name"] == "accurateThroughBalls":
                    accurate_through_balls = stat["value"]
                elif stat["name"] == "crossPct":
                    cross_percentage = stat["value"]
                elif stat["name"] == "freeKickGoals":
                    free_kick_goals = stat["value"]
                elif stat["name"] == "freeKickPct":
                    free_kick_percentage = stat["value"]
                elif stat["name"] == "freeKickShots":
                    free_kick_shots = stat["value"]
                elif stat["name"] == "gameWinningAssists":
                    game_winning_assists = stat["value"]
                elif stat["name"] == "gameWinningGoals":
                    game_winning_goals = stat["value"]
                elif stat["name"] == "headedGoals":
                    headed_goals = stat["value"]
                elif stat["name"] == "inaccurateCrosses":
                    inaccurate_crosses = stat["value"]
                elif stat["name"] == "inaccurateLongBalls":
                    inaccurate_long_balls = stat["value"]
                elif stat["name"] == "inaccuratePasses":
                    inaccurate_passes = stat["value"]
                elif stat["name"] == "inaccurateThroughBalls":
                    inaccurate_through_balls = stat["value"]
                elif stat["name"] == "leftFootedShots":
                    left_footed_shots = stat["value"]
                elif stat["name"] == "longballPct":
                    longball_percentage = stat["value"]
                elif stat["name"] == "offsides":
                    offsides = stat["value"]
                elif stat["name"] == "penaltyKickGoals":
                    penalty_kick_goals = stat["value"]
                elif stat["name"] == "penaltyKickPct":
                    penalty_kick_percentage = stat["value"]
                elif stat["name"] == "penaltyKickShots":
                    penalty_kick_shots = stat["value"]
                elif stat["name"] == "penaltyKicksMissed":
                    penalty_kicks_missed = stat["value"]
                elif stat["name"] == "possessionPct":
                    possession_percentage = stat["value"]
                elif stat["name"] == "possessionTime":
                    possession_time = stat["value"]
                elif stat["name"] == "rightFootedShots":
                    right_footed_shots = stat["value"]
                elif stat["name"] == "shootOutGoals":
                    shoot_out_goals = stat["value"]
                elif stat["name"] == "shootOutMisses":
                    shoot_out_misses = stat["value"]
                elif stat["name"] == "shootOutPct":
                    shoot_out_percentage = stat["value"]
                elif stat["name"] == "shotAssists":
                    shot_assists = stat["value"]
                elif stat["name"] == "shotPct":
                    shot_percentage = stat["value"]
                elif stat["name"] == "shotsHeaded":
                    shots_headed = stat["value"]
                elif stat["name"] == "shotsOffTarget":
                    shots_off_target = stat["value"]
                elif stat["name"] == "shotsOnPost":
                    shots_on_post = stat["value"]
                elif stat["name"] == "shotsOnTarget":
                    shots_on_target = stat["value"]
                elif stat["name"] == "throughBallPct":
                    through_ball_percentage = stat["value"]
                elif stat["name"] == "totalCrosses":
                    total_crosses = stat["value"]
                elif stat["name"] == "totalGoals":
                    total_goals = stat["value"]
                elif stat["name"] == "totalLongBalls":
                    total_long_balls = stat["value"]
                elif stat["name"] == "totalPasses":
                    total_passes = stat["value"]
                elif stat["name"] == "totalShots":
                    total_shots = stat["value"]
                elif stat["name"] == "totalThroughBalls":
                    total_through_balls = stat["value"]
                elif stat["name"] == "hitByPitch":
                    hit_by_pitch = stat["value"]
                elif stat["name"] == "groundBalls":
                    ground_balls = stat["value"]
                elif stat["name"] == "strikeouts":
                    strikeouts = stat["value"]
                elif stat["name"] == "RBIs":
                    rbis = stat["value"]
                elif stat["name"] == "sacHits":
                    sac_hits = stat["value"]
                elif stat["name"] == "hits":
                    hits = stat["value"]
                elif stat["name"] == "stolenBases":
                    stolen_bases = stat["value"]
                elif stat["name"] == "walks":
                    walks = stat["value"]
                elif stat["name"] == "catcherInterference":
                    catcher_interference = stat["value"]
                elif stat["name"] == "runs":
                    runs = stat["value"]
                elif stat["name"] == "GIDPs":
                    gidps = stat["value"]
                elif stat["name"] == "sacFlies":
                    sacrifice_flies = stat["value"]
                elif stat["name"] == "atBats":
                    at_bats = stat["value"]
                elif stat["name"] == "homeRuns":
                    home_runs = stat["value"]
                elif stat["name"] == "grandSlamHomeRuns":
                    grand_slam_home_runs = stat["value"]
                elif stat["name"] == "runnersLeftOnBase":
                    runners_left_on_base = stat["value"]
                elif stat["name"] == "triples":
                    triples = stat["value"]
                elif stat["name"] == "gameWinningRBIs":
                    game_winning_rbis = stat["value"]
                elif stat["name"] == "intentionalWalks":
                    intentional_walks = stat["value"]
                elif stat["name"] == "doubles":
                    doubles = stat["value"]
                elif stat["name"] == "flyBalls":
                    fly_balls = stat["value"]
                elif stat["name"] == "caughtStealing":
                    caught_stealing = stat["value"]
                elif stat["name"] == "pitches":
                    pitches = stat["value"]
                elif stat["name"] == "gamesStarted":
                    games_started = stat["value"]
                elif stat["name"] == "pinchAtBats":
                    pinch_at_bats = stat["value"]
                elif stat["name"] == "pinchHits":
                    pinch_hits = stat["value"]
                elif stat["name"] == "playerRating":
                    player_rating = stat["value"]
                elif stat["name"] == "isQualified":
                    is_qualified = stat["value"]
                elif stat["name"] == "isQualifiedSteals":
                    is_qualified_steals = stat["value"]
                elif stat["name"] == "totalBases":
                    total_bases = stat["value"]
                elif stat["name"] == "plateAppearances":
                    plate_appearances = stat["value"]
                elif stat["name"] == "projectedHomeRuns":
                    projected_home_runs = stat["value"]
                elif stat["name"] == "extraBaseHits":
                    extra_base_hits = stat["value"]
                elif stat["name"] == "runsCreated":
                    runs_created = stat["value"]
                elif stat["name"] == "avg":
                    batting_average = stat["value"]
                elif stat["name"] == "pinchAvg":
                    pinch_average = stat["value"]
                elif stat["name"] == "slugAvg":
                    slug_average = stat["value"]
                elif stat["name"] == "secondaryAvg":
                    secondary_average = stat["value"]
                elif stat["name"] == "onBasePct":
                    on_base_percentage = stat["value"]
                elif stat["name"] == "OPS":
                    ops = stat["value"]
                elif stat["name"] == "groundToFlyRatio":
                    ground_to_fly_ratio = stat["value"]
                elif stat["name"] == "runsCreatedPer27Outs":
                    runs_created_per_27_outs = stat["value"]
                elif stat["name"] == "batterRating":
                    batter_rating = stat["value"]
                elif stat["name"] == "atBatsPerHomeRun":
                    at_bats_per_home_run = stat["value"]
                elif stat["name"] == "stolenBasePct":
                    stolen_base_percentage = stat["value"]
                elif stat["name"] == "pitchesPerPlateAppearance":
                    pitches_per_plate_appearance = stat["value"]
                elif stat["name"] == "isolatedPower":
                    isolated_power = stat["value"]
                elif stat["name"] == "walkToStrikeoutRatio":
                    walk_to_strikeout_ratio = stat["value"]
                elif stat["name"] == "walksPerPlateAppearance":
                    walks_per_plate_appearance = stat["value"]
                elif stat["name"] == "secondaryAvgMinusBA":
                    secondary_average_minus_batting_average = stat["value"]
                elif stat["name"] == "runsProduced":
                    runs_produced = stat["value"]
                elif stat["name"] == "runsRatio":
                    runs_ratio = stat["value"]
                elif stat["name"] == "patienceRatio":
                    patience_ratio = stat["value"]
                elif stat["name"] == "BIPA":
                    balls_in_play_average = stat["value"]
                elif stat["name"] == "MLBRating":
                    mlb_rating = stat["value"]
                elif stat["name"] == "offWARBR":
                    offensive_wins_above_replacement = stat["value"]
                elif stat["name"] == "WARBR":
                    wins_above_replacement = stat["value"]
                elif stat["name"] == "earnedRuns":
                    earned_runs = stat["value"]
                elif stat["name"] == "battersHit":
                    batters_hit = stat["value"]
                elif stat["name"] == "sacBunts":
                    sacrifice_bunts = stat["value"]
                elif stat["name"] == "saveOpportunities":
                    save_opportunities = stat["value"]
                elif stat["name"] == "finishes":
                    finishes = stat["value"]
                elif stat["name"] == "balks":
                    balks = stat["value"]
                elif stat["name"] == "battersFaced":
                    batters_faced = stat["value"]
                elif stat["name"] == "holds":
                    holds = stat["value"]
                elif stat["name"] == "completeGames":
                    complete_games = stat["value"]
                elif stat["name"] == "perfectGames":
                    perfect_games = stat["value"]
                elif stat["name"] == "wildPitches":
                    wild_pitches = stat["value"]
                elif stat["name"] == "thirdInnings":
                    third_innings = stat["value"]
                elif stat["name"] == "teamEarnedRuns":
                    team_earned_runs = stat["value"]
                elif stat["name"] == "shutouts":
                    shutouts = stat["value"]
                elif stat["name"] == "pickoffAttempts":
                    pickoff_attempts = stat["value"]
                elif stat["name"] == "pitches":
                    pitches = stat["value"]
                elif stat["name"] == "runSupport":
                    run_support = stat["value"]
                elif stat["name"] == "catcherInterference":
                    catcher_interference = stat["value"]
                elif stat["name"] == "pitchesAsStarter":
                    pitches_as_starter = stat["value"]
                elif stat["name"] == "avgGameScore":
                    average_game_score = stat["value"]
                elif stat["name"] == "qualityStarts":
                    quality_starts = stat["value"]
                elif stat["name"] == "inheritedRunners":
                    inherited_runners = stat["value"]
                elif stat["name"] == "inheritedRunnersScored":
                    inherited_runners_scored = stat["value"]
                elif stat["name"] == "opponentTotalBases":
                    opponent_total_bases = stat["value"]
                elif stat["name"] == "isQualifiedSaves":
                    is_qualified_saves = stat["value"]
                elif stat["name"] == "fullInnings":
                    full_innings = stat["value"]
                elif stat["name"] == "partInnings":
                    part_innings = stat["value"]
                elif stat["name"] == "blownSaves":
                    blown_saves = stat["value"]
                elif stat["name"] == "innings":
                    innings = stat["value"]
                elif stat["name"] == "ERA":
                    era = stat["value"]
                elif stat["name"] == "WHIP":
                    whip = stat["value"]
                elif stat["name"] == "caughtStealingPct":
                    caught_stealing_percentage = stat["value"]
                elif stat["name"] == "pitchesPerStart":
                    pitches_per_start = stat["value"]
                elif stat["name"] == "pitchesPerInning":
                    pitches_per_inning = stat["value"]
                elif stat["name"] == "pitchesPerPlateAppearance":
                    pitches_per_plate_appearance = stat["value"]
                elif stat["name"] == "runSupportAvg":
                    run_support_average = stat["value"]
                elif stat["name"] == "opponentAvg":
                    opponent_average = stat["value"]
                elif stat["name"] == "opponentSlugAvg":
                    opponent_slug_average = stat["value"]
                elif stat["name"] == "opponentOnBasePct":
                    opponent_on_base_percentage = stat["value"]
                elif stat["name"] == "opponentOPS":
                    opponent_ops = stat["value"]
                elif stat["name"] == "savePct":
                    save_percentage = stat["value"]
                elif stat["name"] == "strikeoutsPerNineInnings":
                    strikeouts_per_nine_innings = stat["value"]
                elif stat["name"] == "strikeoutToWalkRatio":
                    strikeout_to_walk_ratio = stat["value"]
                elif stat["name"] == "toughLosses":
                    tough_losses = stat["value"]
                elif stat["name"] == "cheapWins":
                    cheap_wins = stat["value"]
                elif stat["name"] == "saveOpportunitiesPerWin":
                    save_opportunities_per_win = stat["value"]
                elif stat["name"] == "pitchCount":
                    pitch_count = stat["value"]
                elif stat["name"] == "strikes":
                    strikes = stat["value"]
                elif stat["name"] == "strikePitchRatio":
                    strike_pitch_ratio = stat["value"]
                elif stat["name"] == "gamesPlayed":
                    games_played = stat["value"]
                elif stat["name"] == "teamGamesPlayed":
                    team_games_played = stat["value"]
                elif stat["name"] == "doublePlays":
                    double_plays = stat["value"]
                elif stat["name"] == "opportunities":
                    opportunities = stat["value"]
                elif stat["name"] == "errors":
                    errors = stat["value"]
                elif stat["name"] == "passedBalls":
                    passed_balls = stat["value"]
                elif stat["name"] == "assists":
                    assists = stat["value"]
                elif stat["name"] == "outfieldAssists":
                    outfield_assists = stat["value"]
                elif stat["name"] == "pickoffs":
                    pickoffs = stat["value"]
                elif stat["name"] == "putouts":
                    putouts = stat["value"]
                elif stat["name"] == "outsOnField":
                    outs_on_field = stat["value"]
                elif stat["name"] == "triplePlays":
                    triple_plays = stat["value"]
                elif stat["name"] == "ballsInZone":
                    balls_in_zone = stat["value"]
                elif stat["name"] == "extraBases":
                    extra_bases = stat["value"]
                elif stat["name"] == "outsMade":
                    outs_made = stat["value"]
                elif stat["name"] == "catcherThirdInningsPlayed":
                    catcher_third_innings_played = stat["value"]
                elif stat["name"] == "catcherCaughtStealing":
                    catcher_caught_stealing = stat["value"]
                elif stat["name"] == "catcherStolenBasesAllowed":
                    catcher_stolen_bases_allowed = stat["value"]
                elif stat["name"] == "catcherEarnedRuns":
                    catcher_earned_runs = stat["value"]
                elif stat["name"] == "isQualifiedCatcher":
                    is_qualified_catcher = stat["value"]
                elif stat["name"] == "isQualifiedPitcher":
                    is_qualified_pitcher = stat["value"]
                elif stat["name"] == "successfulChances":
                    successful_chances = stat["value"]
                elif stat["name"] == "totalChances":
                    total_chances = stat["value"]
                elif stat["name"] == "fullInningsPlayed":
                    full_innings_played = stat["value"]
                elif stat["name"] == "partInningsPlayed":
                    part_innings_played = stat["value"]
                elif stat["name"] == "fieldingPct":
                    fielding_percentage = stat["value"]
                elif stat["name"] == "rangeFactor":
                    range_factor = stat["value"]
                elif stat["name"] == "zoneRating":
                    zone_rating = stat["value"]
                elif stat["name"] == "catcherCaughtStealingPct":
                    catcher_caught_stealing_percentage = stat["value"]
                elif stat["name"] == "catcherERA":
                    catcher_era = stat["value"]
                elif stat["name"] == "defWARBR":
                    def_warbr = stat["value"]

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
        field_goals=None,
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
        rebounds=rebound_50s,
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
