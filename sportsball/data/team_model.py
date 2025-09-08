"""The prototype class for a team."""

# pylint: disable=duplicate-code
import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from .coach_model import VERSION as COACH_VERSION
from .coach_model import CoachModel
from .delimiter import DELIMITER
from .field_type import FFILL_KEY, TYPE_KEY, FieldType
from .news_model import NewsModel
from .odds_model import OddsModel
from .player_model import VERSION as PLAYER_VERSION
from .player_model import PlayerModel
from .social_model import SocialModel

TEAM_POINTS_COLUMN: Literal["points"] = "points"
TEAM_IDENTIFIER_COLUMN: Literal["identifier"] = "identifier"
PLAYER_COLUMN_PREFIX: Literal["players"] = "players"
NAME_COLUMN: Literal["name"] = "name"
FIELD_GOALS_COLUMN: Literal["field_goals"] = "field_goals"
FIELD_GOALS_ATTEMPTED_COLUMN: Literal["field_goals_attempted"] = "field_goals_attempted"
OFFENSIVE_REBOUNDS_COLUMN: Literal["offensive_rebounds"] = "offensive_rebounds"
ASSISTS_COLUMN: Literal["assists"] = "assists"
TURNOVERS_COLUMN: Literal["turnovers"] = "turnovers"
KICKS_COLUMN: Literal["kicks"] = "kicks"
TEAM_ODDS_COLUMN: Literal["odds"] = "odds"
TEAM_MARKS_COLUMN: Literal["marks"] = "marks"
TEAM_HANDBALLS_COLUMN: Literal["handballs"] = "handballs"
TEAM_DISPOSALS_COLUMN: Literal["disposals"] = "disposals"
TEAM_GOALS_COLUMN: Literal["goals"] = "goals"
TEAM_BEHINDS_COLUMN: Literal["behinds"] = "behinds"
TEAM_HIT_OUTS_COLUMN: Literal["hit_outs"] = "hit_outs"
TEAM_TACKLES_COLUMN: Literal["tackles"] = "tackles"
TEAM_REBOUNDS_COLUMN: Literal["rebounds"] = "rebounds"
TEAM_INSIDES_COLUMN: Literal["insides"] = "insides"
TEAM_CLEARANCES_COLUMN: Literal["clearances"] = "clearances"
TEAM_CLANGERS_COLUMN: Literal["clangers"] = "clangers"
TEAM_FREE_KICKS_FOR_COLUMN: Literal["free_kicks_for"] = "free_kicks_for"
TEAM_FREE_KICKS_AGAINST_COLUMN: Literal["free_kicks_against"] = "free_kicks_against"
TEAM_BROWNLOW_VOTES_COLUMN: Literal["brownlow_votes"] = "brownlow_votes"
TEAM_CONTESTED_POSSESSIONS_COLUMN: Literal["contested_possessions"] = (
    "contested_possessions"
)
TEAM_UNCONTESTED_POSSESSIONS_COLUMN: Literal["uncontested_possessions"] = (
    "uncontested_possessions"
)
TEAM_CONTESTED_MARKS_COLUMN: Literal["contested_marks"] = "contested_marks"
TEAM_MARKS_INSIDE_COLUMN: Literal["marks_inside"] = "marks_inside"
TEAM_ONE_PERCENTERS_COLUMN: Literal["one_percenters"] = "one_percenters"
TEAM_BOUNCES_COLUMN: Literal["bounces"] = "bounces"
TEAM_GOAL_ASSISTS_COLUMN: Literal["goal_assists"] = "goal_assists"
TEAM_NEWS_COLUMN: Literal["news"] = "news"
TEAM_COACHES_COLUMN: Literal["coaches"] = "coaches"
TEAM_LENGTH_BEHIND_WINNER_COLUMN: Literal["lbw"] = "lbw"
TEAM_END_DT_COLUMN: Literal["end_dt"] = "end_dt"
TEAM_FIELD_GOALS_PERCENTAGE_COLUMN: Literal["field_goals_percentage"] = (
    "field_goals_percentage"
)
TEAM_THREE_POINT_FIELD_GOALS_COLUMN: Literal["three_point_field_goals"] = (
    "three_point_field_goals"
)
TEAM_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "three_point_field_goals_attempted"
] = "three_point_field_goals_attempted"
TEAM_THREE_POINT_FIELD_GOALS_PERCENTAGE_COLUMN: Literal[
    "three_point_field_goals_percentage"
] = "three_point_field_goals_percentage"
TEAM_FREE_THROWS_COLUMN: Literal["free_throws"] = "free_throws"
TEAM_FREE_THROWS_ATTEMPTED_COLUMN: Literal["free_throws_attempted"] = (
    "free_throws_attempted"
)
TEAM_FREE_THROWS_PERCENTAGE_COLUMN: Literal["free_throws_percentage"] = (
    "free_throws_percentage"
)
TEAM_DEFENSIVE_REBOUNDS_COLUMN: Literal["defensive_rebounds"] = "defensive_rebounds"
TEAM_TOTAL_REBOUNDS_COLUMN: Literal["total_rebounds"] = "total_rebounds"
TEAM_STEALS_COLUMN: Literal["steals"] = "steals"
TEAM_BLOCKS_COLUMN: Literal["blocks"] = "blocks"
TEAM_PERSONAL_FOULS_COLUMN: Literal["personal_fouls"] = "personal_fouls"
TEAM_FORCED_FUMBLES_COLUMN: Literal["forced_fumbles"] = "forced_fumbles"
TEAM_FUMBLES_RECOVERED_COLUMN: Literal["fumbles_recovered"] = "fumbles_recovered"
TEAM_FUMBLES_TOUCHDOWNS_COLUMN: Literal["fumbles_touchdowns"] = "fumbles_touchdowns"
TEAM_RUNS_COLUMN: Literal["runs"] = "runs"
TEAM_WICKETS_COLUMN: Literal["wickets"] = "wickets"
TEAM_OVERS_COLUMN: Literal["overs"] = "overs"
TEAM_BALLS_COLUMN: Literal["balls"] = "balls"
TEAM_BYES_COLUMN: Literal["byes"] = "byes"
TEAM_LEG_BYES_COLUMN: Literal["leg_byes"] = "leg_byes"
TEAM_WIDES_COLUMN: Literal["wides"] = "wides"
TEAM_NO_BALLS_COLUMN: Literal["no_balls"] = "no_balls"
TEAM_PENALTIES_COLUMN: Literal["penalties"] = "penalties"
TEAM_BALLS_PER_OVER_COLUMN: Literal["balls_per_over"] = "balls_per_over"
TEAM_FOURS_COLUMN: Literal["fours"] = "fours"
TEAM_SIXES_COLUMN: Literal["sixes"] = "sixes"
TEAM_CATCHES_COLUMN: Literal["catches"] = "catches"
TEAM_CATCHES_DROPPED_COLUMN: Literal["catches_dropped"] = "catches_dropped"
TEAM_TACKLES_INSIDE_50_COLUMN: Literal["tackles_inside_50"] = "tackles_inside_50"
TEAM_TOTAL_POSSESSIONS_COLUMN: Literal["total_possessions"] = "total_possessions"
TEAM_UNCONTESTED_MARKS_COLUMN: Literal["uncontested_marks"] = "uncontested_marks"
TEAM_DISPOSAL_EFFICIENCY_COLUMN: Literal["disposal_efficiency"] = "disposal_efficiency"
TEAM_CENTRE_CLEARANCES_COLUMN: Literal["centre_clearances"] = "centre_clearances"
TEAM_STOPPAGE_CLEARANCES_COLUMN: Literal["stoppage_clearances"] = "stoppage_clearances"
TEAM_GOAL_ACCURACY_COLUMN: Literal["goal_accuracy"] = "goal_accuracy"
TEAM_RUSHED_BEHINDS_COLUMN: Literal["rushed_behinds"] = "rushed_behinds"
TEAM_TOUCHED_BEHINDS_COLUMN: Literal["touched_behinds"] = "touched_behinds"
TEAM_LEFT_BEHINDS_COLUMN: Literal["left_behinds"] = "left_behinds"
TEAM_LEFT_POSTERS_COLUMN: Literal["left_posters"] = "left_posters"
TEAM_RIGHT_BEHINDS_COLUMN: Literal["right_behinds"] = "right_behinds"
TEAM_RIGHT_POSTERS_COLUMN: Literal["right_posters"] = "right_posters"
TEAM_TOTAL_INTERCHANGE_COUNT_COLUMN: Literal["total_interchange_count"] = (
    "total_interchange_count"
)
TEAM_INTERCHANGE_COUNT_Q1_COLUMN: Literal["interchange_count_q1"] = (
    "interchange_count_q1"
)
TEAM_INTERCHANGE_COUNT_Q2_COLUMN: Literal["interchange_count_q2"] = (
    "interchange_count_q2"
)
TEAM_INTERCHANGE_COUNT_Q3_COLUMN: Literal["interchange_count_q3"] = (
    "interchange_count_q3"
)
TEAM_INTERCHANGE_COUNT_Q4_COLUMN: Literal["interchange_count_q4"] = (
    "interchange_count_q4"
)
TEAM_GAME_WINNING_GOALS_COLUMN: Literal["game_winning_goals"] = "game_winning_goals"
TEAM_HEADED_GOALS_COLUMN: Literal["headed_goals"] = "headed_goals"
TEAM_INACCURATE_CROSSES_COLUMN: Literal["inaccurate_crosses"] = "inaccurate_crosses"
TEAM_INACCURATE_LONGBALLS_COLUMN: Literal["inaccurate_long_balls"] = (
    "inaccurate_long_balls"
)
TEAM_INACCURATE_PASSES_COLUMN: Literal["inaccurate_passes"] = "inaccurate_passes"
TEAM_INACCURATE_THROUGH_BALLS_COLUMN: Literal["inaccurate_through_balls"] = (
    "inaccurate_through_balls"
)
TEAM_LEFT_FOOTED_SHOTS_COLUMN: Literal["left_footed_shots"] = "left_footed_shots"
TEAM_LONGBALL_PERCENTAGE_COLUMN: Literal["longball_percentage"] = "longball_percentage"
TEAM_OFFSIDES_COLUMN: Literal["offsides"] = "offsides"
TEAM_PENALTY_KICK_GOALS_COLUMN: Literal["penalty_kick_goals"] = "penalty_kick_goals"
TEAM_PENALTY_KICK_PERCENTAGE_COLUMN: Literal["penalty_kick_percentage"] = (
    "penalty_kick_percentage"
)
TEAM_PENALTY_KICK_SHOTS_COLUMN: Literal["penalty_kick_shots"] = "penalty_kick_shots"
TEAM_PENALTY_KICKS_MISSED_COLUMN: Literal["penalty_kicks_missed"] = (
    "penalty_kicks_missed"
)
TEAM_POSSESSION_PERCENTAGE_COLUMN: Literal["possession_percentage"] = (
    "possession_percentage"
)
TEAM_POSSESSION_TIME_COLUMN: Literal["possession_time"] = "possession_time"
TEAM_RIGHT_FOOTED_SHOTS_COLUMN: Literal["right_footed_shots"] = "right_footed_shots"
TEAM_SHOOT_OUT_GOALS_COLUMN: Literal["shoot_out_goals"] = "shoot_out_goals"
TEAM_SHOOT_OUT_MISSES_COLUMN: Literal["shoot_out_misses"] = "shoot_out_misses"
TEAM_SHOOT_OUT_PERCENTAGE_COLUMN: Literal["shoot_out_percentage"] = (
    "shoot_out_percentage"
)
TEAM_SHOT_ASSISTS_COLUMN: Literal["shot_assists"] = "shot_assists"
TEAM_SHOT_PERCENTAGE_COLUMN: Literal["shot_percentage"] = "shot_percentage"
TEAM_SHOTS_HEADED_COLUMN: Literal["shots_headed"] = "shots_headed"
TEAM_SHOTS_OFF_TARGET_COLUMN: Literal["shots_off_target"] = "shots_off_target"
TEAM_SHOTS_ON_POST_COLUMN: Literal["shots_on_post"] = "shots_on_post"
TEAM_SHOTS_ON_TARGET_COLUMN: Literal["shots_on_target"] = "shots_on_target"
TEAM_THROUGH_BALL_PERCENTAGE_COLUMN: Literal["through_ball_percentage"] = (
    "through_ball_percentage"
)
TEAM_TOTAL_CROSSES_COLUMN: Literal["total_crosses"] = "total_crosses"
TEAM_TOTAL_GOALS_COLUMN: Literal["total_goals"] = "total_goals"
TEAM_TOTAL_LONGBALLS_COLUMN: Literal["total_long_balls"] = "total_long_balls"
TEAM_TOTAL_PASSES_COLUMN: Literal["total_passes"] = "total_passes"
TEAM_TOTAL_SHOTS_COLUMN: Literal["total_shots"] = "total_shots"
TEAM_TOTAL_THROUGH_BALLS_COLUMN: Literal["total_through_balls"] = "total_through_balls"
TEAM_DRAWS_COLUMN: Literal["draws"] = "draws"
TEAM_SUB_OUTS_COLUMN: Literal["sub_outs"] = "sub_outs"
TEAM_SUSPENSIONS_COLUMN: Literal["suspensions"] = "suspensions"
TEAM_TIME_ENDED_COLUMN: Literal["time_ended"] = "time_ended"
TEAM_TIME_STARTED_COLUMN: Literal["time_started"] = "time_started"
TEAM_WIN_PERCENTAGE_COLUMN: Literal["win_percentage"] = "win_percentage"
TEAM_WINS_COLUMN: Literal["wins"] = "wins"
TEAM_WON_CORNERS_COLUMN: Literal["won_corners"] = "won_corners"
TEAM_YELLOW_CARDS_COLUMN: Literal["yellow_cards"] = "yellow_cards"
TEAM_CLEAN_SHEET_COLUMN: Literal["clean_sheet"] = "clean_sheet"
TEAM_CROSSES_CAUGHT_COLUMN: Literal["crosses_caught"] = "crosses_caught"
TEAM_GOALS_CONCEDED_COLUMN: Literal["goals_conceded"] = "goals_conceded"
TEAM_PARTIAL_CLEAN_SHEET_COLUMN: Literal["partial_clean_sheet"] = "partial_clean_sheet"
TEAM_PENALTY_KICK_CONCEDED_COLUMN: Literal["penalty_kick_conceded"] = (
    "penalty_kick_conceded"
)
TEAM_PENALTY_KICK_SAVE_PERCENTAGE_COLUMN: Literal["penalty_kick_save_percentage"] = (
    "penalty_kick_save_percentage"
)
TEAM_PENALTY_KICKS_FACED_COLUMN: Literal["penalty_kicks_faced"] = "penalty_kicks_faced"
TEAM_PENALTY_KICKS_SAVED_COLUMN: Literal["penalty_kicks_saved"] = "penalty_kicks_saved"
TEAM_PUNCHES_COLUMN: Literal["punches"] = "punches"
TEAM_SAVES_COLUMN: Literal["saves"] = "saves"
TEAM_SHOOT_OUT_KICKS_FACED_COLUMN: Literal["shoot_out_kicks_faced"] = (
    "shoot_out_kicks_faced"
)
TEAM_SHOOT_OUT_KICKS_SAVED_COLUMN: Literal["shoot_out_kicks_saved"] = (
    "shoot_out_kicks_saved"
)
TEAM_SHOOT_OUT_SAVE_PERCENTAGE_COLUMN: Literal["shoot_out_save_percentage"] = (
    "shoot_out_save_percentage"
)
TEAM_SHOTS_FACED_COLUMN: Literal["shots_faced"] = "shots_faced"
TEAM_SMOTHERS_COLUMN: Literal["smothers"] = "smothers"
TEAM_UNCLAIMED_CROSSES_COLUMN: Literal["unclaimed_crosses"] = "unclaimed_crosses"
TEAM_ACCURATE_CROSSES_COLUMN: Literal["accurate_crosses"] = "accurate_crosses"
TEAM_ACCURATE_LONG_BALLS_COLUMN: Literal["accurate_long_balls"] = "accurate_long_balls"
TEAM_ACCURATE_PASSES_COLUMN: Literal["accurate_passes"] = "accurate_passes"
TEAM_ACCURATE_THROUGH_BALLS_COLUMN: Literal["accurate_through_balls"] = (
    "accurate_through_balls"
)
TEAM_CROSS_PERCENTAGE_COLUMN: Literal["cross_percentage"] = "cross_percentage"
TEAM_FREE_KICK_GOALS_COLUMN: Literal["free_kick_goals"] = "free_kick_goals"
TEAM_FREE_KICK_PERCENTAGE_COLUMN: Literal["free_kick_percentage"] = (
    "free_kick_percentage"
)
TEAM_FREE_KICK_SHOTS_COLUMN: Literal["free_kick_shots"] = "free_kick_shots"
TEAM_GAME_WINNING_ASSISTS_COLUMN: Literal["game_winning_assists"] = (
    "game_winning_assists"
)
TEAM_BLOCKED_SHOTS_COLUMN: Literal["blocked_shots"] = "blocked_shots"
TEAM_EFFECTIVE_CLEARANCES_COLUMN: Literal["effective_clearances"] = (
    "effective_clearances"
)
TEAM_EFFECTIVE_TACKLES_COLUMN: Literal["effective_tackles"] = "effective_tackles"
TEAM_INEFFECTIVE_TACKLES_COLUMN: Literal["ineffective_tackles"] = "ineffective_tackles"
TEAM_INTERCEPTIONS_COLUMN: Literal["interceptions"] = "interceptions"
TEAM_TACKLE_PERCENTAGE_COLUMN: Literal["tackle_percentage"] = "tackle_percentage"
TEAM_APPEARANCES_COLUMN: Literal["appearances"] = "appearances"
TEAM_AVERAGE_RATING_FROM_CORRESPONDENT_COLUMN: Literal[
    "average_rating_from_correspondent"
] = "average_rating_from_correspondent"
TEAM_AVERAGE_RATING_FROM_DATA_FEED_COLUMN: Literal["average_rating_from_data_feed"] = (
    "average_rating_from_data_feed"
)
TEAM_AVERAGE_RATING_FROM_EDITOR_COLUMN: Literal["average_rating_from_editor"] = (
    "average_rating_from_editor"
)
TEAM_AVERAGE_RATING_FROM_USER_COLUMN: Literal["average_rating_from_user"] = (
    "average_rating_from_user"
)
TEAM_DID_NOT_PLAY_COLUMN: Literal["did_not_play"] = "did_not_play"
TEAM_FOULS_COMMITTED_COLUMN: Literal["fouls_committed"] = "fouls_committed"
TEAM_FOULS_SUFFERED_COLUMN: Literal["fouls_suffered"] = "fouls_suffered"
TEAM_GOAL_DIFFERENCE_COLUMN: Literal["goal_difference"] = "goal_difference"
TEAM_LOSSES_COLUMN: Literal["losses"] = "losses"
TEAM_LOST_CORNERS_COLUMN: Literal["lost_corners"] = "lost_corners"
TEAM_MINUTES_COLUMN: Literal["minutes"] = "minutes"
TEAM_OWN_GOALS_COLUMN: Literal["own_goals"] = "own_goals"
TEAM_PASS_PERCENTAGE_COLUMN: Literal["pass_percentage"] = "pass_percentage"
TEAM_RED_CARDS_COLUMN: Literal["red_cards"] = "red_cards"
TEAM_STARTS_COLUMN: Literal["starts"] = "starts"
TEAM_SUB_INS_COLUMN: Literal["sub_ins"] = "sub_ins"
TEAM_PITCH_COUNT_COLUMN: Literal["pitch_count"] = "pitch_count"
TEAM_STRIKES_COLUMN: Literal["strikes"] = "strikes"
TEAM_STRIKE_PITCH_RATIO_COLUMN: Literal["strike_pitch_ratio"] = "strike_pitch_ratio"
TEAM_GAMES_PLAYED_COLUMN: Literal["games_played"] = "games_played"
TEAM_TEAM_GAMES_PLAYED_COLUMN: Literal["team_games_played"] = "team_games_played"
TEAM_DOUBLE_PLAYS_COLUMN: Literal["double_plays"] = "double_plays"
TEAM_OPPORTUNITIES_COLUMN: Literal["opportunities"] = "opportunities"
TEAM_ERRORS_COLUMN: Literal["errors"] = "errors"
TEAM_PASSED_BALLS_COLUMN: Literal["passed_balls"] = "passed_balls"
TEAM_OUTFIELD_ASSISTS_COLUMN: Literal["outfield_assists"] = "outfield_assists"
TEAM_PICKOFFS_COLUMN: Literal["pickoffs"] = "pickoffs"
TEAM_PUTOUTS_COLUMN: Literal["putouts"] = "putouts"
TEAM_OUTS_ON_FIELD_COLUMN: Literal["outs_on_field"] = "outs_on_field"
TEAM_TRIPLE_PLAYS_COLUMN: Literal["triple_plays"] = "triple_plays"
TEAM_BALLS_IN_ZONE_COLUMN: Literal["balls_in_zone"] = "balls_in_zone"
TEAM_EXTRA_BASES_COLUMN: Literal["extra_bases"] = "extra_bases"
TEAM_OUTS_MADE_COLUMN: Literal["outs_made"] = "outs_made"
TEAM_CATCHER_THIRD_INNINGS_PLAYED_COLUMN: Literal["catcher_third_innings_played"] = (
    "catcher_third_innings_played"
)
TEAM_CATCHER_CAUGHT_STEALING_COLUMN: Literal["catcher_caught_stealing"] = (
    "catcher_caught_stealing"
)
TEAM_CATCHER_STOLEN_BASES_ALLOWED_COLUMN: Literal["catcher_stolen_bases_allowed"] = (
    "catcher_stolen_bases_allowed"
)
TEAM_CATCHER_EARNED_RUNS_COLUMN: Literal["catcher_earned_runs"] = "catcher_earned_runs"
TEAM_IS_QUALIFIED_CATCHER_COLUMN: Literal["is_qualified_catcher"] = (
    "is_qualified_catcher"
)
TEAM_IS_QUALIFIED_PITCHER_COLUMN: Literal["is_qualified_pitcher"] = (
    "is_qualified_pitcher"
)
TEAM_SUCCESSFUL_CHANCES_COLUMN: Literal["successful_chances"] = "successful_chances"
TEAM_TOTAL_CHANCES_COLUMN: Literal["total_chances"] = "total_chances"
TEAM_FULL_INNINGS_PLAYED_COLUMN: Literal["full_innings_played"] = "full_innings_played"
TEAM_PART_INNINGS_PLAYED_COLUMN: Literal["part_innings_played"] = "part_innings_played"
TEAM_FIELDING_PERCENTAGE_COLUMN: Literal["fielding_percentage"] = "fielding_percentage"
TEAM_RANGE_FACTOR_COLUMN: Literal["range_factor"] = "range_factor"
TEAM_ZONE_RATING_COLUMN: Literal["zone_rating"] = "zone_rating"
TEAM_CATCHER_CAUGHT_STEALING_PERCENTAGE_COLUMN: Literal[
    "catcher_caught_stealing_percentage"
] = "catcher_caught_stealing_percentage"
TEAM_CATCHER_ERA_COLUMN: Literal["catcher_era"] = "catcher_era"
TEAM_DEF_WARBR_COLUMN: Literal["def_warbr"] = "def_warbr"
TEAM_PERFECT_GAMES_COLUMN: Literal["perfect_games"] = "perfect_games"
TEAM_WILD_PITCHES_COLUMN: Literal["wild_pitches"] = "wild_pitches"
TEAM_THIRD_INNINGS_COLUMN: Literal["third_innings"] = "third_innings"
TEAM_TEAM_EARNED_RUNS_COLUMN: Literal["team_earned_runs"] = "team_earned_runs"
TEAM_SHUTOUTS_COLUMN: Literal["shutouts"] = "shutouts"
TEAM_PICKOFF_ATTEMPTS_COLUMN: Literal["pickoff_attempts"] = "pickoff_attempts"
TEAM_RUN_SUPPORT_COLUMN: Literal["run_support"] = "run_support"
TEAM_PITCHES_AS_STARTER_COLUMN: Literal["pitches_as_starter"] = "pitches_as_starter"
TEAM_QUALITY_STARTS_COLUMN: Literal["quality_starts"] = "quality_starts"
TEAM_INHERITED_RUNNERS_COLUMN: Literal["inherited_runners"] = "inherited_runners"
TEAM_INHERITED_RUNNERS_SCORED_COLUMN: Literal["inherited_runners_scored"] = (
    "inherited_runners_scored"
)
TEAM_OPPONENT_TOTAL_BASES_COLUMN: Literal["opponent_total_bases"] = (
    "opponent_total_bases"
)
TEAM_IS_QUALIFIED_SAVES_COLUMN: Literal["is_qualified_saves"] = "is_qualified_saves"
TEAM_FULL_INNINGS_COLUMN: Literal["full_innings"] = "full_innings"
TEAM_PART_INNINGS_COLUMN: Literal["part_innings"] = "part_innings"
TEAM_BLOWN_SAVES_COLUMN: Literal["blown_saves"] = "blown_saves"
TEAM_INNINGS_COLUMN: Literal["innings"] = "innings"
TEAM_ERA_COLUMN: Literal["era"] = "era"
TEAM_WHIP_COLUMN: Literal["whip"] = "whip"
TEAM_CAUGHT_STEALING_PERCENTAGE_COLUMN: Literal["caught_stealing_percentage"] = (
    "caught_stealing_percentage"
)
TEAM_PITCHES_PER_START_COLUMN: Literal["pitches_per_start"] = "pitches_per_start"
TEAM_PITCHES_PER_INNING_COLUMN: Literal["pitches_per_inning"] = "pitches_per_inning"
TEAM_RUN_SUPPORT_AVERAGE_COLUMN: Literal["run_support_average"] = "run_support_average"
TEAM_OPPONENT_AVERAGE_COLUMN: Literal["opponent_average"] = "opponent_average"
TEAM_OPPONENT_SLUG_AVERAGE_COLUMN: Literal["opponent_slug_average"] = (
    "opponent_slug_average"
)
TEAM_OPPONENT_ON_BASE_PERCENTAGE_COLUMN: Literal["opponent_on_base_percentage"] = (
    "opponent_on_base_percentage"
)
TEAM_OPPONENT_OPS_COLUMN: Literal["opponent_ops"] = "opponent_ops"
TEAM_SAVE_PERCENTAGE_COLUMN: Literal["save_percentage"] = "save_percentage"
TEAM_STRIKEOUTS_PER_NINE_INNINGS_COLUMN: Literal["strikeouts_per_nine_innings"] = (
    "strikeouts_per_nine_innings"
)
TEAM_STRIKEOUT_TO_WALK_RATIO_COLUMN: Literal["strikeout_to_walk_ratio"] = (
    "strikeout_to_walk_ratio"
)
TEAM_TOUGH_LOSSES_COLUMN: Literal["tough_losses"] = "tough_losses"
TEAM_CHEAP_WINS_COLUMN: Literal["cheap_wins"] = "cheap_wins"
TEAM_SAVE_OPPORTUNITIES_PER_WIN_COLUMN: Literal["save_opportunities_per_win"] = (
    "save_opportunities_per_win"
)
TEAM_RUNS_CREATED_COLUMN: Literal["runs_created"] = "runs_created"
TEAM_BATTING_AVERAGE_COLUMN: Literal["batting_average"] = "batting_average"
TEAM_PINCH_AVERAGE_COLUMN: Literal["pinch_average"] = "pinch_average"
TEAM_SLUG_AVERAGE_COLUMN: Literal["slug_average"] = "slug_average"
TEAM_SECONDARY_AVERAGE_COLUMN: Literal["secondary_average"] = "secondary_average"
TEAM_ON_BASE_PERCENTAGE_COLUMN: Literal["on_base_percentage"] = "on_base_percentage"
TEAM_OPS_COLUMN: Literal["ops"] = "ops"
TEAM_GROUND_TO_FLY_RATIO_COLUMN: Literal["ground_to_fly_ratio"] = "ground_to_fly_ratio"
TEAM_RUNS_CREATED_PER_27_OUTS_COLUMN: Literal["runs_created_per_27_outs"] = (
    "runs_created_per_27_outs"
)
TEAM_BATTER_RATING_COLUMN: Literal["batter_rating"] = "batter_rating"
TEAM_AT_BATS_PER_HOME_RUN_COLUMN: Literal["at_bats_per_home_run"] = (
    "at_bats_per_home_run"
)
TEAM_STOLEN_BASE_PERCENTAGE_COLUMN: Literal["stolen_base_percentage"] = (
    "stolen_base_percentage"
)
TEAM_PITCHES_PER_PLATE_APPEARANCE_COLUMN: Literal["pitches_per_plate_appearance"] = (
    "pitches_per_plate_appearance"
)
TEAM_ISOLATED_POWER_COLUMN: Literal["isolated_power"] = "isolated_power"
TEAM_WALK_TO_STRIKEOUT_RATIO_COLUMN: Literal["walk_to_strikeout_ratio"] = (
    "walk_to_strikeout_ratio"
)
TEAM_WALKS_PER_PLATE_APPEARANCE_COLUMN: Literal["walks_per_plate_appearance"] = (
    "walks_per_plate_appearance"
)
TEAM_SECONDARY_AVERAGE_MINUS_BATTING_AVERAGE_COLUMN: Literal[
    "secondary_average_minus_batting_average"
] = "secondary_average_minus_batting_average"
TEAM_RUNS_PRODUCED_COLUMN: Literal["runs_produced"] = "runs_produced"
TEAM_RUNS_RATIO_COLUMN: Literal["runs_ratio"] = "runs_ratio"
TEAM_PATIENCE_RATIO_COLUMN: Literal["patience_ratio"] = "patience_ratio"
TEAM_BALLS_IN_PLAY_AVERAGE_COLUMN: Literal["balls_in_play_average"] = (
    "balls_in_play_average"
)
TEAM_MLB_RATING_COLUMN: Literal["mlb_rating"] = "mlb_rating"
TEAM_OFFENSIVE_WINS_ABOVE_REPLACEMENT_COLUMN: Literal[
    "offensive_wins_above_replacement"
] = "offensive_wins_above_replacement"
TEAM_WINS_ABOVE_REPLACEMENT_COLUMN: Literal["wins_above_replacement"] = (
    "wins_above_replacement"
)
TEAM_EARNED_RUNS_COLUMN: Literal["earned_runs"] = "earned_runs"
TEAM_BATTERS_HIT_COLUMN: Literal["batters_hit"] = "batters_hit"
TEAM_SACRIFICE_BUNTS_COLUMN: Literal["sacrifice_bunts"] = "sacrifice_bunts"
TEAM_SAVE_OPPORTUNITIES_COLUMN: Literal["save_opportunities"] = "save_opportunities"
TEAM_FINISHES_COLUMN: Literal["finishes"] = "finishes"
TEAM_BALKS_COLUMN: Literal["balks"] = "balks"
TEAM_BATTERS_FACED_COLUMN: Literal["batters_faced"] = "batters_faced"
TEAM_HOLDS_COLUMN: Literal["holds"] = "holds"
TEAM_COMPLETE_GAMES_COLUMN: Literal["complete_games"] = "complete_games"
TEAM_HIT_BY_PITCH_COLUMN: Literal["hit_by_pitch"] = "hit_by_pitch"
TEAM_GROUND_BALLS_COLUMN: Literal["ground_balls"] = "ground_balls"
TEAM_STRIKEOUTS_COLUMN: Literal["strikeouts"] = "strikeouts"
TEAM_RBIS_COLUMN: Literal["rbis"] = "rbis"
TEAM_SAC_HITS_COLUMN: Literal["sac_hits"] = "sac_hits"
TEAM_HITS_COLUMN: Literal["hits"] = "hits"
TEAM_STOLEN_BASES_COLUMN: Literal["stolen_bases"] = "stolen_bases"
TEAM_WALKS_COLUMN: Literal["walks"] = "walks"
TEAM_CATCHER_INTERFERENCE_COLUMN: Literal["catcher_interference"] = (
    "catcher_interference"
)
TEAM_GIDPS_COLUMN: Literal["gidps"] = "gidps"
TEAM_SACRIFICE_FLIES_COLUMN: Literal["sacrifice_flies"] = "sacrifice_flies"
TEAM_AT_BATS_COLUMN: Literal["at_bats"] = "at_bats"
TEAM_HOME_RUNS_COLUMN: Literal["home_runs"] = "home_runs"
TEAM_GRAND_SLAM_HOME_RUNS_COLUMN: Literal["grand_slam_home_runs"] = (
    "grand_slam_home_runs"
)
TEAM_RUNNERS_LEFT_ON_BASE_COLUMN: Literal["runners_left_on_base"] = (
    "runners_left_on_base"
)
TEAM_TRIPLES_COLUMN: Literal["triples"] = "triples"
TEAM_GAME_WINNING_RBIS_COLUMN: Literal["game_winning_rbis"] = "game_winning_rbis"
TEAM_INTENTIONAL_WALKS_COLUMN: Literal["intentional_walks"] = "intentional_walks"
TEAM_DOUBLES_COLUMN: Literal["doubles"] = "doubles"
TEAM_FLY_BALLS_COLUMN: Literal["fly_balls"] = "fly_balls"
TEAM_CAUGHT_STEALING_COLUMN: Literal["caught_stealing"] = "caught_stealing"
TEAM_PITCHES_COLUMN: Literal["pitches"] = "pitches"
TEAM_GAMES_STARTED_COLUMN: Literal["games_started"] = "games_started"
TEAM_PINCH_AT_BATS_COLUMN: Literal["pinch_at_bats"] = "pinch_at_bats"
TEAM_PINCH_HITS_COLUMN: Literal["pinch_hits"] = "pinch_hits"
TEAM_PLAYER_RATING_COLUMN: Literal["player_rating"] = "player_rating"
TEAM_IS_QUALIFIED_COLUMN: Literal["is_qualified"] = "is_qualified"
TEAM_IS_QUALIFIED_STEALS_COLUMN: Literal["is_qualified_steals"] = "is_qualified_steals"
TEAM_TOTAL_BASES_COLUMN: Literal["total_bases"] = "total_bases"
TEAM_PLATE_APPEARANCES_COLUMN: Literal["plate_appearances"] = "plate_appearances"
TEAM_PROJECTED_HOME_RUNS_COLUMN: Literal["projected_home_runs"] = "projected_home_runs"
TEAM_EXTRA_BASE_HITS_COLUMN: Literal["extra_base_hits"] = "extra_base_hits"
TEAM_AVERAGE_GAME_SCORE_COLUMN: Literal["average_game_score"] = "average_game_score"
TEAM_AVERAGE_FIELD_GOALS_ATTEMPTED_COLUMN: Literal["average_field_goals_attempted"] = (
    "average_field_goals_attempted"
)
TEAM_AVERAGE_THREE_POINT_FIELD_GOALS_MADE_COLUMN: Literal[
    "average_three_point_field_goals_made"
] = "average_three_point_field_goals_made"
TEAM_AVERAGE_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_three_point_field_goals_attempted"
] = "average_three_point_field_goals_attempted"
TEAM_AVERAGE_FREE_THROWS_MADE_COLUMN: Literal["average_free_throws_made"] = (
    "average_free_throws_made"
)
TEAM_AVERAGE_FREE_THROWS_ATTEMPTED_COLUMN: Literal["average_free_throws_attempted"] = (
    "average_free_throws_attempted"
)
TEAM_AVERAGE_POINTS_COLUMN: Literal["average_points"] = "average_points"
TEAM_AVERAGE_OFFENSIVE_REBOUNDS_COLUMN: Literal["average_offensive_rebounds"] = (
    "average_offensive_rebounds"
)
TEAM_AVERAGE_ASSISTS_COLUMN: Literal["average_assists"] = "average_assists"
TEAM_AVERAGE_TURNOVERS_COLUMN: Literal["average_turnovers"] = "average_turnovers"
TEAM_OFFENSIVE_REBOUND_PERCENTAGE_COLUMN: Literal["offensive_rebound_percentage"] = (
    "offensive_rebound_percentage"
)
TEAM_ESTIMATED_POSSESSIONS_COLUMN: Literal["estimated_possessions"] = (
    "estimated_possessions"
)
TEAM_AVERAGE_ESTIMATED_POSSESSIONS_COLUMN: Literal["average_estimated_possessions"] = (
    "average_estimated_possessions"
)
TEAM_POINTS_PER_ESTIMATED_POSSESSIONS_COLUMN: Literal[
    "points_per_estimated_possessions"
] = "points_per_estimated_possessions"
TEAM_AVERAGE_TEAM_TURNOVERS_COLUMN: Literal["average_team_turnovers"] = (
    "average_team_turnovers"
)
TEAM_AVERAGE_TOTAL_TURNOVERS_COLUMN: Literal["average_total_turnovers"] = (
    "average_total_turnovers"
)
TEAM_TWO_POINT_FIELD_GOALS_MADE_COLUMN: Literal["two_point_field_goals_made"] = (
    "two_point_field_goals_made"
)
TEAM_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "two_point_field_goals_attempted"
] = "two_point_field_goals_attempted"
TEAM_AVERAGE_TWO_POINT_FIELD_GOALS_MADE_COLUMN: Literal[
    "average_two_point_field_goals_made"
] = "average_two_point_field_goals_made"
TEAM_AVERAGE_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_two_point_field_goals_attempted"
] = "average_two_point_field_goals_attempted"
TEAM_TWO_POINT_FIELD_GOAL_PERCENTAGE_COLUMN: Literal[
    "two_point_field_goal_percentage"
] = "two_point_field_goal_percentage"
TEAM_SHOOTING_EFFICIENCY_COLUMN: Literal["shooting_efficiency"] = "shooting_efficiency"
TEAM_SCORING_EFFICIENCY_COLUMN: Literal["scoring_efficiency"] = "scoring_efficiency"
TEAM_AVERAGE_48_FIELD_GOALS_MADE_COLUMN: Literal["average_48_field_goals_made"] = (
    "average_48_field_goals_made"
)
TEAM_AVERAGE_48_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_48_field_goals_attempted"
] = "average_48_field_goals_attempted"
TEAM_AVERAGE_48_THREE_POINT_FIELD_GOALS_MADE_COLUMN: Literal[
    "average_48_three_point_field_goals_made"
] = "average_48_three_point_field_goals_made"
TEAM_AVERAGE_48_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_48_three_point_field_goals_attempted"
] = "average_48_three_point_field_goals_attempted"
TEAM_AVERAGE_48_FREE_THROWS_MADE_COLUMN: Literal["average_48_free_throws_made"] = (
    "average_48_free_throws_made"
)
TEAM_AVERAGE_48_FREE_THROWS_ATTEMPTED_COLUMN: Literal[
    "average_48_free_throws_attempted"
] = "average_48_free_throws_attempted"
TEAM_AVERAGE_48_POINTS_COLUMN: Literal["average_48_points"] = "average_48_points"
TEAM_AVERAGE_48_OFFENSIVE_REBOUNDS_COLUMN: Literal["average_48_offensive_rebounds"] = (
    "average_48_offensive_rebounds"
)
TEAM_AVERAGE_48_ASSISTS_COLUMN: Literal["average_48_assists"] = "average_48_assists"
TEAM_AVERAGE_48_TURNOVERS_COLUMN: Literal["average_48_turnovers"] = (
    "average_48_turnovers"
)
TEAM_AVERAGE_REBOUNDS_COLUMN: Literal["average_rebounds"] = "average_rebounds"
TEAM_AVERAGE_FOULS_COLUMN: Literal["average_fouls"] = "average_fouls"
TEAM_AVERAGE_FLAGRANT_FOULS_COLUMN: Literal["average_flagrant_fouls"] = (
    "average_flagrant_fouls"
)
TEAM_AVERAGE_TECHNICAL_FOULS_COLUMN: Literal["average_technical_fouls"] = (
    "average_technical_fouls"
)
TEAM_AVERAGE_EJECTIONS_COLUMN: Literal["average_ejections"] = "average_ejections"
TEAM_AVERAGE_DISQUALIFICATIONS_COLUMN: Literal["average_disqualifications"] = (
    "average_disqualifications"
)
TEAM_ASSIST_TURNOVER_RATIO_COLUMN: Literal["assist_turnover_ratio"] = (
    "assist_turnover_ratio"
)
TEAM_STEAL_FOUL_RATIO_COLUMN: Literal["steal_foul_ratio"] = "steal_foul_ratio"
TEAM_BLOCK_FOUL_RATIO_COLUMN: Literal["block_foul_ratio"] = "block_foul_ratio"
TEAM_AVERAGE_TEAM_REBOUNDS_COLUMN: Literal["average_team_rebounds"] = (
    "average_team_rebounds"
)
TEAM_TOTAL_TECHNICAL_FOULS_COLUMN: Literal["total_technical_fouls"] = (
    "total_technical_fouls"
)
TEAM_TEAM_ASSIST_TURNOVER_RATIO_COLUMN: Literal["team_assist_turnover_ratio"] = (
    "team_assist_turnover_ratio"
)
TEAM_STEAL_TURNOVER_RATIO_COLUMN: Literal["steal_turnover_ratio"] = (
    "steal_turnover_ratio"
)
TEAM_AVERAGE_48_REBOUNDS_COLUMN: Literal["average_48_rebounds"] = "average_48_rebounds"
TEAM_AVERAGE_48_FOULS_COLUMN: Literal["average_48_fouls"] = "average_48_fouls"
TEAM_AVERAGE_48_FLAGRANT_FOULS_COLUMN: Literal["average_48_flagrant_fouls"] = (
    "average_48_flagrant_fouls"
)
TEAM_AVERAGE_48_TECHNICAL_FOULS_COLUMN: Literal["average_48_technical_fouls"] = (
    "average_48_technical_fouls"
)
TEAM_AVERAGE_48_EJECTIONS_COLUMN: Literal["average_48_ejections"] = (
    "average_48_ejections"
)
TEAM_AVERAGE_48_DISQUALIFICATIONS_COLUMN: Literal["average_48_disqualifications"] = (
    "average_48_disqualifications"
)
TEAM_DOUBLE_DOUBLE_COLUMN: Literal["double_double"] = "double_double"
TEAM_TRIPLE_DOUBLE_COLUMN: Literal["triple_double"] = "triple_double"
TEAM_FIELD_GOALS_MADE_COLUMN: Literal["field_goals_made"] = "field_goals_made"
TEAM_FREE_THROWS_MADE_COLUMN: Literal["free_throws_made"] = "free_throws_made"
TEAM_THREE_POINT_PERCENTAGE_COLUMN: Literal["three_point_percentage"] = (
    "three_point_percentage"
)
TEAM_THREE_POINT_FIELD_GOALS_MADE_COLUMN: Literal["three_point_field_goals_made"] = (
    "three_point_field_goals_made"
)
TEAM_TEAM_TURNOVERS_COLUMN: Literal["team_turnovers"] = "team_turnovers"
TEAM_TOTAL_TURNOVERS_COLUMN: Literal["total_turnovers"] = "total_turnovers"
TEAM_POINTS_IN_PAINT_COLUMN: Literal["points_in_paint"] = "points_in_paint"
TEAM_BRICK_INDEX_COLUMN: Literal["brick_index"] = "brick_index"
TEAM_FAST_BREAK_POINTS_COLUMN: Literal["fast_break_points"] = "fast_break_points"
TEAM_AVERAGE_FIELD_GOALS_MADE_COLUMN: Literal["average_field_goals_made"] = (
    "average_field_goals_made"
)
TEAM_TURNOVER_POINTS_COLUMN: Literal["turnover_points"] = "turnover_points"
TEAM_AVERAGE_DEFENSIVE_REBOUNDS_COLUMN: Literal["average_defensive_rebounds"] = (
    "average_defensive_rebounds"
)
TEAM_AVERAGE_BLOCKS_COLUMN: Literal["average_blocks"] = "average_blocks"
TEAM_AVERAGE_STEALS_COLUMN: Literal["average_steals"] = "average_steals"
TEAM_AVERAGE_48_DEFENSIVE_REBOUNDS_COLUMN: Literal["average_48_defensive_rebounds"] = (
    "average_48_defensive_rebounds"
)
TEAM_AVERAGE_48_BLOCKS_COLUMN: Literal["average_48_blocks"] = "average_48_blocks"
TEAM_AVERAGE_48_STEALS_COLUMN: Literal["average_48_steals"] = "average_48_steals"
TEAM_LARGEST_LEAD_COLUMN: Literal["largest_lead"] = "largest_lead"
TEAM_DISQUALIFICATIONS_COLUMN: Literal["disqualifications"] = "disqualifications"
TEAM_FLAGRANT_FOULS_COLUMN: Literal["flagrant_fouls"] = "flagrant_fouls"
TEAM_FOULS_COLUMN: Literal["fouls"] = "fouls"
TEAM_EJECTIONS_COLUMN: Literal["ejections"] = "ejections"
TEAM_TECHNICAL_FOULS_COLUMN: Literal["technical_fouls"] = "technical_fouls"
TEAM_VORP_COLUMN: Literal["vorp"] = "vorp"
TEAM_AVERAGE_MINUTES_COLUMN: Literal["average_minutes"] = "average_minutes"
TEAM_NBA_RATING_COLUMN: Literal["nba_rating"] = "nba_rating"
TEAM_FOURTH_DOWN_ATTEMPTS_COLUMN: Literal["fourth_down_attempts"] = (
    "fourth_down_attempts"
)
TEAM_FOURTH_DOWN_CONVERSION_PERCENTAGE_COLUMN: Literal[
    "fourth_down_conversion_percentage"
] = "fourth_down_conversion_percentage"
TEAM_FOURTH_DOWN_CONVERSIONS_COLUMN: Literal["fourth_down_conversions"] = (
    "fourth_down_conversions"
)
TEAM_POSSESSION_TIME_SECONDS_COLUMN: Literal["possession_time_seconds"] = (
    "possession_time_seconds"
)
TEAM_REDZONE_ATTEMPT_POINTS_COLUMN: Literal["redzone_attempt_points"] = (
    "redzone_attempt_points"
)
TEAM_REDZONE_ATTEMPTS_COLUMN: Literal["redzone_attempts"] = "redzone_attempts"
TEAM_REDZONE_CONVERSIONS_COLUMN: Literal["redzone_conversions"] = "redzone_conversions"
TEAM_REDZONE_EFFICIENCY_PERCENTAGE_COLUMN: Literal["redzone_efficiency_percentage"] = (
    "redzone_efficiency_percentage"
)
TEAM_REDZONE_END_DOWNS_COLUMN: Literal["redzone_end_downs"] = "redzone_end_downs"
TEAM_REDZONE_END_GAME_COLUMN: Literal["redzone_end_game"] = "redzone_end_game"
TEAM_REDZONE_END_HALF_COLUMN: Literal["redzone_end_half"] = "redzone_end_half"
TEAM_REDZONE_FIELD_GOAL_PERCENTAGE_COLUMN: Literal["redzone_field_goal_percentage"] = (
    "redzone_field_goal_percentage"
)
TEAM_REDZONE_FIELD_GOAL_POINTS_COLUMN: Literal["redzone_field_goal_points"] = (
    "redzone_field_goal_points"
)
TEAM_REDZONE_FIELD_GOALS_COLUMN: Literal["redzone_field_goals"] = "redzone_field_goals"
TEAM_REDZONE_FIELD_GOALS_MISSED_COLUMN: Literal["redzone_field_goals_missed"] = (
    "redzone_field_goals_missed"
)
TEAM_REDZONE_FUMBLE_COLUMN: Literal["redzone_fumble"] = "redzone_fumble"
TEAM_REDZONE_INTERCEPTION_COLUMN: Literal["redzone_interception"] = (
    "redzone_interception"
)
TEAM_REDZONE_SCORING_PERCENTAGE_COLUMN: Literal["redzone_scoring_percentage"] = (
    "redzone_scoring_percentage"
)
TEAM_REDZONE_TOTAL_POINTS_COLUMN: Literal["redzone_total_points"] = (
    "redzone_total_points"
)
TEAM_REDZONE_TOUCHDOWN_PASS_COLUMN: Literal["redzone_touchdown_pass"] = (
    "redzone_touchdown_pass"
)
TEAM_REDZONE_TOUCHDOWN_PERCENTAGE_COLUMN: Literal["redzone_touchdown_percentage"] = (
    "redzone_touchdown_percentage"
)
TEAM_REDZONE_TOUCHDOWN_POINTS_COLUMN: Literal["redzone_touchdown_points"] = (
    "redzone_touchdown_points"
)
TEAM_REDZONE_TOUCHDOWN_RUSH_COLUMN: Literal["redzone_touchdown_rush"] = (
    "redzone_touchdown_rush"
)
TEAM_REDZONE_TOUCHDOWNS_COLUMN: Literal["redzone_touchdowns"] = "redzone_touchdowns"
TEAM_THIRD_DOWN_ATTEMPTS_COLUMN: Literal["third_down_attempts"] = "third_down_attempts"
TEAM_THIRD_DOWN_CONVERSION_PERCENTAGE_COLUMN: Literal[
    "third_down_conversion_percentage"
] = "third_down_conversion_percentage"
TEAM_THIRD_DOWN_CONVERSIONS_COLUMN: Literal["third_down_conversions"] = (
    "third_down_conversions"
)
TEAM_TIMEOUTS_USED_COLUMN: Literal["timeouts_used"] = "timeouts_used"
TEAM_TOTAL_PENALTIES_COLUMN: Literal["total_penalties"] = "total_penalties"
TEAM_TOTAL_PENALTY_YARDS_COLUMN: Literal["total_penalty_yards"] = "total_penalty_yards"
TEAM_TOTAL_PLAYS_COLUMN: Literal["total_plays"] = "total_plays"
TEAM_TOTAL_DRIVES_COLUMN: Literal["total_drives"] = "total_drives"
TEAM_TURN_OVER_DIFFERENTIAL_COLUMN: Literal["turn_over_differential"] = (
    "turn_over_differential"
)
TEAM_PUNT_RETURNS_STARTED_INSIDE_THE_10_COLUMN: Literal[
    "punt_returns_started_inside_the_10"
] = "punt_returns_started_inside_the_10"
TEAM_PUNT_RETURNS_STARTED_INSIDE_THE_20_COLUMN: Literal[
    "punt_returns_started_inside_the_20"
] = "punt_returns_started_inside_the_20"
TEAM_PUNT_RETURN_TOUCHDOWNS_COLUMN: Literal["punt_return_touchdowns"] = (
    "punt_return_touchdowns"
)
TEAM_PUNT_RETURN_YARDS_COLUMN: Literal["punt_return_yards"] = "punt_return_yards"
TEAM_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN: Literal["special_team_fumble_returns"] = (
    "special_team_fumble_returns"
)
TEAM_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN: Literal[
    "special_team_fumble_return_yards"
] = "special_team_fumble_return_yards"
TEAM_YARDS_PER_KICK_RETURN_COLUMN: Literal["yards_per_kick_return"] = (
    "yards_per_kick_return"
)
TEAM_YARDS_PER_PUNT_RETURN_COLUMN: Literal["yards_per_punt_return"] = (
    "yards_per_punt_return"
)
TEAM_YARDS_PER_RETURN_COLUMN: Literal["yards_per_return"] = "yards_per_return"
TEAM_AVERAGE_PUNT_RETURN_YARDS_COLUMN: Literal["average_punt_return_yards"] = (
    "average_punt_return_yards"
)
TEAM_GROSS_AVERAGE_PUNT_YARDS_COLUMN: Literal["gross_average_punt_yards"] = (
    "gross_average_punt_yards"
)
TEAM_LONG_PUNT_COLUMN: Literal["long_punt"] = "long_punt"
TEAM_NET_AVERAGE_PUNT_YARDS_COLUMN: Literal["net_average_punt_yards"] = (
    "net_average_punt_yards"
)
TEAM_PUNTS_COLUMN: Literal["punts"] = "punts"
TEAM_PUNTS_BLOCKED_COLUMN: Literal["punts_blocked"] = "punts_blocked"
TEAM_PUNTS_BLOCKED_PERCENTAGE_COLUMN: Literal["punts_blocked_percentage"] = (
    "punts_blocked_percentage"
)
TEAM_PUNTS_INSIDE_THE_10_COLUMN: Literal["punts_inside_10"] = "punts_inside_10"
TEAM_PUNTS_INSIDE_THE_10_PERCENTAGE_COLUMN: Literal["punts_inside_10_percentage"] = (
    "punts_inside_10_percentage"
)
TEAM_PUNTS_INSIDE_THE_20_COLUMN: Literal["punts_inside_20"] = "punts_inside_20"
TEAM_PUNTS_INSIDE_THE_20_PERCENTAGE_COLUMN: Literal["punts_inside_20_percentage"] = (
    "punts_inside_20_percentage"
)
TEAM_PUNTS_OVER_50_COLUMN: Literal["punts_over_50"] = "punts_over_50"
TEAM_PUNT_YARDS_COLUMN: Literal["punt_yards"] = "punt_yards"
TEAM_DEFENSIVE_POINTS_COLUMN: Literal["defensive_points"] = "defensive_points"
TEAM_KICK_EXTRA_POINTS_COLUMN: Literal["kick_extra_points"] = "kick_extra_points"
TEAM_KICK_EXTRA_POINTS_MADE_COLUMN: Literal["kick_extra_points_made"] = (
    "kick_extra_points_made"
)
TEAM_MISC_POINTS_COLUMN: Literal["misc_points"] = "misc_points"
TEAM_RETURN_TOUCHDOWNS_COLUMN: Literal["return_touchdowns"] = "return_touchdowns"
TEAM_TOTAL_TWO_POINT_CONVERSIONS_COLUMN: Literal["total_two_point_conversions"] = (
    "total_two_point_conversions"
)
TEAM_FIRST_DOWNS_COLUMN: Literal["first_downs"] = "first_downs"
TEAM_FIRST_DOWNS_PASSING_COLUMN: Literal["first_downs_passing"] = "first_downs_passing"
TEAM_FIRST_DOWNS_PENALTY_COLUMN: Literal["first_downs_penalty"] = "first_downs_penalty"
TEAM_FIRST_DOWNS_PER_GAME_COLUMN: Literal["first_downs_per_game"] = (
    "first_downs_per_game"
)
TEAM_FIRST_DOWNS_RUSHING_COLUMN: Literal["first_downs_rushing"] = "first_downs_rushing"
TEAM_KICKOFF_RETURN_YARDS_COLUMN: Literal["kickoff_return_yards"] = (
    "kickoff_return_yards"
)
TEAM_KICKOFFS_COLUMN: Literal["kickoffs"] = "kickoffs"
TEAM_KICKOFF_YARDS_COLUMN: Literal["kickoff_yards"] = "kickoff_yards"
TEAM_LONG_FIELD_GOAL_ATTEMPT_COLUMN: Literal["long_field_goal_attempt"] = (
    "long_field_goal_attempt"
)
TEAM_LONG_FIELD_GOAL_MADE_COLUMN: Literal["long_field_goal_made"] = (
    "long_field_goal_made"
)
TEAM_LONG_KICKOFF_COLUMN: Literal["long_kickoff"] = "long_kickoff"
TEAM_TOTAL_KICKING_POINTS_COLUMN: Literal["total_kicking_points"] = (
    "total_kicking_points"
)
TEAM_TOUCHBACK_PERCENTAGE_COLUMN: Literal["touchback_percentage"] = (
    "touchback_percentage"
)
TEAM_TOUCHBACKS_COLUMN: Literal["touchbacks"] = "touchbacks"
TEAM_DEF_FUMBLE_RETURNS_COLUMN: Literal["def_fumble_returns"] = "def_fumble_returns"
TEAM_DEF_FUMBLE_RETURN_YARDS_COLUMN: Literal["def_fumble_return_yards"] = (
    "def_fumble_return_yards"
)
TEAM_FUMBLE_RECOVERIES_COLUMN: Literal["fumble_recoveries"] = "fumble_recoveries"
TEAM_FUMBLE_RECOVERY_YARDS_COLUMN: Literal["fumble_recovery_yards"] = (
    "fumble_recovery_yards"
)
TEAM_KICK_RETURN_FAIR_CATCHES_COLUMN: Literal["kick_return_fair_catches"] = (
    "kick_return_fair_catches"
)
TEAM_KICK_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN: Literal[
    "kick_return_fair_catch_percentage"
] = "kick_return_fair_catch_percentage"
TEAM_KICK_RETURN_FUMBLES_COLUMN: Literal["kick_return_fumbles"] = "kick_return_fumbles"
TEAM_KICK_RETURN_FUMBLES_LOST_COLUMN: Literal["kick_return_fumbles_lost"] = (
    "kick_return_fumbles_lost"
)
TEAM_KICK_RETURNS_COLUMN: Literal["kick_returns"] = "kick_returns"
TEAM_KICK_RETURN_TOUCHDOWNS_COLUMN: Literal["kick_return_touchdowns"] = (
    "kick_return_touchdowns"
)
TEAM_KICK_RETURN_YARDS_COLUMN: Literal["kick_return_yards"] = "kick_return_yards"
TEAM_LONG_KICK_RETURN_COLUMN: Literal["long_kick_return"] = "long_kick_return"
TEAM_LONG_PUNT_RETURN_COLUMN: Literal["long_punt_return"] = "long_punt_return"
TEAM_MISC_FUMBLE_RETURNS_COLUMN: Literal["misc_fumble_returns"] = "misc_fumble_returns"
TEAM_MISC_FUMBLE_RETURN_YARDS_COLUMN: Literal["misc_fumble_return_yards"] = (
    "misc_fumble_return_yards"
)
TEAM_OPP_FUMBLE_RECOVERIES_COLUMN: Literal["opp_fumble_recoveries"] = (
    "opp_fumble_recoveries"
)
TEAM_OPP_FUMBLE_RECOVERY_YARDS_COLUMN: Literal["opp_fumble_recovery_yards"] = (
    "opp_fumble_recovery_yards"
)
TEAM_OPP_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN: Literal[
    "opp_special_team_fumble_returns"
] = "opp_special_team_fumble_returns"
TEAM_OPP_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN: Literal[
    "opp_special_team_fumble_return_yards"
] = "opp_special_team_fumble_return_yards"
TEAM_PUNT_RETURN_FAIR_CATCHES_COLUMN: Literal["punt_return_fair_catches"] = (
    "punt_return_fair_catches"
)
TEAM_PUNT_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN: Literal[
    "punt_return_fair_catch_percentage"
] = "punt_return_fair_catch_percentage"
TEAM_PUNT_RETURN_FUMBLES_COLUMN: Literal["punt_return_fumbles"] = "punt_return_fumbles"
TEAM_PUNT_RETURN_FUMBLES_LOST_COLUMN: Literal["punt_return_fumbles_lost"] = (
    "punt_return_fumbles_lost"
)
TEAM_PUNT_RETURNS_COLUMN: Literal["punt_returns"] = "punt_returns"
TEAM_INTERCEPTION_YARDS_COLUMN: Literal["interception_yards"] = "interception_yards"
TEAM_AVERAGE_KICKOFF_RETURN_YARDS_COLUMN: Literal["average_kickoff_return_yards"] = (
    "average_kickoff_return_yards"
)
TEAM_AVERAGE_KICKOFF_YARDS_COLUMN: Literal["average_kickoff_yards"] = (
    "average_kickoff_yards"
)
TEAM_EXTRA_POINT_ATTEMPTS_COLUMN: Literal["extra_point_attempts"] = (
    "extra_point_attempts"
)
TEAM_EXTRA_POINT_PERCENTAGE_COLUMN: Literal["extra_point_percentage"] = (
    "extra_point_percentage"
)
TEAM_EXTRA_POINTS_BLOCKED_COLUMN: Literal["extra_points_blocked"] = (
    "extra_points_blocked"
)
TEAM_EXTRA_POINTS_BLOCKED_PERCENTAGE_COLUMN: Literal[
    "extra_points_blocked_percentage"
] = "extra_points_blocked_percentage"
TEAM_EXTRA_POINTS_MADE_COLUMN: Literal["extra_points_made"] = "extra_points_made"
TEAM_FAIR_CATCHES_COLUMN: Literal["fair_catches"] = "fair_catches"
TEAM_FAIR_CATCH_PERCENTAGE_COLUMN: Literal["fair_catch_percentage"] = (
    "fair_catch_percentage"
)
TEAM_FIELD_GOAL_ATTEMPTS_COLUMN: Literal["field_goal_attempts"] = "field_goal_attempts"
TEAM_FIELD_GOAL_ATTEMPTS_1_19_COLUMN: Literal["field_goal_attempts_1_19"] = (
    "field_goal_attempts_1_19"
)
TEAM_FIELD_GOAL_ATTEMPTS_20_29_COLUMN: Literal["field_goal_attempts_20_29"] = (
    "field_goal_attempts_20_29"
)
TEAM_FIELD_GOAL_ATTEMPTS_30_39_COLUMN: Literal["field_goal_attempts_30_39"] = (
    "field_goal_attempts_30_39"
)
TEAM_FIELD_GOAL_ATTEMPTS_40_49_COLUMN: Literal["field_goal_attempts_40_49"] = (
    "field_goal_attempts_40_49"
)
TEAM_FIELD_GOAL_ATTEMPTS_50_59_COLUMN: Literal["field_goal_attempts_50_59"] = (
    "field_goal_attempts_50_59"
)
TEAM_FIELD_GOAL_ATTEMPTS_60_99_COLUMN: Literal["field_goal_attempts_60_99"] = (
    "field_goal_attempts_60_99"
)
TEAM_FIELD_GOAL_ATTEMPTS_50_COLUMN: Literal["field_goal_attempts_50"] = (
    "field_goal_attempts_50"
)
TEAM_FIELD_GOAL_ATTEMPT_YARDS_COLUMN: Literal["field_goal_attempt_yards"] = (
    "field_goal_attempt_yards"
)
TEAM_FIELD_GOALS_BLOCKED_COLUMN: Literal["field_goals_blocked"] = "field_goals_blocked"
TEAM_FIELD_GOALS_BLOCKED_PERCENTAGE_COLUMN: Literal[
    "field_goals_blocked_percentage"
] = "field_goals_blocked_percentage"
TEAM_FIELD_GOALS_MADE_1_19_COLUMN: Literal["field_goals_made_1_19"] = (
    "field_goals_made_1_19"
)
TEAM_FIELD_GOALS_MADE_20_29_COLUMN: Literal["field_goals_made_20_29"] = (
    "field_goals_made_20_29"
)
TEAM_FIELD_GOALS_MADE_30_39_COLUMN: Literal["field_goals_made_30_39"] = (
    "field_goals_made_30_39"
)
TEAM_FIELD_GOALS_MADE_40_49_COLUMN: Literal["field_goals_made_40_49"] = (
    "field_goals_made_40_49"
)
TEAM_FIELD_GOALS_MADE_50_59_COLUMN: Literal["field_goals_made_50_59"] = (
    "field_goals_made_50_59"
)
TEAM_FIELD_GOALS_MADE_60_99_COLUMN: Literal["field_goals_made_60_99"] = (
    "field_goals_made_60_99"
)
TEAM_FIELD_GOALS_MADE_50_COLUMN: Literal["field_goals_made_50"] = "field_goals_made_50"
TEAM_FIELD_GOALS_MADE_YARDS_COLUMN: Literal["field_goals_made_yards"] = (
    "field_goals_made_yards"
)
TEAM_FIELD_GOALS_MISSED_YARDS_COLUMN: Literal["field_goals_missed_yards"] = (
    "field_goals_missed_yards"
)
TEAM_KICKOFF_OB_COLUMN: Literal["kickoff_ob"] = "kickoff_ob"
TEAM_KICKOFF_RETURNS_COLUMN: Literal["kickoff_returns"] = "kickoff_returns"
TEAM_KICKOFF_RETURN_TOUCHDOWNS_COLUMN: Literal["kickoff_return_touchdowns"] = (
    "kickoff_return_touchdowns"
)
TEAM_TWO_POINT_REC_CONVERSIONS_COLUMN: Literal["two_point_rec_conversions"] = (
    "two_point_rec_conversions"
)
TEAM_TWO_POINT_RECEPTION_COLUMN: Literal["two_point_reception"] = "two_point_reception"
TEAM_TWO_POINT_RECEPTION_ATTEMPTS_COLUMN: Literal["two_point_reception_attempts"] = (
    "two_point_reception_attempts"
)
TEAM_YARDS_PER_RECEPTION_COLUMN: Literal["yards_per_reception"] = "yards_per_reception"
TEAM_ASSIST_TACKLES_COLUMN: Literal["assist_tackles"] = "assist_tackles"
TEAM_AVERAGE_INTERCEPTION_YARDS_COLUMN: Literal["average_interception_yards"] = (
    "average_interception_yards"
)
TEAM_AVERAGE_SACK_YARDS_COLUMN: Literal["average_sack_yards"] = "average_sack_yards"
TEAM_AVERAGE_STUFF_YARDS_COLUMN: Literal["average_stuff_yards"] = "average_stuff_yards"
TEAM_BLOCKED_FIELD_GOAL_TOUCHDOWNS_COLUMN: Literal["blocked_field_goal_touchdowns"] = (
    "blocked_field_goal_touchdowns"
)
TEAM_BLOCKED_PUNT_TOUCHDOWNS_COLUMN: Literal["blocked_punt_touchdowns"] = (
    "blocked_punt_touchdowns"
)
TEAM_DEFENSIVE_TOUCHDOWNS_COLUMN: Literal["defensive_touchdowns"] = (
    "defensive_touchdowns"
)
TEAM_HURRIES_COLUMN: Literal["hurries"] = "hurries"
TEAM_KICKS_BLOCKED_COLUMN: Literal["kicks_blocked"] = "kicks_blocked"
TEAM_LONG_INTERCEPTION_COLUMN: Literal["long_interception"] = "long_interception"
TEAM_MISC_TOUCHDOWNS_COLUMN: Literal["misc_touchdowns"] = "misc_touchdowns"
TEAM_PASSES_BATTED_DOWN_COLUMN: Literal["passes_batted_down"] = "passes_batted_down"
TEAM_PASSES_DEFENDED_COLUMN: Literal["passes_defended"] = "passes_defended"
TEAM_QB_HITS_COLUMN: Literal["qb_hits"] = "qb_hits"
TEAM_TWO_POINT_RETURNS_COLUMN: Literal["two_point_returns"] = "two_point_returns"
TEAM_SACKS_ASSISTED_COLUMN: Literal["sacks_assisted"] = "sacks_assisted"
TEAM_SACKS_UNASSISTED_COLUMN: Literal["sacks_unassisted"] = "sacks_unassisted"
TEAM_SACK_YARDS_COLUMN: Literal["sack_yards"] = "sack_yards"
TEAM_SAFETIES_COLUMN: Literal["safeties"] = "safeties"
TEAM_SOLO_TACKLES_COLUMN: Literal["solo_tackles"] = "solo_tackles"
TEAM_STUFF_YARDS_COLUMN: Literal["stuff_yards"] = "stuff_yards"
TEAM_TACKLES_FOR_LOSS_COLUMN: Literal["tackles_for_loss"] = "tackles_for_loss"
TEAM_TACKLES_YARDS_LOST_COLUMN: Literal["tackles_yards_lost"] = "tackles_yards_lost"
TEAM_YARDS_ALLOWED_COLUMN: Literal["yards_allowed"] = "yards_allowed"
TEAM_POINTS_ALLOWED_COLUMN: Literal["points_allowed"] = "points_allowed"
TEAM_ONE_POINT_SAFETIES_MADE_COLUMN: Literal["one_point_safeties_made"] = (
    "one_point_safeties_made"
)
TEAM_MISSED_FIELD_GOAL_RETURN_TD_COLUMN: Literal["missed_field_goal_return_td"] = (
    "missed_field_goal_return_td"
)
TEAM_BLOCKED_PUNT_EZ_REC_TD_COLUMN: Literal["blocked_punt_ez_rec_td"] = (
    "blocked_punt_ez_rec_td"
)
TEAM_INTERCEPTION_TOUCHDOWNS_COLUMN: Literal["interception_touchdowns"] = (
    "interception_touchdowns"
)
TEAM_YARDS_PER_GAME_COLUMN: Literal["yards_per_game"] = "yards_per_game"
TEAM_YARDS_PER_PASS_ATTEMPT_COLUMN: Literal["yards_per_pass_attempt"] = (
    "yards_per_pass_attempt"
)
TEAM_NET_YARDS_PER_PASS_ATTEMPT_COLUMN: Literal["net_yards_per_pass_attempt"] = (
    "net_yards_per_pass_attempt"
)
TEAM_QUARTERBACK_RATING_COLUMN: Literal["quarterback_rating"] = "quarterback_rating"
TEAM_ESPN_RB_RATING_COLUMN: Literal["espn_rb_rating"] = "espn_rb_rating"
TEAM_LONG_RUSHING_COLUMN: Literal["long_rushing"] = "long_rushing"
TEAM_RUSHING_ATTEMPTS_COLUMN: Literal["rushing_attempts"] = "rushing_attempts"
TEAM_RUSHING_BIG_PLAYS_COLUMN: Literal["rushing_big_plays"] = "rushing_big_plays"
TEAM_RUSHING_FIRST_DOWNS_COLUMN: Literal["rushing_first_downs"] = "rushing_first_downs"
TEAM_RUSHING_FUMBLES_COLUMN: Literal["rushing_fumbles"] = "rushing_fumbles"
TEAM_RUSHING_FUMBLES_LOST_COLUMN: Literal["rushing_fumbles_lost"] = (
    "rushing_fumbles_lost"
)
TEAM_RUSHING_TOUCHDOWNS_COLUMN: Literal["rushing_touchdowns"] = "rushing_touchdowns"
TEAM_RUSHING_YARDS_COLUMN: Literal["rushing_yards"] = "rushing_yards"
TEAM_RUSHING_YARDS_PER_GAME_COLUMN: Literal["rushing_yards_per_game"] = (
    "rushing_yards_per_game"
)
TEAM_STUFFS_COLUMN: Literal["stuffs"] = "stuffs"
TEAM_STUFF_YARDS_LOST_COLUMN: Literal["stuff_yards_lost"] = "stuff_yards_lost"
TEAM_TWO_POINT_RUSH_CONVERSIONS_COLUMN: Literal["two_point_rush_conversions"] = (
    "two_point_rush_conversions"
)
TEAM_TWO_POINT_RUSH_COLUMN: Literal["two_point_rush"] = "two_point_rush"
TEAM_TWO_POINT_RUSH_ATTEMPTS_COLUMN: Literal["two_point_rush_attempts"] = (
    "two_point_rush_attempts"
)
TEAM_YARDS_PER_RUSH_ATTEMPT_COLUMN: Literal["yards_per_rush_attempt"] = (
    "yards_per_rush_attempt"
)
TEAM_ESPN_WR_RATING_COLUMN: Literal["espn_wr_rating"] = "espn_wr_rating"
TEAM_LONG_RECEPTION_COLUMN: Literal["long_reception"] = "long_reception"
TEAM_RECEIVING_BIG_PLAYS_COLUMN: Literal["receiving_big_plays"] = "receiving_big_plays"
TEAM_RECEIVING_FIRST_DOWNS_COLUMN: Literal["receiving_first_downs"] = (
    "receiving_first_downs"
)
TEAM_RECEIVING_FUMBLES_COLUMN: Literal["receiving_fumbles"] = "receiving_fumbles"
TEAM_RECEIVING_FUMBLES_LOST_COLUMN: Literal["receiving_fumbles_lost"] = (
    "receiving_fumbles_lost"
)
TEAM_RECEIVING_TARGETS_COLUMN: Literal["receiving_targets"] = "receiving_targets"
TEAM_RECEIVING_TOUCHDOWNS_COLUMN: Literal["receiving_touchdowns"] = (
    "receiving_touchdowns"
)
TEAM_RECEIVING_YARDS_COLUMN: Literal["receiving_yards"] = "receiving_yards"
TEAM_RECEIVING_YARDS_AFTER_CATCH_COLUMN: Literal["receiving_yards_after_catch"] = (
    "receiving_yards_after_catch"
)
TEAM_RECEIVING_YARDS_AT_CATCH_COLUMN: Literal["receiving_yards_at_catch"] = (
    "receiving_yards_at_catch"
)
TEAM_RECEIVING_YARDS_PER_GAME_COLUMN: Literal["receiving_yards_per_game"] = (
    "receiving_yards_per_game"
)
TEAM_RECEPTIONS_COLUMN: Literal["receptions"] = "receptions"
TEAM_INTERCEPTION_PERCENTAGE_COLUMN: Literal["interception_percentage"] = (
    "interception_percentage"
)
TEAM_LONG_PASSING_COLUMN: Literal["long_passing"] = "long_passing"
TEAM_MISC_YARDS_COLUMN: Literal["misc_yards"] = "misc_yards"
TEAM_NET_PASSING_YARDS_COLUMN: Literal["net_passing_yards"] = "net_passing_yards"
TEAM_NET_PASSING_YARDS_PER_GAME_COLUMN: Literal["net_passing_yards_per_game"] = (
    "net_passing_yards_per_game"
)
TEAM_NET_TOTAL_YARDS_COLUMN: Literal["net_total_yards"] = "net_total_yards"
TEAM_NET_YARDS_PER_GAME_COLUMN: Literal["net_yards_per_game"] = "net_yards_per_game"
TEAM_PASSING_ATTEMPTS_COLUMN: Literal["passing_attempts"] = "passing_attempts"
TEAM_PASSING_BIG_PLAYS_COLUMN: Literal["passing_big_plays"] = "passing_big_plays"
TEAM_PASSING_FIRST_DOWNS_COLUMN: Literal["passing_first_downs"] = "passing_first_downs"
TEAM_PASSING_FUMBLES_COLUMN: Literal["passing_fumbles"] = "passing_fumbles"
TEAM_PASSING_FUMBLES_LOST_COLUMN: Literal["passing_fumbles_lost"] = (
    "passing_fumbles_lost"
)
TEAM_PASSING_TOUCHDOWN_PERCENTAGE_COLUMN: Literal["passing_touchdown_percentage"] = (
    "passing_touchdown_percentage"
)
TEAM_PASSING_TOUCHDOWNS_COLUMN: Literal["passing_touchdowns"] = "passing_touchdowns"
TEAM_PASSING_YARDS_COLUMN: Literal["passing_yards"] = "passing_yards"
TEAM_PASSING_YARDS_AFTER_CATCH_COLUMN: Literal["passing_yards_after_catch"] = (
    "passing_yards_after_catch"
)
TEAM_PASSING_YARDS_AT_CATCH_COLUMN: Literal["passing_yards_at_catch"] = (
    "passing_yards_at_catch"
)
TEAM_PASSING_YARDS_PER_GAME_COLUMN: Literal["passing_yards_per_game"] = (
    "passing_yards_per_game"
)
TEAM_QB_RATING_COLUMN: Literal["qb_rating"] = "qb_rating"
TEAM_SACKS_COLUMN: Literal["sacks"] = "sacks"
TEAM_SACK_YARDS_LOST_COLUMN: Literal["sack_yards_lost"] = "sack_yards_lost"
TEAM_NET_PASSING_ATTEMPTS_COLUMN: Literal["net_passing_attempts"] = (
    "net_passing_attempts"
)
TEAM_TOTAL_OFFENSIVE_PLAYS_COLUMN: Literal["total_offensive_plays"] = (
    "total_offensive_plays"
)
TEAM_TOTAL_POINTS_COLUMN: Literal["total_points"] = "total_points"
TEAM_TOTAL_POINTS_PER_GAME_COLUMN: Literal["total_points_per_game"] = (
    "total_points_per_game"
)
TEAM_TOTAL_TOUCHDOWNS_COLUMN: Literal["total_touchdowns"] = "total_touchdowns"
TEAM_TOTAL_YARDS_COLUMN: Literal["total_yards"] = "total_yards"
TEAM_TOTAL_YARDS_FROM_SCRIMMAGE_COLUMN: Literal["total_yards_from_scrimmage"] = (
    "total_yards_from_scrimmage"
)
TEAM_TWO_POINT_PASS_CONVERSIONS_COLUMN: Literal["two_point_pass_convs"] = (
    "two_point_pass_convs"
)
TEAM_TWO_POINT_PASS_COLUMN: Literal["two_point_pass"] = "two_point_pass"
TEAM_TWO_POINT_PASS_ATTEMPTS_COLUMN: Literal["two_point_pass_attempts"] = (
    "two_point_pass_attempts"
)
TEAM_YARDS_FROM_SCRIMMAGE_PER_GAME_COLUMN: Literal["yards_from_scrimmage_per_game"] = (
    "yards_from_scrimmage_per_game"
)
TEAM_YARDS_PER_COMPLETION_COLUMN: Literal["yards_per_completion"] = (
    "yards_per_completion"
)
TEAM_FUMBLES_COLUMN: Literal["fumbles"] = "fumbles"
TEAM_FUMBLES_LOST_COLUMN: Literal["fumbles_lost"] = "fumbles_lost"
TEAM_FUMBLES_FORCED_COLUMN: Literal["fumbles_forced"] = "fumbles_forced"
TEAM_FUMBLES_RECOVERED_YARDS_COLUMN: Literal["fumbles_recovered_yards"] = (
    "fumbles_recovered_yards"
)
TEAM_OFFENSIVE_TWO_POINT_RETURNS_COLUMN: Literal["offensive_two_point_returns"] = (
    "offensive_two_point_returns"
)
TEAM_OFFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN: Literal["offensive_fumbles_touchdowns"] = (
    "offensive_fumbles_touchdowns"
)
TEAM_DEFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN: Literal["defensive_fumbles_touchdowns"] = (
    "defensive_fumbles_touchdowns"
)
TEAM_AVERAGE_GAIN_COLUMN: Literal["average_gain"] = "average_gain"
TEAM_COMPLETION_PERCENTAGE_COLUMN: Literal["completion_percentage"] = (
    "completion_percentage"
)
TEAM_COMPLETIONS_COLUMN: Literal["completions"] = "completions"
TEAM_ESPN_QB_RATING_COLUMN: Literal["espn_qb_rating"] = "espn_qb_rating"
TEAM_POWER_PLAY_TIME_ON_ICE_COLUMN: Literal["power_play_time_on_ice"] = (
    "power_play_time_on_ice"
)
TEAM_SHORT_HANDED_TIME_ON_ICE_COLUMN: Literal["short_handed_time_on_ice"] = (
    "short_handed_time_on_ice"
)
TEAM_EVEN_STRENGTH_TIME_ON_ICE_COLUMN: Literal["even_strength_time_on_ice"] = (
    "even_strength_time_on_ice"
)
TEAM_SHIFTS_COLUMN: Literal["shifts"] = "shifts"
TEAM_SHOT_DIFFERENTIAL_COLUMN: Literal["shot_differential"] = "shot_differential"
TEAM_GOAL_DIFFERENTIAL_COLUMN: Literal["goal_differential"] = "goal_differential"
TEAM_PIM_DIFFERENTIAL_COLUMN: Literal["pim_differential"] = "pim_differential"
TEAM_RATING_COLUMN: Literal["rating"] = "rating"
TEAM_YTD_GOALS_COLUMN: Literal["ytd_goals"] = "ytd_goals"
TEAM_SHOTS_IN_FIRST_PERIOD_COLUMN: Literal["shots_in_first_period"] = (
    "shots_in_first_period"
)
TEAM_SHOTS_IN_SECOND_PERIOD_COLUMN: Literal["shots_in_second_period"] = (
    "shots_in_second_period"
)
TEAM_SHOTS_IN_THIRD_PERIOD_COLUMN: Literal["shots_in_third_period"] = (
    "shots_in_third_period"
)
TEAM_SHOTS_OT_COLUMN: Literal["shots_ot"] = "shots_ot"
TEAM_SHOTS_TOTAL_COLUMN: Literal["shots_total"] = "shots_total"
TEAM_SHOTS_MISSED_COLUMN: Literal["shots_missed"] = "shots_missed"
TEAM_POINTS_PER_GAME_COLUMN: Literal["points_per_game"] = "points_per_game"
TEAM_POWER_PLAY_GOALS_COLUMN: Literal["power_play_goals"] = "power_play_goals"
TEAM_POWER_PLAY_ASSISTS_COLUMN: Literal["power_play_assists"] = "power_play_assists"
TEAM_POWER_PLAY_OPPORTUNITIES_COLUMN: Literal["power_play_opportunities"] = (
    "power_play_opportunities"
)
TEAM_POWER_PLAY_PERCENTAGE_COLUMN: Literal["power_play_percentage"] = (
    "power_play_percentage"
)
TEAM_SHORT_HANDED_GOALS_COLUMN: Literal["short_handed_goals"] = "short_handed_goals"
TEAM_SHORT_HANDED_ASSISTS_COLUMN: Literal["short_handed_assists"] = (
    "short_handed_assists"
)
TEAM_SHOOTOUT_ATTEMPTS_COLUMN: Literal["shootout_attempts"] = "shootout_attempts"
TEAM_SHOOTOUT_SHOT_PERCENTAGE_COLUMN: Literal["shootout_shot_percentage"] = (
    "shootout_shot_percentage"
)
TEAM_EMPTY_NET_GOALS_FOR_COLUMN: Literal["empty_net_goals_for"] = "empty_net_goals_for"
TEAM_SHOOTING_PERCENTAGE_COLUMN: Literal["shooting_percentage"] = "shooting_percentage"
TEAM_TOTAL_FACE_OFFS_COLUMN: Literal["total_face_offs"] = "total_face_offs"
TEAM_FACEOFFS_WON_COLUMN: Literal["faceoffs_won"] = "faceoffs_won"
TEAM_FACEOFFS_LOST_COLUMN: Literal["faceoffs_lost"] = "faceoffs_lost"
TEAM_FACEOFF_PERCENTAGE_COLUMN: Literal["faceoff_percentage"] = "faceoff_percentage"
TEAM_UNASSISTED_GOALS_COLUMN: Literal["unassisted_goals"] = "unassisted_goals"
TEAM_GIVEAWAYS_COLUMN: Literal["giveaways"] = "giveaways"
TEAM_PENALTY_MINUTES_COLUMN: Literal["penalty_minutes"] = "penalty_minutes"
TEAM_GOALS_AGAINST_COLUMN: Literal["goals_against"] = "goals_against"
TEAM_SHOTS_AGAINST_COLUMN: Literal["shots_against"] = "shots_against"
TEAM_PENALTY_KILL_PERCENTAGE_COLUMN: Literal["penalty_kill_percentage"] = (
    "penalty_kill_percentage"
)
TEAM_POWER_PLAY_GOALS_AGAINST_COLUMN: Literal["power_play_goals_against"] = (
    "power_play_goals_against"
)
TEAM_SHORT_HANDED_GOALS_AGAINST_COLUMN: Literal["short_handed_goals_against"] = (
    "short_handed_goals_against"
)
TEAM_SHOOTOUT_SAVES_COLUMN: Literal["shootout_saves"] = "shootout_saves"
TEAM_SHOOTOUT_SHOTS_AGAINST_COLUMN: Literal["shootout_shots_against"] = (
    "shootout_shots_against"
)
TEAM_TIMES_SHORT_HANDED_COLUMN: Literal["times_short_handed"] = "times_short_handed"
TEAM_EMPTY_NET_GOALS_AGAINST_COLUMN: Literal["empty_net_goals_against"] = (
    "empty_net_goals_against"
)
TEAM_TAKEAWAYS_COLUMN: Literal["takeaways"] = "takeaways"
TEAM_EVEN_STRENGTH_SAVES_COLUMN: Literal["even_strength_saves"] = "even_strength_saves"
TEAM_POWER_PLAY_SAVES_COLUMN: Literal["power_play_saves"] = "power_play_saves"
TEAM_SHORT_HANDED_SAVES_COLUMN: Literal["short_handed_saves"] = "short_handed_saves"
TEAM_TIME_ON_ICE_COLUMN: Literal["time_on_ice"] = "time_on_ice"
TEAM_TOTAL_GIVEAWAYS_COLUMN: Literal["total_giveaways"] = "total_giveaways"
TEAM_TOTAL_TAKEAWAYS_COLUMN: Literal["total_takeaways"] = "total_takeaways"
TEAM_FANTASY_RATING_COLUMN: Literal["fantasy_rating"] = "fantasy_rating"
TEAM_SECOND_CHANCE_POINTS_COLUMN: Literal["second_chance_points"] = (
    "second_chance_points"
)
TEAM_PLUS_MINUS_COLUMN: Literal["plus_minus"] = "plus_minus"
VERSION = DELIMITER.join(["0.0.14", PLAYER_VERSION, COACH_VERSION])


