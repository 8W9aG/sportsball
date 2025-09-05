"""Combined team model."""

# pylint: disable=too-many-locals,too-many-branches,too-many-statements,too-many-arguments,duplicate-code,too-many-positional-arguments
import functools
from typing import Any

from ..coach_model import CoachModel
from ..news_model import NewsModel
from ..odds_model import OddsModel
from ..player_model import PlayerModel
from ..social_model import SocialModel
from ..team_model import VERSION, TeamModel
from .combined_coach_model import create_combined_coach_model
from .combined_player_model import create_combined_player_model
from .ffill import ffill
from .most_interesting import more_interesting
from .normalise_name import normalise_name


def _compare_player_models(left: PlayerModel, right: PlayerModel) -> int:
    if left.jersey is not None and right.jersey is not None:
        if left.jersey < right.jersey:
            return -1
        if left.jersey > right.jersey:
            return 1
    if left.name < right.name:
        return -1
    if left.name < right.name:
        return 1
    return 0


def create_combined_team_model(
    team_models: list[TeamModel],
    identifier: str,
    player_identity_map: dict[str, str],
    names: dict[str, str],
    coach_names: dict[str, str],
    player_ffill: dict[str, dict[str, Any]],
    team_ffill: dict[str, dict[str, Any]],
    coach_ffill: dict[str, dict[str, Any]],
) -> TeamModel:
    """Create a team model by combining many team models."""
    location = None
    players: dict[str, list[PlayerModel]] = {}
    odds: dict[str, list[OddsModel]] = {}
    news: dict[str, NewsModel] = {}
    social: dict[str, SocialModel] = {}
    coaches: dict[str, list[CoachModel]] = {}
    points = None
    ladder_rank = None
    field_goals = None
    lbw = None
    end_dt = None
    runs = None
    wickets = None
    overs = None
    balls = None
    byes = None
    leg_byes = None
    wides = None
    no_balls = None
    penalties = None
    balls_per_over = None
    fours = None
    sixes = None
    catches = None
    catches_dropped = None
    disposal_efficiency = None
    uncontested_marks = None
    total_possessions = None
    tackles_inside_50 = None
    centre_clearances = None
    stoppage_clearances = None
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
    game_winning_goals = None
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
    draws = None
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
    perfect_games = None
    wild_pitches = None
    third_innings = None
    team_earned_runs = None
    shutouts = None
    pickoff_attempts = None
    run_support = None
    pitches_as_starter = None
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
    save_percentage = None
    strikeouts_per_nine_innings = None
    strikeout_to_walk_ratio = None
    tough_losses = None
    cheap_wins = None
    save_opportunities_per_win = None
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
    hit_by_pitch = None
    ground_balls = None
    strikeouts = None
    rbis = None
    sac_hits = None
    hits = None
    stolen_bases = None
    walks = None
    catcher_interference = None
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
    average_game_score = None
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
    field_goals_made = None
    free_throws_made = None
    three_point_percentage = None
    three_point_field_goals_made = None
    team_turnovers = None
    total_turnovers = None
    points_in_paint = None
    brick_index = None
    fast_break_points = None
    average_field_goals_made = None
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
    vorp = None
    average_minutes = None
    nba_rating = None
    for team_model in team_models:
        location = more_interesting(location, team_model.location)
        for player_model in team_model.players:
            player_id = player_model.identifier
            player_name_key = normalise_name(player_model.name)
            if player_model.identifier in player_identity_map:
                player_id = player_identity_map[player_id]
            elif player_name_key in names:
                player_id = names[player_name_key]
            else:
                names[player_name_key] = player_id
            players[player_id] = players.get(player_id, []) + [player_model]
        for odds_model in team_model.odds:
            key = f"{odds_model.bookie.identifier}-{odds_model.odds}"
            odds[key] = odds.get(key, []) + [odds_model]
        points = more_interesting(points, team_model.points)
        ladder_rank = more_interesting(ladder_rank, team_model.ladder_rank)
        for news_model in team_model.news:
            news_key = "-".join(
                [
                    news_model.title,
                    str(news_model.published),
                    news_model.summary,
                    news_model.source,
                ]
            )
            news[news_key] = news_model
        for social_model in team_model.social:
            social_key = "-".join(
                [social_model.network, social_model.post, str(social_model.published)]
            )
            social[social_key] = social_model
        field_goals = more_interesting(field_goals, team_model.field_goals)
        for coach_model in team_model.coaches:
            coach_id = coach_model.identifier
            coach_name_key = normalise_name(coach_model.name)
            if coach_name_key in coach_names:
                coach_id = coach_names[coach_name_key]
            else:
                coach_names[coach_name_key] = coach_id
            coaches[coach_id] = coaches.get(coach_id, []) + [coach_model]
        lbw = more_interesting(lbw, team_model.lbw)
        end_dt = more_interesting(end_dt, team_model.end_dt)
        runs = more_interesting(runs, team_model.runs)
        wickets = more_interesting(wickets, team_model.wickets)
        overs = more_interesting(overs, team_model.overs)
        balls = more_interesting(balls, team_model.balls)
        byes = more_interesting(byes, team_model.byes)
        leg_byes = more_interesting(leg_byes, team_model.leg_byes)
        wides = more_interesting(wides, team_model.wides)
        no_balls = more_interesting(no_balls, team_model.no_balls)
        penalties = more_interesting(penalties, team_model.penalties)
        balls_per_over = more_interesting(balls_per_over, team_model.balls_per_over)
        fours = more_interesting(fours, team_model.fours)
        sixes = more_interesting(sixes, team_model.sixes)
        catches = more_interesting(catches, team_model.catches)
        catches_dropped = more_interesting(catches_dropped, team_model.catches_dropped)
        disposal_efficiency = more_interesting(
            disposal_efficiency, team_model.disposal_efficiency
        )
        uncontested_marks = more_interesting(
            uncontested_marks, team_model.uncontested_marks
        )
        total_possessions = more_interesting(
            total_possessions, team_model.total_possessions
        )
        tackles_inside_50 = more_interesting(
            tackles_inside_50, team_model.tackles_inside_50
        )
        centre_clearances = more_interesting(
            centre_clearances, team_model.centre_clearances
        )
        stoppage_clearances = more_interesting(
            stoppage_clearances, team_model.stoppage_clearances
        )
        goal_accuracy = more_interesting(goal_accuracy, team_model.goal_accuracy)
        rushed_behinds = more_interesting(rushed_behinds, team_model.rushed_behinds)
        touched_behinds = more_interesting(touched_behinds, team_model.touched_behinds)
        left_behinds = more_interesting(left_behinds, team_model.left_behinds)
        left_posters = more_interesting(left_posters, team_model.left_posters)
        right_behinds = more_interesting(right_behinds, team_model.right_behinds)
        right_posters = more_interesting(right_posters, team_model.right_posters)
        total_interchange_count = more_interesting(
            total_interchange_count, team_model.total_interchange_count
        )
        interchange_count_q1 = more_interesting(
            interchange_count_q1, team_model.interchange_count_q1
        )
        interchange_count_q2 = more_interesting(
            interchange_count_q2, team_model.interchange_count_q2
        )
        interchange_count_q3 = more_interesting(
            interchange_count_q3, team_model.interchange_count_q3
        )
        interchange_count_q4 = more_interesting(
            interchange_count_q4, team_model.interchange_count_q4
        )
        game_winning_goals = more_interesting(
            game_winning_goals, team_model.game_winning_goals
        )
        headed_goals = more_interesting(headed_goals, team_model.headed_goals)
        inaccurate_crosses = more_interesting(
            inaccurate_crosses, team_model.inaccurate_crosses
        )
        inaccurate_long_balls = more_interesting(
            inaccurate_long_balls, team_model.inaccurate_long_balls
        )
        inaccurate_passes = more_interesting(
            inaccurate_passes, team_model.inaccurate_passes
        )
        inaccurate_through_balls = more_interesting(
            inaccurate_through_balls, team_model.inaccurate_through_balls
        )
        left_footed_shots = more_interesting(
            left_footed_shots, team_model.left_footed_shots
        )
        longball_percentage = more_interesting(
            longball_percentage, team_model.longball_percentage
        )
        offsides = more_interesting(offsides, team_model.offsides)
        penalty_kick_goals = more_interesting(
            penalty_kick_goals, team_model.penalty_kick_goals
        )
        penalty_kick_percentage = more_interesting(
            penalty_kick_percentage, team_model.penalty_kick_percentage
        )
        penalty_kick_shots = more_interesting(
            penalty_kick_shots, team_model.penalty_kick_shots
        )
        penalty_kicks_missed = more_interesting(
            penalty_kicks_missed, team_model.penalty_kicks_missed
        )
        possession_percentage = more_interesting(
            possession_percentage, team_model.possession_percentage
        )
        possession_time = more_interesting(possession_time, team_model.possession_time)
        right_footed_shots = more_interesting(
            right_footed_shots, team_model.right_footed_shots
        )
        shoot_out_goals = more_interesting(shoot_out_goals, team_model.shoot_out_goals)
        shoot_out_misses = more_interesting(
            shoot_out_misses, team_model.shoot_out_misses
        )
        shoot_out_percentage = more_interesting(
            shoot_out_percentage, team_model.shoot_out_percentage
        )
        shot_assists = more_interesting(shot_assists, team_model.shot_assists)
        shot_percentage = more_interesting(shot_percentage, team_model.shot_percentage)
        shots_headed = more_interesting(shots_headed, team_model.shots_headed)
        shots_off_target = more_interesting(
            shots_off_target, team_model.shots_off_target
        )
        shots_on_post = more_interesting(shots_on_post, team_model.shots_on_post)
        shots_on_target = more_interesting(shots_on_target, team_model.shots_on_target)
        through_ball_percentage = more_interesting(
            through_ball_percentage, team_model.through_ball_percentage
        )
        total_crosses = more_interesting(total_crosses, team_model.total_crosses)
        total_goals = more_interesting(total_goals, team_model.total_goals)
        total_long_balls = more_interesting(
            total_long_balls, team_model.total_long_balls
        )
        total_passes = more_interesting(total_passes, team_model.total_passes)
        total_shots = more_interesting(total_shots, team_model.total_shots)
        total_through_balls = more_interesting(
            total_through_balls, team_model.total_through_balls
        )
        draws = more_interesting(draws, team_model.draws)
        sub_outs = more_interesting(sub_outs, team_model.sub_outs)
        suspensions = more_interesting(suspensions, team_model.suspensions)
        time_ended = more_interesting(time_ended, team_model.time_ended)
        time_started = more_interesting(time_started, team_model.time_started)
        win_percentage = more_interesting(win_percentage, team_model.win_percentage)
        wins = more_interesting(wins, team_model.wins)
        won_corners = more_interesting(won_corners, team_model.won_corners)
        yellow_cards = more_interesting(yellow_cards, team_model.yellow_cards)
        clean_sheet = more_interesting(clean_sheet, team_model.clean_sheet)
        crosses_caught = more_interesting(crosses_caught, team_model.crosses_caught)
        goals_conceded = more_interesting(goals_conceded, team_model.goals_conceded)
        partial_clean_sheet = more_interesting(
            partial_clean_sheet, team_model.partial_clean_sheet
        )
        penalty_kick_conceded = more_interesting(
            penalty_kick_conceded, team_model.penalty_kick_conceded
        )
        penalty_kick_save_percentage = more_interesting(
            penalty_kick_save_percentage, team_model.penalty_kick_save_percentage
        )
        penalty_kicks_faced = more_interesting(
            penalty_kicks_faced, team_model.penalty_kicks_faced
        )
        penalty_kicks_saved = more_interesting(
            penalty_kicks_saved, team_model.penalty_kicks_saved
        )
        punches = more_interesting(punches, team_model.punches)
        saves = more_interesting(saves, team_model.saves)
        shoot_out_kicks_faced = more_interesting(
            shoot_out_kicks_faced, team_model.shoot_out_kicks_faced
        )
        shoot_out_kicks_saved = more_interesting(
            shoot_out_kicks_saved, team_model.shoot_out_kicks_saved
        )
        shoot_out_save_percentage = more_interesting(
            shoot_out_save_percentage, team_model.shoot_out_save_percentage
        )
        shots_faced = more_interesting(shots_faced, team_model.shots_faced)
        smothers = more_interesting(smothers, team_model.smothers)
        unclaimed_crosses = more_interesting(
            unclaimed_crosses, team_model.unclaimed_crosses
        )
        accurate_crosses = more_interesting(
            accurate_crosses, team_model.accurate_crosses
        )
        accurate_long_balls = more_interesting(
            accurate_long_balls, team_model.accurate_long_balls
        )
        accurate_passes = more_interesting(accurate_passes, team_model.accurate_passes)
        accurate_through_balls = more_interesting(
            accurate_through_balls, team_model.accurate_through_balls
        )
        cross_percentage = more_interesting(
            cross_percentage, team_model.cross_percentage
        )
        free_kick_goals = more_interesting(free_kick_goals, team_model.free_kick_goals)
        free_kick_percentage = more_interesting(
            free_kick_percentage, team_model.free_kick_percentage
        )
        free_kick_shots = more_interesting(free_kick_shots, team_model.free_kick_shots)
        game_winning_assists = more_interesting(
            game_winning_assists, team_model.game_winning_assists
        )
        blocked_shots = more_interesting(blocked_shots, team_model.blocked_shots)
        effective_clearances = more_interesting(
            effective_clearances, team_model.effective_clearances
        )
        effective_tackles = more_interesting(
            effective_tackles, team_model.effective_tackles
        )
        ineffective_tackles = more_interesting(
            ineffective_tackles, team_model.ineffective_tackles
        )
        interceptions = more_interesting(interceptions, team_model.interceptions)
        tackle_percentage = more_interesting(
            tackle_percentage, team_model.tackle_percentage
        )
        appearances = more_interesting(appearances, team_model.appearances)
        average_rating_from_correspondent = more_interesting(
            average_rating_from_correspondent,
            team_model.average_rating_from_correspondent,
        )
        average_rating_from_data_feed = more_interesting(
            average_rating_from_data_feed, team_model.average_rating_from_data_feed
        )
        average_rating_from_editor = more_interesting(
            average_rating_from_editor, team_model.average_rating_from_editor
        )
        average_rating_from_user = more_interesting(
            average_rating_from_user, team_model.average_rating_from_user
        )
        did_not_play = more_interesting(did_not_play, team_model.did_not_play)
        fouls_committed = more_interesting(fouls_committed, team_model.fouls_committed)
        fouls_suffered = more_interesting(fouls_suffered, team_model.fouls_suffered)
        goal_difference = more_interesting(goal_difference, team_model.goal_difference)
        losses = more_interesting(losses, team_model.losses)
        lost_corners = more_interesting(lost_corners, team_model.lost_corners)
        minutes = more_interesting(minutes, team_model.minutes)
        own_goals = more_interesting(own_goals, team_model.own_goals)
        pass_percentage = more_interesting(pass_percentage, team_model.pass_percentage)
        red_cards = more_interesting(red_cards, team_model.red_cards)
        starts = more_interesting(starts, team_model.starts)
        sub_ins = more_interesting(sub_ins, team_model.sub_ins)
        pitch_count = more_interesting(pitch_count, team_model.pitch_count)
        strikes = more_interesting(strikes, team_model.strikes)
        strike_pitch_ratio = more_interesting(
            strike_pitch_ratio, team_model.strike_pitch_ratio
        )
        games_played = more_interesting(games_played, team_model.games_played)
        team_games_played = more_interesting(
            team_games_played, team_model.team_games_played
        )
        double_plays = more_interesting(double_plays, team_model.double_plays)
        opportunities = more_interesting(opportunities, team_model.opportunities)
        errors = more_interesting(errors, team_model.errors)
        passed_balls = more_interesting(passed_balls, team_model.passed_balls)
        outfield_assists = more_interesting(
            outfield_assists, team_model.outfield_assists
        )
        pickoffs = more_interesting(pickoffs, team_model.pickoffs)
        putouts = more_interesting(putouts, team_model.putouts)
        outs_on_field = more_interesting(outs_on_field, team_model.outs_on_field)
        triple_plays = more_interesting(triple_plays, team_model.triple_plays)
        balls_in_zone = more_interesting(balls_in_zone, team_model.balls_in_zone)
        extra_bases = more_interesting(extra_bases, team_model.extra_bases)
        outs_made = more_interesting(outs_made, team_model.outs_made)
        catcher_third_innings_played = more_interesting(
            catcher_third_innings_played, team_model.catcher_third_innings_played
        )
        catcher_caught_stealing = more_interesting(
            catcher_caught_stealing, team_model.catcher_caught_stealing
        )
        catcher_stolen_bases_allowed = more_interesting(
            catcher_stolen_bases_allowed, team_model.catcher_stolen_bases_allowed
        )
        catcher_earned_runs = more_interesting(
            catcher_earned_runs, team_model.catcher_earned_runs
        )
        is_qualified_catcher = more_interesting(
            is_qualified_catcher, team_model.is_qualified_catcher
        )
        is_qualified_pitcher = more_interesting(
            is_qualified_pitcher, team_model.is_qualified_pitcher
        )
        successful_chances = more_interesting(
            successful_chances, team_model.successful_chances
        )
        total_chances = more_interesting(total_chances, team_model.total_chances)
        full_innings_played = more_interesting(
            full_innings_played, team_model.full_innings_played
        )
        part_innings_played = more_interesting(
            part_innings_played, team_model.part_innings_played
        )
        fielding_percentage = more_interesting(
            fielding_percentage, team_model.fielding_percentage
        )
        range_factor = more_interesting(range_factor, team_model.range_factor)
        zone_rating = more_interesting(zone_rating, team_model.zone_rating)
        catcher_caught_stealing_percentage = more_interesting(
            catcher_caught_stealing_percentage,
            team_model.catcher_caught_stealing_percentage,
        )
        catcher_era = more_interesting(catcher_era, team_model.catcher_era)
        def_warbr = more_interesting(def_warbr, team_model.def_warbr)
        perfect_games = more_interesting(perfect_games, team_model.perfect_games)
        wild_pitches = more_interesting(wild_pitches, team_model.wild_pitches)
        third_innings = more_interesting(third_innings, team_model.third_innings)
        team_earned_runs = more_interesting(
            team_earned_runs, team_model.team_earned_runs
        )
        shutouts = more_interesting(shutouts, team_model.shutouts)
        pickoff_attempts = more_interesting(
            pickoff_attempts, team_model.pickoff_attempts
        )
        run_support = more_interesting(run_support, team_model.run_support)
        pitches_as_starter = more_interesting(
            pitches_as_starter, team_model.pitches_as_starter
        )
        quality_starts = more_interesting(quality_starts, team_model.quality_starts)
        inherited_runners = more_interesting(
            inherited_runners, team_model.inherited_runners
        )
        inherited_runners_scored = more_interesting(
            inherited_runners_scored, team_model.inherited_runners_scored
        )
        opponent_total_bases = more_interesting(
            opponent_total_bases, team_model.opponent_total_bases
        )
        is_qualified_saves = more_interesting(
            is_qualified_saves, team_model.is_qualified_saves
        )
        full_innings = more_interesting(full_innings, team_model.full_innings)
        part_innings = more_interesting(part_innings, team_model.part_innings)
        blown_saves = more_interesting(blown_saves, team_model.blown_saves)
        innings = more_interesting(innings, team_model.innings)
        era = more_interesting(era, team_model.era)
        whip = more_interesting(whip, team_model.whip)
        caught_stealing_percentage = more_interesting(
            caught_stealing_percentage, team_model.caught_stealing_percentage
        )
        pitches_per_start = more_interesting(
            pitches_per_start, team_model.pitches_per_start
        )
        pitches_per_inning = more_interesting(
            pitches_per_inning, team_model.pitches_per_inning
        )
        run_support_average = more_interesting(
            run_support_average, team_model.run_support_average
        )
        opponent_average = more_interesting(
            opponent_average, team_model.opponent_average
        )
        opponent_slug_average = more_interesting(
            opponent_slug_average, team_model.opponent_slug_average
        )
        opponent_on_base_percentage = more_interesting(
            opponent_on_base_percentage, team_model.opponent_on_base_percentage
        )
        opponent_ops = more_interesting(opponent_ops, team_model.opponent_ops)
        save_percentage = more_interesting(save_percentage, team_model.save_percentage)
        strikeouts_per_nine_innings = more_interesting(
            strikeouts_per_nine_innings, team_model.strikeouts_per_nine_innings
        )
        strikeout_to_walk_ratio = more_interesting(
            strikeout_to_walk_ratio, team_model.strikeout_to_walk_ratio
        )
        tough_losses = more_interesting(tough_losses, team_model.tough_losses)
        cheap_wins = more_interesting(cheap_wins, team_model.cheap_wins)
        save_opportunities_per_win = more_interesting(
            save_opportunities_per_win, team_model.save_opportunities_per_win
        )
        runs_created = more_interesting(runs_created, team_model.runs_created)
        batting_average = more_interesting(batting_average, team_model.batting_average)
        pinch_average = more_interesting(pinch_average, team_model.pinch_average)
        slug_average = more_interesting(slug_average, team_model.slug_average)
        secondary_average = more_interesting(
            secondary_average, team_model.secondary_average
        )
        on_base_percentage = more_interesting(
            on_base_percentage, team_model.on_base_percentage
        )
        ops = more_interesting(ops, team_model.ops)
        ground_to_fly_ratio = more_interesting(
            ground_to_fly_ratio, team_model.ground_to_fly_ratio
        )
        runs_created_per_27_outs = more_interesting(
            runs_created_per_27_outs, team_model.runs_created_per_27_outs
        )
        batter_rating = more_interesting(batter_rating, team_model.batter_rating)
        at_bats_per_home_run = more_interesting(
            at_bats_per_home_run, team_model.at_bats_per_home_run
        )
        stolen_base_percentage = more_interesting(
            stolen_base_percentage, team_model.stolen_base_percentage
        )
        pitches_per_plate_appearance = more_interesting(
            pitches_per_plate_appearance, team_model.pitches_per_plate_appearance
        )
        isolated_power = more_interesting(isolated_power, team_model.isolated_power)
        walk_to_strikeout_ratio = more_interesting(
            walk_to_strikeout_ratio, team_model.walk_to_strikeout_ratio
        )
        walks_per_plate_appearance = more_interesting(
            walks_per_plate_appearance, team_model.walks_per_plate_appearance
        )
        secondary_average_minus_batting_average = more_interesting(
            secondary_average_minus_batting_average,
            team_model.secondary_average_minus_batting_average,
        )
        runs_produced = more_interesting(runs_produced, team_model.runs_produced)
        runs_ratio = more_interesting(runs_ratio, team_model.runs_ratio)
        patience_ratio = more_interesting(patience_ratio, team_model.patience_ratio)
        balls_in_play_average = more_interesting(
            balls_in_play_average, team_model.balls_in_play_average
        )
        mlb_rating = more_interesting(mlb_rating, team_model.mlb_rating)
        offensive_wins_above_replacement = more_interesting(
            offensive_wins_above_replacement,
            team_model.offensive_wins_above_replacement,
        )
        wins_above_replacement = more_interesting(
            wins_above_replacement, team_model.wins_above_replacement
        )
        earned_runs = more_interesting(earned_runs, team_model.earned_runs)
        batters_hit = more_interesting(batters_hit, team_model.batters_hit)
        sacrifice_bunts = more_interesting(sacrifice_bunts, team_model.sacrifice_bunts)
        save_opportunities = more_interesting(
            save_opportunities, team_model.save_opportunities
        )
        finishes = more_interesting(finishes, team_model.finishes)
        balks = more_interesting(balks, team_model.balks)
        batters_faced = more_interesting(batters_faced, team_model.batters_faced)
        holds = more_interesting(holds, team_model.holds)
        complete_games = more_interesting(complete_games, team_model.complete_games)
        hit_by_pitch = more_interesting(hit_by_pitch, team_model.hit_by_pitch)
        ground_balls = more_interesting(ground_balls, team_model.ground_balls)
        strikeouts = more_interesting(strikeouts, team_model.strikeouts)
        rbis = more_interesting(rbis, team_model.rbis)
        sac_hits = more_interesting(sac_hits, team_model.sac_hits)
        hits = more_interesting(hits, team_model.hits)
        stolen_bases = more_interesting(stolen_bases, team_model.stolen_bases)
        walks = more_interesting(walks, team_model.walks)
        catcher_interference = more_interesting(
            catcher_interference, team_model.catcher_interference
        )
        gidps = more_interesting(gidps, team_model.gidps)
        sacrifice_flies = more_interesting(sacrifice_flies, team_model.sacrifice_flies)
        at_bats = more_interesting(at_bats, team_model.at_bats)
        home_runs = more_interesting(home_runs, team_model.home_runs)
        grand_slam_home_runs = more_interesting(
            grand_slam_home_runs, team_model.grand_slam_home_runs
        )
        runners_left_on_base = more_interesting(
            runners_left_on_base, team_model.runners_left_on_base
        )
        triples = more_interesting(triples, team_model.triples)
        game_winning_rbis = more_interesting(
            game_winning_rbis, team_model.game_winning_rbis
        )
        intentional_walks = more_interesting(
            intentional_walks, team_model.intentional_walks
        )
        doubles = more_interesting(doubles, team_model.doubles)
        fly_balls = more_interesting(fly_balls, team_model.fly_balls)
        caught_stealing = more_interesting(caught_stealing, team_model.caught_stealing)
        pitches = more_interesting(pitches, team_model.pitches)
        games_started = more_interesting(games_started, team_model.games_started)
        pinch_at_bats = more_interesting(pinch_at_bats, team_model.pinch_at_bats)
        pinch_hits = more_interesting(pinch_hits, team_model.pinch_hits)
        player_rating = more_interesting(player_rating, team_model.player_rating)
        is_qualified = more_interesting(is_qualified, team_model.is_qualified)
        is_qualified_steals = more_interesting(
            is_qualified_steals, team_model.is_qualified_steals
        )
        total_bases = more_interesting(total_bases, team_model.total_bases)
        plate_appearances = more_interesting(
            plate_appearances, team_model.plate_appearances
        )
        projected_home_runs = more_interesting(
            projected_home_runs, team_model.projected_home_runs
        )
        extra_base_hits = more_interesting(extra_base_hits, team_model.extra_base_hits)
        average_game_score = more_interesting(
            average_game_score, team_model.average_game_score
        )
        average_field_goals_attempted = more_interesting(
            average_field_goals_attempted, team_model.average_field_goals_attempted
        )
        average_three_point_field_goals_made = more_interesting(
            average_three_point_field_goals_made,
            team_model.average_three_point_field_goals_made,
        )
        average_three_point_field_goals_attempted = more_interesting(
            average_three_point_field_goals_attempted,
            team_model.average_three_point_field_goals_attempted,
        )
        average_free_throws_made = more_interesting(
            average_free_throws_made, team_model.average_free_throws_made
        )
        average_free_throws_attempted = more_interesting(
            average_free_throws_attempted, team_model.average_free_throws_attempted
        )
        average_points = more_interesting(average_points, team_model.average_points)
        average_offensive_rebounds = more_interesting(
            average_offensive_rebounds, team_model.average_offensive_rebounds
        )
        average_assists = more_interesting(average_assists, team_model.average_assists)
        average_turnovers = more_interesting(
            average_turnovers, team_model.average_turnovers
        )
        offensive_rebound_percentage = more_interesting(
            offensive_rebound_percentage, team_model.offensive_rebound_percentage
        )
        estimated_possessions = more_interesting(
            estimated_possessions, team_model.estimated_possessions
        )
        average_estimated_possessions = more_interesting(
            average_estimated_possessions, team_model.average_estimated_possessions
        )
        points_per_estimated_possessions = more_interesting(
            points_per_estimated_possessions,
            team_model.points_per_estimated_possessions,
        )
        average_team_turnovers = more_interesting(
            average_team_turnovers, team_model.average_team_turnovers
        )
        average_total_turnovers = more_interesting(
            average_total_turnovers, team_model.average_total_turnovers
        )
        two_point_field_goals_made = more_interesting(
            two_point_field_goals_made, team_model.two_point_field_goals_made
        )
        two_point_field_goals_attempted = more_interesting(
            two_point_field_goals_attempted, team_model.two_point_field_goals_attempted
        )
        average_two_point_field_goals_made = more_interesting(
            average_two_point_field_goals_made,
            team_model.average_two_point_field_goals_made,
        )
        average_two_point_field_goals_attempted = more_interesting(
            average_two_point_field_goals_attempted,
            team_model.average_two_point_field_goals_attempted,
        )
        two_point_field_goal_percentage = more_interesting(
            two_point_field_goal_percentage, team_model.two_point_field_goal_percentage
        )
        shooting_efficiency = more_interesting(
            shooting_efficiency, team_model.shooting_efficiency
        )
        scoring_efficiency = more_interesting(
            scoring_efficiency, team_model.scoring_efficiency
        )
        average_48_field_goals_made = more_interesting(
            average_48_field_goals_made, team_model.average_48_field_goals_made
        )
        average_48_field_goals_attempted = more_interesting(
            average_48_field_goals_attempted,
            team_model.average_48_field_goals_attempted,
        )
        average_48_three_point_field_goals_made = more_interesting(
            average_48_three_point_field_goals_made,
            team_model.average_48_three_point_field_goals_made,
        )
        average_48_three_point_field_goals_attempted = more_interesting(
            average_48_three_point_field_goals_attempted,
            team_model.average_48_three_point_field_goals_attempted,
        )
        average_48_free_throws_made = more_interesting(
            average_48_free_throws_made, team_model.average_48_free_throws_made
        )
        average_48_free_throws_attempted = more_interesting(
            average_48_free_throws_attempted,
            team_model.average_48_free_throws_attempted,
        )
        average_48_points = more_interesting(
            average_48_points, team_model.average_48_points
        )
        average_48_offensive_rebounds = more_interesting(
            average_48_offensive_rebounds, team_model.average_48_offensive_rebounds
        )
        average_48_assists = more_interesting(
            average_48_assists, team_model.average_48_assists
        )
        average_48_turnovers = more_interesting(
            average_48_turnovers, team_model.average_48_turnovers
        )
        average_rebounds = more_interesting(
            average_rebounds, team_model.average_rebounds
        )
        average_fouls = more_interesting(average_fouls, team_model.average_fouls)
        average_flagrant_fouls = more_interesting(
            average_flagrant_fouls, team_model.average_flagrant_fouls
        )
        average_technical_fouls = more_interesting(
            average_technical_fouls, team_model.average_technical_fouls
        )
        average_ejections = more_interesting(
            average_ejections, team_model.average_ejections
        )
        average_disqualifications = more_interesting(
            average_disqualifications, team_model.average_disqualifications
        )
        assist_turnover_ratio = more_interesting(
            assist_turnover_ratio, team_model.assist_turnover_ratio
        )
        steal_foul_ratio = more_interesting(
            steal_foul_ratio, team_model.steal_foul_ratio
        )
        block_foul_ratio = more_interesting(
            block_foul_ratio, team_model.block_foul_ratio
        )
        average_team_rebounds = more_interesting(
            average_team_rebounds, team_model.average_team_rebounds
        )
        total_technical_fouls = more_interesting(
            total_technical_fouls, team_model.total_technical_fouls
        )
        team_assist_turnover_ratio = more_interesting(
            team_assist_turnover_ratio, team_model.team_assist_turnover_ratio
        )
        steal_turnover_ratio = more_interesting(
            steal_turnover_ratio, team_model.steal_turnover_ratio
        )
        average_48_rebounds = more_interesting(
            average_48_rebounds, team_model.average_48_rebounds
        )
        average_48_fouls = more_interesting(
            average_48_fouls, team_model.average_48_fouls
        )
        average_48_flagrant_fouls = more_interesting(
            average_48_flagrant_fouls, team_model.average_48_flagrant_fouls
        )
        average_48_technical_fouls = more_interesting(
            average_48_technical_fouls, team_model.average_48_technical_fouls
        )
        average_48_ejections = more_interesting(
            average_48_ejections, team_model.average_48_ejections
        )
        average_48_disqualifications = more_interesting(
            average_48_disqualifications, team_model.average_48_disqualifications
        )
        double_double = more_interesting(double_double, team_model.double_double)
        triple_double = more_interesting(triple_double, team_model.triple_double)
        field_goals_made = more_interesting(
            field_goals_made, team_model.field_goals_made
        )
        free_throws_made = more_interesting(
            free_throws_made, team_model.free_throws_made
        )
        three_point_percentage = more_interesting(
            three_point_percentage, team_model.three_point_percentage
        )
        three_point_field_goals_made = more_interesting(
            three_point_field_goals_made, team_model.three_point_field_goals_made
        )
        team_turnovers = more_interesting(team_turnovers, team_model.team_turnovers)
        total_turnovers = more_interesting(total_turnovers, team_model.total_turnovers)
        points_in_paint = more_interesting(points_in_paint, team_model.points_in_paint)
        brick_index = more_interesting(brick_index, team_model.brick_index)
        fast_break_points = more_interesting(
            fast_break_points, team_model.fast_break_points
        )
        average_field_goals_made = more_interesting(
            average_field_goals_made, team_model.average_field_goals_made
        )
        turnover_points = more_interesting(turnover_points, team_model.turnover_points)
        average_defensive_rebounds = more_interesting(
            average_defensive_rebounds, team_model.average_defensive_rebounds
        )
        average_blocks = more_interesting(average_blocks, team_model.average_blocks)
        average_steals = more_interesting(average_steals, team_model.average_steals)
        average_48_defensive_rebounds = more_interesting(
            average_48_defensive_rebounds, team_model.average_48_defensive_rebounds
        )
        average_48_blocks = more_interesting(
            average_48_blocks, team_model.average_48_blocks
        )
        average_48_steals = more_interesting(
            average_48_steals, team_model.average_48_steals
        )
        largest_lead = more_interesting(largest_lead, team_model.largest_lead)
        disqualifications = more_interesting(
            disqualifications, team_model.disqualifications
        )
        flagrant_fouls = more_interesting(flagrant_fouls, team_model.flagrant_fouls)
        fouls = more_interesting(fouls, team_model.fouls)
        ejections = more_interesting(ejections, team_model.ejections)
        technical_fouls = more_interesting(technical_fouls, team_model.technical_fouls)
        vorp = more_interesting(vorp, team_model.vorp)
        average_minutes = more_interesting(average_minutes, team_model.average_minutes)
        nba_rating = more_interesting(nba_rating, team_model.nba_rating)

    player_list = [
        create_combined_player_model(v, k, player_ffill) for k, v in players.items()
    ]
    player_list.sort(key=functools.cmp_to_key(_compare_player_models))

    team_model = TeamModel.model_construct(
        identifier=identifier,
        name=team_models[0].name,
        location=location,
        players=player_list,
        odds=[x[0] for x in odds.values()],
        points=points,
        ladder_rank=ladder_rank,
        news=sorted(news.values(), key=lambda x: x.published),
        social=sorted(social.values(), key=lambda x: x.published),
        field_goals=field_goals,
        coaches=[
            create_combined_coach_model(v, k, coach_ffill) for k, v in coaches.items()
        ],
        lbw=lbw,
        end_dt=end_dt,
        runs=runs,
        wickets=wickets,
        overs=overs,
        balls=balls,
        byes=byes,
        leg_byes=leg_byes,
        wides=wides,
        no_balls=no_balls,
        penalties=penalties,
        balls_per_over=balls_per_over,
        fours=fours,
        sixes=sixes,
        catches=catches,
        catches_dropped=catches_dropped,
        disposal_efficiency=disposal_efficiency,
        uncontested_marks=uncontested_marks,
        total_possessions=total_possessions,
        tackles_inside_50=tackles_inside_50,
        centre_clearances=centre_clearances,
        stoppage_clearances=stoppage_clearances,
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
        pitch_count=pitch_count,
        strikes=strikes,
        strike_pitch_ratio=strike_pitch_ratio,
        games_played=games_played,
        team_games_played=team_games_played,
        double_plays=double_plays,
        opportunities=opportunities,
        errors=errors,
        passed_balls=passed_balls,
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
        average_game_score=average_game_score,
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
        field_goals_made=field_goals_made,
        free_throws_made=free_throws_made,
        three_point_percentage=three_point_percentage,
        three_point_field_goals_made=three_point_field_goals_made,
        team_turnovers=team_turnovers,
        total_turnovers=total_turnovers,
        points_in_paint=points_in_paint,
        brick_index=brick_index,
        fast_break_points=fast_break_points,
        average_field_goals_made=average_field_goals_made,
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
        version=VERSION,
    )

    ffill(team_ffill, identifier, team_model)

    return team_model
