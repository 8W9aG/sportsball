"""Combined player model."""

# pylint: disable=too-many-locals,too-many-branches,too-many-statements,duplicate-code,too-many-lines
from typing import Any

from ..player_model import VERSION, PlayerModel
from .ffill import ffill
from .most_interesting import more_interesting


def create_combined_player_model(
    player_models: list[PlayerModel],
    identifier: str,
    player_ffill: dict[str, dict[str, Any]],
) -> PlayerModel:
    """Create a player model by combining many player models."""
    jersey = None
    kicks = None
    fumbles = None
    fumbles_lost = None
    field_goals = None
    field_goals_attempted = None
    offensive_rebounds = None
    assists = None
    turnovers = None
    name = None
    marks = None
    handballs = None
    disposals = None
    goals = None
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
    birth_date = None
    species = None
    handicap_weight = None
    father = None
    sex = None
    age = None
    starting_position = None
    weight = None
    birth_address = None
    owner = None
    seconds_played = None
    three_point_field_goals = None
    three_point_field_goals_attempted = None
    free_throws = None
    free_throws_attempted = None
    defensive_rebounds = None
    steals = None
    blocks = None
    personal_fouls = None
    points = None
    game_score = None
    point_differential = None
    height = None
    colleges = None
    headshot = None
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
    passing_yards_at_catch = None
    quarterback_rating = None
    sacks = None
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
    punt_return_yards = None
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
    receiving_touchdowns_49_yards = None
    receiving_touchdowns_above_50_yards = None
    rushing_touchdowns_9_yards = None
    rushing_touchdowns_19_yards = None
    rushing_touchdowns_29_yards = None
    rushing_touchdowns_39_yards = None
    rushing_touchdowns_49_yards = None
    rushing_touchdowns_above_50_yards = None
    penalties_in_minutes = None
    even_strength_goals = None
    power_play_goals = None
    short_handed_goals = None
    game_winning_goals = None
    even_strength_assists = None
    power_play_assists = None
    short_handed_assists = None
    shots_on_goal = None
    shooting_percentage = None
    shifts = None
    time_on_ice = None
    decision = None
    goals_against = None
    shots_against = None
    saves = None
    save_percentage = None
    shutouts = None
    individual_corsi_for_events = None
    on_shot_ice_for_events = None
    on_shot_ice_against_events = None
    corsi_for_percentage = None
    relative_corsi_for_percentage = None
    offensive_zone_starts = None
    defensive_zone_starts = None
    offensive_zone_start_percentage = None
    hits = None
    true_shooting_percentage = None
    at_bats = None
    runs_scored = None
    runs_batted_in = None
    bases_on_balls = None
    strikeouts = None
    plate_appearances = None
    hits_at_bats = None
    obp = None
    slg = None
    ops = None
    pitches = None
    strikes = None
    win_probability_added = None
    average_leverage_index = None
    wpa_plus = None
    wpa_minus = None
    cwpa = None
    acli = None
    re24 = None
    putouts = None
    innings_pitched = None
    earned_runs = None
    home_runs = None
    era = None
    batters_faced = None
    strikes_by_contact = None
    strikes_swinging = None
    strikes_looking = None
    ground_balls = None
    fly_balls = None
    line_drives = None
    inherited_runners = None
    inherited_scores = None
    effective_field_goal_percentage = None
    penalty_kicks_made = None
    penalty_kicks_attempted = None
    shots_total = None
    shots_on_target = None
    yellow_cards = None
    red_cards = None
    touches = None
    expected_goals = None
    non_penalty_expected_goals = None
    expected_assisted_goals = None
    shot_creating_actions = None
    goal_creating_actions = None
    passes_completed = None
    passes_attempted = None
    pass_completion = None
    progressive_passes = None
    carries = None
    progressive_carries = None
    take_ons_attempted = None
    successful_take_ons = None
    total_passing_distance = None
    progressive_passing_distance = None
    passes_completed_short = None
    passes_attempted_short = None
    pass_completion_short = None
    passes_completed_medium = None
    passes_attempted_medium = None
    pass_completion_medium = None
    passes_completed_long = None
    passes_attempted_long = None
    pass_completion_long = None
    expected_assists = None
    key_passes = None
    passes_into_final_third = None
    passes_into_penalty_area = None
    crosses_into_penalty_area = None
    live_ball_passes = None
    dead_ball_passes = None
    passes_from_free_kicks = None
    through_balls = None
    switches = None
    crosses = None
    throw_ins_taken = None
    corner_kicks = None
    inswinging_corner_kicks = None
    outswinging_corner_kicks = None
    straight_corner_kicks = None
    passes_offside = None
    passes_blocked = None
    tackles_won = None
    tackles_in_defensive_third = None
    tackles_in_middle_third = None
    tackles_in_attacking_third = None
    dribblers_tackled = None
    dribbles_challenged = None
    percent_of_dribblers_tackled = None
    challenges_lost = None
    shots_blocked = None
    tackles_plus_interceptions = None
    errors = None
    touches_in_defensive_penalty_area = None
    touches_in_defensive_third = None
    touches_in_middle_third = None
    touches_in_attacking_third = None
    touches_in_attacking_penalty_area = None
    live_ball_touches = None
    successful_take_on_percentage = None
    times_tackled_during_take_ons = None
    tackled_during_take_on_percentage = None
    total_carrying_distance = None
    progressive_carrying_distance = None
    carries_into_final_third = None
    carries_into_penalty_area = None
    miscontrols = None
    dispossessed = None
    passes_received = None
    progressive_passes_received = None
    second_yellow_card = None
    fouls_committed = None
    fouls_drawn = None
    offsides = None
    penalty_kicks_won = None
    penalty_kicks_conceded = None
    own_goals = None
    ball_recoveries = None
    aerials_won = None
    aerials_lost = None
    percentage_of_aerials_won = None
    shots_on_target_against = None
    post_shot_expected_goals = None
    passes_attempted_minus_goal_kicks = None
    throws_attempted = None
    percentage_of_passes_that_were_launched = None
    average_pass_length = None
    goal_kicks_attempted = None
    percentage_of_goal_kicks_that_were_launched = None
    average_goal_kick_length = None
    crosses_faced = None
    crosses_stopped = None
    percentage_crosses_stopped = None
    defensive_actions_outside_penalty_area = None
    average_distance_of_defensive_actions = None
    three_point_attempt_rate = None
    batting_style = None
    bowling_style = None
    playing_roles = None
    runs = None
    balls = None
    fours = None
    sixes = None
    strikerate = None
    fall_of_wicket_order = None
    fall_of_wicket_num = None
    fall_of_wicket_runs = None
    fall_of_wicket_balls = None
    fall_of_wicket_overs = None
    fall_of_wicket_over_number = None
    ball_over_actual = None
    ball_over_unique = None
    ball_total_runs = None
    ball_batsman_runs = None
    overs = None
    maidens = None
    conceded = None
    wickets = None
    economy = None
    runs_per_ball = None
    dots = None
    wides = None
    no_balls = None
    free_throw_attempt_rate = None
    offensive_rebound_percentage = None
    defensive_rebound_percentage = None
    total_rebound_percentage = None
    assist_percentage = None
    steal_percentage = None
    block_percentage = None
    turnover_percentage = None
    usage_percentage = None
    offensive_rating = None
    defensive_rating = None
    box_plus_minus = None
    ace_percentage = None
    double_fault_percentage = None
    first_serves_in = None
    first_serve_percentage = None
    second_serve_percentage = None
    break_points_saved = None
    return_points_won_percentage = None
    winners = None
    winners_fronthand = None
    winners_backhand = None
    unforced_errors = None
    unforced_errors_fronthand = None
    unforced_errors_backhand = None
    serve_points = None
    serves_won = None
    serves_aces = None
    serves_unreturned = None
    serves_forced_error_percentage = None
    serves_won_in_three_shots_or_less = None
    serves_wide_percentage = None
    serves_body_percentage = None
    serves_t_percentage = None
    serves_wide_deuce_percentage = None
    serves_body_deuce_percentage = None
    serves_t_deuce_percentage = None
    serves_wide_ad_percentage = None
    serves_body_ad_percentage = None
    serves_t_ad_percentage = None
    serves_net_percentage = None
    serves_wide_direction_percentage = None
    shots_deep_percentage = None
    shots_deep_wide_percentage = None
    shots_foot_errors_percentage = None
    shots_unknown_percentage = None
    points_won_percentage = None
    centre_clearances = None
    disposal_efficiency = None
    tackles_inside_50 = None
    total_possessions = None
    score_involvements = None
    goal_accuracy = None
    stoppage_clearances = None
    uncontested_marks = None
    accurate_crosses = None
    accurate_long_balls = None
    accurate_passes = None
    accurate_through_balls = None
    cross_percentage = None
    free_kick_goals = None
    free_kick_percentage = None
    free_kick_shots = None
    game_winning_assists = None
    headed_goals = None
    inaccurate_crosses = None
    inaccurate_long_balls = None
    inaccurate_passes = None
    inaccurate_through_balls = None
    left_footed_shots = None
    long_ball_percentage = None
    penalty_kick_goals = None
    penalty_kick_percentage = None
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
    through_ball_percentage = None
    long_balls = None
    total_passes = None
    average_rating_from_editor = None
    average_rating_from_user = None
    did_not_play = None
    draws = None
    goal_difference = None
    losses = None
    lost_corners = None
    minutes = None
    pass_percentage = None
    starts = None
    sub_ins = None
    sub_outs = None
    suspensions = None
    time_ended = None
    time_started = None
    win_percentage = None
    wins = None
    won_corners = None
    clean_sheet = None
    crosses_caught = None
    goals_conceded = None
    partial_clean_sheet = None
    penalty_kick_conceded = None
    penalty_kick_save_percentage = None
    penalty_kicks_faced = None
    penalty_kicks_saved = None
    punches = None
    shoot_out_kicks_faced = None
    shoot_out_kicks_saved = None
    shoot_out_save_percentage = None
    shots_faced = None
    smothers = None
    unclaimed_crosses = None
    effective_clearances = None
    effective_tackles = None
    ineffective_tackles = None
    tackle_percentage = None
    appearances = None
    average_rating_from_correspondent = None
    average_rating_from_data_feed = None
    games_played = None
    team_games_played = None
    hit_by_pitch = None
    rbis = None
    sac_hits = None
    stolen_bases = None
    walks = None
    catcher_interference = None
    gidps = None
    sac_flies = None
    grand_slam_home_runs = None
    runners_left_on_base = None
    triples = None
    game_winning_rbis = None
    intentional_walks = None
    doubles = None
    caught_stealing = None
    games_started = None
    pinch_at_bats = None
    pinch_hits = None
    player_rating = None
    is_qualified = None
    is_qualified_steals = None
    total_bases = None
    projected_home_runs = None
    extra_base_hits = None
    runs_created = None
    batting_average = None
    pinch_average = None
    slug_average = None
    secondary_average = None
    on_base_percentage = None
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
    batters_hit = None
    sacrifice_bunts = None
    save_opportunities = None
    finishes = None
    balks = None
    holds = None
    complete_games = None
    perfect_games = None
    wild_pitches = None
    third_innings = None
    team_earned_runs = None
    pickoff_attempts = None
    run_support = None
    pitches_as_starter = None
    average_game_score = None
    quality_starts = None
    inherited_runners_scored = None
    opponent_total_bases = None
    is_qualified_saves = None
    full_innings = None
    part_innings = None
    blown_saves = None
    innings = None
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
    passed_balls = None
    outfield_assists = None
    pickoffs = None
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
    for player_model in player_models:
        jersey = more_interesting(jersey, player_model.jersey)
        kicks = more_interesting(kicks, player_model.kicks)
        fumbles = more_interesting(fumbles, player_model.fumbles)
        fumbles_lost = more_interesting(fumbles_lost, player_model.fumbles_lost)
        field_goals = more_interesting(field_goals, player_model.field_goals)
        field_goals_attempted = more_interesting(
            field_goals_attempted, player_model.field_goals_attempted
        )
        offensive_rebounds = more_interesting(
            offensive_rebounds, player_model.offensive_rebounds
        )
        assists = more_interesting(assists, player_model.assists)
        turnovers = more_interesting(turnovers, player_model.turnovers)
        name = more_interesting(name, player_model.name)
        marks = more_interesting(marks, player_model.marks)
        handballs = more_interesting(handballs, player_model.handballs)
        disposals = more_interesting(disposals, player_model.disposals)
        goals = more_interesting(goals, player_model.goals)
        behinds = more_interesting(behinds, player_model.behinds)
        hit_outs = more_interesting(hit_outs, player_model.hit_outs)
        tackles = more_interesting(tackles, player_model.tackles)
        rebounds = more_interesting(rebounds, player_model.rebounds)
        insides = more_interesting(insides, player_model.insides)
        clearances = more_interesting(clearances, player_model.clearances)
        clangers = more_interesting(clangers, player_model.clangers)
        free_kicks_for = more_interesting(free_kicks_for, player_model.free_kicks_for)
        free_kicks_against = more_interesting(
            free_kicks_against, player_model.free_kicks_against
        )
        brownlow_votes = more_interesting(brownlow_votes, player_model.brownlow_votes)
        contested_possessions = more_interesting(
            contested_possessions, player_model.contested_possessions
        )
        uncontested_possessions = more_interesting(
            uncontested_possessions, player_model.uncontested_possessions
        )
        contested_marks = more_interesting(
            contested_marks, player_model.contested_marks
        )
        marks_inside = more_interesting(marks_inside, player_model.marks_inside)
        one_percenters = more_interesting(one_percenters, player_model.one_percenters)
        bounces = more_interesting(bounces, player_model.bounces)
        goal_assists = more_interesting(goal_assists, player_model.goal_assists)
        percentage_played = more_interesting(
            percentage_played, player_model.percentage_played
        )
        birth_date = more_interesting(birth_date, player_model.birth_date)
        species = more_interesting(species, player_model.species)
        handicap_weight = more_interesting(
            handicap_weight, player_model.handicap_weight
        )
        father = more_interesting(father, player_model.father)
        sex = more_interesting(sex, player_model.sex)
        age = more_interesting(age, player_model.age)
        starting_position = more_interesting(
            starting_position, player_model.starting_position
        )
        weight = more_interesting(weight, player_model.weight)
        birth_address = more_interesting(birth_address, player_model.birth_address)
        owner = more_interesting(owner, player_model.owner)
        seconds_played = more_interesting(seconds_played, player_model.seconds_played)
        three_point_field_goals = more_interesting(
            three_point_field_goals, player_model.three_point_field_goals
        )
        three_point_field_goals_attempted = more_interesting(
            three_point_field_goals_attempted,
            player_model.three_point_field_goals_attempted,
        )
        free_throws = more_interesting(free_throws, player_model.free_throws)
        free_throws_attempted = more_interesting(
            free_throws_attempted, player_model.free_throws_attempted
        )
        defensive_rebounds = more_interesting(
            defensive_rebounds, player_model.defensive_rebounds
        )
        steals = more_interesting(steals, player_model.steals)
        blocks = more_interesting(blocks, player_model.blocks)
        personal_fouls = more_interesting(personal_fouls, player_model.personal_fouls)
        points = more_interesting(points, player_model.points)
        game_score = more_interesting(game_score, player_model.game_score)
        point_differential = more_interesting(
            point_differential, player_model.point_differential
        )
        height = more_interesting(height, player_model.height)
        colleges = more_interesting(colleges, player_model.colleges)
        headshot = more_interesting(headshot, player_model.headshot)
        forced_fumbles = more_interesting(forced_fumbles, player_model.forced_fumbles)
        fumbles_recovered = more_interesting(
            fumbles_recovered, player_model.fumbles_recovered
        )
        fumbles_recovered_yards = more_interesting(
            fumbles_recovered_yards, player_model.fumbles_recovered_yards
        )
        fumbles_touchdowns = more_interesting(
            fumbles_touchdowns, player_model.fumbles_touchdowns
        )
        offensive_two_point_returns = more_interesting(
            offensive_two_point_returns, player_model.offensive_two_point_returns
        )
        offensive_fumbles_touchdowns = more_interesting(
            offensive_fumbles_touchdowns, player_model.offensive_fumbles_touchdowns
        )
        defensive_fumbles_touchdowns = more_interesting(
            defensive_fumbles_touchdowns, player_model.defensive_fumbles_touchdowns
        )
        average_gain = more_interesting(average_gain, player_model.average_gain)
        completion_percentage = more_interesting(
            completion_percentage, player_model.completion_percentage
        )
        completions = more_interesting(completions, player_model.completions)
        espn_quarterback_rating = more_interesting(
            espn_quarterback_rating, player_model.espn_quarterback_rating
        )
        interception_percentage = more_interesting(
            interception_percentage, player_model.interception_percentage
        )
        interceptions = more_interesting(interceptions, player_model.interceptions)
        long_passing = more_interesting(long_passing, player_model.long_passing)
        misc_yards = more_interesting(misc_yards, player_model.misc_yards)
        net_passing_yards = more_interesting(
            net_passing_yards, player_model.net_passing_yards
        )
        net_total_yards = more_interesting(
            net_total_yards, player_model.net_total_yards
        )
        passing_attempts = more_interesting(
            passing_attempts, player_model.passing_attempts
        )
        passing_big_plays = more_interesting(
            passing_big_plays, player_model.passing_big_plays
        )
        passing_first_downs = more_interesting(
            passing_first_downs, player_model.passing_first_downs
        )
        passing_fumbles = more_interesting(
            passing_fumbles, player_model.passing_fumbles
        )
        passing_fumbles_lost = more_interesting(
            passing_fumbles_lost, player_model.passing_fumbles_lost
        )
        passing_touchdown_percentage = more_interesting(
            passing_touchdown_percentage, player_model.passing_touchdown_percentage
        )
        passing_touchdowns = more_interesting(
            passing_touchdowns, player_model.passing_touchdowns
        )
        passing_yards = more_interesting(passing_yards, player_model.passing_yards)
        passing_yards_after_catch = more_interesting(
            passing_yards_after_catch, player_model.passing_yards_after_catch
        )
        passing_yards_at_catch = more_interesting(
            passing_yards_at_catch, player_model.passing_yards_at_catch
        )
        quarterback_rating = more_interesting(
            quarterback_rating, player_model.quarterback_rating
        )
        sacks = more_interesting(sacks, player_model.sacks)
        sacks_yards_lost = more_interesting(
            sacks_yards_lost, player_model.sacks_yards_lost
        )
        net_passing_attempts = more_interesting(
            net_passing_attempts, player_model.net_passing_attempts
        )
        total_offensive_plays = more_interesting(
            total_offensive_plays, player_model.total_offensive_plays
        )
        total_points = more_interesting(total_points, player_model.total_points)
        total_touchdowns = more_interesting(
            total_touchdowns, player_model.total_touchdowns
        )
        total_yards = more_interesting(total_yards, player_model.total_yards)
        total_yards_from_scrimmage = more_interesting(
            total_yards_from_scrimmage, player_model.total_yards_from_scrimmage
        )
        two_point_pass = more_interesting(two_point_pass, player_model.two_point_pass)
        two_point_pass_attempt = more_interesting(
            two_point_pass_attempt, player_model.two_point_pass_attempt
        )
        yards_per_completion = more_interesting(
            yards_per_completion, player_model.yards_per_completion
        )
        yards_per_pass_attempt = more_interesting(
            yards_per_pass_attempt, player_model.yards_per_pass_attempt
        )
        net_yards_per_pass_attempt = more_interesting(
            net_yards_per_pass_attempt, player_model.net_yards_per_pass_attempt
        )
        long_rushing = more_interesting(long_rushing, player_model.long_rushing)
        rushing_attempts = more_interesting(
            rushing_attempts, player_model.rushing_attempts
        )
        rushing_big_plays = more_interesting(
            rushing_big_plays, player_model.rushing_big_plays
        )
        rushing_first_downs = more_interesting(
            rushing_first_downs, player_model.rushing_first_downs
        )
        rushing_fumbles = more_interesting(
            rushing_fumbles, player_model.rushing_fumbles
        )
        rushing_fumbles_lost = more_interesting(
            rushing_fumbles_lost, player_model.rushing_fumbles_lost
        )
        rushing_touchdowns = more_interesting(
            rushing_touchdowns, player_model.rushing_touchdowns
        )
        rushing_yards = more_interesting(rushing_yards, player_model.rushing_yards)
        stuffs = more_interesting(stuffs, player_model.stuffs)
        stuff_yards_lost = more_interesting(
            stuff_yards_lost, player_model.stuff_yards_lost
        )
        two_point_rush = more_interesting(two_point_rush, player_model.two_point_rush)
        two_point_rush_attempts = more_interesting(
            two_point_rush_attempts, player_model.two_point_rush_attempts
        )
        yards_per_rush_attempt = more_interesting(
            yards_per_rush_attempt, player_model.yards_per_rush_attempt
        )
        espn_widereceiver = more_interesting(
            espn_widereceiver, player_model.espn_widereceiver
        )
        long_reception = more_interesting(long_reception, player_model.long_reception)
        receiving_big_plays = more_interesting(
            receiving_big_plays, player_model.receiving_big_plays
        )
        receiving_first_downs = more_interesting(
            receiving_first_downs, player_model.receiving_first_downs
        )
        receiving_fumbles = more_interesting(
            receiving_fumbles, player_model.receiving_fumbles
        )
        receiving_fumbles_lost = more_interesting(
            receiving_fumbles_lost, player_model.receiving_fumbles_lost
        )
        receiving_targets = more_interesting(
            receiving_targets, player_model.receiving_targets
        )
        receiving_touchdowns = more_interesting(
            receiving_touchdowns, player_model.receiving_touchdowns
        )
        receiving_yards = more_interesting(
            receiving_yards, player_model.receiving_yards
        )
        receiving_yards_after_catch = more_interesting(
            receiving_yards_after_catch, player_model.receiving_yards_after_catch
        )
        receiving_yards_at_catch = more_interesting(
            receiving_yards_at_catch, player_model.receiving_yards_at_catch
        )
        receptions = more_interesting(receptions, player_model.receptions)
        two_point_receptions = more_interesting(
            two_point_receptions, player_model.two_point_receptions
        )
        two_point_reception_attempts = more_interesting(
            two_point_reception_attempts, player_model.two_point_reception_attempts
        )
        yards_per_reception = more_interesting(
            yards_per_reception, player_model.yards_per_reception
        )
        assist_tackles = more_interesting(assist_tackles, player_model.assist_tackles)
        average_interception_yards = more_interesting(
            average_interception_yards, player_model.average_interception_yards
        )
        average_sack_yards = more_interesting(
            average_sack_yards, player_model.average_sack_yards
        )
        average_stuff_yards = more_interesting(
            average_stuff_yards, player_model.average_stuff_yards
        )
        blocked_field_goal_touchdowns = more_interesting(
            blocked_field_goal_touchdowns, player_model.blocked_field_goal_touchdowns
        )
        blocked_punt_touchdowns = more_interesting(
            blocked_punt_touchdowns, player_model.blocked_punt_touchdowns
        )
        defensive_touchdowns = more_interesting(
            defensive_touchdowns, player_model.defensive_touchdowns
        )
        hurries = more_interesting(hurries, player_model.hurries)
        kicks_blocked = more_interesting(kicks_blocked, player_model.kicks_blocked)
        long_interception = more_interesting(
            long_interception, player_model.long_interception
        )
        misc_touchdowns = more_interesting(
            misc_touchdowns, player_model.misc_touchdowns
        )
        passes_batted_down = more_interesting(
            passes_batted_down, player_model.passes_batted_down
        )
        passes_defended = more_interesting(
            passes_defended, player_model.passes_defended
        )
        quarterback_hits = more_interesting(
            quarterback_hits, player_model.quarterback_hits
        )
        sacks_assisted = more_interesting(sacks_assisted, player_model.sacks_assisted)
        sacks_unassisted = more_interesting(
            sacks_unassisted, player_model.sacks_unassisted
        )
        sacks_yards = more_interesting(sacks_yards, player_model.sacks_yards)
        safeties = more_interesting(safeties, player_model.safeties)
        solo_tackles = more_interesting(solo_tackles, player_model.solo_tackles)
        stuff_yards = more_interesting(stuff_yards, player_model.stuff_yards)
        tackles_for_loss = more_interesting(
            tackles_for_loss, player_model.tackles_for_loss
        )
        tackles_yards_lost = more_interesting(
            tackles_yards_lost, player_model.tackles_yards_lost
        )
        yards_allowed = more_interesting(yards_allowed, player_model.yards_allowed)
        points_allowed = more_interesting(points_allowed, player_model.points_allowed)
        one_point_safeties_made = more_interesting(
            one_point_safeties_made, player_model.one_point_safeties_made
        )
        missed_field_goal_return_td = more_interesting(
            missed_field_goal_return_td, player_model.missed_field_goal_return_td
        )
        blocked_punt_ez_rec_td = more_interesting(
            blocked_punt_ez_rec_td, player_model.blocked_punt_ez_rec_td
        )
        interception_touchdowns = more_interesting(
            interception_touchdowns, player_model.interception_touchdowns
        )
        interception_yards = more_interesting(
            interception_yards, player_model.interception_yards
        )
        average_kickoff_return_yards = more_interesting(
            average_kickoff_return_yards, player_model.average_kickoff_return_yards
        )
        average_kickoff_yards = more_interesting(
            average_kickoff_yards, player_model.average_kickoff_yards
        )
        extra_point_attempts = more_interesting(
            extra_point_attempts, player_model.extra_point_attempts
        )
        extra_point_percentage = more_interesting(
            extra_point_percentage, player_model.extra_point_percentage
        )
        extra_point_blocked = more_interesting(
            extra_point_blocked, player_model.extra_point_blocked
        )
        extra_points_blocked_percentage = more_interesting(
            extra_points_blocked_percentage,
            player_model.extra_points_blocked_percentage,
        )
        extra_points_made = more_interesting(
            extra_points_made, player_model.extra_points_made
        )
        fair_catches = more_interesting(fair_catches, player_model.fair_catches)
        fair_catch_percentage = more_interesting(
            fair_catch_percentage, player_model.fair_catch_percentage
        )
        field_goal_attempts_max_19_yards = more_interesting(
            field_goal_attempts_max_19_yards,
            player_model.field_goal_attempts_max_19_yards,
        )
        field_goal_attempts_max_29_yards = more_interesting(
            field_goal_attempts_max_29_yards,
            player_model.field_goal_attempts_max_29_yards,
        )
        field_goal_attempts_max_39_yards = more_interesting(
            field_goal_attempts_max_39_yards,
            player_model.field_goal_attempts_max_39_yards,
        )
        field_goal_attempts_max_49_yards = more_interesting(
            field_goal_attempts_max_49_yards,
            player_model.field_goal_attempts_max_49_yards,
        )
        field_goal_attempts_max_59_yards = more_interesting(
            field_goal_attempts_max_59_yards,
            player_model.field_goal_attempts_max_59_yards,
        )
        field_goal_attempts_max_99_yards = more_interesting(
            field_goal_attempts_max_99_yards,
            player_model.field_goal_attempts_max_99_yards,
        )
        field_goal_attempts_above_50_yards = more_interesting(
            field_goal_attempts_above_50_yards,
            player_model.field_goal_attempts_above_50_yards,
        )
        field_goal_attempt_yards = more_interesting(
            field_goal_attempt_yards, player_model.field_goal_attempt_yards
        )
        field_goals_blocked = more_interesting(
            field_goals_blocked, player_model.field_goals_blocked
        )
        field_goals_blocked_percentage = more_interesting(
            field_goals_blocked_percentage, player_model.field_goals_blocked_percentage
        )
        field_goals_made = more_interesting(
            field_goals_made, player_model.field_goals_made
        )
        field_goals_made_max_19_yards = more_interesting(
            field_goals_made_max_19_yards, player_model.field_goals_made_max_19_yards
        )
        field_goals_made_max_29_yards = more_interesting(
            field_goals_made_max_29_yards, player_model.field_goals_made_max_29_yards
        )
        field_goals_made_max_39_yards = more_interesting(
            field_goals_made_max_39_yards, player_model.field_goals_made_max_39_yards
        )
        field_goals_made_max_49_yards = more_interesting(
            field_goals_made_max_49_yards, player_model.field_goals_made_max_49_yards
        )
        field_goals_made_max_59_yards = more_interesting(
            field_goals_made_max_59_yards, player_model.field_goals_made_max_59_yards
        )
        field_goals_made_max_99_yards = more_interesting(
            field_goals_made_max_99_yards, player_model.field_goals_made_max_99_yards
        )
        field_goals_made_above_50_yards = more_interesting(
            field_goals_made_above_50_yards,
            player_model.field_goals_made_above_50_yards,
        )
        field_goals_made_yards = more_interesting(
            field_goals_made_yards, player_model.field_goals_made_yards
        )
        field_goals_missed_yards = more_interesting(
            field_goals_missed_yards, player_model.field_goals_missed_yards
        )
        kickoff_out_of_bounds = more_interesting(
            kickoff_out_of_bounds, player_model.kickoff_out_of_bounds
        )
        kickoff_returns = more_interesting(
            kickoff_returns, player_model.kickoff_returns
        )
        kickoff_returns_touchdowns = more_interesting(
            kickoff_returns_touchdowns, player_model.kickoff_returns_touchdowns
        )
        kickoff_return_yards = more_interesting(
            kickoff_return_yards, player_model.kickoff_return_yards
        )
        kickoffs = more_interesting(kickoffs, player_model.kickoffs)
        kickoff_yards = more_interesting(kickoff_yards, player_model.kickoff_yards)
        long_field_goal_attempt = more_interesting(
            long_field_goal_attempt, player_model.long_field_goal_attempt
        )
        long_field_goal_made = more_interesting(
            long_field_goal_made, player_model.long_field_goal_made
        )
        long_kickoff = more_interesting(long_kickoff, player_model.long_kickoff)
        total_kicking_points = more_interesting(
            total_kicking_points, player_model.total_kicking_points
        )
        touchback_percentage = more_interesting(
            touchback_percentage, player_model.touchback_percentage
        )
        touchbacks = more_interesting(touchbacks, player_model.touchbacks)
        defensive_fumble_returns = more_interesting(
            defensive_fumble_returns, player_model.defensive_fumble_returns
        )
        defensive_fumble_return_yards = more_interesting(
            defensive_fumble_return_yards, player_model.defensive_fumble_return_yards
        )
        fumble_recoveries = more_interesting(
            fumble_recoveries, player_model.fumble_recoveries
        )
        fumble_recovery_yards = more_interesting(
            fumble_recovery_yards, player_model.fumble_recovery_yards
        )
        kick_return_fair_catches = more_interesting(
            kick_return_fair_catches, player_model.kick_return_fair_catches
        )
        kick_return_fair_catch_percentage = more_interesting(
            kick_return_fair_catch_percentage,
            player_model.kick_return_fair_catch_percentage,
        )
        kick_return_fumbles = more_interesting(
            kick_return_fumbles, player_model.kick_return_fumbles
        )
        kick_return_fumbles_lost = more_interesting(
            kick_return_fumbles_lost, player_model.kick_return_fumbles_lost
        )
        kick_returns = more_interesting(kick_returns, player_model.kick_returns)
        kick_return_touchdowns = more_interesting(
            kick_return_touchdowns, player_model.kick_return_touchdowns
        )
        kick_return_yards = more_interesting(
            kick_return_yards, player_model.kick_return_yards
        )
        long_kick_return = more_interesting(
            long_kick_return, player_model.long_kick_return
        )
        long_punt_return = more_interesting(
            long_punt_return, player_model.long_punt_return
        )
        misc_fumble_returns = more_interesting(
            misc_fumble_returns, player_model.misc_fumble_returns
        )
        misc_fumble_return_yards = more_interesting(
            misc_fumble_return_yards, player_model.misc_fumble_return_yards
        )
        opposition_fumble_recoveries = more_interesting(
            opposition_fumble_recoveries, player_model.opposition_fumble_recoveries
        )
        opposition_fumble_recovery_yards = more_interesting(
            opposition_fumble_recovery_yards,
            player_model.opposition_fumble_recovery_yards,
        )
        opposition_special_team_fumble_returns = more_interesting(
            opposition_special_team_fumble_returns,
            player_model.opposition_special_team_fumble_returns,
        )
        opposition_special_team_fumble_return_yards = more_interesting(
            opposition_special_team_fumble_return_yards,
            player_model.opposition_special_team_fumble_return_yards,
        )
        punt_return_fair_catches = more_interesting(
            punt_return_fair_catches, player_model.punt_return_fair_catches
        )
        punt_return_fair_catch_percentage = more_interesting(
            punt_return_fair_catch_percentage,
            player_model.punt_return_fair_catch_percentage,
        )
        punt_return_fumbles = more_interesting(
            punt_return_fumbles, player_model.punt_return_fumbles
        )
        punt_return_fumbles_lost = more_interesting(
            punt_return_fumbles_lost, player_model.punt_return_fumbles_lost
        )
        punt_returns = more_interesting(punt_returns, player_model.punt_returns)
        punt_returns_started_inside_the_10 = more_interesting(
            punt_returns_started_inside_the_10,
            player_model.punt_returns_started_inside_the_10,
        )
        punt_returns_started_inside_the_20 = more_interesting(
            punt_returns_started_inside_the_20,
            player_model.punt_returns_started_inside_the_20,
        )
        punt_return_touchdowns = more_interesting(
            punt_return_touchdowns, player_model.punt_return_touchdowns
        )
        punt_return_yards = more_interesting(
            punt_return_yards, player_model.punt_return_yards
        )
        special_team_fumble_returns = more_interesting(
            special_team_fumble_returns, player_model.special_team_fumble_returns
        )
        yards_per_kick_return = more_interesting(
            yards_per_kick_return, player_model.yards_per_kick_return
        )
        yards_per_punt_return = more_interesting(
            yards_per_punt_return, player_model.yards_per_punt_return
        )
        yards_per_return = more_interesting(
            yards_per_return, player_model.yards_per_return
        )
        average_punt_return_yards = more_interesting(
            average_punt_return_yards, player_model.average_punt_return_yards
        )
        gross_average_punt_yards = more_interesting(
            gross_average_punt_yards, player_model.gross_average_punt_yards
        )
        long_punt = more_interesting(long_punt, player_model.long_punt)
        net_average_punt_yards = more_interesting(
            net_average_punt_yards, player_model.net_average_punt_yards
        )
        punts = more_interesting(punts, player_model.punts)
        punts_blocked = more_interesting(punts_blocked, player_model.punts_blocked)
        punts_blocked_percentage = more_interesting(
            punts_blocked_percentage, player_model.punts_blocked_percentage
        )
        punts_inside_10 = more_interesting(
            punts_inside_10, player_model.punts_inside_10
        )
        punts_inside_10_percentage = more_interesting(
            punts_inside_10_percentage, player_model.punts_inside_10_percentage
        )
        punts_inside_20 = more_interesting(
            punts_inside_20, player_model.punts_inside_20
        )
        punts_inside_20_percentage = more_interesting(
            punts_inside_20_percentage, player_model.punts_inside_20_percentage
        )
        punts_over_50 = more_interesting(punts_over_50, player_model.punts_over_50)
        punt_yards = more_interesting(punt_yards, player_model.punt_yards)
        defensive_points = more_interesting(
            defensive_points, player_model.defensive_points
        )
        misc_points = more_interesting(misc_points, player_model.misc_points)
        return_touchdowns = more_interesting(
            return_touchdowns, player_model.return_touchdowns
        )
        total_two_point_conversions = more_interesting(
            total_two_point_conversions, player_model.total_two_point_conversions
        )
        passing_touchdowns_9_yards = more_interesting(
            passing_touchdowns_9_yards, player_model.passing_touchdowns_9_yards
        )
        passing_touchdowns_19_yards = more_interesting(
            passing_touchdowns_19_yards, player_model.passing_touchdowns_19_yards
        )
        passing_touchdowns_29_yards = more_interesting(
            passing_touchdowns_29_yards, player_model.passing_touchdowns_29_yards
        )
        passing_touchdowns_39_yards = more_interesting(
            passing_touchdowns_39_yards, player_model.passing_touchdowns_39_yards
        )
        passing_touchdowns_49_yards = more_interesting(
            passing_touchdowns_49_yards, player_model.passing_touchdowns_49_yards
        )
        passing_touchdowns_above_50_yards = more_interesting(
            passing_touchdowns_above_50_yards,
            player_model.passing_touchdowns_above_50_yards,
        )
        receiving_touchdowns_9_yards = more_interesting(
            receiving_touchdowns_9_yards, player_model.receiving_touchdowns_9_yards
        )
        receiving_touchdowns_19_yards = more_interesting(
            receiving_touchdowns_19_yards, player_model.receiving_touchdowns_19_yards
        )
        receiving_touchdowns_29_yards = more_interesting(
            receiving_touchdowns_29_yards, player_model.receiving_touchdowns_29_yards
        )
        receiving_touchdowns_39_yards = more_interesting(
            receiving_touchdowns_39_yards, player_model.receiving_touchdowns_39_yards
        )
        receiving_touchdowns_49_yards = more_interesting(
            receiving_touchdowns_49_yards, player_model.receiving_touchdowns_49_yards
        )
        receiving_touchdowns_above_50_yards = more_interesting(
            receiving_touchdowns_above_50_yards,
            player_model.receiving_touchdowns_above_50_yards,
        )
        rushing_touchdowns_9_yards = more_interesting(
            rushing_touchdowns_9_yards, player_model.rushing_touchdowns_9_yards
        )
        rushing_touchdowns_19_yards = more_interesting(
            rushing_touchdowns_19_yards, player_model.rushing_touchdowns_19_yards
        )
        rushing_touchdowns_29_yards = more_interesting(
            rushing_touchdowns_29_yards, player_model.rushing_touchdowns_29_yards
        )
        rushing_touchdowns_39_yards = more_interesting(
            rushing_touchdowns_39_yards, player_model.rushing_touchdowns_39_yards
        )
        rushing_touchdowns_49_yards = more_interesting(
            rushing_touchdowns_49_yards, player_model.rushing_touchdowns_49_yards
        )
        rushing_touchdowns_above_50_yards = more_interesting(
            rushing_touchdowns_above_50_yards,
            player_model.rushing_touchdowns_above_50_yards,
        )
        penalties_in_minutes = more_interesting(
            penalties_in_minutes, player_model.penalties_in_minutes
        )
        even_strength_goals = more_interesting(
            even_strength_goals, player_model.even_strength_goals
        )
        power_play_goals = more_interesting(
            power_play_goals, player_model.power_play_goals
        )
        short_handed_goals = more_interesting(
            short_handed_goals, player_model.short_handed_goals
        )
        game_winning_goals = more_interesting(
            game_winning_goals, player_model.game_winning_goals
        )
        even_strength_assists = more_interesting(
            even_strength_assists, player_model.even_strength_assists
        )
        power_play_assists = more_interesting(
            power_play_assists, player_model.power_play_assists
        )
        short_handed_assists = more_interesting(
            short_handed_assists, player_model.short_handed_assists
        )
        shots_on_goal = more_interesting(shots_on_goal, player_model.shots_on_goal)
        shooting_percentage = more_interesting(
            shooting_percentage, player_model.shooting_percentage
        )
        shifts = more_interesting(shifts, player_model.shifts)
        time_on_ice = more_interesting(time_on_ice, player_model.time_on_ice)
        decision = more_interesting(decision, player_model.decision)
        goals_against = more_interesting(goals_against, player_model.goals_against)
        shots_against = more_interesting(shots_against, player_model.shots_against)
        saves = more_interesting(saves, player_model.saves)
        save_percentage = more_interesting(
            save_percentage, player_model.save_percentage
        )
        shutouts = more_interesting(shutouts, player_model.shutouts)
        individual_corsi_for_events = more_interesting(
            individual_corsi_for_events, player_model.individual_corsi_for_events
        )
        on_shot_ice_for_events = more_interesting(
            on_shot_ice_for_events, player_model.on_shot_ice_for_events
        )
        on_shot_ice_against_events = more_interesting(
            on_shot_ice_against_events, player_model.on_shot_ice_against_events
        )
        corsi_for_percentage = more_interesting(
            corsi_for_percentage, player_model.corsi_for_percentage
        )
        relative_corsi_for_percentage = more_interesting(
            relative_corsi_for_percentage, player_model.relative_corsi_for_percentage
        )
        offensive_zone_starts = more_interesting(
            offensive_zone_starts, player_model.offensive_zone_starts
        )
        defensive_zone_starts = more_interesting(
            defensive_zone_starts, player_model.defensive_zone_starts
        )
        offensive_zone_start_percentage = more_interesting(
            offensive_zone_start_percentage,
            player_model.offensive_zone_start_percentage,
        )
        hits = more_interesting(hits, player_model.hits)
        true_shooting_percentage = more_interesting(
            true_shooting_percentage, player_model.true_shooting_percentage
        )
        at_bats = more_interesting(at_bats, player_model.at_bats)
        runs_scored = more_interesting(runs_scored, player_model.runs_scored)
        runs_batted_in = more_interesting(runs_batted_in, player_model.runs_batted_in)
        bases_on_balls = more_interesting(bases_on_balls, player_model.bases_on_balls)
        strikeouts = more_interesting(strikeouts, player_model.strikeouts)
        plate_appearances = more_interesting(
            plate_appearances, player_model.plate_appearances
        )
        hits_at_bats = more_interesting(hits_at_bats, player_model.hits_at_bats)
        obp = more_interesting(obp, player_model.obp)
        slg = more_interesting(slg, player_model.slg)
        ops = more_interesting(ops, player_model.ops)
        pitches = more_interesting(pitches, player_model.pitches)
        strikes = more_interesting(strikes, player_model.strikes)
        win_probability_added = more_interesting(
            win_probability_added, player_model.win_probability_added
        )
        average_leverage_index = more_interesting(
            average_leverage_index, player_model.average_leverage_index
        )
        wpa_plus = more_interesting(wpa_plus, player_model.wpa_plus)
        wpa_minus = more_interesting(wpa_minus, player_model.wpa_minus)
        cwpa = more_interesting(cwpa, player_model.cwpa)
        acli = more_interesting(acli, player_model.acli)
        re24 = more_interesting(re24, player_model.re24)
        putouts = more_interesting(putouts, player_model.putouts)
        innings_pitched = more_interesting(
            innings_pitched, player_model.innings_pitched
        )
        earned_runs = more_interesting(earned_runs, player_model.earned_runs)
        home_runs = more_interesting(home_runs, player_model.home_runs)
        era = more_interesting(era, player_model.era)
        batters_faced = more_interesting(batters_faced, player_model.batters_faced)
        strikes_by_contact = more_interesting(
            strikes_by_contact, player_model.strikes_by_contact
        )
        strikes_swinging = more_interesting(
            strikes_swinging, player_model.strikes_swinging
        )
        strikes_looking = more_interesting(
            strikes_looking, player_model.strikes_looking
        )
        ground_balls = more_interesting(ground_balls, player_model.ground_balls)
        fly_balls = more_interesting(fly_balls, player_model.fly_balls)
        line_drives = more_interesting(line_drives, player_model.line_drives)
        inherited_runners = more_interesting(
            inherited_runners, player_model.inherited_runners
        )
        inherited_scores = more_interesting(
            inherited_scores, player_model.inherited_scores
        )
        effective_field_goal_percentage = more_interesting(
            effective_field_goal_percentage,
            player_model.effective_field_goal_percentage,
        )
        penalty_kicks_made = more_interesting(
            penalty_kicks_made, player_model.penalty_kicks_made
        )
        penalty_kicks_attempted = more_interesting(
            penalty_kicks_attempted, player_model.penalty_kicks_attempted
        )
        shots_total = more_interesting(shots_total, player_model.shots_total)
        shots_on_target = more_interesting(
            shots_on_target, player_model.shots_on_target
        )
        yellow_cards = more_interesting(yellow_cards, player_model.yellow_cards)
        red_cards = more_interesting(red_cards, player_model.red_cards)
        touches = more_interesting(touches, player_model.touches)
        expected_goals = more_interesting(expected_goals, player_model.expected_goals)
        non_penalty_expected_goals = more_interesting(
            non_penalty_expected_goals, player_model.non_penalty_expected_goals
        )
        expected_assisted_goals = more_interesting(
            expected_assisted_goals, player_model.expected_assisted_goals
        )
        shot_creating_actions = more_interesting(
            shot_creating_actions, player_model.shot_creating_actions
        )
        goal_creating_actions = more_interesting(
            goal_creating_actions, player_model.goal_creating_actions
        )
        passes_completed = more_interesting(
            passes_completed, player_model.passes_completed
        )
        passes_attempted = more_interesting(
            passes_attempted, player_model.passes_attempted
        )
        pass_completion = more_interesting(
            pass_completion, player_model.pass_completion
        )
        progressive_passes = more_interesting(
            progressive_passes, player_model.progressive_passes
        )
        carries = more_interesting(carries, player_model.carries)
        progressive_carries = more_interesting(
            progressive_carries, player_model.progressive_carries
        )
        take_ons_attempted = more_interesting(
            take_ons_attempted, player_model.take_ons_attempted
        )
        successful_take_ons = more_interesting(
            successful_take_ons, player_model.successful_take_ons
        )
        total_passing_distance = more_interesting(
            total_passing_distance, player_model.total_passing_distance
        )
        progressive_passing_distance = more_interesting(
            progressive_passing_distance, player_model.progressive_passing_distance
        )
        passes_completed_short = more_interesting(
            passes_completed_short, player_model.passes_completed_short
        )
        passes_attempted_short = more_interesting(
            passes_attempted_short, player_model.passes_attempted_short
        )
        pass_completion_short = more_interesting(
            pass_completion_short, player_model.pass_completion_short
        )
        passes_completed_medium = more_interesting(
            passes_completed_medium, player_model.passes_completed_medium
        )
        passes_attempted_medium = more_interesting(
            passes_attempted_medium, player_model.passes_attempted_medium
        )
        pass_completion_medium = more_interesting(
            pass_completion_medium, player_model.pass_completion_medium
        )
        passes_completed_long = more_interesting(
            passes_completed_long, player_model.passes_completed_long
        )
        passes_attempted_long = more_interesting(
            passes_attempted_long, player_model.passes_attempted_long
        )
        pass_completion_long = more_interesting(
            pass_completion_long, player_model.pass_completion_long
        )
        expected_assists = more_interesting(
            expected_assists, player_model.expected_assists
        )
        key_passes = more_interesting(key_passes, player_model.key_passes)
        passes_into_final_third = more_interesting(
            passes_into_final_third, player_model.passes_into_final_third
        )
        passes_into_penalty_area = more_interesting(
            passes_into_penalty_area, player_model.passes_into_penalty_area
        )
        crosses_into_penalty_area = more_interesting(
            crosses_into_penalty_area, player_model.crosses_into_penalty_area
        )
        live_ball_passes = more_interesting(
            live_ball_passes, player_model.live_ball_passes
        )
        dead_ball_passes = more_interesting(
            dead_ball_passes, player_model.dead_ball_passes
        )
        passes_from_free_kicks = more_interesting(
            passes_from_free_kicks, player_model.passes_from_free_kicks
        )
        through_balls = more_interesting(through_balls, player_model.through_balls)
        switches = more_interesting(switches, player_model.switches)
        crosses = more_interesting(crosses, player_model.crosses)
        throw_ins_taken = more_interesting(
            throw_ins_taken, player_model.throw_ins_taken
        )
        corner_kicks = more_interesting(corner_kicks, player_model.corner_kicks)
        inswinging_corner_kicks = more_interesting(
            inswinging_corner_kicks, player_model.inswinging_corner_kicks
        )
        outswinging_corner_kicks = more_interesting(
            outswinging_corner_kicks, player_model.outswinging_corner_kicks
        )
        straight_corner_kicks = more_interesting(
            straight_corner_kicks, player_model.straight_corner_kicks
        )
        passes_offside = more_interesting(passes_offside, player_model.passes_offside)
        passes_blocked = more_interesting(passes_blocked, player_model.passes_blocked)
        tackles_won = more_interesting(tackles_won, player_model.tackles_won)
        tackles_in_defensive_third = more_interesting(
            tackles_in_defensive_third, player_model.tackles_in_defensive_third
        )
        tackles_in_middle_third = more_interesting(
            tackles_in_middle_third, player_model.tackles_in_middle_third
        )
        tackles_in_attacking_third = more_interesting(
            tackles_in_attacking_third, player_model.tackles_in_attacking_third
        )
        dribblers_tackled = more_interesting(
            dribblers_tackled, player_model.dribblers_tackled
        )
        dribbles_challenged = more_interesting(
            dribbles_challenged, player_model.dribbles_challenged
        )
        percent_of_dribblers_tackled = more_interesting(
            percent_of_dribblers_tackled, player_model.percent_of_dribblers_tackled
        )
        challenges_lost = more_interesting(
            challenges_lost, player_model.challenges_lost
        )
        shots_blocked = more_interesting(shots_blocked, player_model.shots_blocked)
        tackles_plus_interceptions = more_interesting(
            tackles_plus_interceptions, player_model.tackles_plus_interceptions
        )
        errors = more_interesting(errors, player_model.errors)
        touches_in_defensive_penalty_area = more_interesting(
            touches_in_defensive_penalty_area,
            player_model.touches_in_defensive_penalty_area,
        )
        touches_in_defensive_third = more_interesting(
            touches_in_defensive_third, player_model.touches_in_defensive_third
        )
        touches_in_middle_third = more_interesting(
            touches_in_middle_third, player_model.touches_in_middle_third
        )
        touches_in_attacking_third = more_interesting(
            touches_in_attacking_third, player_model.touches_in_attacking_third
        )
        touches_in_attacking_penalty_area = more_interesting(
            touches_in_attacking_penalty_area,
            player_model.touches_in_attacking_penalty_area,
        )
        live_ball_touches = more_interesting(
            live_ball_touches, player_model.live_ball_touches
        )
        successful_take_on_percentage = more_interesting(
            successful_take_on_percentage, player_model.successful_take_on_percentage
        )
        times_tackled_during_take_ons = more_interesting(
            times_tackled_during_take_ons, player_model.times_tackled_during_take_ons
        )
        tackled_during_take_on_percentage = more_interesting(
            tackled_during_take_on_percentage,
            player_model.tackled_during_take_on_percentage,
        )
        total_carrying_distance = more_interesting(
            total_carrying_distance, player_model.total_carrying_distance
        )
        progressive_carrying_distance = more_interesting(
            progressive_carrying_distance, player_model.progressive_carrying_distance
        )
        carries_into_final_third = more_interesting(
            carries_into_final_third, player_model.carries_into_final_third
        )
        carries_into_penalty_area = more_interesting(
            carries_into_penalty_area, player_model.carries_into_penalty_area
        )
        miscontrols = more_interesting(miscontrols, player_model.miscontrols)
        dispossessed = more_interesting(dispossessed, player_model.dispossessed)
        passes_received = more_interesting(
            passes_received, player_model.passes_received
        )
        progressive_passes_received = more_interesting(
            progressive_passes_received, player_model.progressive_passes_received
        )
        second_yellow_card = more_interesting(
            second_yellow_card, player_model.second_yellow_card
        )
        fouls_committed = more_interesting(
            fouls_committed, player_model.fouls_committed
        )
        fouls_drawn = more_interesting(fouls_drawn, player_model.fouls_drawn)
        offsides = more_interesting(offsides, player_model.offsides)
        penalty_kicks_won = more_interesting(
            penalty_kicks_won, player_model.penalty_kicks_won
        )
        penalty_kicks_conceded = more_interesting(
            penalty_kicks_conceded, player_model.penalty_kicks_conceded
        )
        own_goals = more_interesting(own_goals, player_model.own_goals)
        ball_recoveries = more_interesting(
            ball_recoveries, player_model.ball_recoveries
        )
        aerials_won = more_interesting(aerials_won, player_model.aerials_won)
        aerials_lost = more_interesting(aerials_lost, player_model.aerials_lost)
        percentage_of_aerials_won = more_interesting(
            percentage_of_aerials_won, player_model.percentage_of_aerials_won
        )
        shots_on_target_against = more_interesting(
            shots_on_target_against, player_model.shots_on_target_against
        )
        post_shot_expected_goals = more_interesting(
            post_shot_expected_goals, player_model.post_shot_expected_goals
        )
        passes_attempted_minus_goal_kicks = more_interesting(
            passes_attempted_minus_goal_kicks,
            player_model.passes_attempted_minus_goal_kicks,
        )
        throws_attempted = more_interesting(
            throws_attempted, player_model.throws_attempted
        )
        percentage_of_passes_that_were_launched = more_interesting(
            percentage_of_passes_that_were_launched,
            player_model.percentage_of_passes_that_were_launched,
        )
        average_pass_length = more_interesting(
            average_pass_length, player_model.average_pass_length
        )
        goal_kicks_attempted = more_interesting(
            goal_kicks_attempted, player_model.goal_kicks_attempted
        )
        percentage_of_goal_kicks_that_were_launched = more_interesting(
            percentage_of_goal_kicks_that_were_launched,
            player_model.percentage_of_goal_kicks_that_were_launched,
        )
        average_goal_kick_length = more_interesting(
            average_goal_kick_length, player_model.average_goal_kick_length
        )
        crosses_faced = more_interesting(crosses_faced, player_model.crosses_faced)
        crosses_stopped = more_interesting(
            crosses_stopped, player_model.crosses_stopped
        )
        percentage_crosses_stopped = more_interesting(
            percentage_crosses_stopped, player_model.percentage_crosses_stopped
        )
        defensive_actions_outside_penalty_area = more_interesting(
            defensive_actions_outside_penalty_area,
            player_model.defensive_actions_outside_penalty_area,
        )
        average_distance_of_defensive_actions = more_interesting(
            average_distance_of_defensive_actions,
            player_model.average_distance_of_defensive_actions,
        )
        three_point_attempt_rate = more_interesting(
            three_point_attempt_rate, player_model.three_point_attempt_rate
        )
        batting_style = more_interesting(batting_style, player_model.batting_style)
        bowling_style = more_interesting(bowling_style, player_model.bowling_style)
        playing_roles = more_interesting(playing_roles, player_model.playing_roles)
        runs = more_interesting(runs, player_model.runs)
        balls = more_interesting(balls, player_model.balls)
        fours = more_interesting(fours, player_model.fours)
        sixes = more_interesting(sixes, player_model.sixes)
        strikerate = more_interesting(strikerate, player_model.strikerate)
        fall_of_wicket_order = more_interesting(
            fall_of_wicket_order, player_model.fall_of_wicket_order
        )
        fall_of_wicket_num = more_interesting(
            fall_of_wicket_num, player_model.fall_of_wicket_num
        )
        fall_of_wicket_runs = more_interesting(
            fall_of_wicket_runs, player_model.fall_of_wicket_runs
        )
        fall_of_wicket_balls = more_interesting(
            fall_of_wicket_balls, player_model.fall_of_wicket_balls
        )
        fall_of_wicket_overs = more_interesting(
            fall_of_wicket_overs, player_model.fall_of_wicket_overs
        )
        fall_of_wicket_over_number = more_interesting(
            fall_of_wicket_over_number, player_model.fall_of_wicket_over_number
        )
        ball_over_actual = more_interesting(
            ball_over_actual, player_model.ball_over_actual
        )
        ball_over_unique = more_interesting(
            ball_over_unique, player_model.ball_over_unique
        )
        ball_total_runs = more_interesting(
            ball_total_runs, player_model.ball_total_runs
        )
        ball_batsman_runs = more_interesting(
            ball_batsman_runs, player_model.ball_batsman_runs
        )
        overs = more_interesting(overs, player_model.overs)
        maidens = more_interesting(maidens, player_model.maidens)
        conceded = more_interesting(conceded, player_model.conceded)
        wickets = more_interesting(wickets, player_model.wickets)
        economy = more_interesting(economy, player_model.economy)
        runs_per_ball = more_interesting(runs_per_ball, player_model.runs_per_ball)
        dots = more_interesting(dots, player_model.dots)
        wides = more_interesting(wides, player_model.wides)
        no_balls = more_interesting(no_balls, player_model.no_balls)
        free_throw_attempt_rate = more_interesting(
            free_throw_attempt_rate, player_model.free_throw_attempt_rate
        )
        offensive_rebound_percentage = more_interesting(
            offensive_rebound_percentage, player_model.offensive_rebound_percentage
        )
        defensive_rebound_percentage = more_interesting(
            defensive_rebound_percentage, player_model.defensive_rebound_percentage
        )
        total_rebound_percentage = more_interesting(
            total_rebound_percentage, player_model.total_rebound_percentage
        )
        assist_percentage = more_interesting(
            assist_percentage, player_model.assist_percentage
        )
        steal_percentage = more_interesting(
            steal_percentage, player_model.steal_percentage
        )
        block_percentage = more_interesting(
            block_percentage, player_model.block_percentage
        )
        turnover_percentage = more_interesting(
            turnover_percentage, player_model.turnover_percentage
        )
        usage_percentage = more_interesting(
            usage_percentage, player_model.usage_percentage
        )
        offensive_rating = more_interesting(
            offensive_rating, player_model.offensive_rating
        )
        defensive_rating = more_interesting(
            defensive_rating, player_model.defensive_rating
        )
        box_plus_minus = more_interesting(box_plus_minus, player_model.box_plus_minus)
        ace_percentage = more_interesting(ace_percentage, player_model.ace_percentage)
        double_fault_percentage = more_interesting(
            double_fault_percentage, player_model.double_fault_percentage
        )
        first_serves_in = more_interesting(
            first_serves_in, player_model.first_serves_in
        )
        first_serve_percentage = more_interesting(
            first_serve_percentage, player_model.first_serve_percentage
        )
        second_serve_percentage = more_interesting(
            second_serve_percentage, player_model.second_serve_percentage
        )
        break_points_saved = more_interesting(
            break_points_saved, player_model.break_points_saved
        )
        return_points_won_percentage = more_interesting(
            return_points_won_percentage, player_model.return_points_won_percentage
        )
        winners = more_interesting(winners, player_model.winners)
        winners_fronthand = more_interesting(
            winners_fronthand, player_model.winners_fronthand
        )
        winners_backhand = more_interesting(
            winners_backhand, player_model.winners_backhand
        )
        unforced_errors = more_interesting(
            unforced_errors, player_model.unforced_errors
        )
        unforced_errors_fronthand = more_interesting(
            unforced_errors_fronthand, player_model.unforced_errors_fronthand
        )
        unforced_errors_backhand = more_interesting(
            unforced_errors_backhand, player_model.unforced_errors_backhand
        )
        serve_points = more_interesting(serve_points, player_model.serve_points)
        serves_won = more_interesting(serves_won, player_model.serves_won)
        serves_aces = more_interesting(serves_aces, player_model.serves_aces)
        serves_unreturned = more_interesting(
            serves_unreturned, player_model.serves_unreturned
        )
        serves_forced_error_percentage = more_interesting(
            serves_forced_error_percentage, player_model.serves_forced_error_percentage
        )
        serves_won_in_three_shots_or_less = more_interesting(
            serves_won_in_three_shots_or_less,
            player_model.serves_won_in_three_shots_or_less,
        )
        serves_wide_percentage = more_interesting(
            serves_wide_percentage, player_model.serves_wide_percentage
        )
        serves_body_percentage = more_interesting(
            serves_body_percentage, player_model.serves_body_percentage
        )
        serves_t_percentage = more_interesting(
            serves_t_percentage, player_model.serves_t_percentage
        )
        serves_wide_deuce_percentage = more_interesting(
            serves_wide_deuce_percentage, player_model.serves_wide_deuce_percentage
        )
        serves_body_deuce_percentage = more_interesting(
            serves_body_deuce_percentage, player_model.serves_body_deuce_percentage
        )
        serves_t_deuce_percentage = more_interesting(
            serves_t_deuce_percentage, player_model.serves_t_deuce_percentage
        )
        serves_wide_ad_percentage = more_interesting(
            serves_wide_ad_percentage, player_model.serves_wide_ad_percentage
        )
        serves_body_ad_percentage = more_interesting(
            serves_body_ad_percentage, player_model.serves_body_ad_percentage
        )
        serves_t_ad_percentage = more_interesting(
            serves_t_ad_percentage, player_model.serves_t_ad_percentage
        )
        serves_net_percentage = more_interesting(
            serves_net_percentage, player_model.serves_net_percentage
        )
        serves_wide_direction_percentage = more_interesting(
            serves_wide_direction_percentage,
            player_model.serves_wide_direction_percentage,
        )
        shots_deep_percentage = more_interesting(
            shots_deep_percentage, player_model.shots_deep_percentage
        )
        shots_deep_wide_percentage = more_interesting(
            shots_deep_wide_percentage, player_model.shots_deep_wide_percentage
        )
        shots_foot_errors_percentage = more_interesting(
            shots_foot_errors_percentage, player_model.shots_foot_errors_percentage
        )
        shots_unknown_percentage = more_interesting(
            shots_unknown_percentage, player_model.shots_unknown_percentage
        )
        points_won_percentage = more_interesting(
            points_won_percentage, player_model.points_won_percentage
        )
        centre_clearances = more_interesting(
            centre_clearances, player_model.centre_clearances
        )
        disposal_efficiency = more_interesting(
            disposal_efficiency, player_model.disposal_efficiency
        )
        tackles_inside_50 = more_interesting(
            tackles_inside_50, player_model.tackles_inside_50
        )
        total_possessions = more_interesting(
            total_possessions, player_model.total_possessions
        )
        score_involvements = more_interesting(
            score_involvements, player_model.score_involvements
        )
        goal_accuracy = more_interesting(goal_accuracy, player_model.goal_accuracy)
        stoppage_clearances = more_interesting(
            stoppage_clearances, player_model.stoppage_clearances
        )
        uncontested_marks = more_interesting(
            uncontested_marks, player_model.uncontested_marks
        )
        accurate_crosses = more_interesting(
            accurate_crosses, player_model.accurate_crosses
        )
        accurate_long_balls = more_interesting(
            accurate_long_balls, player_model.accurate_long_balls
        )
        accurate_passes = more_interesting(
            accurate_passes, player_model.accurate_passes
        )
        accurate_through_balls = more_interesting(
            accurate_through_balls, player_model.accurate_through_balls
        )
        cross_percentage = more_interesting(
            cross_percentage, player_model.cross_percentage
        )
        free_kick_goals = more_interesting(
            free_kick_goals, player_model.free_kick_goals
        )
        free_kick_percentage = more_interesting(
            free_kick_percentage, player_model.free_kick_percentage
        )
        free_kick_shots = more_interesting(
            free_kick_shots, player_model.free_kick_shots
        )
        game_winning_assists = more_interesting(
            game_winning_assists, player_model.game_winning_assists
        )
        headed_goals = more_interesting(headed_goals, player_model.headed_goals)
        inaccurate_crosses = more_interesting(
            inaccurate_crosses, player_model.inaccurate_crosses
        )
        inaccurate_long_balls = more_interesting(
            inaccurate_long_balls, player_model.inaccurate_long_balls
        )
        inaccurate_passes = more_interesting(
            inaccurate_passes, player_model.inaccurate_passes
        )
        inaccurate_through_balls = more_interesting(
            inaccurate_through_balls, player_model.inaccurate_through_balls
        )
        left_footed_shots = more_interesting(
            left_footed_shots, player_model.left_footed_shots
        )
        long_ball_percentage = more_interesting(
            long_ball_percentage, player_model.long_ball_percentage
        )
        penalty_kick_goals = more_interesting(
            penalty_kick_goals, player_model.penalty_kick_goals
        )
        penalty_kick_percentage = more_interesting(
            penalty_kick_percentage, player_model.penalty_kick_percentage
        )
        penalty_kicks_missed = more_interesting(
            penalty_kicks_missed, player_model.penalty_kicks_missed
        )
        possession_percentage = more_interesting(
            possession_percentage, player_model.possession_percentage
        )
        possession_time = more_interesting(
            possession_time, player_model.possession_time
        )
        right_footed_shots = more_interesting(
            right_footed_shots, player_model.right_footed_shots
        )
        shoot_out_goals = more_interesting(
            shoot_out_goals, player_model.shoot_out_goals
        )
        shoot_out_misses = more_interesting(
            shoot_out_misses, player_model.shoot_out_misses
        )
        shoot_out_percentage = more_interesting(
            shoot_out_percentage, player_model.shoot_out_percentage
        )
        shot_assists = more_interesting(shot_assists, player_model.shot_assists)
        shot_percentage = more_interesting(
            shot_percentage, player_model.shot_percentage
        )
        shots_headed = more_interesting(shots_headed, player_model.shots_headed)
        shots_off_target = more_interesting(
            shots_off_target, player_model.shots_off_target
        )
        shots_on_post = more_interesting(shots_on_post, player_model.shots_on_post)
        through_ball_percentage = more_interesting(
            through_ball_percentage, player_model.through_ball_percentage
        )
        long_balls = more_interesting(long_balls, player_model.long_balls)
        total_passes = more_interesting(total_passes, player_model.total_passes)
        average_rating_from_editor = more_interesting(
            average_rating_from_editor, player_model.average_rating_from_editor
        )
        average_rating_from_user = more_interesting(
            average_rating_from_user, player_model.average_rating_from_user
        )
        did_not_play = more_interesting(did_not_play, player_model.did_not_play)
        draws = more_interesting(draws, player_model.draws)
        goal_difference = more_interesting(
            goal_difference, player_model.goal_difference
        )
        losses = more_interesting(losses, player_model.losses)
        lost_corners = more_interesting(lost_corners, player_model.lost_corners)
        minutes = more_interesting(minutes, player_model.minutes)
        pass_percentage = more_interesting(
            pass_percentage, player_model.pass_percentage
        )
        starts = more_interesting(starts, player_model.starts)
        sub_ins = more_interesting(sub_ins, player_model.sub_ins)
        sub_outs = more_interesting(sub_outs, player_model.sub_outs)
        suspensions = more_interesting(suspensions, player_model.suspensions)
        time_ended = more_interesting(time_ended, player_model.time_ended)
        time_started = more_interesting(time_started, player_model.time_started)
        win_percentage = more_interesting(win_percentage, player_model.win_percentage)
        wins = more_interesting(wins, player_model.wins)
        won_corners = more_interesting(won_corners, player_model.won_corners)
        clean_sheet = more_interesting(clean_sheet, player_model.clean_sheet)
        crosses_caught = more_interesting(crosses_caught, player_model.crosses_caught)
        goals_conceded = more_interesting(goals_conceded, player_model.goals_conceded)
        partial_clean_sheet = more_interesting(
            partial_clean_sheet, player_model.partial_clean_sheet
        )
        penalty_kick_conceded = more_interesting(
            penalty_kick_conceded, player_model.penalty_kick_conceded
        )
        penalty_kick_save_percentage = more_interesting(
            penalty_kick_save_percentage, player_model.penalty_kick_save_percentage
        )
        penalty_kicks_faced = more_interesting(
            penalty_kicks_faced, player_model.penalty_kicks_faced
        )
        penalty_kicks_saved = more_interesting(
            penalty_kicks_saved, player_model.penalty_kicks_saved
        )
        punches = more_interesting(punches, player_model.punches)
        shoot_out_kicks_faced = more_interesting(
            shoot_out_kicks_faced, player_model.shoot_out_kicks_faced
        )
        shoot_out_kicks_saved = more_interesting(
            shoot_out_kicks_saved, player_model.shoot_out_kicks_saved
        )
        shoot_out_save_percentage = more_interesting(
            shoot_out_save_percentage, player_model.shoot_out_save_percentage
        )
        shots_faced = more_interesting(shots_faced, player_model.shots_faced)
        smothers = more_interesting(smothers, player_model.smothers)
        unclaimed_crosses = more_interesting(
            unclaimed_crosses, player_model.unclaimed_crosses
        )
        effective_clearances = more_interesting(
            effective_clearances, player_model.effective_clearances
        )
        effective_tackles = more_interesting(
            effective_tackles, player_model.effective_tackles
        )
        ineffective_tackles = more_interesting(
            ineffective_tackles, player_model.ineffective_tackles
        )
        tackle_percentage = more_interesting(
            tackle_percentage, player_model.tackle_percentage
        )
        appearances = more_interesting(appearances, player_model.appearances)
        average_rating_from_correspondent = more_interesting(
            average_rating_from_correspondent,
            player_model.average_rating_from_correspondent,
        )
        average_rating_from_data_feed = more_interesting(
            average_rating_from_data_feed, player_model.average_rating_from_data_feed
        )
        games_played = more_interesting(games_played, player_model.games_played)
        team_games_played = more_interesting(
            team_games_played, player_model.team_games_played
        )
        hit_by_pitch = more_interesting(hit_by_pitch, player_model.hit_by_pitch)
        rbis = more_interesting(rbis, player_model.rbis)
        sac_hits = more_interesting(sac_hits, player_model.sac_hits)
        stolen_bases = more_interesting(stolen_bases, player_model.stolen_bases)
        walks = more_interesting(walks, player_model.walks)
        catcher_interference = more_interesting(
            catcher_interference, player_model.catcher_interference
        )
        gidps = more_interesting(gidps, player_model.gidps)
        sac_flies = more_interesting(sac_flies, player_model.sac_flies)
        grand_slam_home_runs = more_interesting(
            grand_slam_home_runs, player_model.grand_slam_home_runs
        )
        runners_left_on_base = more_interesting(
            runners_left_on_base, player_model.runners_left_on_base
        )
        triples = more_interesting(triples, player_model.triples)
        game_winning_rbis = more_interesting(
            game_winning_rbis, player_model.game_winning_rbis
        )
        intentional_walks = more_interesting(
            intentional_walks, player_model.intentional_walks
        )
        doubles = more_interesting(doubles, player_model.doubles)
        caught_stealing = more_interesting(
            caught_stealing, player_model.caught_stealing
        )
        games_started = more_interesting(games_started, player_model.games_started)
        pinch_at_bats = more_interesting(pinch_at_bats, player_model.pinch_at_bats)
        pinch_hits = more_interesting(pinch_hits, player_model.pinch_hits)
        player_rating = more_interesting(player_rating, player_model.player_rating)
        is_qualified = more_interesting(is_qualified, player_model.is_qualified)
        is_qualified_steals = more_interesting(
            is_qualified_steals, player_model.is_qualified_steals
        )
        total_bases = more_interesting(total_bases, player_model.total_bases)
        projected_home_runs = more_interesting(
            projected_home_runs, player_model.projected_home_runs
        )
        extra_base_hits = more_interesting(
            extra_base_hits, player_model.extra_base_hits
        )
        runs_created = more_interesting(runs_created, player_model.runs_created)
        batting_average = more_interesting(
            batting_average, player_model.batting_average
        )
        pinch_average = more_interesting(pinch_average, player_model.pinch_average)
        slug_average = more_interesting(slug_average, player_model.slug_average)
        secondary_average = more_interesting(
            secondary_average, player_model.secondary_average
        )
        on_base_percentage = more_interesting(
            on_base_percentage, player_model.on_base_percentage
        )
        ground_to_fly_ratio = more_interesting(
            ground_to_fly_ratio, player_model.ground_to_fly_ratio
        )
        runs_created_per_27_outs = more_interesting(
            runs_created_per_27_outs, player_model.runs_created_per_27_outs
        )
        batter_rating = more_interesting(batter_rating, player_model.batter_rating)
        at_bats_per_home_run = more_interesting(
            at_bats_per_home_run, player_model.at_bats_per_home_run
        )
        stolen_base_percentage = more_interesting(
            stolen_base_percentage, player_model.stolen_base_percentage
        )
        pitches_per_plate_appearance = more_interesting(
            pitches_per_plate_appearance, player_model.pitches_per_plate_appearance
        )
        isolated_power = more_interesting(isolated_power, player_model.isolated_power)
        walk_to_strikeout_ratio = more_interesting(
            walk_to_strikeout_ratio, player_model.walk_to_strikeout_ratio
        )
        walks_per_plate_appearance = more_interesting(
            walks_per_plate_appearance, player_model.walks_per_plate_appearance
        )
        secondary_average_minus_batting_average = more_interesting(
            secondary_average_minus_batting_average,
            player_model.secondary_average_minus_batting_average,
        )
        runs_produced = more_interesting(runs_produced, player_model.runs_produced)
        runs_ratio = more_interesting(runs_ratio, player_model.runs_ratio)
        patience_ratio = more_interesting(patience_ratio, player_model.patience_ratio)
        balls_in_play_average = more_interesting(
            balls_in_play_average, player_model.balls_in_play_average
        )
        mlb_rating = more_interesting(mlb_rating, player_model.mlb_rating)
        offensive_wins_above_replacement = more_interesting(
            offensive_wins_above_replacement,
            player_model.offensive_wins_above_replacement,
        )
        wins_above_replacement = more_interesting(
            wins_above_replacement, player_model.wins_above_replacement
        )
        batters_hit = more_interesting(batters_hit, player_model.batters_hit)
        sacrifice_bunts = more_interesting(
            sacrifice_bunts, player_model.sacrifice_bunts
        )
        save_opportunities = more_interesting(
            save_opportunities, player_model.save_opportunities
        )
        finishes = more_interesting(finishes, player_model.finishes)
        balks = more_interesting(balks, player_model.balks)
        holds = more_interesting(holds, player_model.holds)
        complete_games = more_interesting(complete_games, player_model.complete_games)
        perfect_games = more_interesting(perfect_games, player_model.perfect_games)
        wild_pitches = more_interesting(wild_pitches, player_model.wild_pitches)
        third_innings = more_interesting(third_innings, player_model.third_innings)
        team_earned_runs = more_interesting(
            team_earned_runs, player_model.team_earned_runs
        )
        pickoff_attempts = more_interesting(
            pickoff_attempts, player_model.pickoff_attempts
        )
        run_support = more_interesting(run_support, player_model.run_support)
        pitches_as_starter = more_interesting(
            pitches_as_starter, player_model.pitches_as_starter
        )
        average_game_score = more_interesting(
            average_game_score, player_model.average_game_score
        )
        quality_starts = more_interesting(quality_starts, player_model.quality_starts)
        inherited_runners_scored = more_interesting(
            inherited_runners_scored, player_model.inherited_runners_scored
        )
        opponent_total_bases = more_interesting(
            opponent_total_bases, player_model.opponent_total_bases
        )
        is_qualified_saves = more_interesting(
            is_qualified_saves, player_model.is_qualified_saves
        )
        full_innings = more_interesting(full_innings, player_model.full_innings)
        part_innings = more_interesting(part_innings, player_model.part_innings)
        blown_saves = more_interesting(blown_saves, player_model.blown_saves)
        innings = more_interesting(innings, player_model.innings)
        whip = more_interesting(whip, player_model.whip)
        caught_stealing_percentage = more_interesting(
            caught_stealing_percentage, player_model.caught_stealing_percentage
        )
        pitches_per_start = more_interesting(
            pitches_per_start, player_model.pitches_per_start
        )
        pitches_per_inning = more_interesting(
            pitches_per_inning, player_model.pitches_per_inning
        )
        run_support_average = more_interesting(
            run_support_average, player_model.run_support_average
        )
        opponent_average = more_interesting(
            opponent_average, player_model.opponent_average
        )
        opponent_slug_average = more_interesting(
            opponent_slug_average, player_model.opponent_slug_average
        )
        opponent_on_base_percentage = more_interesting(
            opponent_on_base_percentage, player_model.opponent_on_base_percentage
        )
        opponent_ops = more_interesting(opponent_ops, player_model.opponent_ops)
        strikeouts_per_nine_innings = more_interesting(
            strikeouts_per_nine_innings, player_model.strikeouts_per_nine_innings
        )
        strikeout_to_walk_ratio = more_interesting(
            strikeout_to_walk_ratio, player_model.strikeout_to_walk_ratio
        )
        tough_losses = more_interesting(tough_losses, player_model.tough_losses)
        cheap_wins = more_interesting(cheap_wins, player_model.cheap_wins)
        save_opportunities_per_win = more_interesting(
            save_opportunities_per_win, player_model.save_opportunities_per_win
        )
        pitch_count = more_interesting(pitch_count, player_model.pitch_count)
        strike_pitch_ratio = more_interesting(
            strike_pitch_ratio, player_model.strike_pitch_ratio
        )
        double_plays = more_interesting(double_plays, player_model.double_plays)
        opportunities = more_interesting(opportunities, player_model.opportunities)
        passed_balls = more_interesting(passed_balls, player_model.passed_balls)
        outfield_assists = more_interesting(
            outfield_assists, player_model.outfield_assists
        )
        pickoffs = more_interesting(pickoffs, player_model.pickoffs)
        outs_on_field = more_interesting(outs_on_field, player_model.outs_on_field)
        triple_plays = more_interesting(triple_plays, player_model.triple_plays)
        balls_in_zone = more_interesting(balls_in_zone, player_model.balls_in_zone)
        extra_bases = more_interesting(extra_bases, player_model.extra_bases)
        outs_made = more_interesting(outs_made, player_model.outs_made)
        catcher_third_innings_played = more_interesting(
            catcher_third_innings_played, player_model.catcher_third_innings_played
        )
        catcher_caught_stealing = more_interesting(
            catcher_caught_stealing, player_model.catcher_caught_stealing
        )
        catcher_stolen_bases_allowed = more_interesting(
            catcher_stolen_bases_allowed, player_model.catcher_stolen_bases_allowed
        )
        catcher_earned_runs = more_interesting(
            catcher_earned_runs, player_model.catcher_earned_runs
        )
        is_qualified_catcher = more_interesting(
            is_qualified_catcher, player_model.is_qualified_catcher
        )
        is_qualified_pitcher = more_interesting(
            is_qualified_pitcher, player_model.is_qualified_pitcher
        )
        successful_chances = more_interesting(
            successful_chances, player_model.successful_chances
        )
        total_chances = more_interesting(total_chances, player_model.total_chances)
        full_innings_played = more_interesting(
            full_innings_played, player_model.full_innings_played
        )
        part_innings_played = more_interesting(
            part_innings_played, player_model.part_innings_played
        )
        fielding_percentage = more_interesting(
            fielding_percentage, player_model.fielding_percentage
        )
        range_factor = more_interesting(range_factor, player_model.range_factor)
        zone_rating = more_interesting(zone_rating, player_model.zone_rating)
        catcher_caught_stealing_percentage = more_interesting(
            catcher_caught_stealing_percentage,
            player_model.catcher_caught_stealing_percentage,
        )
        catcher_era = more_interesting(catcher_era, player_model.catcher_era)
        def_warbr = more_interesting(def_warbr, player_model.def_warbr)
    if name is None:
        raise ValueError("name is null")
    if species is None:
        raise ValueError("species is null")

    player_model = PlayerModel.model_construct(
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
        hit_outs=hit_outs,
        tackles=tackles,
        rebounds=rebounds,
        insides=insides,
        clearances=clearances,
        clangers=clangers,
        free_kicks_for=free_kicks_for,
        free_kicks_against=free_kicks_against,
        brownlow_votes=brownlow_votes,
        contested_possessions=contested_possessions,
        uncontested_possessions=uncontested_possessions,
        contested_marks=contested_marks,
        marks_inside=marks_inside,
        one_percenters=one_percenters,
        bounces=bounces,
        goal_assists=goal_assists,
        percentage_played=percentage_played,
        birth_date=birth_date,
        species=species,
        handicap_weight=handicap_weight,
        father=father,
        sex=sex,
        age=age,
        starting_position=starting_position,
        weight=weight,
        birth_address=birth_address,
        owner=owner,
        seconds_played=seconds_played,
        three_point_field_goals=three_point_field_goals,
        three_point_field_goals_attempted=three_point_field_goals_attempted,
        free_throws=free_throws,
        free_throws_attempted=free_throws_attempted,
        defensive_rebounds=defensive_rebounds,
        steals=steals,
        blocks=blocks,
        personal_fouls=personal_fouls,
        points=points,
        game_score=game_score,
        point_differential=point_differential,
        version=VERSION,
        height=height,
        colleges=colleges if colleges is not None else [],
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
        passing_yards_at_catch=passing_yards_at_catch,
        quarterback_rating=quarterback_rating,
        sacks=sacks,
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
        punt_return_yards=punt_return_yards,
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
        receiving_touchdowns_49_yards=receiving_touchdowns_49_yards,
        receiving_touchdowns_above_50_yards=receiving_touchdowns_above_50_yards,
        rushing_touchdowns_9_yards=rushing_touchdowns_9_yards,
        rushing_touchdowns_19_yards=rushing_touchdowns_19_yards,
        rushing_touchdowns_29_yards=rushing_touchdowns_29_yards,
        rushing_touchdowns_39_yards=rushing_touchdowns_39_yards,
        rushing_touchdowns_49_yards=rushing_touchdowns_49_yards,
        rushing_touchdowns_above_50_yards=rushing_touchdowns_above_50_yards,
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
        tackled_during_take_on_percentage=tackled_during_take_on_percentage,
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
        batting_style=batting_style,
        bowling_style=bowling_style,
        playing_roles=playing_roles,
        runs=runs,
        balls=balls,
        fours=fours,
        sixes=sixes,
        strikerate=strikerate,
        fall_of_wicket_order=fall_of_wicket_order,
        fall_of_wicket_num=fall_of_wicket_num,
        fall_of_wicket_runs=fall_of_wicket_runs,
        fall_of_wicket_balls=fall_of_wicket_balls,
        fall_of_wicket_overs=fall_of_wicket_overs,
        fall_of_wicket_over_number=fall_of_wicket_over_number,
        ball_over_actual=ball_over_actual,
        ball_over_unique=ball_over_unique,
        ball_total_runs=ball_total_runs,
        ball_batsman_runs=ball_batsman_runs,
        overs=overs,
        maidens=maidens,
        conceded=conceded,
        wickets=wickets,
        economy=economy,
        runs_per_ball=runs_per_ball,
        dots=dots,
        wides=wides,
        no_balls=no_balls,
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
        ace_percentage=ace_percentage,
        double_fault_percentage=double_fault_percentage,
        first_serves_in=first_serves_in,
        first_serve_percentage=first_serve_percentage,
        second_serve_percentage=second_serve_percentage,
        break_points_saved=break_points_saved,
        return_points_won_percentage=return_points_won_percentage,
        winners=winners,
        winners_fronthand=winners_fronthand,
        winners_backhand=winners_backhand,
        unforced_errors=unforced_errors,
        unforced_errors_fronthand=unforced_errors_fronthand,
        unforced_errors_backhand=unforced_errors_backhand,
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
        centre_clearances=centre_clearances,
        disposal_efficiency=disposal_efficiency,
        tackles_inside_50=tackles_inside_50,
        total_possessions=total_possessions,
        score_involvements=score_involvements,
        goal_accuracy=goal_accuracy,
        stoppage_clearances=stoppage_clearances,
        uncontested_marks=uncontested_marks,
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
        clean_sheet=clean_sheet,
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
        effective_clearances=effective_clearances,
        effective_tackles=effective_tackles,
        ineffective_tackles=ineffective_tackles,
        tackle_percentage=tackle_percentage,
        appearances=appearances,
        average_rating_from_correspondent=average_rating_from_correspondent,
        average_rating_from_data_feed=average_rating_from_data_feed,
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
    )

    ffill(player_ffill, identifier, player_model)

    return player_model