def _calculate_kicks(data: dict[str, Any]) -> int | None:
    kicks = 0
    found_kicks = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_kicks = player.kicks
        if player_kicks is None:
            continue
        found_kicks = True
        kicks += player_kicks
    if not found_kicks:
        return None
    return kicks


def _calculate_field_goals(data: dict[str, Any]) -> int | None:
    field_goals = 0
    found_field_goals = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_field_goals = player.field_goals
        if player_field_goals is None:
            continue
        found_field_goals = True
        field_goals += player_field_goals
    if not found_field_goals:
        return None
    return field_goals


def _calculate_field_goals_attempted(data: dict[str, Any]) -> int | None:
    field_goals_attempted = 0
    found_field_goals_attempted = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_field_goals_attempted = player.field_goals_attempted
        if player_field_goals_attempted is None:
            continue
        found_field_goals_attempted = True
        field_goals_attempted += player_field_goals_attempted
    if not found_field_goals_attempted:
        return None
    return field_goals_attempted


def _calculate_offensive_rebounds(data: dict[str, Any]) -> int | None:
    offensive_rebounds = 0
    found_offensive_rebounds = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_offensive_rebounds = player.offensive_rebounds
        if player_offensive_rebounds is None:
            continue
        found_offensive_rebounds = True
        offensive_rebounds += player_offensive_rebounds
    if not found_offensive_rebounds:
        return None
    return offensive_rebounds


def _calculate_assists(data: dict[str, Any]) -> int | None:
    assists = 0
    found_assists = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_assists = player.assists
        if player_assists is None:
            continue
        found_assists = True
        assists += player_assists
    if not found_assists:
        return None
    return assists


def _calculate_turnovers(data: dict[str, Any]) -> int | None:
    turnovers = 0
    found_turnovers = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_turnovers = player.turnovers
        if player_turnovers is None:
            continue
        found_turnovers = True
        turnovers += player_turnovers
    if not found_turnovers:
        return None
    return turnovers


def _calculate_marks(data: dict[str, Any]) -> int | None:
    marks = 0
    found_marks = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_marks = player.marks
        if player_marks is None:
            continue
        found_marks = True
        marks += player_marks
    if not found_marks:
        return None
    return marks


def _calculate_handballs(data: dict[str, Any]) -> int | None:
    handballs = 0
    found_handballs = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_handballs = player.handballs
        if player_handballs is None:
            continue
        found_handballs = True
        handballs += player_handballs
    if not found_handballs:
        return None
    return handballs


def _calculate_disposals(data: dict[str, Any]) -> int | None:
    disposals = 0
    found_disposals = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_disposals = player.disposals
        if player_disposals is None:
            continue
        found_disposals = True
        disposals += player_disposals
    if not found_disposals:
        return None
    return disposals


def _calculate_goals(data: dict[str, Any]) -> int | None:
    goals = 0
    found_goals = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_goals = player.goals
        if player_goals is None:
            continue
        found_goals = True
        goals += player_goals
    if not found_goals:
        return None
    return goals


def _calculate_behinds(data: dict[str, Any]) -> int | None:
    behinds = 0
    found_behinds = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_behinds = player.behinds
        if player_behinds is None:
            continue
        found_behinds = True
        behinds += player_behinds
    if not found_behinds:
        return None
    return behinds


def _calculate_hit_outs(data: dict[str, Any]) -> int | None:
    hit_outs = 0
    found_hit_outs = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_hit_outs = player.hit_outs
        if player_hit_outs is None:
            continue
        found_hit_outs = True
        hit_outs += player_hit_outs
    if not found_hit_outs:
        return None
    return hit_outs


def _calculate_tackles(data: dict[str, Any]) -> int | None:
    tackles = 0
    found_tackles = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_tackles = player.tackles
        if player_tackles is None:
            continue
        found_tackles = True
        tackles += player_tackles
    if not found_tackles:
        return None
    return tackles


def _calculate_rebounds(data: dict[str, Any]) -> int | None:
    rebounds = 0
    found_rebounds = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_rebounds = player.rebounds
        if player_rebounds is None:
            continue
        found_rebounds = True
        rebounds += player_rebounds
    if not found_rebounds:
        return None
    return rebounds


def _calculate_insides(data: dict[str, Any]) -> int | None:
    insides = 0
    found_insides = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_insides = player.insides
        if player_insides is None:
            continue
        found_insides = True
        insides += player_insides
    if not found_insides:
        return None
    return insides


def _calculate_clearances(data: dict[str, Any]) -> int | None:
    clearances = 0
    found_clearances = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_clearances = player.clearances
        if player_clearances is None:
            continue
        found_clearances = True
        clearances += player_clearances
    if not found_clearances:
        return None
    return clearances


def _calculate_clangers(data: dict[str, Any]) -> int | None:
    clangers = 0
    found_clangers = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_clangers = player.clangers
        if player_clangers is None:
            continue
        found_clangers = True
        clangers += player_clangers
    if not found_clangers:
        return None
    return clangers


def _calculate_free_kicks_for(data: dict[str, Any]) -> int | None:
    free_kicks_for = 0
    found_free_kicks_for = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_free_kicks_for = player.free_kicks_for
        if player_free_kicks_for is None:
            continue
        found_free_kicks_for = True
        free_kicks_for += player_free_kicks_for
    if not found_free_kicks_for:
        return None
    return free_kicks_for


def _calculate_free_kicks_against(data: dict[str, Any]) -> int | None:
    free_kicks_against = 0
    found_free_kicks_against = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_free_kicks_against = player.free_kicks_against
        if player_free_kicks_against is None:
            continue
        found_free_kicks_against = True
        free_kicks_against += player_free_kicks_against
    if not found_free_kicks_against:
        return None
    return free_kicks_against


def _calculate_brownlow_votes(data: dict[str, Any]) -> int | None:
    brownlow_votes = 0
    found_brownlow_votes = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_brownlow_votes = player.brownlow_votes
        if player_brownlow_votes is None:
            continue
        found_brownlow_votes = True
        brownlow_votes += player_brownlow_votes
    if not found_brownlow_votes:
        return None
    return brownlow_votes


def _calculate_contested_possessions(data: dict[str, Any]) -> int | None:
    contested_possessions = 0
    found_contested_possessions = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_contested_possessions = player.contested_possessions
        if player_contested_possessions is None:
            continue
        found_contested_possessions = True
        contested_possessions += player_contested_possessions
    if not found_contested_possessions:
        return None
    return contested_possessions


def _calculate_uncontested_possessions(data: dict[str, Any]) -> int | None:
    uncontested_possessions = 0
    found_uncontested_possessions = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_uncontested_possessions = player.uncontested_possessions
        if player_uncontested_possessions is None:
            continue
        found_uncontested_possessions = True
        uncontested_possessions += player_uncontested_possessions
    if not found_uncontested_possessions:
        return None
    return uncontested_possessions


def _calculate_contested_marks(data: dict[str, Any]) -> int | None:
    contested_marks = 0
    found_contested_marks = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_contested_marks = player.contested_marks
        if player_contested_marks is None:
            continue
        found_contested_marks = True
        contested_marks += player_contested_marks
    if not found_contested_marks:
        return None
    return contested_marks


def _calculate_marks_inside(data: dict[str, Any]) -> int | None:
    marks_inside = 0
    found_marks_inside = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_marks_inside = player.marks_inside
        if player_marks_inside is None:
            continue
        found_marks_inside = True
        marks_inside += player_marks_inside
    if not found_marks_inside:
        return None
    return marks_inside


def _calculate_one_percenters(data: dict[str, Any]) -> int | None:
    one_percenters = 0
    found_one_percenters = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_one_percenters = player.one_percenters
        if player_one_percenters is None:
            continue
        found_one_percenters = True
        one_percenters += player_one_percenters
    if not found_one_percenters:
        return None
    return one_percenters


def _calculate_bounces(data: dict[str, Any]) -> int | None:
    bounces = 0
    found_bounces = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_bounces = player.bounces
        if player_bounces is None:
            continue
        found_bounces = True
        bounces += player_bounces
    if not found_bounces:
        return None
    return bounces


def _calculate_goal_assists(data: dict[str, Any]) -> int | None:
    goal_assists = 0
    found_goal_assists = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_goal_assists = player.goal_assists
        if player_goal_assists is None:
            continue
        found_goal_assists = True
        goal_assists += player_goal_assists
    if not found_goal_assists:
        return None
    return goal_assists


def _calcualte_field_goals_percentage(data: dict[str, Any]) -> float | None:
    field_goals = data.get(FIELD_GOALS_COLUMN)
    if field_goals is None:
        return None
    field_goals_attempted = data.get(FIELD_GOALS_ATTEMPTED_COLUMN)
    if field_goals_attempted is None:
        return None
    if field_goals_attempted == 0:
        return 0.0
    return float(field_goals) / float(field_goals_attempted)  # type: ignore


def _calculate_three_point_field_goals(data: dict[str, Any]) -> int | None:
    three_point_field_goals = 0
    found_three_point_field_goals = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_three_point_field_goals = player.three_point_field_goals
        if player_three_point_field_goals is None:
            continue
        found_three_point_field_goals = True
        three_point_field_goals += player_three_point_field_goals
    if not found_three_point_field_goals:
        return None
    return three_point_field_goals


def _calculate_three_point_field_goals_attempted(data: dict[str, Any]) -> int | None:
    three_point_field_goals_attempted = 0
    found_three_point_field_goals_attempted = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_three_point_field_goals_attempted = (
            player.three_point_field_goals_attempted
        )
        if player_three_point_field_goals_attempted is None:
            continue
        found_three_point_field_goals_attempted = True
        three_point_field_goals_attempted += player_three_point_field_goals_attempted
    if not found_three_point_field_goals_attempted:
        return None
    return three_point_field_goals_attempted


def _calculate_three_point_field_goals_percentage(data: dict[str, Any]) -> float | None:
    three_point_field_goals = data.get(TEAM_THREE_POINT_FIELD_GOALS_COLUMN)
    if three_point_field_goals is None:
        return None
    three_point_field_goals_attempted = data.get(
        TEAM_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN
    )
    if three_point_field_goals_attempted is None:
        return None
    if three_point_field_goals_attempted == 0:
        return 0.0
    return float(three_point_field_goals) / float(three_point_field_goals_attempted)  # type: ignore


def _calculate_free_throws(data: dict[str, Any]) -> int | None:
    free_throws = 0
    found_free_throws = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_free_throws = player.free_throws
        if player_free_throws is None:
            continue
        found_free_throws = True
        free_throws += player_free_throws
    if not found_free_throws:
        return None
    return free_throws


def _calculate_free_throws_attempted(data: dict[str, Any]) -> int | None:
    free_throws_attempted = 0
    found_free_throws_attempted = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_free_throws_attempted = player.free_throws_attempted
        if player_free_throws_attempted is None:
            continue
        found_free_throws_attempted = True
        free_throws_attempted += player_free_throws_attempted
    if not found_free_throws_attempted:
        return None
    return free_throws_attempted


def _calculate_free_throws_percentage(data: dict[str, Any]) -> float | None:
    free_throws = data.get(TEAM_FREE_THROWS_COLUMN)
    if free_throws is None:
        return None
    free_throws_attempted = data.get(TEAM_FREE_THROWS_ATTEMPTED_COLUMN)
    if free_throws_attempted is None:
        return None
    if free_throws_attempted == 0:
        return 0.0
    return float(free_throws) / float(free_throws_attempted)  # type: ignore


def _calculate_defensive_rebounds(data: dict[str, Any]) -> int | None:
    defensive_rebounds = 0
    found_defensive_rebounds = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_defensive_rebounds = player.defensive_rebounds
        if player_defensive_rebounds is None:
            continue
        found_defensive_rebounds = True
        defensive_rebounds += player_defensive_rebounds
    if not found_defensive_rebounds:
        return None
    return defensive_rebounds


def _calculate_total_rebounds(data: dict[str, Any]) -> int | None:
    offensive_rebounds = data.get(OFFENSIVE_REBOUNDS_COLUMN)
    if offensive_rebounds is None:
        return None
    defensive_rebounds = data.get(TEAM_DEFENSIVE_REBOUNDS_COLUMN)
    if defensive_rebounds is None:
        return None
    return offensive_rebounds + defensive_rebounds


def _calculate_steals(data: dict[str, Any]) -> int | None:
    steals = 0
    found_steals = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_steals = player.steals
        if player_steals is None:
            continue
        found_steals = True
        steals += player_steals
    if not found_steals:
        return None
    return steals


def _calculate_blocks(data: dict[str, Any]) -> int | None:
    blocks = 0
    found_blocks = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_blocks = player.blocks
        if player_blocks is None:
            continue
        found_blocks = True
        blocks += player_blocks
    if not found_blocks:
        return None
    return blocks


def _calculate_personal_fouls(data: dict[str, Any]) -> int | None:
    personal_fouls = 0
    found_personal_fouls = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_personal_fouls = player.personal_fouls
        if player_personal_fouls is None:
            continue
        found_personal_fouls = True
        personal_fouls += player_personal_fouls
    if not found_personal_fouls:
        return None
    return personal_fouls


def _calculate_forced_fumbles(data: dict[str, Any]) -> float | None:
    forced_fumbles = 0.0
    found_forced_fumbles = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_forced_fumbles = player.forced_fumbles
        if player_forced_fumbles is None:
            continue
        found_forced_fumbles = True
        forced_fumbles += player_forced_fumbles
    if not found_forced_fumbles:
        return None
    return forced_fumbles


def _calculate_fumbles_recovered(data: dict[str, Any]) -> float | None:
    fumbles_recovered = 0.0
    found_fumbles_recovered = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_fumbles_recovered = player.fumbles_recovered
        if player_fumbles_recovered is None:
            continue
        found_fumbles_recovered = True
        fumbles_recovered += player_fumbles_recovered
    if not found_fumbles_recovered:
        return None
    return fumbles_recovered


def _calculate_fumbles_touchdowns(data: dict[str, Any]) -> float | None:
    fumbles_touchdowns = 0.0
    found_fumbles_touchdowns = False
    for player in data.get(PLAYER_COLUMN_PREFIX, []):
        player_fumbles_touchdowns = player.fumbles_touchdowns
        if player_fumbles_touchdowns is None:
            continue
        found_fumbles_touchdowns = True
        fumbles_touchdowns += player_fumbles_touchdowns
    if not found_fumbles_touchdowns:
        return None
    return fumbles_touchdowns


class TeamModel(BaseModel):
    """The serialisable team class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    identifier: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=TEAM_IDENTIFIER_COLUMN,
    )
    name: str = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.TEXT}, alias=NAME_COLUMN
    )
    location: str | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL}
    )
    players: list[PlayerModel] = Field(..., alias=PLAYER_COLUMN_PREFIX)
    odds: list[OddsModel] = Field(..., alias=TEAM_ODDS_COLUMN)
    points: float | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.POINTS}, alias=TEAM_POINTS_COLUMN
    )
    ladder_rank: int | None
    kicks: int | None = Field(
        default_factory=_calculate_kicks,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=KICKS_COLUMN,
    )
    news: list[NewsModel] = Field(..., alias=TEAM_NEWS_COLUMN)
    social: list[SocialModel]
    field_goals: float | None = Field(
        default_factory=_calculate_field_goals,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=FIELD_GOALS_COLUMN,
    )
    field_goals_attempted: int | None = Field(
        default_factory=_calculate_field_goals_attempted,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    offensive_rebounds: int | None = Field(
        default_factory=_calculate_offensive_rebounds,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=OFFENSIVE_REBOUNDS_COLUMN,
    )
    assists: int | None = Field(
        default_factory=_calculate_assists,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=ASSISTS_COLUMN,
    )
    turnovers: int | None = Field(
        default_factory=_calculate_turnovers,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TURNOVERS_COLUMN,
    )
    marks: int | None = Field(
        default_factory=_calculate_marks,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MARKS_COLUMN,
    )
    handballs: int | None = Field(
        default_factory=_calculate_handballs,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HANDBALLS_COLUMN,
    )
    disposals: int | None = Field(
        default_factory=_calculate_disposals,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DISPOSALS_COLUMN,
    )
    goals: int | None = Field(
        default_factory=_calculate_goals,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOALS_COLUMN,
    )
    behinds: int | None = Field(
        default_factory=_calculate_behinds,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BEHINDS_COLUMN,
    )
    hit_outs: int | None = Field(
        default_factory=_calculate_hit_outs,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HIT_OUTS_COLUMN,
    )
    tackles: int | None = Field(
        default_factory=_calculate_tackles,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TACKLES_COLUMN,
    )
    rebounds: int | None = Field(
        default_factory=_calculate_rebounds,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REBOUNDS_COLUMN,
    )
    insides: int | None = Field(
        default_factory=_calculate_insides,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INSIDES_COLUMN,
    )
    clearances: int | None = Field(
        default_factory=_calculate_clearances,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CLEARANCES_COLUMN,
    )
    clangers: int | None = Field(
        default_factory=_calculate_clangers,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CLANGERS_COLUMN,
    )
    free_kicks_for: int | None = Field(
        default_factory=_calculate_free_kicks_for,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_KICKS_FOR_COLUMN,
    )
    free_kicks_against: int | None = Field(
        default_factory=_calculate_free_kicks_against,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_KICKS_AGAINST_COLUMN,
    )
    brownlow_votes: int | None = Field(
        default_factory=_calculate_brownlow_votes,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BROWNLOW_VOTES_COLUMN,
    )
    contested_possessions: int | None = Field(
        default_factory=_calculate_contested_possessions,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CONTESTED_POSSESSIONS_COLUMN,
    )
    uncontested_possessions: int | None = Field(
        default_factory=_calculate_uncontested_possessions,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_UNCONTESTED_POSSESSIONS_COLUMN,
    )
    contested_marks: int | None = Field(
        default_factory=_calculate_contested_marks,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CONTESTED_MARKS_COLUMN,
    )
    marks_inside: int | None = Field(
        default_factory=_calculate_marks_inside,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MARKS_INSIDE_COLUMN,
    )
    one_percenters: int | None = Field(
        default_factory=_calculate_one_percenters,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ONE_PERCENTERS_COLUMN,
    )
    bounces: int | None = Field(
        default_factory=_calculate_bounces,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BOUNCES_COLUMN,
    )
    goal_assists: int | None = Field(
        default_factory=_calculate_goal_assists,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOAL_ASSISTS_COLUMN,
    )
    coaches: list[CoachModel] = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=TEAM_COACHES_COLUMN
    )
    lbw: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LENGTH_BEHIND_WINNER_COLUMN,
    )
    end_dt: datetime.datetime | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD}, alias=TEAM_END_DT_COLUMN
    )
    field_goals_percentage: float | None = Field(
        default_factory=_calcualte_field_goals_percentage,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_PERCENTAGE_COLUMN,
    )
    three_point_field_goals: int | None = Field(
        default_factory=_calculate_three_point_field_goals,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THREE_POINT_FIELD_GOALS_COLUMN,
    )
    three_point_field_goals_attempted: int | None = Field(
        default_factory=_calculate_three_point_field_goals_attempted,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    three_point_field_goals_percentage: float | None = Field(
        default_factory=_calculate_three_point_field_goals_percentage,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THREE_POINT_FIELD_GOALS_PERCENTAGE_COLUMN,
    )
    free_throws: float | None = Field(
        default_factory=_calculate_free_throws,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_THROWS_COLUMN,
    )
    free_throws_attempted: int | None = Field(
        default_factory=_calculate_free_throws_attempted,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_THROWS_ATTEMPTED_COLUMN,
    )
    free_throws_percentage: float | None = Field(
        default_factory=_calculate_free_throws_percentage,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_THROWS_PERCENTAGE_COLUMN,
    )
    defensive_rebounds: int | None = Field(
        default_factory=_calculate_defensive_rebounds,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEFENSIVE_REBOUNDS_COLUMN,
    )
    total_rebounds: int | None = Field(
        default_factory=_calculate_total_rebounds,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_REBOUNDS_COLUMN,
    )
    steals: int | None = Field(
        default_factory=_calculate_steals,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STEALS_COLUMN,
    )
    blocks: int | None = Field(
        default_factory=_calculate_blocks,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOCKS_COLUMN,
    )
    personal_fouls: int | None = Field(
        default_factory=_calculate_personal_fouls,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PERSONAL_FOULS_COLUMN,
    )
    forced_fumbles: float | None = Field(
        default_factory=_calculate_forced_fumbles,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FORCED_FUMBLES_COLUMN,
    )
    fumbles_recovered: float | None = Field(
        default_factory=_calculate_fumbles_recovered,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLES_RECOVERED_COLUMN,
    )
    fumbles_touchdowns: float | None = Field(
        default_factory=_calculate_fumbles_touchdowns,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLES_TOUCHDOWNS_COLUMN,
    )
    runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUNS_COLUMN,
    )
    wickets: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WICKETS_COLUMN,
    )
    overs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OVERS_COLUMN,
    )
    balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BALLS_COLUMN,
    )
    byes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BYES_COLUMN,
    )
    leg_byes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LEG_BYES_COLUMN,
    )
    wides: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WIDES_COLUMN,
    )
    no_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NO_BALLS_COLUMN,
    )
    penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTIES_COLUMN,
    )
    balls_per_over: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BALLS_PER_OVER_COLUMN,
    )
    fours: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOURS_COLUMN,
    )
    sixes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SIXES_COLUMN,
    )
    catches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHES_COLUMN,
    )
    catches_dropped: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHES_DROPPED_COLUMN,
    )
    tackles_inside_50: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TACKLES_INSIDE_50_COLUMN,
    )
    total_possessions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_POSSESSIONS_COLUMN,
    )
    uncontested_marks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_UNCONTESTED_MARKS_COLUMN,
    )
    disposal_efficiency: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DISPOSAL_EFFICIENCY_COLUMN,
    )
    centre_clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CENTRE_CLEARANCES_COLUMN,
    )
    stoppage_clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STOPPAGE_CLEARANCES_COLUMN,
    )
    goal_accuracy: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOAL_ACCURACY_COLUMN,
    )
    rushed_behinds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHED_BEHINDS_COLUMN,
    )
    touched_behinds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOUCHED_BEHINDS_COLUMN,
    )
    left_behinds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LEFT_BEHINDS_COLUMN,
    )
    left_posters: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LEFT_POSTERS_COLUMN,
    )
    right_behinds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RIGHT_BEHINDS_COLUMN,
    )
    right_posters: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RIGHT_POSTERS_COLUMN,
    )
    total_interchange_count: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_INTERCHANGE_COUNT_COLUMN,
    )
    interchange_count_q1: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCHANGE_COUNT_Q1_COLUMN,
    )
    interchange_count_q2: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCHANGE_COUNT_Q2_COLUMN,
    )
    interchange_count_q3: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCHANGE_COUNT_Q3_COLUMN,
    )
    interchange_count_q4: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCHANGE_COUNT_Q4_COLUMN,
    )
    game_winning_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GAME_WINNING_GOALS_COLUMN,
    )
    headed_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HEADED_GOALS_COLUMN,
    )
    inaccurate_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INACCURATE_CROSSES_COLUMN,
    )
    inaccurate_long_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INACCURATE_LONGBALLS_COLUMN,
    )
    inaccurate_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INACCURATE_PASSES_COLUMN,
    )
    inaccurate_through_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INACCURATE_THROUGH_BALLS_COLUMN,
    )
    left_footed_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LEFT_FOOTED_SHOTS_COLUMN,
    )
    longball_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONGBALL_PERCENTAGE_COLUMN,
    )
    offsides: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OFFSIDES_COLUMN,
    )
    penalty_kick_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICK_GOALS_COLUMN,
    )
    penalty_kick_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICK_PERCENTAGE_COLUMN,
    )
    penalty_kick_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICK_SHOTS_COLUMN,
    )
    penalty_kicks_missed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICKS_MISSED_COLUMN,
    )
    possession_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POSSESSION_PERCENTAGE_COLUMN,
    )
    possession_time: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POSSESSION_TIME_COLUMN,
    )
    right_footed_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RIGHT_FOOTED_SHOTS_COLUMN,
    )
    shoot_out_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOT_OUT_GOALS_COLUMN,
    )
    shoot_out_misses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOT_OUT_MISSES_COLUMN,
    )
    shoot_out_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOT_OUT_PERCENTAGE_COLUMN,
    )
    shot_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOT_ASSISTS_COLUMN,
    )
    shot_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOT_PERCENTAGE_COLUMN,
    )
    shots_headed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_HEADED_COLUMN,
    )
    shots_off_target: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_OFF_TARGET_COLUMN,
    )
    shots_on_post: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_ON_POST_COLUMN,
    )
    shots_on_target: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_ON_TARGET_COLUMN,
    )
    through_ball_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THROUGH_BALL_PERCENTAGE_COLUMN,
    )
    total_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_CROSSES_COLUMN,
    )
    total_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_GOALS_COLUMN,
    )
    total_long_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_LONGBALLS_COLUMN,
    )
    total_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_PASSES_COLUMN,
    )
    total_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_SHOTS_COLUMN,
    )
    total_through_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_THROUGH_BALLS_COLUMN,
    )
    draws: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DRAWS_COLUMN,
    )
    sub_outs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SUB_OUTS_COLUMN,
    )
    suspensions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SUSPENSIONS_COLUMN,
    )
    time_ended: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TIME_ENDED_COLUMN,
    )
    time_started: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TIME_STARTED_COLUMN,
    )
    win_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WIN_PERCENTAGE_COLUMN,
    )
    wins: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WINS_COLUMN,
    )
    won_corners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WON_CORNERS_COLUMN,
    )
    yellow_cards: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YELLOW_CARDS_COLUMN,
    )
    clean_sheet: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CLEAN_SHEET_COLUMN,
    )
    crosses_caught: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CROSSES_CAUGHT_COLUMN,
    )
    goals_conceded: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOALS_CONCEDED_COLUMN,
    )
    partial_clean_sheet: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PARTIAL_CLEAN_SHEET_COLUMN,
    )
    penalty_kick_conceded: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICK_CONCEDED_COLUMN,
    )
    penalty_kick_save_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICK_SAVE_PERCENTAGE_COLUMN,
    )
    penalty_kicks_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICKS_FACED_COLUMN,
    )
    penalty_kicks_saved: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KICKS_SAVED_COLUMN,
    )
    punches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNCHES_COLUMN,
    )
    saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SAVES_COLUMN,
    )
    shoot_out_kicks_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOT_OUT_KICKS_FACED_COLUMN,
    )
    shoot_out_kicks_saved: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOT_OUT_KICKS_SAVED_COLUMN,
    )
    shoot_out_save_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOT_OUT_SAVE_PERCENTAGE_COLUMN,
    )
    shots_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_FACED_COLUMN,
    )
    smothers: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SMOTHERS_COLUMN,
    )
    unclaimed_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_UNCLAIMED_CROSSES_COLUMN,
    )
    accurate_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ACCURATE_CROSSES_COLUMN,
    )
    accurate_long_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ACCURATE_LONG_BALLS_COLUMN,
    )
    accurate_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ACCURATE_PASSES_COLUMN,
    )
    accurate_through_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ACCURATE_THROUGH_BALLS_COLUMN,
    )
    cross_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CROSS_PERCENTAGE_COLUMN,
    )
    free_kick_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_KICK_GOALS_COLUMN,
    )
    free_kick_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_KICK_PERCENTAGE_COLUMN,
    )
    free_kick_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_KICK_SHOTS_COLUMN,
    )
    game_winning_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GAME_WINNING_ASSISTS_COLUMN,
    )
    blocked_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOCKED_SHOTS_COLUMN,
    )
    effective_clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EFFECTIVE_CLEARANCES_COLUMN,
    )
    effective_tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EFFECTIVE_TACKLES_COLUMN,
    )
    ineffective_tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INEFFECTIVE_TACKLES_COLUMN,
    )
    interceptions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCEPTIONS_COLUMN,
    )
    tackle_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TACKLE_PERCENTAGE_COLUMN,
    )
    appearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_APPEARANCES_COLUMN,
    )
    average_rating_from_correspondent: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_RATING_FROM_CORRESPONDENT_COLUMN,
    )
    average_rating_from_data_feed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_RATING_FROM_DATA_FEED_COLUMN,
    )
    average_rating_from_editor: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_RATING_FROM_EDITOR_COLUMN,
    )
    average_rating_from_user: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_RATING_FROM_USER_COLUMN,
    )
    did_not_play: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DID_NOT_PLAY_COLUMN,
    )
    fouls_committed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOULS_COMMITTED_COLUMN,
    )
    fouls_suffered: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOULS_SUFFERED_COLUMN,
    )
    goal_difference: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOAL_DIFFERENCE_COLUMN,
    )
    losses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LOSSES_COLUMN,
    )
    lost_corners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LOST_CORNERS_COLUMN,
    )
    minutes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MINUTES_COLUMN,
    )
    own_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OWN_GOALS_COLUMN,
    )
    pass_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASS_PERCENTAGE_COLUMN,
    )
    red_cards: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RED_CARDS_COLUMN,
    )
    starts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STARTS_COLUMN,
    )
    sub_ins: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SUB_INS_COLUMN,
    )
    pitch_count: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PITCH_COUNT_COLUMN,
    )
    strikes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STRIKES_COLUMN,
    )
    strike_pitch_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STRIKE_PITCH_RATIO_COLUMN,
    )
    games_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GAMES_PLAYED_COLUMN,
    )
    team_games_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TEAM_GAMES_PLAYED_COLUMN,
    )
    double_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DOUBLE_PLAYS_COLUMN,
    )
    opportunities: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPPORTUNITIES_COLUMN,
    )
    errors: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ERRORS_COLUMN,
    )
    passed_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSED_BALLS_COLUMN,
    )
    outfield_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OUTFIELD_ASSISTS_COLUMN,
    )
    pickoffs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PICKOFFS_COLUMN,
    )
    putouts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUTOUTS_COLUMN,
    )
    outs_on_field: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OUTS_ON_FIELD_COLUMN,
    )
    triple_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TRIPLE_PLAYS_COLUMN,
    )
    balls_in_zone: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BALLS_IN_ZONE_COLUMN,
    )
    extra_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_BASES_COLUMN,
    )
    outs_made: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OUTS_MADE_COLUMN,
    )
    catcher_third_innings_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_THIRD_INNINGS_PLAYED_COLUMN,
    )
    catcher_caught_stealing: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_CAUGHT_STEALING_COLUMN,
    )
    catcher_stolen_bases_allowed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_STOLEN_BASES_ALLOWED_COLUMN,
    )
    catcher_earned_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_EARNED_RUNS_COLUMN,
    )
    is_qualified_catcher: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_IS_QUALIFIED_CATCHER_COLUMN,
    )
    is_qualified_pitcher: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_IS_QUALIFIED_PITCHER_COLUMN,
    )
    successful_chances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SUCCESSFUL_CHANCES_COLUMN,
    )
    total_chances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_CHANCES_COLUMN,
    )
    full_innings_played: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FULL_INNINGS_PLAYED_COLUMN,
    )
    part_innings_played: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PART_INNINGS_PLAYED_COLUMN,
    )
    fielding_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELDING_PERCENTAGE_COLUMN,
    )
    range_factor: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RANGE_FACTOR_COLUMN,
    )
    zone_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ZONE_RATING_COLUMN,
    )
    catcher_caught_stealing_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_CAUGHT_STEALING_PERCENTAGE_COLUMN,
    )
    catcher_era: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_ERA_COLUMN,
    )
    def_warbr: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEF_WARBR_COLUMN,
    )
    perfect_games: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PERFECT_GAMES_COLUMN,
    )
    wild_pitches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WILD_PITCHES_COLUMN,
    )
    third_innings: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THIRD_INNINGS_COLUMN,
    )
    team_earned_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TEAM_EARNED_RUNS_COLUMN,
    )
    shutouts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHUTOUTS_COLUMN,
    )
    pickoff_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PICKOFF_ATTEMPTS_COLUMN,
    )
    run_support: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUN_SUPPORT_COLUMN,
    )
    pitches_as_starter: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PITCHES_AS_STARTER_COLUMN,
    )
    quality_starts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_QUALITY_STARTS_COLUMN,
    )
    inherited_runners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INHERITED_RUNNERS_COLUMN,
    )
    inherited_runners_scored: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INHERITED_RUNNERS_SCORED_COLUMN,
    )
    opponent_total_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPPONENT_TOTAL_BASES_COLUMN,
    )
    is_qualified_saves: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_IS_QUALIFIED_SAVES_COLUMN,
    )
    full_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FULL_INNINGS_COLUMN,
    )
    part_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PART_INNINGS_COLUMN,
    )
    blown_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOWN_SAVES_COLUMN,
    )
    innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INNINGS_COLUMN,
    )
    era: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ERA_COLUMN,
    )
    whip: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WHIP_COLUMN,
    )
    caught_stealing_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CAUGHT_STEALING_PERCENTAGE_COLUMN,
    )
    pitches_per_start: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PITCHES_PER_START_COLUMN,
    )
    pitches_per_inning: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PITCHES_PER_INNING_COLUMN,
    )
    run_support_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUN_SUPPORT_AVERAGE_COLUMN,
    )
    opponent_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPPONENT_AVERAGE_COLUMN,
    )
    opponent_slug_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPPONENT_SLUG_AVERAGE_COLUMN,
    )
    opponent_on_base_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPPONENT_ON_BASE_PERCENTAGE_COLUMN,
    )
    opponent_ops: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPPONENT_OPS_COLUMN,
    )
    save_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SAVE_PERCENTAGE_COLUMN,
    )
    strikeouts_per_nine_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STRIKEOUTS_PER_NINE_INNINGS_COLUMN,
    )
    strikeout_to_walk_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STRIKEOUT_TO_WALK_RATIO_COLUMN,
    )
    tough_losses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOUGH_LOSSES_COLUMN,
    )
    cheap_wins: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CHEAP_WINS_COLUMN,
    )
    save_opportunities_per_win: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SAVE_OPPORTUNITIES_PER_WIN_COLUMN,
    )
    runs_created: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUNS_CREATED_COLUMN,
    )
    batting_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BATTING_AVERAGE_COLUMN,
    )
    pinch_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PINCH_AVERAGE_COLUMN,
    )
    slug_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SLUG_AVERAGE_COLUMN,
    )
    secondary_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SECONDARY_AVERAGE_COLUMN,
    )
    on_base_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ON_BASE_PERCENTAGE_COLUMN,
    )
    ops: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPS_COLUMN,
    )
    ground_to_fly_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GROUND_TO_FLY_RATIO_COLUMN,
    )
    runs_created_per_27_outs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUNS_CREATED_PER_27_OUTS_COLUMN,
    )
    batter_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BATTER_RATING_COLUMN,
    )
    at_bats_per_home_run: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AT_BATS_PER_HOME_RUN_COLUMN,
    )
    stolen_base_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STOLEN_BASE_PERCENTAGE_COLUMN,
    )
    pitches_per_plate_appearance: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PITCHES_PER_PLATE_APPEARANCE_COLUMN,
    )
    isolated_power: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ISOLATED_POWER_COLUMN,
    )
    walk_to_strikeout_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WALK_TO_STRIKEOUT_RATIO_COLUMN,
    )
    walks_per_plate_appearance: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WALKS_PER_PLATE_APPEARANCE_COLUMN,
    )
    secondary_average_minus_batting_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SECONDARY_AVERAGE_MINUS_BATTING_AVERAGE_COLUMN,
    )
    runs_produced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUNS_PRODUCED_COLUMN,
    )
    runs_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUNS_RATIO_COLUMN,
    )
    patience_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PATIENCE_RATIO_COLUMN,
    )
    balls_in_play_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BALLS_IN_PLAY_AVERAGE_COLUMN,
    )
    mlb_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MLB_RATING_COLUMN,
    )
    offensive_wins_above_replacement: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OFFENSIVE_WINS_ABOVE_REPLACEMENT_COLUMN,
    )
    wins_above_replacement: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WINS_ABOVE_REPLACEMENT_COLUMN,
    )
    earned_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EARNED_RUNS_COLUMN,
    )
    batters_hit: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BATTERS_HIT_COLUMN,
    )
    sacrifice_bunts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACRIFICE_BUNTS_COLUMN,
    )
    save_opportunities: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SAVE_OPPORTUNITIES_COLUMN,
    )
    finishes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FINISHES_COLUMN,
    )
    balks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BALKS_COLUMN,
    )
    batters_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BATTERS_FACED_COLUMN,
    )
    holds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HOLDS_COLUMN,
    )
    complete_games: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_COMPLETE_GAMES_COLUMN,
    )
    hit_by_pitch: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HIT_BY_PITCH_COLUMN,
    )
    ground_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GROUND_BALLS_COLUMN,
    )
    strikeouts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STRIKEOUTS_COLUMN,
    )
    rbis: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RBIS_COLUMN,
    )
    sac_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SAC_HITS_COLUMN,
    )
    hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HITS_COLUMN,
    )
    stolen_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STOLEN_BASES_COLUMN,
    )
    walks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_WALKS_COLUMN,
    )
    catcher_interference: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CATCHER_INTERFERENCE_COLUMN,
    )
    gidps: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GIDPS_COLUMN,
    )
    sacrifice_flies: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACRIFICE_FLIES_COLUMN,
    )
    at_bats: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AT_BATS_COLUMN,
    )
    home_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HOME_RUNS_COLUMN,
    )
    grand_slam_home_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GRAND_SLAM_HOME_RUNS_COLUMN,
    )
    runners_left_on_base: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUNNERS_LEFT_ON_BASE_COLUMN,
    )
    triples: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TRIPLES_COLUMN,
    )
    game_winning_rbis: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GAME_WINNING_RBIS_COLUMN,
    )
    intentional_walks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTENTIONAL_WALKS_COLUMN,
    )
    doubles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DOUBLES_COLUMN,
    )
    fly_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FLY_BALLS_COLUMN,
    )
    caught_stealing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_CAUGHT_STEALING_COLUMN,
    )
    pitches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PITCHES_COLUMN,
    )
    games_started: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GAMES_STARTED_COLUMN,
    )
    pinch_at_bats: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PINCH_AT_BATS_COLUMN,
    )
    pinch_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PINCH_HITS_COLUMN,
    )
    player_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PLAYER_RATING_COLUMN,
    )
    is_qualified: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_IS_QUALIFIED_COLUMN,
    )
    is_qualified_steals: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_IS_QUALIFIED_STEALS_COLUMN,
    )
    total_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_BASES_COLUMN,
    )
    plate_appearances: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PLATE_APPEARANCES_COLUMN,
    )
    projected_home_runs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PROJECTED_HOME_RUNS_COLUMN,
    )
    extra_base_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_BASE_HITS_COLUMN,
    )
    average_game_score: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_GAME_SCORE_COLUMN,
    )
    average_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_three_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_THREE_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    average_three_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_free_throws_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_FREE_THROWS_MADE_COLUMN,
    )
    average_free_throws_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_FREE_THROWS_ATTEMPTED_COLUMN,
    )
    average_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_POINTS_COLUMN,
    )
    average_offensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_OFFENSIVE_REBOUNDS_COLUMN,
    )
    average_assists: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_ASSISTS_COLUMN,
    )
    average_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TURNOVERS_COLUMN,
    )
    offensive_rebound_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OFFENSIVE_REBOUND_PERCENTAGE_COLUMN,
    )
    estimated_possessions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ESTIMATED_POSSESSIONS_COLUMN,
    )
    average_estimated_possessions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_ESTIMATED_POSSESSIONS_COLUMN,
    )
    points_per_estimated_possessions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POINTS_PER_ESTIMATED_POSSESSIONS_COLUMN,
    )
    average_team_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TEAM_TURNOVERS_COLUMN,
    )
    average_total_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TOTAL_TURNOVERS_COLUMN,
    )
    two_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    two_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_two_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TWO_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    average_two_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    two_point_field_goal_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_FIELD_GOAL_PERCENTAGE_COLUMN,
    )
    shooting_efficiency: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOTING_EFFICIENCY_COLUMN,
    )
    scoring_efficiency: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SCORING_EFFICIENCY_COLUMN,
    )
    average_48_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_FIELD_GOALS_MADE_COLUMN,
    )
    average_48_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_48_three_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_THREE_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    average_48_three_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_48_free_throws_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_FREE_THROWS_MADE_COLUMN,
    )
    average_48_free_throws_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_FREE_THROWS_ATTEMPTED_COLUMN,
    )
    average_48_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_POINTS_COLUMN,
    )
    average_48_offensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_OFFENSIVE_REBOUNDS_COLUMN,
    )
    average_48_assists: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_ASSISTS_COLUMN,
    )
    average_48_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_TURNOVERS_COLUMN,
    )
    average_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_REBOUNDS_COLUMN,
    )
    average_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_FOULS_COLUMN,
    )
    average_flagrant_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_FLAGRANT_FOULS_COLUMN,
    )
    average_technical_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TECHNICAL_FOULS_COLUMN,
    )
    average_ejections: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_EJECTIONS_COLUMN,
    )
    average_disqualifications: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_DISQUALIFICATIONS_COLUMN,
    )
    assist_turnover_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ASSIST_TURNOVER_RATIO_COLUMN,
    )
    steal_foul_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STEAL_FOUL_RATIO_COLUMN,
    )
    block_foul_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOCK_FOUL_RATIO_COLUMN,
    )
    average_team_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_TEAM_REBOUNDS_COLUMN,
    )
    total_technical_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_TECHNICAL_FOULS_COLUMN,
    )
    team_assist_turnover_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TEAM_ASSIST_TURNOVER_RATIO_COLUMN,
    )
    steal_turnover_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STEAL_TURNOVER_RATIO_COLUMN,
    )
    average_48_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_REBOUNDS_COLUMN,
    )
    average_48_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_FOULS_COLUMN,
    )
    average_48_flagrant_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_FLAGRANT_FOULS_COLUMN,
    )
    average_48_technical_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_TECHNICAL_FOULS_COLUMN,
    )
    average_48_ejections: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_EJECTIONS_COLUMN,
    )
    average_48_disqualifications: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_DISQUALIFICATIONS_COLUMN,
    )
    double_double: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DOUBLE_DOUBLE_COLUMN,
    )
    triple_double: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TRIPLE_DOUBLE_COLUMN,
    )
    field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_COLUMN,
    )
    free_throws_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FREE_THROWS_MADE_COLUMN,
    )
    three_point_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THREE_POINT_PERCENTAGE_COLUMN,
    )
    three_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THREE_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    team_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TEAM_TURNOVERS_COLUMN,
    )
    total_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_TURNOVERS_COLUMN,
    )
    points_in_paint: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POINTS_IN_PAINT_COLUMN,
    )
    brick_index: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BRICK_INDEX_COLUMN,
    )
    fast_break_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FAST_BREAK_POINTS_COLUMN,
    )
    average_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_FIELD_GOALS_MADE_COLUMN,
    )
    turnover_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TURNOVER_POINTS_COLUMN,
    )
    average_defensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_DEFENSIVE_REBOUNDS_COLUMN,
    )
    average_blocks: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_BLOCKS_COLUMN,
    )
    average_steals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_STEALS_COLUMN,
    )
    average_48_defensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_DEFENSIVE_REBOUNDS_COLUMN,
    )
    average_48_blocks: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_BLOCKS_COLUMN,
    )
    average_48_steals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_48_STEALS_COLUMN,
    )
    largest_lead: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LARGEST_LEAD_COLUMN,
    )
    disqualifications: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DISQUALIFICATIONS_COLUMN,
    )
    flagrant_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FLAGRANT_FOULS_COLUMN,
    )
    fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOULS_COLUMN,
    )
    ejections: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EJECTIONS_COLUMN,
    )
    technical_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TECHNICAL_FOULS_COLUMN,
    )
    vorp: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_VORP_COLUMN,
    )
    average_minutes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_MINUTES_COLUMN,
    )
    nba_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NBA_RATING_COLUMN,
    )
    fourth_down_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOURTH_DOWN_ATTEMPTS_COLUMN,
    )
    fourth_down_conversion_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOURTH_DOWN_CONVERSION_PERCENTAGE_COLUMN,
    )
    fourth_down_conversions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FOURTH_DOWN_CONVERSIONS_COLUMN,
    )
    possession_time_seconds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POSSESSION_TIME_SECONDS_COLUMN,
    )
    redzone_attempt_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_ATTEMPT_POINTS_COLUMN,
    )
    redzone_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_ATTEMPTS_COLUMN,
    )
    redzone_conversions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_CONVERSIONS_COLUMN,
    )
    redzone_efficiency_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_EFFICIENCY_PERCENTAGE_COLUMN,
    )
    redzone_end_downs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_END_DOWNS_COLUMN,
    )
    redzone_end_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_END_GAME_COLUMN,
    )
    redzone_end_half: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_END_HALF_COLUMN,
    )
    redzone_field_goal_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_FIELD_GOAL_PERCENTAGE_COLUMN,
    )
    redzone_field_goal_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_FIELD_GOAL_POINTS_COLUMN,
    )
    redzone_field_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_FIELD_GOALS_COLUMN,
    )
    redzone_field_goals_missed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_FIELD_GOALS_MISSED_COLUMN,
    )
    redzone_fumble: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_FUMBLE_COLUMN,
    )
    redzone_interception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_INTERCEPTION_COLUMN,
    )
    redzone_scoring_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_SCORING_PERCENTAGE_COLUMN,
    )
    redzone_total_points: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_TOTAL_POINTS_COLUMN,
    )
    redzone_touchdown_pass: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_TOUCHDOWN_PASS_COLUMN,
    )
    redzone_touchdown_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_TOUCHDOWN_PERCENTAGE_COLUMN,
    )
    redzone_touchdown_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_TOUCHDOWN_POINTS_COLUMN,
    )
    redzone_touchdown_rush: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_TOUCHDOWN_RUSH_COLUMN,
    )
    redzone_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_REDZONE_TOUCHDOWNS_COLUMN,
    )
    third_down_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THIRD_DOWN_ATTEMPTS_COLUMN,
    )
    third_down_conversion_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THIRD_DOWN_CONVERSION_PERCENTAGE_COLUMN,
    )
    third_down_conversions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_THIRD_DOWN_CONVERSIONS_COLUMN,
    )
    timeouts_used: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TIMEOUTS_USED_COLUMN,
    )
    total_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_PENALTIES_COLUMN,
    )
    total_penalty_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_PENALTY_YARDS_COLUMN,
    )
    total_plays: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_PLAYS_COLUMN,
    )
    total_drives: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_DRIVES_COLUMN,
    )
    turn_over_differential: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TURN_OVER_DIFFERENTIAL_COLUMN,
    )
    punt_returns_started_inside_the_10: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURNS_STARTED_INSIDE_THE_10_COLUMN,
    )
    punt_returns_started_inside_the_20: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURNS_STARTED_INSIDE_THE_20_COLUMN,
    )
    punt_return_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURN_TOUCHDOWNS_COLUMN,
    )
    punt_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURN_YARDS_COLUMN,
    )
    special_team_fumble_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN,
    )
    special_team_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN,
    )
    yards_per_kick_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_KICK_RETURN_COLUMN,
    )
    yards_per_punt_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_PUNT_RETURN_COLUMN,
    )
    yards_per_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_RETURN_COLUMN,
    )
    average_punt_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_PUNT_RETURN_YARDS_COLUMN,
    )
    gross_average_punt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GROSS_AVERAGE_PUNT_YARDS_COLUMN,
    )
    long_punt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_PUNT_COLUMN,
    )
    net_average_punt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_AVERAGE_PUNT_YARDS_COLUMN,
    )
    punts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_COLUMN,
    )
    punts_blocked: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_BLOCKED_COLUMN,
    )
    punts_blocked_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_BLOCKED_PERCENTAGE_COLUMN,
    )
    punts_inside_10: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_INSIDE_THE_10_COLUMN,
    )
    punts_inside_10_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_INSIDE_THE_10_PERCENTAGE_COLUMN,
    )
    punts_inside_20: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_INSIDE_THE_20_COLUMN,
    )
    punts_inside_20_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_INSIDE_THE_20_PERCENTAGE_COLUMN,
    )
    punts_over_50: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNTS_OVER_50_COLUMN,
    )
    punt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_YARDS_COLUMN,
    )
    defensive_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEFENSIVE_POINTS_COLUMN,
    )
    kick_extra_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_EXTRA_POINTS_COLUMN,
    )
    kick_extra_points_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_EXTRA_POINTS_MADE_COLUMN,
    )
    misc_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MISC_POINTS_COLUMN,
    )
    return_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RETURN_TOUCHDOWNS_COLUMN,
    )
    total_two_point_conversions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_TWO_POINT_CONVERSIONS_COLUMN,
    )
    first_downs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIRST_DOWNS_COLUMN,
    )
    first_downs_passing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIRST_DOWNS_PASSING_COLUMN,
    )
    first_downs_penalty: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIRST_DOWNS_PENALTY_COLUMN,
    )
    first_downs_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIRST_DOWNS_PER_GAME_COLUMN,
    )
    first_downs_rushing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIRST_DOWNS_RUSHING_COLUMN,
    )
    kickoff_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKOFF_RETURN_YARDS_COLUMN,
    )
    kickoffs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKOFFS_COLUMN,
    )
    kickoff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKOFF_YARDS_COLUMN,
    )
    long_field_goal_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_FIELD_GOAL_ATTEMPT_COLUMN,
    )
    long_field_goal_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_FIELD_GOAL_MADE_COLUMN,
    )
    long_kickoff: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_KICKOFF_COLUMN,
    )
    total_kicking_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_KICKING_POINTS_COLUMN,
    )
    touchback_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOUCHBACK_PERCENTAGE_COLUMN,
    )
    touchbacks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOUCHBACKS_COLUMN,
    )
    def_fumble_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEF_FUMBLE_RETURNS_COLUMN,
    )
    def_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEF_FUMBLE_RETURN_YARDS_COLUMN,
    )
    fumble_recoveries: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLE_RECOVERIES_COLUMN,
    )
    fumble_recovery_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLE_RECOVERY_YARDS_COLUMN,
    )
    kick_return_fair_catches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURN_FAIR_CATCHES_COLUMN,
    )
    kick_return_fair_catch_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN,
    )
    kick_return_fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURN_FUMBLES_COLUMN,
    )
    kick_return_fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURN_FUMBLES_LOST_COLUMN,
    )
    kick_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURNS_COLUMN,
    )
    kick_return_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURN_TOUCHDOWNS_COLUMN,
    )
    kick_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICK_RETURN_YARDS_COLUMN,
    )
    long_kick_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_KICK_RETURN_COLUMN,
    )
    long_punt_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_PUNT_RETURN_COLUMN,
    )
    misc_fumble_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MISC_FUMBLE_RETURNS_COLUMN,
    )
    misc_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MISC_FUMBLE_RETURN_YARDS_COLUMN,
    )
    opp_fumble_recoveries: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPP_FUMBLE_RECOVERIES_COLUMN,
    )
    opp_fumble_recovery_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPP_FUMBLE_RECOVERY_YARDS_COLUMN,
    )
    opp_special_team_fumble_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPP_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN,
    )
    opp_special_team_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OPP_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN,
    )
    punt_return_fair_catches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURN_FAIR_CATCHES_COLUMN,
    )
    punt_return_fair_catch_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN,
    )
    punt_return_fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURN_FUMBLES_COLUMN,
    )
    punt_return_fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURN_FUMBLES_LOST_COLUMN,
    )
    punt_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PUNT_RETURNS_COLUMN,
    )
    interception_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCEPTION_YARDS_COLUMN,
    )
    average_kickoff_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_KICKOFF_RETURN_YARDS_COLUMN,
    )
    average_kickoff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_KICKOFF_YARDS_COLUMN,
    )
    extra_point_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_POINT_ATTEMPTS_COLUMN,
    )
    extra_point_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_POINT_PERCENTAGE_COLUMN,
    )
    extra_points_blocked: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_POINTS_BLOCKED_COLUMN,
    )
    extra_points_blocked_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_POINTS_BLOCKED_PERCENTAGE_COLUMN,
    )
    extra_points_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EXTRA_POINTS_MADE_COLUMN,
    )
    fair_catches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FAIR_CATCHES_COLUMN,
    )
    fair_catch_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FAIR_CATCH_PERCENTAGE_COLUMN,
    )
    field_goal_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_COLUMN,
    )
    field_goal_attempts_1_19: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_1_19_COLUMN,
    )
    field_goal_attempts_20_29: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_20_29_COLUMN,
    )
    field_goal_attempts_30_39: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_30_39_COLUMN,
    )
    field_goal_attempts_40_49: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_40_49_COLUMN,
    )
    field_goal_attempts_50_59: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_50_59_COLUMN,
    )
    field_goal_attempts_60_99: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_60_99_COLUMN,
    )
    field_goal_attempts_50: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPTS_50_COLUMN,
    )
    field_goal_attempt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOAL_ATTEMPT_YARDS_COLUMN,
    )
    field_goals_blocked: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_BLOCKED_COLUMN,
    )
    field_goals_blocked_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_BLOCKED_PERCENTAGE_COLUMN,
    )
    field_goals_made_1_19: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_1_19_COLUMN,
    )
    field_goals_made_20_29: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_20_29_COLUMN,
    )
    field_goals_made_30_39: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_30_39_COLUMN,
    )
    field_goals_made_40_49: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_40_49_COLUMN,
    )
    field_goals_made_50_59: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_50_59_COLUMN,
    )
    field_goals_made_60_99: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_60_99_COLUMN,
    )
    field_goals_made_50: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_50_COLUMN,
    )
    field_goals_made_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MADE_YARDS_COLUMN,
    )
    field_goals_missed_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FIELD_GOALS_MISSED_YARDS_COLUMN,
    )
    kickoff_ob: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKOFF_OB_COLUMN,
    )
    kickoff_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKOFF_RETURNS_COLUMN,
    )
    kickoff_return_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKOFF_RETURN_TOUCHDOWNS_COLUMN,
    )
    two_point_rec_conversions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_REC_CONVERSIONS_COLUMN,
    )
    two_point_reception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_RECEPTION_COLUMN,
    )
    two_point_reception_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_RECEPTION_ATTEMPTS_COLUMN,
    )
    yards_per_reception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_RECEPTION_COLUMN,
    )
    assist_tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ASSIST_TACKLES_COLUMN,
    )
    average_interception_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_INTERCEPTION_YARDS_COLUMN,
    )
    average_sack_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_SACK_YARDS_COLUMN,
    )
    average_stuff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_STUFF_YARDS_COLUMN,
    )
    blocked_field_goal_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOCKED_FIELD_GOAL_TOUCHDOWNS_COLUMN,
    )
    blocked_punt_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOCKED_PUNT_TOUCHDOWNS_COLUMN,
    )
    defensive_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEFENSIVE_TOUCHDOWNS_COLUMN,
    )
    hurries: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_HURRIES_COLUMN,
    )
    kicks_blocked: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_KICKS_BLOCKED_COLUMN,
    )
    long_interception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_INTERCEPTION_COLUMN,
    )
    misc_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MISC_TOUCHDOWNS_COLUMN,
    )
    passes_batted_down: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSES_BATTED_DOWN_COLUMN,
    )
    passes_defended: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSES_DEFENDED_COLUMN,
    )
    qb_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_QB_HITS_COLUMN,
    )
    two_point_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_RETURNS_COLUMN,
    )
    sacks_assisted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACKS_ASSISTED_COLUMN,
    )
    sacks_unassisted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACKS_UNASSISTED_COLUMN,
    )
    sack_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACK_YARDS_COLUMN,
    )
    safeties: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SAFETIES_COLUMN,
    )
    solo_tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SOLO_TACKLES_COLUMN,
    )
    stuff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STUFF_YARDS_COLUMN,
    )
    tackles_for_loss: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TACKLES_FOR_LOSS_COLUMN,
    )
    tackles_yards_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TACKLES_YARDS_LOST_COLUMN,
    )
    yards_allowed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_ALLOWED_COLUMN,
    )
    points_allowed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POINTS_ALLOWED_COLUMN,
    )
    one_point_safeties_made: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ONE_POINT_SAFETIES_MADE_COLUMN,
    )
    missed_field_goal_return_td: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MISSED_FIELD_GOAL_RETURN_TD_COLUMN,
    )
    blocked_punt_ez_rec_td: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_BLOCKED_PUNT_EZ_REC_TD_COLUMN,
    )
    interception_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCEPTION_TOUCHDOWNS_COLUMN,
    )
    yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_GAME_COLUMN,
    )
    yards_per_pass_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_PASS_ATTEMPT_COLUMN,
    )
    net_yards_per_pass_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_YARDS_PER_PASS_ATTEMPT_COLUMN,
    )
    quarterback_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_QUARTERBACK_RATING_COLUMN,
    )
    espn_rb_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ESPN_RB_RATING_COLUMN,
    )
    long_rushing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_RUSHING_COLUMN,
    )
    rushing_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_ATTEMPTS_COLUMN,
    )
    rushing_big_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_BIG_PLAYS_COLUMN,
    )
    rushing_first_downs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_FIRST_DOWNS_COLUMN,
    )
    rushing_fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_FUMBLES_COLUMN,
    )
    rushing_fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_FUMBLES_LOST_COLUMN,
    )
    rushing_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_TOUCHDOWNS_COLUMN,
    )
    rushing_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_YARDS_COLUMN,
    )
    rushing_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RUSHING_YARDS_PER_GAME_COLUMN,
    )
    stuffs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STUFFS_COLUMN,
    )
    stuff_yards_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_STUFF_YARDS_LOST_COLUMN,
    )
    two_point_rush_conversions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_RUSH_CONVERSIONS_COLUMN,
    )
    two_point_rush: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_RUSH_COLUMN,
    )
    two_point_rush_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_RUSH_ATTEMPTS_COLUMN,
    )
    yards_per_rush_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_RUSH_ATTEMPT_COLUMN,
    )
    espn_wr_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ESPN_WR_RATING_COLUMN,
    )
    long_reception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_RECEPTION_COLUMN,
    )
    receiving_big_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_BIG_PLAYS_COLUMN,
    )
    receiving_first_downs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_FIRST_DOWNS_COLUMN,
    )
    receiving_fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_FUMBLES_COLUMN,
    )
    receiving_fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_FUMBLES_LOST_COLUMN,
    )
    receiving_targets: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_TARGETS_COLUMN,
    )
    receiving_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_TOUCHDOWNS_COLUMN,
    )
    receiving_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_YARDS_COLUMN,
    )
    receiving_yards_after_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_YARDS_AFTER_CATCH_COLUMN,
    )
    receiving_yards_at_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_YARDS_AT_CATCH_COLUMN,
    )
    receiving_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEIVING_YARDS_PER_GAME_COLUMN,
    )
    receptions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RECEPTIONS_COLUMN,
    )
    interception_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_INTERCEPTION_PERCENTAGE_COLUMN,
    )
    long_passing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_LONG_PASSING_COLUMN,
    )
    misc_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_MISC_YARDS_COLUMN,
    )
    net_passing_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_PASSING_YARDS_COLUMN,
    )
    net_passing_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_PASSING_YARDS_PER_GAME_COLUMN,
    )
    net_total_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_TOTAL_YARDS_COLUMN,
    )
    net_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_YARDS_PER_GAME_COLUMN,
    )
    passing_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_ATTEMPTS_COLUMN,
    )
    passing_big_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_BIG_PLAYS_COLUMN,
    )
    passing_first_downs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_FIRST_DOWNS_COLUMN,
    )
    passing_fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_FUMBLES_COLUMN,
    )
    passing_fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_FUMBLES_LOST_COLUMN,
    )
    passing_touchdown_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_TOUCHDOWN_PERCENTAGE_COLUMN,
    )
    passing_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_TOUCHDOWNS_COLUMN,
    )
    passing_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_YARDS_COLUMN,
    )
    passing_yards_after_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_YARDS_AFTER_CATCH_COLUMN,
    )
    passing_yards_at_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_YARDS_AT_CATCH_COLUMN,
    )
    passing_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PASSING_YARDS_PER_GAME_COLUMN,
    )
    qb_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_QB_RATING_COLUMN,
    )
    sacks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACKS_COLUMN,
    )
    sack_yards_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SACK_YARDS_LOST_COLUMN,
    )
    net_passing_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_NET_PASSING_ATTEMPTS_COLUMN,
    )
    total_offensive_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_OFFENSIVE_PLAYS_COLUMN,
    )
    total_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_POINTS_COLUMN,
    )
    total_points_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_POINTS_PER_GAME_COLUMN,
    )
    total_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_TOUCHDOWNS_COLUMN,
    )
    total_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_YARDS_COLUMN,
    )
    total_yards_from_scrimmage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_YARDS_FROM_SCRIMMAGE_COLUMN,
    )
    two_point_pass_convs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_PASS_CONVERSIONS_COLUMN,
    )
    two_point_pass: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_PASS_COLUMN,
    )
    two_point_pass_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TWO_POINT_PASS_ATTEMPTS_COLUMN,
    )
    yards_from_scrimmage_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_FROM_SCRIMMAGE_PER_GAME_COLUMN,
    )
    yards_per_completion: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YARDS_PER_COMPLETION_COLUMN,
    )
    fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLES_COLUMN,
    )
    fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLES_LOST_COLUMN,
    )
    fumbles_forced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLES_FORCED_COLUMN,
    )
    fumbles_recovered_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FUMBLES_RECOVERED_YARDS_COLUMN,
    )
    offensive_two_point_returns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OFFENSIVE_TWO_POINT_RETURNS_COLUMN,
    )
    offensive_fumbles_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_OFFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN,
    )
    defensive_fumbles_touchdowns: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_DEFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN,
    )
    average_gain: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_AVERAGE_GAIN_COLUMN,
    )
    completion_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_COMPLETION_PERCENTAGE_COLUMN,
    )
    completions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_COMPLETIONS_COLUMN,
    )
    espn_qb_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_ESPN_QB_RATING_COLUMN,
    )
    power_play_time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_TIME_ON_ICE_COLUMN,
    )
    short_handed_time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHORT_HANDED_TIME_ON_ICE_COLUMN,
    )
    even_strength_time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EVEN_STRENGTH_TIME_ON_ICE_COLUMN,
    )
    shifts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHIFTS_COLUMN,
    )
    shot_differential: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOT_DIFFERENTIAL_COLUMN,
    )
    goal_differential: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOAL_DIFFERENTIAL_COLUMN,
    )
    pim_differential: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PIM_DIFFERENTIAL_COLUMN,
    )
    rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_RATING_COLUMN,
    )
    ytd_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_YTD_GOALS_COLUMN,
    )
    shots_in_first_period: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_IN_FIRST_PERIOD_COLUMN,
    )
    shots_in_second_period: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_IN_SECOND_PERIOD_COLUMN,
    )
    shots_in_third_period: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_IN_THIRD_PERIOD_COLUMN,
    )
    shots_ot: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_OT_COLUMN,
    )
    shots_total: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_TOTAL_COLUMN,
    )
    shots_missed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_MISSED_COLUMN,
    )
    points_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POINTS_PER_GAME_COLUMN,
    )
    power_play_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_GOALS_COLUMN,
    )
    power_play_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_ASSISTS_COLUMN,
    )
    power_play_opportunities: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_OPPORTUNITIES_COLUMN,
    )
    power_play_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_PERCENTAGE_COLUMN,
    )
    short_handed_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHORT_HANDED_GOALS_COLUMN,
    )
    short_handed_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHORT_HANDED_ASSISTS_COLUMN,
    )
    shootout_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOTOUT_ATTEMPTS_COLUMN,
    )
    shootout_shot_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOTOUT_SHOT_PERCENTAGE_COLUMN,
    )
    empty_net_goals_for: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EMPTY_NET_GOALS_FOR_COLUMN,
    )
    shooting_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOTING_PERCENTAGE_COLUMN,
    )
    total_face_offs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_FACE_OFFS_COLUMN,
    )
    faceoffs_won: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FACEOFFS_WON_COLUMN,
    )
    faceoffs_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FACEOFFS_LOST_COLUMN,
    )
    faceoff_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FACEOFF_PERCENTAGE_COLUMN,
    )
    unassisted_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_UNASSISTED_GOALS_COLUMN,
    )
    giveaways: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GIVEAWAYS_COLUMN,
    )
    penalty_minutes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_MINUTES_COLUMN,
    )
    goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_GOALS_AGAINST_COLUMN,
    )
    shots_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOTS_AGAINST_COLUMN,
    )
    penalty_kill_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PENALTY_KILL_PERCENTAGE_COLUMN,
    )
    power_play_goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_GOALS_AGAINST_COLUMN,
    )
    short_handed_goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHORT_HANDED_GOALS_AGAINST_COLUMN,
    )
    shootout_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOTOUT_SAVES_COLUMN,
    )
    shootout_shots_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHOOTOUT_SHOTS_AGAINST_COLUMN,
    )
    times_short_handed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TIMES_SHORT_HANDED_COLUMN,
    )
    empty_net_goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EMPTY_NET_GOALS_AGAINST_COLUMN,
    )
    takeaways: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TAKEAWAYS_COLUMN,
    )
    even_strength_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_EVEN_STRENGTH_SAVES_COLUMN,
    )
    power_play_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_POWER_PLAY_SAVES_COLUMN,
    )
    short_handed_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SHORT_HANDED_SAVES_COLUMN,
    )
    time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TIME_ON_ICE_COLUMN,
    )
    total_giveaways: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_GIVEAWAYS_COLUMN,
    )
    total_takeaways: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_TOTAL_TAKEAWAYS_COLUMN,
    )
    fantasy_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_FANTASY_RATING_COLUMN,
    )
    second_chance_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_SECOND_CHANCE_POINTS_COLUMN,
    )
    plus_minus: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TEAM_PLUS_MINUS_COLUMN,
    )
    version: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
