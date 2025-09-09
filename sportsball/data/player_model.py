"""The prototype class for a player."""

# pylint: disable=duplicate-code,too-many-lines
from __future__ import annotations

import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from .address_model import VERSION as ADDRESS_VERSION
from .address_model import AddressModel
from .delimiter import DELIMITER
from .field_type import FFILL_KEY, TYPE_KEY, FieldType
from .owner_model import VERSION as OWNER_VERSION
from .owner_model import OwnerModel
from .sex import (FEMALE_GENDERS, GENDER_DETECTOR, MALE_GENDERS,
                  UNCERTAIN_GENDERS, Sex)
from .venue_model import VERSION as VENUE_VERSION
from .venue_model import VenueModel

PLAYER_KICKS_COLUMN: Literal["kicks"] = "kicks"
PLAYER_IDENTIFIER_COLUMN: Literal["identifier"] = "identifier"
PLAYER_FUMBLES_COLUMN: Literal["fumbles"] = "fumbles"
PLAYER_FUMBLES_LOST_COLUMN: Literal["fumbles_lost"] = "fumbles_lost"
FIELD_GOALS_COLUMN: Literal["field_goals"] = "field_goals"
FIELD_GOALS_ATTEMPTED_COLUMN: Literal["field_goals_attempted"] = "field_goals_attempted"
OFFENSIVE_REBOUNDS_COLUMN: Literal["offensive_rebounds"] = "offensive_rebounds"
PLAYER_ASSISTS_COLUMN: Literal["assists"] = "assists"
TURNOVERS_COLUMN: Literal["turnovers"] = "turnovers"
PLAYER_MARKS_COLUMN: Literal["marks"] = "marks"
PLAYER_HANDBALLS_COLUMN: Literal["handballs"] = "handballs"
PLAYER_DISPOSALS_COLUMN: Literal["disposals"] = "disposals"
PLAYER_GOALS_COLUMN: Literal["goals"] = "goals"
PLAYER_BEHINDS_COLUMN: Literal["behinds"] = "behinds"
PLAYER_HIT_OUTS_COLUMN: Literal["hit_outs"] = "hit_outs"
PLAYER_TACKLES_COLUMN: Literal["tackles"] = "tackles"
PLAYER_REBOUNDS_COLUMN: Literal["rebounds"] = "rebounds"
PLAYER_INSIDES_COLUMN: Literal["insides"] = "insides"
PLAYER_CLEARANCES_COLUMN: Literal["clearances"] = "clearances"
PLAYER_CLANGERS_COLUMN: Literal["clangers"] = "clangers"
PLAYER_FREE_KICKS_FOR_COLUMN: Literal["free_kicks_for"] = "free_kicks_for"
PLAYER_FREE_KICKS_AGAINST_COLUMN: Literal["free_kicks_against"] = "free_kicks_against"
PLAYER_BROWNLOW_VOTES_COLUMN: Literal["brownlow_votes"] = "brownlow_votes"
PLAYER_CONTESTED_POSSESSIONS_COLUMN: Literal["contested_possessions"] = (
    "contested_possessions"
)
PLAYER_UNCONTESTED_POSSESSIONS_COLUMN: Literal["uncontested_possessions"] = (
    "uncontested_possessions"
)
PLAYER_CONTESTED_MARKS_COLUMN: Literal["contested_marks"] = "contested_marks"
PLAYER_MARKS_INSIDE_COLUMN: Literal["marks_inside"] = "marks_inside"
PLAYER_ONE_PERCENTERS_COLUMN: Literal["one_percenters"] = "one_percenters"
PLAYER_BOUNCES_COLUMN: Literal["bounces"] = "bounces"
PLAYER_GOAL_ASSISTS_COLUMN: Literal["goal_assists"] = "goal_assists"
PLAYER_PERCENTAGE_PLAYED_COLUMN: Literal["percentage_played"] = "percentage_played"
PLAYER_NAME_COLUMN: Literal["name"] = "name"
PLAYER_BIRTH_DATE_COLUMN: Literal["birth_date"] = "birth_date"
PLAYER_SPECIES_COLUMN: Literal["species"] = "species"
PLAYER_HANDICAP_WEIGHT_COLUMN: Literal["handicap_weight"] = "handicap_weight"
PLAYER_FATHER_COLUMN: Literal["father"] = "father"
PLAYER_SEX_COLUMN: Literal["sex"] = "sex"
PLAYER_AGE_COLUMN: Literal["age"] = "age"
PLAYER_STARTING_POSITION_COLUMN: Literal["starting_position"] = "starting_position"
PLAYER_WEIGHT_COLUMN: Literal["weight"] = "weight"
PLAYER_BIRTH_ADDRESS_COLUMN: Literal["birth_address"] = "birth_address"
PLAYER_OWNER_COLUMN: Literal["owner"] = "owner"
PLAYER_SECONDS_PLAYED_COLUMN: Literal["seconds_played"] = "seconds_played"
PLAYER_FIELD_GOALS_PERCENTAGE_COLUMN: Literal["field_goals_percentage"] = (
    "field_goals_percentage"
)
PLAYER_THREE_POINT_FIELD_GOALS_COLUMN: Literal["three_point_field_goals"] = (
    "three_point_field_goals"
)
PLAYER_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "three_point_field_goals_attempted"
] = "three_point_field_goals_attempted"
PLAYER_THREE_POINT_FIELD_GOALS_PERCENTAGE_COLUMN: Literal[
    "three_point_field_goals_percentage"
] = "three_point_field_goals_percentage"
PLAYER_FREE_THROWS_COLUMN: Literal["free_throws"] = "free_throws"
PLAYER_FREE_THROWS_ATTEMPTED_COLUMN: Literal["free_throws_attempted"] = (
    "free_throws_attempted"
)
PLAYER_FREE_THROWS_PERCENTAGE_COLUMN: Literal["free_throws_percentage"] = (
    "free_throws_percentage"
)
PLAYER_DEFENSIVE_REBOUNDS_COLUMN: Literal["defensive_rebounds"] = "defensive_rebounds"
PLAYER_TOTAL_REBOUNDS_COLUMN: Literal["total_rebounds"] = "total_rebounds"
PLAYER_STEALS_COLUMN: Literal["steals"] = "steals"
PLAYER_BLOCKS_COLUMN: Literal["blocks"] = "blocks"
PLAYER_PERSONAL_FOULS_COLUMN: Literal["personal_fouls"] = "personal_fouls"
PLAYER_POINTS_COLUMN: Literal["points"] = "points"
PLAYER_GAME_SCORE_COLUMN: Literal["game_score"] = "game_score"
PLAYER_POINT_DIFFERENTIAL_COLUMN: Literal["point_differential"] = "point_differential"
PLAYER_HEIGHT_COLUMN: Literal["height"] = "height"
PLAYER_COLLEGES_COLUMN: Literal["colleges"] = "colleges"
PLAYER_HEADSHOT_COLUMN: Literal["headshot"] = "headshot"
PLAYER_FORCED_FUMBLES_COLUMN: Literal["forced_fumbles"] = "forced_fumbles"
PLAYER_FUMBLES_RECOVERED_COLUMN: Literal["fumbles_recovered"] = "fumbles_recovered"
PLAYER_FUMBLES_RECOVERED_YARDS_COLUMN: Literal["fumbles_recovered_yards"] = (
    "fumbles_recovered_yards"
)
PLAYER_FUMBLES_TOUCHDOWNS_COLUMN: Literal["fumbles_touchdowns"] = "fumbles_touchdowns"
PLAYER_OFFENSIVE_TWO_POINT_RETURNS_COLUMN: Literal["offensive_two_point_returns"] = (
    "offensive_two_point_returns"
)
PLAYER_OFFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN: Literal["offensive_fumbles_touchdowns"] = (
    "offensive_fumbles_touchdowns"
)
PLAYER_DEFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN: Literal["defensive_fumbles_touchdowns"] = (
    "defensive_fumbles_touchdowns"
)
PLAYER_AVERAGE_GAIN_COLUMN: Literal["average_gain"] = "average_gain"
PLAYER_COMPLETION_PERCENTAGE_COLUMN: Literal["completion_percentage"] = (
    "completion_percentage"
)
PLAYER_COMPLETIONS_COLUMN: Literal["completions"] = "completions"
PLAYER_ESPN_QUARTERBACK_RATING_COLUMN: Literal["espn_quarterback_rating"] = (
    "espn_quarterback_rating"
)
PLAYER_INTERCEPTION_PERCENTAGE_COLUMN: Literal["interception_percentage"] = (
    "interception_percentage"
)
PLAYER_INTERCEPTIONS_COLUMN: Literal["interceptions"] = "interceptions"
PLAYER_LONG_PASSING_COLUMN: Literal["long_passing"] = "long_passing"
PLAYER_MISC_YARDS_COLUMN: Literal["misc_yards"] = "misc_yards"
PLAYER_NET_PASSING_YARDS_COLUMN: Literal["net_passing_yards"] = "net_passing_yards"
PLAYER_NET_TOTAL_YARDS_COLUMN: Literal["net_total_yards"] = "net_total_yards"
PLAYER_PASSING_ATTEMPTS_COLUMN: Literal["passing_attempts"] = "passing_attempts"
PLAYER_PASSING_BIG_PLAYS_COLUMN: Literal["passing_big_plays"] = "passing_big_plays"
PLAYER_PASSING_FIRST_DOWNS_COLUMN: Literal["passing_first_downs"] = (
    "passing_first_downs"
)
PLAYER_PASSING_FUMBLES_COLUMN: Literal["passing_fumbles"] = "passing_fumbles"
PLAYER_PASSING_FUMBLES_LOST_COLUMN: Literal["passing_fumbles_lost"] = (
    "passing_fumbles_lost"
)
PLAYER_PASSING_TOUCHDOWN_PERCENTAGE_COLUMN: Literal["passing_touchdown_percentage"] = (
    "passing_touchdown_percentage"
)
PLAYER_PASSING_TOUCHDOWNS_COLUMN: Literal["passing_touchdowns"] = "passing_touchdowns"
PLAYER_PASSING_YARDS_COLUMN: Literal["passing_yards"] = "passing_yards"
PLAYER_PASSING_YARDS_AFTER_CATCH_COLUMN: Literal["passing_yards_after_catch"] = (
    "passing_yards_after_catch"
)
PLAYER_PASSING_YARDS_AT_CATCH_COLUMN: Literal["passing_yards_at_catch"] = (
    "passing_yards_at_catch"
)
PLAYER_QUARTERBACK_RATING_COLUMN: Literal["quarterback_rating"] = "quarterback_rating"
PLAYER_SACKS_COLUMN: Literal["sacks"] = "sacks"
PLAYER_SACKS_YARDS_LOST_COLUMN: Literal["sacks_yards_lost"] = "sacks_yards_lost"
PLAYER_NET_PASSING_ATTEMPTS_COLUMN: Literal["net_passing_attempts"] = (
    "net_passing_attempts"
)
PLAYER_TOTAL_OFFENSIVE_PLAYS_COLUMN: Literal["total_offensive_plays"] = (
    "total_offensive_plays"
)
PLAYER_TOTAL_POINTS_COLUMN: Literal["total_points"] = "total_points"
PLAYER_TOTAL_TOUCHDOWNS_COLUMN: Literal["total_touchdowns"] = "total_touchdowns"
PLAYER_TOTAL_YARDS_COLUMN: Literal["total_yards"] = "total_yards"
PLAYER_TOTAL_YARDS_FROM_SCRIMMAGE_COLUMN: Literal["total_yards_from_scrimmage"] = (
    "total_yards_from_scrimmage"
)
PLAYER_TWO_POINT_PASS_COLUMN: Literal["two_point_pass"] = "two_point_pass"
PLAYER_TWO_POINT_PASS_ATTEMPT_COLUMN: Literal["two_point_pass_attempt"] = (
    "two_point_pass_attempt"
)
PLAYER_YARDS_PER_COMPLETION_COLUMN: Literal["yards_per_completion"] = (
    "yards_per_completion"
)
PLAYER_YARDS_PER_PASS_ATTEMPT_COLUMN: Literal["yards_per_pass_attempt"] = (
    "yards_per_pass_attempt"
)
PLAYER_NET_YARDS_PER_PASS_ATTEMPT_COLUMN: Literal["net_yards_per_pass_attempt"] = (
    "net_yards_per_pass_attempt"
)
PLAYER_ESPN_RUNNINGBACK_RATING_COLUMN: Literal["espn_runningback"] = "espn_runningback"
PLAYER_LONG_RUSHING_COLUMN: Literal["long_rushing"] = "long_rushing"
PLAYER_RUSHING_ATTEMPTS_COLUMN: Literal["rushing_attempts"] = "rushing_attempts"
PLAYER_RUSHING_BIG_PLAYS_COLUMN: Literal["rushing_big_plays"] = "rushing_big_plays"
PLAYER_RUSHING_FIRST_DOWNS_COLUMN: Literal["rushing_first_downs"] = (
    "rushing_first_downs"
)
PLAYER_RUSHING_FUMBLES_COLUMN: Literal["rushing_fumbles"] = "rushing_fumbles"
PLAYER_RUSHING_FUMBLES_LOST_COLUMN: Literal["rushing_fumbles_lost"] = (
    "rushing_fumbles_lost"
)
PLAYER_RUSHING_TOUCHDOWNS_COLUMN: Literal["rushing_touchdowns"] = "rushing_touchdowns"
PLAYER_RUSHING_YARDS_COLUMN: Literal["rushing_yards"] = "rushing_yards"
PLAYER_STUFFS_COLUMN: Literal["stuffs"] = "stuffs"
PLAYER_STUFF_YARDS_LOST: Literal["stuff_yards_lost"] = "stuff_yards_lost"
PLAYER_TWO_POINT_RUSH_COLUMN: Literal["two_point_rush"] = "two_point_rush"
PLAYER_TWO_POINT_RUSH_ATTEMPTS_COLUMN: Literal["two_point_rush_attempts"] = (
    "two_point_rush_attempts"
)
PLAYER_YARDS_PER_RUSH_ATTEMPT_COLUMN: Literal["yards_per_rush_attempt"] = (
    "yards_per_rush_attempt"
)
PLAYER_ESPN_WIDERECEIVER_COLUMN: Literal["espn_widereceiver"] = "espn_widereceiver"
PLAYER_LONG_RECEPTION_COLUMN: Literal["long_reception"] = "long_reception"
PLAYER_RECEIVING_BIG_PLAYS_COLUMN: Literal["receiving_big_plays"] = (
    "receiving_big_plays"
)
PLAYER_RECEIVING_FIRST_DOWNS_COLUMN: Literal["receiving_first_downs"] = (
    "receiving_first_downs"
)
PLAYER_RECEIVING_FUMBLES_COLUMN: Literal["receiving_fumbles"] = "receiving_fumbles"
PLAYER_RECEIVING_FUMBLES_LOST_COLUMN: Literal["receiving_fumbles_lost"] = (
    "receiving_fumbles_lost"
)
PLAYER_RECEIVING_TARGETS_COLUMN: Literal["receiving_targets"] = "receiving_targets"
PLAYER_RECEIVING_TOUCHDOWNS_COLUMN: Literal["receiving_touchdowns"] = (
    "receiving_touchdowns"
)
PLAYER_RECEIVING_YARDS_COLUMN: Literal["receiving_yards"] = "receiving_yards"
PLAYER_RECEIVING_YARDS_AFTER_CATCH_COLUMN: Literal["receiving_yards_after_catch"] = (
    "receiving_yards_after_catch"
)
PLAYER_RECEIVING_YARDS_AT_CATCH_COLUMN: Literal["receiving_yards_at_catch"] = (
    "receiving_yards_at_catch"
)
PLAYER_RECEPTIONS_COLUMN: Literal["receptions"] = "receptions"
PLAYER_TWO_POINT_RECEPTIONS_COLUMN: Literal["two_point_receptions"] = (
    "two_point_receptions"
)
PLAYER_TWO_POINT_RECEPTION_ATTEMPTS_COLUMN: Literal["two_point_reception_attempts"] = (
    "two_point_reception_attempts"
)
PLAYER_YARDS_PER_RECEPTION_COLUMN: Literal["yards_per_reception"] = (
    "yards_per_reception"
)
PLAYER_ASSIST_TACKLES_COLUMN: Literal["assist_tackles"] = "assist_tackles"
PLAYER_AVERAGE_INTERCEPTION_YARDS_COLUMN: Literal["average_interception_yards"] = (
    "average_interception_yards"
)
PLAYER_AVERAGE_SACK_YARDS_COLUMN: Literal["average_sack_yards"] = "average_sack_yards"
PLAYER_AVERAGE_STUFF_YARDS_COLUMN: Literal["average_stuff_yards"] = (
    "average_stuff_yards"
)
PLAYER_BLOCKED_FIELD_GOAL_TOUCHDOWNS_COLUMN: Literal[
    "blocked_field_goal_touchdowns"
] = "blocked_field_goal_touchdowns"
PLAYER_BLOCKED_PUNT_TOUCHDOWNS_COLUMN: Literal["blocked_punt_touchdowns"] = (
    "blocked_punt_touchdowns"
)
PLAYER_DEFENSIVE_TOUCHDOWNS_COLUMN: Literal["defensive_touchdowns"] = (
    "defensive_touchdowns"
)
PLAYER_HURRIES_COLUMN: Literal["hurries"] = "hurries"
PLAYER_KICKS_BLOCKED_COLUMN: Literal["kicks_blocked"] = "kicks_blocked"
PLAYER_LONG_INTERCEPTION_COLUMN: Literal["long_interception"] = "long_interception"
PLAYER_MISC_TOUCHDOWNS_COLUMN: Literal["misc_touchdowns"] = "misc_touchdowns"
PLAYER_PASSES_BATTED_DOWN_COLUMN: Literal["passes_batted_down"] = "passes_batted_down"
PLAYER_PASSES_DEFENDED_COLUMN: Literal["passes_defended"] = "passes_defended"
PLAYER_QUARTERBACK_HITS_COLUMN: Literal["quarterback_hits"] = "quarterback_hits"
PLAYER_SACKS_ASSISTED_COLUMN: Literal["sacks_assisted"] = "sacks_assisted"
PLAYER_SACKS_UNASSISTED_COLUMN: Literal["sacks_unassisted"] = "sacks_unassisted"
PLAYER_SACKS_YARDS_COLUMN: Literal["sacks_yards"] = "sacks_yards"
PLAYER_SAFETIES_COLUMN: Literal["safeties"] = "safeties"
PLAYER_SOLO_TACKLES_COLUMN: Literal["solo_tackles"] = "solo_tackles"
PLAYER_STUFF_YARDS_COLUMN: Literal["stuff_yards"] = "stuff_yards"
PLAYER_TACKLES_FOR_LOSS_COLUMN: Literal["tackles_for_loss"] = "tackles_for_loss"
PLAYER_TACKLES_YARDS_LOST_COLUMN: Literal["tackles_yards_lost"] = "tackles_yards_lost"
PLAYER_YARDS_ALLOWED_COLUMN: Literal["yards_allowed"] = "yards_allowed"
PLAYER_POINTS_ALLOWED_COLUMN: Literal["points_allowed"] = "points_allowed"
PLAYER_ONE_POINT_SAFETIES_MADE_COLUMN: Literal["one_point_safeties_made"] = (
    "one_point_safeties_made"
)
PLAYER_MISSED_FIELD_GOAL_RETURN_TD_COLUMN: Literal["missed_field_goal_return_td"] = (
    "missed_field_goal_return_td"
)
PLAYER_BLOCKED_PUNT_EZ_REC_TD_COLUMN: Literal["blocked_punt_ez_rec_td"] = (
    "blocked_punt_ez_rec_td"
)
PLAYER_INTERCEPTION_TOUCHDOWNS_COLUMN: Literal["interception_touchdowns"] = (
    "interception_touchdowns"
)
PLAYER_INTERCEPTION_YARDS_COLUMN: Literal["interception_yards"] = "interception_yards"
PLAYER_AVERAGE_KICKOFF_RETURN_YARDS_COLUMN: Literal["average_kickoff_return_yards"] = (
    "average_kickoff_return_yards"
)
PLAYER_AVERAGE_KICKOFF_YARDS_COLUMN: Literal["average_kickoff_yards"] = (
    "average_kickoff_yards"
)
PLAYER_EXTRA_POINT_ATTEMPTS_COLUMN: Literal["extra_point_attempts"] = (
    "extra_point_attempts"
)
PLAYER_EXTRA_POINT_PERCENTAGE_COLUMN: Literal["extra_point_percentage"] = (
    "extra_point_percentage"
)
PLAYER_EXTRA_POINT_BLOCKED_COLUMN: Literal["extra_point_blocked"] = (
    "extra_point_blocked"
)
PLAYER_EXTRA_POINTS_BLOCKED_PERCENTAGE_COLUMN: Literal[
    "extra_points_blocked_percentage"
] = "extra_points_blocked_percentage"
PLAYER_EXTRA_POINTS_MADE_COLUMN: Literal["extra_points_made"] = "extra_points_made"
PLAYER_FAIR_CATCHES_COLUMN: Literal["fair_catches"] = "fair_catches"
PLAYER_FAIR_CATCH_PERCENTAGE_COLUMN: Literal["fair_catch_percentage"] = (
    "fair_catch_percentage"
)
PLAYER_FIELD_GOAL_ATTEMPTS_MAX_19_YARDS_COLUMN: Literal[
    "field_goal_attempts_max_19_yards"
] = "field_goal_attempts_max_19_yards"
PLAYER_FIELD_GOAL_ATTEMPTS_MAX_29_YARDS_COLUMN: Literal[
    "field_goal_attempts_max_29_yards"
] = "field_goal_attempts_max_29_yards"
PLAYER_FIELD_GOAL_ATTEMPTS_MAX_39_YARDS_COLUMN: Literal[
    "field_goal_attempts_max_39_yards"
] = "field_goal_attempts_max_39_yards"
PLAYER_FIELD_GOAL_ATTEMPTS_MAX_49_YARDS_COLUMN: Literal[
    "field_goal_attempts_max_49_yards"
] = "field_goal_attempts_max_49_yards"
PLAYER_FIELD_GOAL_ATTEMPTS_MAX_59_YARDS_COLUMN: Literal[
    "field_goal_attempts_max_59_yards"
] = "field_goal_attempts_max_59_yards"
PLAYER_FIELD_GOAL_ATTEMPTS_MAX_99_YARDS_COLUMN: Literal[
    "field_goal_attempts_max_99_yards"
] = "field_goal_attempts_max_99_yards"
PLAYER_FIELD_GOAL_ATTEMPTS_ABOVE_50_YARDS_COLUMN: Literal[
    "field_goal_attempts_above_50_yards"
] = "field_goal_attempts_above_50_yards"
PLAYER_FIELD_GOAL_ATTEMPT_YARDS_COLUMN: Literal["field_goal_attempt_yards"] = (
    "field_goal_attempt_yards"
)
PLAYER_FIELD_GOALS_BLOCKED_COLUMN: Literal["field_goals_blocked"] = (
    "field_goals_blocked"
)
PLAYER_FIELD_GOALS_BLOCKED_PERCENTAGE_COLUMN: Literal[
    "field_goals_blocked_percentage"
] = "field_goals_blocked_percentage"
PLAYER_FIELD_GOALS_MADE_COLUMN: Literal["field_goals_made"] = "field_goals_made"
PLAYER_FIELD_GOALS_MADE_MAX_19_YARDS_COLUMN: Literal[
    "field_goals_made_max_19_yards"
] = "field_goals_made_max_19_yards"
PLAYER_FIELD_GOALS_MADE_MAX_29_YARDS_COLUMN: Literal[
    "field_goals_made_max_29_yards"
] = "field_goals_made_max_29_yards"
PLAYER_FIELD_GOALS_MADE_MAX_39_YARDS_COLUMN: Literal[
    "field_goals_made_max_39_yards"
] = "field_goals_made_max_39_yards"
PLAYER_FIELD_GOALS_MADE_MAX_49_YARDS_COLUMN: Literal[
    "field_goals_made_max_49_yards"
] = "field_goals_made_max_49_yards"
PLAYER_FIELD_GOALS_MADE_MAX_59_YARDS_COLUMN: Literal[
    "field_goals_made_max_59_yards"
] = "field_goals_made_max_59_yards"
PLAYER_FIELD_GOALS_MADE_MAX_99_YARDS_COLUMN: Literal[
    "field_goals_made_max_99_yards"
] = "field_goals_made_max_99_yards"
PLAYER_FIELD_GOALS_MADE_ABOVE_50_YARDS_COLUMN: Literal[
    "field_goals_made_above_50_yards"
] = "field_goals_made_above_50_yards"
PLAYER_FIELD_GOALS_MADE_YARDS_COLUMN: Literal["field_goals_made_yards"] = (
    "field_goals_made_yards"
)
PLAYER_FIELD_GOALS_MISSED_YARDS_COLUMN: Literal["field_goals_missed_yards"] = (
    "field_goals_missed_yards"
)
PLAYER_KICKOFF_OUT_OF_BOUNDS_COLUMN: Literal["kickoff_out_of_bounds"] = (
    "kickoff_out_of_bounds"
)
PLAYER_KICKOFF_RETURNS_COLUMN: Literal["kickoff_returns"] = "kickoff_returns"
PLAYER_KICKOFF_RETURNS_TOUCHDOWNS_COLUMN: Literal["kickoff_returns_touchdowns"] = (
    "kickoff_returns_touchdowns"
)
PLAYER_KICKOFF_RETURN_YARDS_COLUMN: Literal["kickoff_return_yards"] = (
    "kickoff_return_yards"
)
PLAYER_KICKOFFS_COLUMN: Literal["kickoffs"] = "kickoffs"
PLAYER_KICKOFF_YARDS_COLUMN: Literal["kickoff_yards"] = "kickoff_yards"
PLAYER_LONG_FIELD_GOAL_ATTEMPT_COLUMN: Literal["long_field_goal_attempt"] = (
    "long_field_goal_attempt"
)
PLAYER_LONG_FIELD_GOAL_MADE_COLUMN: Literal["long_field_goal_made"] = (
    "long_field_goal_made"
)
PLAYER_LONG_KICKOFF_COLUMN: Literal["long_kickoff"] = "long_kickoff"
PLAYER_TOTAL_KICKING_POINTS_COLUMN: Literal["total_kicking_points"] = (
    "total_kicking_points"
)
PLAYER_TOUCHBACK_PERCENTAGE_COLUMN: Literal["touchback_percentage"] = (
    "touchback_percentage"
)
PLAYER_TOUCHBACKS_COLUMN: Literal["touchbacks"] = "touchbacks"
PLAYER_DEFENSIVE_FUMBLE_RETURNS_COLUMN: Literal["defensive_fumble_returns"] = (
    "defensive_fumble_returns"
)
PLAYER_DEFENSIVE_FUMBLE_RETURN_YARDS_COLUMN: Literal[
    "defensive_fumble_return_yards"
] = "defensive_fumble_return_yards"
PLAYER_FUMBLE_RECOVERIES_COLUMN: Literal["fumble_recoveries"] = "fumble_recoveries"
PLAYER_FUMBLE_RECOVERY_YARDS_COLUMN: Literal["fumble_recovery_yards"] = (
    "fumble_recovery_yards"
)
PLAYER_KICK_RETURN_FAIR_CATCHES_COLUMN: Literal["kick_return_fair_catches"] = (
    "kick_return_fair_catches"
)
PLAYER_KICK_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN: Literal[
    "kick_return_fair_catch_percentage"
] = "kick_return_fair_catch_percentage"
PLAYER_KICK_RETURN_FUMBLES_COLUMN: Literal["kick_return_fumbles"] = (
    "kick_return_fumbles"
)
PLAYER_KICK_RETURN_FUMBLES_LOST_COLUMN: Literal["kick_return_fumbles_lost"] = (
    "kick_return_fumbles_lost"
)
PLAYER_KICK_RETURNS_COLUMN: Literal["kick_returns"] = "kick_returns"
PLAYER_KICK_RETURN_TOUCHDOWNS_COLUMN: Literal["kick_return_touchdowns"] = (
    "kick_return_touchdowns"
)
PLAYER_KICK_RETURN_YARDS_COLUMN: Literal["kick_return_yards"] = "kick_return_yards"
PLAYER_LONG_KICK_RETURN_COLUMN: Literal["long_kick_return"] = "long_kick_return"
PLAYER_LONG_PUNT_RETURN_COLUMN: Literal["long_punt_return"] = "long_punt_return"
PLAYER_MISC_FUMBLE_RETURNS_COLUMN: Literal["misc_fumble_returns"] = (
    "misc_fumble_returns"
)
PLAYER_MISC_FUMBLE_RETURN_YARDS_COLUMN: Literal["misc_fumble_return_yards"] = (
    "misc_fumble_return_yards"
)
PLAYER_OPPOSITION_FUMBLE_RECOVERIES_COLUMN: Literal["opposition_fumble_recoveries"] = (
    "opposition_fumble_recoveries"
)
PLAYER_OPPOSITION_FUMBLE_RECOVERY_YARDS_COLUMN: Literal[
    "opposition_fumble_recovery_yards"
] = "opposition_fumble_recovery_yards"
PLAYER_OPPOSITION_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN: Literal[
    "opposition_special_team_fumble_returns"
] = "opposition_special_team_fumble_returns"
PLAYER_OPPOSITION_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN: Literal[
    "opposition_special_team_fumble_return_yards"
] = "opposition_special_team_fumble_return_yards"
PLAYER_PUNT_RETURN_FAIR_CATCHES_COLUMN: Literal["punt_return_fair_catches"] = (
    "punt_return_fair_catches"
)
PLAYER_PUNT_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN: Literal[
    "punt_return_fair_catch_percentage"
] = "punt_return_fair_catch_percentage"
PLAYER_PUNT_RETURN_FUMBLES_COLUMN: Literal["punt_return_fumbles"] = (
    "punt_return_fumbles"
)
PLAYER_PUNT_RETURN_FUMBLES_LOST_COLUMN: Literal["punt_return_fumbles_lost"] = (
    "punt_return_fumbles_lost"
)
PLAYER_PUNT_RETURNS_COLUMN: Literal["punt_returns"] = "punt_returns"
PLAYER_PUNT_RETURNS_STARTED_INSIDE_THE_10_COLUMN: Literal[
    "punt_returns_started_inside_the_10"
] = "punt_returns_started_inside_the_10"
PLAYER_PUNT_RETURNS_STARTED_INSIDE_THE_20_COLUMN: Literal[
    "punt_returns_started_inside_the_20"
] = "punt_returns_started_inside_the_20"
PLAYER_PUNT_RETURN_TOUCHDOWNS_COLUMN: Literal["punt_return_touchdowns"] = (
    "punt_return_touchdowns"
)
PLAYER_PUNT_RETURN_YARDS_COLUMN: Literal["punt_return_yards"] = "punt_return_yards"
PLAYER_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN: Literal["special_team_fumble_returns"] = (
    "special_team_fumble_returns"
)
PLAYER_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN: Literal[
    "special_team_fumble_return_yards"
] = "special_team_fumble_return_yards"
PLAYER_YARDS_PER_KICK_RETURN_COLUMN: Literal["yards_per_kick_return"] = (
    "yards_per_kick_return"
)
PLAYER_YARDS_PER_PUNT_RETURN_COLUMN: Literal["yards_per_punt_return"] = (
    "yards_per_punt_return"
)
PLAYER_YARDS_PER_RETURN_COLUMN: Literal["yards_per_return"] = "yards_per_return"
PLAYER_AVERAGE_PUNT_RETURN_YARDS_COLUMN: Literal["average_punt_return_yards"] = (
    "average_punt_return_yards"
)
PLAYER_GROSS_AVERAGE_PUNT_YARDS_COLUMN: Literal["gross_average_punt_yards"] = (
    "gross_average_punt_yards"
)
PLAYER_LONG_PUNT_COLUMN: Literal["long_punt"] = "long_punt"
PLAYER_NET_AVERAGE_PUNT_YARDS_COLUMN: Literal["net_average_punt_yards"] = (
    "net_average_punt_yards"
)
PLAYER_PUNTS_COLUMN: Literal["punts"] = "punts"
PLAYER_PUNTS_BLOCKED_COLUMN: Literal["punts_blocked"] = "punts_blocked"
PLAYER_PUNTS_BLOCKED_PERCENTAGE_COLUMN: Literal["punts_blocked_percentage"] = (
    "punts_blocked_percentage"
)
PLAYER_PUNTS_INSIDE_10_COLUMN: Literal["punts_inside_10"] = "punts_inside_10"
PLAYER_PUNTS_INSIDE_10_PERCENTAGE_COLUMN: Literal["punts_inside_10_percentage"] = (
    "punts_inside_10_percentage"
)
PLAYER_PUNTS_INSIDE_20_COLUMN: Literal["punts_inside_20"] = "punts_inside_20"
PLAYER_PUNTS_INSIDE_20_PERCENTAGE_COLUMN: Literal["punts_inside_20_percentage"] = (
    "punts_inside_20_percentage"
)
PLAYER_PUNTS_OVER_50_COLUMN: Literal["punts_over_50"] = "punts_over_50"
PLAYER_PUNT_YARDS_COLUMN: Literal["punt_yards"] = "punt_yards"
PLAYER_DEFENSIVE_POINTS_COLUMN: Literal["defensive_points"] = "defensive_points"
PLAYER_MISC_POINTS_COLUMN: Literal["misc_points"] = "misc_points"
PLAYER_RETURN_TOUCHDOWNS_COLUMN: Literal["return_touchdowns"] = "return_touchdowns"
PLAYER_TOTAL_TWO_POINT_CONVERSIONS_COLUMN: Literal["total_two_point_conversions"] = (
    "total_two_point_conversions"
)
PLAYER_PASSING_TOUCHDOWNS_9_YARDS_COLUMN: Literal["passing_touchdowns_9_yards"] = (
    "passing_touchdowns_9_yards"
)
PLAYER_PASSING_TOUCHDOWNS_19_YARDS_COLUMN: Literal["passing_touchdowns_19_yards"] = (
    "passing_touchdowns_19_yards"
)
PLAYER_PASSING_TOUCHDOWNS_29_YARDS_COLUMN: Literal["passing_touchdowns_29_yards"] = (
    "passing_touchdowns_29_yards"
)
PLAYER_PASSING_TOUCHDOWNS_39_YARDS_COLUMN: Literal["passing_touchdowns_39_yards"] = (
    "passing_touchdowns_39_yards"
)
PLAYER_PASSING_TOUCHDOWNS_49_YARDS_COLUMN: Literal["passing_touchdowns_49_yards"] = (
    "passing_touchdowns_49_yards"
)
PLAYER_PASSING_TOUCHDOWNS_ABOVE_50_YARDS_COLUMN: Literal[
    "passing_touchdowns_above_50_yards"
] = "passing_touchdowns_above_50_yards"
PLAYER_RECEIVING_TOUCHDOWNS_9_YARDS_COLUMN: Literal["receiving_touchdowns_9_yards"] = (
    "receiving_touchdowns_9_yards"
)
PLAYER_RECEIVING_TOUCHDOWNS_19_YARDS_COLUMN: Literal[
    "receiving_touchdowns_19_yards"
] = "receiving_touchdowns_19_yards"
PLAYER_RECEIVING_TOUCHDOWNS_29_YARDS_COLUMN: Literal[
    "receiving_touchdowns_29_yards"
] = "receiving_touchdowns_29_yards"
PLAYER_RECEIVING_TOUCHDOWNS_39_YARDS_COLUMN: Literal[
    "receiving_touchdowns_39_yards"
] = "receiving_touchdowns_39_yards"
PLAYER_RECEIVING_TOUCHDOWNS_49_YARDS_COLUMN: Literal[
    "receiving_touchdowns_49_yards"
] = "receiving_touchdowns_49_yards"
PLAYER_RECEIVING_TOUCHDOWNS_ABOVE_50_YARDS_COLUMN: Literal[
    "receiving_touchdowns_above_50_yards"
] = "receiving_touchdowns_above_50_yards"
PLAYER_RUSHING_TOUCHDOWNS_9_YARDS_COLUMN: Literal["rushing_touchdowns_9_yards"] = (
    "rushing_touchdowns_9_yards"
)
PLAYER_RUSHING_TOUCHDOWNS_19_YARDS_COLUMN: Literal["rushing_touchdowns_19_yards"] = (
    "rushing_touchdowns_19_yards"
)
PLAYER_RUSHING_TOUCHDOWNS_29_YARDS_COLUMN: Literal["rushing_touchdowns_29_yards"] = (
    "rushing_touchdowns_29_yards"
)
PLAYER_RUSHING_TOUCHDOWNS_39_YARDS_COLUMN: Literal["rushing_touchdowns_39_yards"] = (
    "rushing_touchdowns_39_yards"
)
PLAYER_RUSHING_TOUCHDOWNS_49_YARDS_COLUMN: Literal["rushing_touchdowns_49_yards"] = (
    "rushing_touchdowns_49_yards"
)
PLAYER_RUSHING_TOUCHDOWNS_ABOVE_50_YARDS_COLUMN: Literal[
    "rushing_touchdowns_above_50_yards"
] = "rushing_touchdowns_above_50_yards"
PLAYER_PENALTIES_IN_MINUTES_COLUMN: Literal["penalties_in_minutes"] = (
    "penalties_in_minutes"
)
PLAYER_EVEN_STRENGTH_GOALS_COLUMN: Literal["even_strength_goals"] = (
    "even_strength_goals"
)
PLAYER_POWER_PLAY_GOALS_COLUMN: Literal["power_play_goals"] = "power_play_goals"
PLAYER_SHORT_HANDED_GOALS_COLUMN: Literal["short_handed_goals"] = "short_handed_goals"
PLAYER_GAME_WINNING_GOALS_COLUMN: Literal["game_winning_goals"] = "game_winning_goals"
PLAYER_EVEN_STRENGTH_ASSISTS_COLUMN: Literal["even_strength_assists"] = (
    "even_strength_assists"
)
PLAYER_POWER_PLAY_ASSISTS_COLUMN: Literal["power_play_assists"] = "power_play_assists"
PLAYER_SHORT_HANDED_ASSISTS_COLUMN: Literal["short_handed_assists"] = (
    "short_handed_assists"
)
PLAYER_SHOTS_ON_GOAL_COLUMN: Literal["shots_on_goal"] = "shots_on_goal"
PLAYER_SHOOTING_PERCENTAGE_COLUMN: Literal["shooting_percentage"] = (
    "shooting_percentage"
)
PLAYER_SHIFTS_COLUMN: Literal["shifts"] = "shifts"
PLAYER_TIME_ON_ICE_COLUMN: Literal["time_on_ice"] = "time_on_ice"
PLAYER_DECISION_COLUMN: Literal["decision"] = "decision"
PLAYER_GOALS_AGAINST_COLUMN: Literal["goals_against"] = "goals_against"
PLAYER_SHOTS_AGAINST_COLUMN: Literal["shots_against"] = "shots_against"
PLAYER_SAVES_COLUMN: Literal["saves"] = "saves"
PLAYER_SAVE_PERCENTAGE_COLUMN: Literal["save_percentage"] = "save_percentage"
PLAYER_SHUTOUTS_COLUMN: Literal["shutouts"] = "shutouts"
PLAYER_INDIVIDUAL_CORSI_FOR_EVENTS_COLUMN: Literal["individual_corsi_for_events"] = (
    "individual_corsi_for_events"
)
PLAYER_ON_SHOT_ICE_FOR_EVENTS_COLUMN: Literal["on_shot_ice_for_events"] = (
    "on_shot_ice_for_events"
)
PLAYER_ON_SHOT_ICE_AGAINST_EVENTS_COLUMN: Literal["on_shot_ice_against_events"] = (
    "on_shot_ice_against_events"
)
PLAYER_CORSI_FOR_PERCENTAGE_COLUMN: Literal["corsi_for_percentage"] = (
    "corsi_for_percentage"
)
PLAYER_RELATIVE_CORSI_FOR_PERCENTAGE_COLUMN: Literal[
    "relative_corsi_for_percentage"
] = "relative_corsi_for_percentage"
PLAYER_OFFENSIVE_ZONE_STARTS_COLUMN: Literal["offensive_zone_starts"] = (
    "offensive_zone_starts"
)
PLAYER_DEFENSIVE_ZONE_STARTS_COLUMN: Literal["defensive_zone_starts"] = (
    "defensive_zone_starts"
)
PLAYER_OFFENSIVE_ZONE_START_PERCENTAGE_COLUMN: Literal[
    "offensive_zone_start_percentage"
] = "offensive_zone_start_percentage"
PLAYER_HITS_COLUMN: Literal["hits"] = "hits"
PLAYER_TRUE_SHOOTING_PERCENTAGE_COLUMN: Literal["true_shooting_percentage"] = (
    "true_shooting_percentage"
)
PLAYER_AT_BATS_COLUMN: Literal["at_bats"] = "at_bats"
PLAYER_RUNS_SCORED_COLUMN: Literal["runs_scored"] = "runs_scored"
PLAYER_RUNS_BATTED_IN_COLUMN: Literal["runs_batted_in"] = "runs_batted_in"
PLAYER_BASES_ON_BALLS_COLUMN: Literal["bases_on_balls"] = "bases_on_balls"
PLAYER_STRIKEOUTS_COLUMN: Literal["strikeouts"] = "strikeouts"
PLAYER_PLATE_APPEARANCES_COLUMN: Literal["plate_appearances"] = "plate_appearances"
PLAYER_HITS_AT_BATS_COLUMN: Literal["hits_at_bats"] = "hits_at_bats"
PLAYER_OBP_COLUMN: Literal["obp"] = "obp"
PLAYER_SLG_COLUMN: Literal["slg"] = "slg"
PLAYER_OPS_COLUMN: Literal["ops"] = "ops"
PLAYER_PITCHES_COLUMN: Literal["pitches"] = "pitches"
PLAYER_STRIKES_COLUMN: Literal["strikes"] = "strikes"
PLAYER_WIN_PROBABILITY_ADDED_COLUMN: Literal["win_probability_added"] = (
    "win_probability_added"
)
PLAYER_AVERAGE_LEVERAGE_INDEX_COLUMN: Literal["average_leverage_index"] = (
    "average_leverage_index"
)
PLAYER_WPA_PLUS_COLUMN: Literal["wpa_plus"] = "wpa_plus"
PLAYER_WPA_MINUS_COLUMN: Literal["wpa_minus"] = "wpa_minus"
PLAYER_CWPA_COLUMN: Literal["cwpa"] = "cwpa"
PLAYER_ACLI_COLUMN: Literal["acli"] = "acli"
PLAYER_RE24_COLUMN: Literal["re24"] = "re24"
PLAYER_PUTOUTS_COLUMN: Literal["putouts"] = "putouts"
PLAYER_INNINGS_PITCHED_COLUMN: Literal["innings_pitched"] = "innings_pitched"
PLAYER_EARNED_RUNS_COLUMN: Literal["earned_runs"] = "earned_runs"
PLAYER_HOME_RUNS_COLUMN: Literal["home_runs"] = "home_runs"
PLAYER_ERA_COLUMN: Literal["era"] = "era"
PLAYER_BATTERS_FACED_COLUMN: Literal["batters_faced"] = "batters_faced"
PLAYER_STRIKES_BY_CONTACT_COLUMN: Literal["strikes_by_contact"] = "strikes_by_contact"
PLAYER_STRIKES_SWINGING_COLUMN: Literal["strikes_swinging"] = "strikes_swinging"
PLAYER_STRIKES_LOOKING_COLUMN: Literal["strikes_looking"] = "strikes_looking"
PLAYER_GROUND_BALLS_COLUMN: Literal["ground_balls"] = "ground_balls"
PLAYER_FLY_BALLS_COLUMN: Literal["fly_balls"] = "fly_balls"
PLAYER_LINE_DRIVES_COLUMN: Literal["line_drives"] = "line_drives"
PLAYER_INHERITED_RUNNERS_COLUMN: Literal["inherited_runners"] = "inherited_runners"
PLAYER_INHERITED_SCORES_COLUMN: Literal["inherited_scores"] = "inherited_scores"
PLAYER_EFFECTIVE_FIELD_GOAL_PERCENTAGE_COLUMN: Literal[
    "effective_field_goal_percentage"
] = "effective_field_goal_percentage"
PLAYER_PENALTY_KICKS_MADE_COLUMN: Literal["penalty_kicks_made"] = "penalty_kicks_made"
PLAYER_PENALTY_KICKS_ATTEMPTED_COLUMN: Literal["penalty_kicks_attempted"] = (
    "penalty_kicks_attempted"
)
PLAYER_SHOTS_TOTAL_COLUMN: Literal["shots_total"] = "shots_total"
PLAYER_SHOTS_ON_TARGET_COLUMN: Literal["shots_on_target"] = "shots_on_target"
PLAYER_YELLOW_CARDS_COLUMN: Literal["yellow_cards"] = "yellow_cards"
PLAYER_RED_CARDS_COLUMN: Literal["red_cards"] = "red_cards"
PLAYER_TOUCHES_COLUMN: Literal["touches"] = "touches"
PLAYER_EXPECTED_GOALS_COLUMN: Literal["expected_goals"] = "expected_goals"
PLAYER_NON_PENALTY_EXPECTED_GOALS_COLUMN: Literal["non_penalty_expected_goals"] = (
    "non_penalty_expected_goals"
)
PLAYER_EXPECTED_ASSISTED_GOALS_COLUMN: Literal["expected_assisted_goals"] = (
    "expected_assisted_goals"
)
PLAYER_SHOT_CREATING_ACTIONS_COLUMN: Literal["shot_creating_actions"] = (
    "shot_creating_actions"
)
PLAYER_GOAL_CREATING_ACTIONS_COLUMN: Literal["goal_creating_actions"] = (
    "goal_creating_actions"
)
PLAYER_PASSES_COMPLETED_COLUMN: Literal["passes_completed"] = "passes_completed"
PLAYER_PASSES_ATTEMPTED_COLUMN: Literal["passes_attempted"] = "passes_attempted"
PLAYER_PASS_COMPLETION_COLUMN: Literal["pass_completion"] = "pass_completion"
PLAYER_PROGRESSIVE_PASSES_COLUMN: Literal["progressive_passes"] = "progressive_passes"
PLAYER_CARRIES_COLUMN: Literal["carries"] = "carries"
PLAYER_PROGRESSIVE_CARRIES_COLUMN: Literal["progressive_carries"] = (
    "progressive_carries"
)
PLAYER_TAKE_ONS_ATTEMPTED_COLUMN: Literal["take_ons_attempted"] = "take_ons_attempted"
PLAYER_SUCCESSFUL_TAKE_ONS_COLUMN: Literal["successful_take_ons"] = (
    "successful_take_ons"
)
PLAYER_TOTAL_PASSING_DISTANCE_COLUMN: Literal["total_passing_distance"] = (
    "total_passing_distance"
)
PLAYER_PROGRESSIVE_PASSING_DISTANCE_COLUMN: Literal["progressive_passing_distance"] = (
    "progressive_passing_distance"
)
PLAYER_PASSES_COMPLETED_SHORT_COLUMN: Literal["passes_completed_short"] = (
    "passes_completed_short"
)
PLAYER_PASSES_ATTEMPTED_SHORT_COLUMN: Literal["passes_attempted_short"] = (
    "passes_attempted_short"
)
PLAYER_PASS_COMPLETION_SHORT_COLUMN: Literal["pass_completion_short"] = (
    "pass_completion_short"
)
PLAYER_PASSES_COMPLETED_MEDIUM_COLUMN: Literal["passes_completed_medium"] = (
    "passes_completed_medium"
)
PLAYER_PASSES_ATTEMPTED_MEDIUM_COLUMN: Literal["passes_attempted_medium"] = (
    "passes_attempted_medium"
)
PLAYER_PASS_COMPLETION_MEDIUM_COLUMN: Literal["pass_completion_medium"] = (
    "pass_completion_medium"
)
PLAYER_PASSES_COMPLETED_LONG_COLUMN: Literal["passes_completed_long"] = (
    "passes_completed_long"
)
PLAYER_PASSES_ATTEMPTED_LONG_COLUMN: Literal["passes_attempted_long"] = (
    "passes_attempted_long"
)
PLAYER_PASS_COMPLETION_LONG_COLUMN: Literal["pass_completion_long"] = (
    "pass_completion_long"
)
PLAYER_EXPECTED_ASSISTS_COLUMN: Literal["expected_assists"] = "expected_assists"
PLAYER_KEY_PASSES_COLUMN: Literal["key_passes"] = "key_passes"
PLAYER_PASSES_INTO_FINAL_THIRD_COLUMN: Literal["passes_into_final_third"] = (
    "passes_into_final_third"
)
PLAYER_PASSES_INTO_PENALTY_AREA_COLUMN: Literal["passes_into_penalty_area"] = (
    "passes_into_penalty_area"
)
PLAYER_CROSSES_INTO_PENALTY_AREA_COLUMN: Literal["crosses_into_penalty_area"] = (
    "crosses_into_penalty_area"
)
PLAYER_LIVE_BALL_PASSES_COLUMN: Literal["live_ball_passes"] = "live_ball_passes"
PLAYER_DEAD_BALL_PASSES_COLUMN: Literal["dead_ball_passes"] = "dead_ball_passes"
PLAYER_PASSES_FROM_FREE_KICKS_COLUMN: Literal["passes_from_free_kicks"] = (
    "passes_from_free_kicks"
)
PLAYER_THROUGH_BALLS_COLUMN: Literal["through_balls"] = "through_balls"
PLAYER_SWITCHES_COLUNM: Literal["switches"] = "switches"
PLAYER_CROSSES_COLUMN: Literal["crosses"] = "crosses"
PLAYER_THROW_INS_TAKEN_COLUMN: Literal["throw_ins_taken"] = "throw_ins_taken"
PLAYER_CORNER_KICKS_COLUMN: Literal["corner_kicks"] = "corner_kicks"
PLAYER_INSWINGING_CORNER_KICKS_COLUMN: Literal["inswinging_corner_kicks"] = (
    "inswinging_corner_kicks"
)
PLAYER_OUTSWINGING_CORNER_KICKS_COLUMN: Literal["outswinging_corner_kicks"] = (
    "outswinging_corner_kicks"
)
PLAYER_STRAIGHT_CORNER_KICKS_COLUMN: Literal["straight_corner_kicks"] = (
    "straight_corner_kicks"
)
PLAYER_PASSES_OFFSIDE_COLUMN: Literal["passes_offside"] = "passes_offside"
PLAYER_PASSES_BLOCKED_COLUMN: Literal["passes_blocked"] = "passes_blocked"
PLAYER_TACKLES_WON_COLUMN: Literal["tackles_won"] = "tackles_won"
PLAYER_TACKLES_IN_DEFENSIVE_THIRD_COLUMN: Literal["tackles_in_defensive_third"] = (
    "tackles_in_defensive_third"
)
PLAYER_TACKLES_IN_MIDDLE_THIRD_COLUMN: Literal["tackles_in_middle_third"] = (
    "tackles_in_middle_third"
)
PLAYER_TACKLES_IN_ATTACKING_THIRD_COLUMN: Literal["tackles_in_attacking_third"] = (
    "tackles_in_attacking_third"
)
PLAYER_DRIBBLERS_TACKLED_COLUMN: Literal["dribblers_tackled"] = "dribblers_tackled"
PLAYER_DRIBBLES_CHALLENGED_COLUMN: Literal["dribbles_challenged"] = (
    "dribbles_challenged"
)
PLAYER_PERCENT_OF_DRIBBLERS_TACKLED_COLUMN: Literal["percent_of_dribblers_tackled"] = (
    "percent_of_dribblers_tackled"
)
PLAYER_CHALLENGES_LOST_COLUMN: Literal["challenges_lost"] = "challenges_lost"
PLAYER_SHOTS_BLOCKED_COLUMN: Literal["shots_blocked"] = "shots_blocked"
PLAYER_TACKLES_PLUS_INTERCEPTIONS_COLUMN: Literal["tackles_plus_interceptions"] = (
    "tackles_plus_interceptions"
)
PLAYER_ERRORS_COLUMN: Literal["errors"] = "errors"
PLAYER_TOUCHES_IN_DEFENSIVE_PENALTY_AREA_COLUMN: Literal[
    "touches_in_defensive_penalty_area"
] = "touches_in_defensive_penalty_area"
PLAYER_TOUCHES_IN_DEFENSIVE_THIRD_COLUMN: Literal["touches_in_defensive_third"] = (
    "touches_in_defensive_third"
)
PLAYER_TOUCHES_IN_MIDDLE_THIRD_COLUMN: Literal["touches_in_middle_third"] = (
    "touches_in_middle_third"
)
PLAYER_TOUCHES_IN_ATTACKING_THIRD_COLUMN: Literal["touches_in_attacking_third"] = (
    "touches_in_attacking_third"
)
PLAYER_TOUCHES_IN_ATTACKING_PENALTY_AREA_COLUMN: Literal[
    "touches_in_attacking_penalty_area"
] = "touches_in_attacking_penalty_area"
PLAYER_LIVE_BALL_TOUCHES_COLUMN: Literal["live_ball_touches"] = "live_ball_touches"
PLAYER_SUCCESSFUL_TAKE_ON_PERCENTAGE_COLUMN: Literal[
    "successful_take_on_percentage"
] = "successful_take_on_percentage"
PLAYER_TIMES_TACKLED_DURING_TAKE_ONS_COLUMN: Literal[
    "times_tackled_during_take_ons"
] = "times_tackled_during_take_ons"
PLAYER_TACKLED_DURING_TAKE_ON_PERCENTAGE_COLUMN: Literal[
    "tackled_during_take_on_percentage"
] = "tackled_during_take_on_percentage"
PLAYER_TOTAL_CARRYING_DISTANCE_COLUMN: Literal["total_carrying_distance"] = (
    "total_carrying_distance"
)
PLAYER_PROGRESSIVE_CARRYING_DISTANCE_COLUMN: Literal[
    "progressive_carrying_distance"
] = "progressive_carrying_distance"
PLAYER_CARRIES_INTO_FINAL_THIRD_COLUMN: Literal["carries_into_final_third"] = (
    "carries_into_final_third"
)
PLAYER_CARRIES_INTO_PENALTY_AREA_COLUMN: Literal["carries_into_penalty_area"] = (
    "carries_into_penalty_area"
)
PLAYER_MISCONTROLS_COLUMN: Literal["miscontrols"] = "miscontrols"
PLAYER_DISPOSSESSED_COLUMN: Literal["dispossessed"] = "dispossessed"
PLAYER_PASSES_RECEIVED_COLUMN: Literal["passes_received"] = "passes_received"
PLAYER_PROGRESSIVE_PASSES_RECEIVED_COLUMN: Literal["progressive_passes_received"] = (
    "progressive_passes_received"
)
PLAYER_SECOND_YELLOW_CARD_COLUMN: Literal["second_yellow_card"] = "second_yellow_card"
PLAYER_FOULS_COMMITTED_COLUMN: Literal["fouls_committed"] = "fouls_committed"
PLAYER_FOULS_DRAWN_COLUMN: Literal["fouls_drawn"] = "fouls_drawn"
PLAYER_OFFSIDES_COLUMN: Literal["offsides"] = "offsides"
PLAYER_PENALTY_KICKS_WON_COLUMN: Literal["penalty_kicks_won"] = "penalty_kicks_won"
PLAYER_PENALTY_KICKS_CONCEDED_COLUMN: Literal["penalty_kicks_conceded"] = (
    "penalty_kicks_conceded"
)
PLAYER_OWN_GOALS_COLUMN: Literal["own_goals"] = "own_goals"
PLAYER_BALL_RECOVERIES_COLUMN: Literal["ball_recoveries"] = "ball_recoveries"
PLAYER_AERIALS_WON_COLUMN: Literal["aerials_won"] = "aerials_won"
PLAYER_AERIALS_LOST_COLUMN: Literal["aerials_lost"] = "aerials_lost"
PLAYER_PERCENTAGE_OF_AERIALS_WON_COLUMN: Literal["percentage_of_aerials_won"] = (
    "percentage_of_aerials_won"
)
PLAYER_SHOTS_ON_TARGET_AGAINST_COLUMN: Literal["shots_on_target_against"] = (
    "shots_on_target_against"
)
PLAYER_POST_SHOT_EXPECTED_GOALS_COLUMN: Literal["post_shot_expected_goals"] = (
    "post_shot_expected_goals"
)
PLAYER_PASSES_ATTEMPTED_MINUS_GOAL_KICKS_COLUMN: Literal[
    "passes_attempted_minus_goal_kicks"
] = "passes_attempted_minus_goal_kicks"
PLAYER_THROWS_ATTEMPTED_COLUMN: Literal["throws_attempted"] = "throws_attempted"
PLAYER_PERCENTAGE_OF_PASSES_THAT_WERE_LAUNCHED_COLUMN: Literal[
    "percentage_of_passes_that_were_launched"
] = "percentage_of_passes_that_were_launched"
PLAYER_AVERAGE_PASS_LENGTH_COLUMN: Literal["average_pass_length"] = (
    "average_pass_length"
)
PLAYER_GOAL_KICKS_ATTEMPTED_COLUMN: Literal["goal_kicks_attempted"] = (
    "goal_kicks_attempted"
)
PLAYER_PERCENTAGE_OF_GOAL_KICKS_THAT_WERE_LAUNCHED_COLUMN: Literal[
    "percentage_of_goal_kicks_that_were_launched"
] = "percentage_of_goal_kicks_that_were_launched"
PLAYER_AVERAGE_GOAL_KICK_LENGTH_COLUMN: Literal["average_goal_kick_length"] = (
    "average_goal_kick_length"
)
PLAYER_CROSSES_FACED_COLUMN: Literal["crosses_faced"] = "crosses_faced"
PLAYER_CROSSES_STOPPED_COLUMN: Literal["crosses_stopped"] = "crosses_stopped"
PLAYER_PERCENTAGE_CROSSES_STOPPED_COLUMN: Literal["percentage_crosses_stopped"] = (
    "percentage_crosses_stopped"
)
PLAYER_DEFENSIVE_ACTIONS_OUTSIDE_PENALTY_AREA_COLUMN: Literal[
    "defensive_actions_outside_penalty_area"
] = "defensive_actions_outside_penalty_area"
PLAYER_AVERAGE_DISTANCE_OF_DEFENSIVE_ACTIONS_COLUMN: Literal[
    "average_distance_of_defensive_actions"
] = "average_distance_of_defensive_actions"
PLAYER_THREE_POINT_ATTEMPT_RATE_COLUMN: Literal["three_point_attempt_rate"] = (
    "three_point_attempt_rate"
)
PLAYER_BATTING_STYLE_COLUMN: Literal["batting_style"] = "batting_style"
PLAYER_BOWLING_STYLE_COLUMN: Literal["bowling_style"] = "bowling_style"
PLAYER_PLAYING_ROLES_COLUMN: Literal["playing_roles"] = "playing_roles"
PLAYER_RUNS_COLUMN: Literal["runs"] = "runs"
PLAYER_BALLS_COLUMN: Literal["balls"] = "balls"
PLAYER_FOURS_COLUMN: Literal["fours"] = "fours"
PLAYER_SIXES_COLUMN: Literal["sixes"] = "sixes"
PLAYER_STRIKERATE_COLUMN: Literal["strikerate"] = "strikerate"
PLAYER_FALL_OF_WICKET_ORDER_COLUMN: Literal["fall_of_wicket_order"] = (
    "fall_of_wicket_order"
)
PLAYER_FALL_OF_WICKET_NUM_COLUMN: Literal["fall_of_wicket_num"] = "fall_of_wicket_num"
PLAYER_FALL_OF_WICKET_RUNS_COLUMN: Literal["fall_of_wicket_runs"] = (
    "fall_of_wicket_runs"
)
PLAYER_FALL_OF_WICKET_BALLS_COLUMN: Literal["fall_of_wicket_balls"] = (
    "fall_of_wicket_balls"
)
PLAYER_FALL_OF_WICKET_OVERS_COLUMN: Literal["fall_of_wicket_overs"] = (
    "fall_of_wicket_overs"
)
PLAYER_FALL_OF_WICKET_OVER_NUMBER_COLUMN: Literal["fall_of_wicket_over_number"] = (
    "fall_of_wicket_over_number"
)
PLAYER_BALL_OVER_ACTUAL_COLUMN: Literal["ball_over_actual"] = "ball_over_actual"
PLAYER_BALL_OVER_UNIQUE_COLUMN: Literal["ball_over_unique"] = "ball_over_unique"
PLAYER_BALL_TOTAL_RUNS_COLUMN: Literal["ball_total_runs"] = "ball_total_runs"
PLAYER_BALL_BATSMAN_RUNS_COLUMN: Literal["ball_batsman_runs"] = "ball_batsman_runs"
PLAYER_OVERS_COLUMN: Literal["overs"] = "overs"
PLAYER_MAIDENS_COLUMN: Literal["maidens"] = "maidens"
PLAYER_CONCEDED_COLUMN: Literal["conceded"] = "conceded"
PLAYER_WICKETS_COLUMN: Literal["wickets"] = "wickets"
PLAYER_ECONOMY_COLUMN: Literal["economy"] = "economy"
PLAYER_RUNS_PER_BALL_COLUMN: Literal["runs_per_ball"] = "runs_per_ball"
PLAYER_DOTS_COLUMN: Literal["dots"] = "dots"
PLAYER_WIDES_COLUMN: Literal["wides"] = "wides"
PLAYER_NO_BALLS_COLUMN: Literal["no_balls"] = "no_balls"
PLAYER_FREE_THROW_ATTEMPT_RATE_COLUMN: Literal["free_throw_attempt_rate"] = (
    "free_throw_attempt_rate"
)
PLAYER_OFFENSIVE_REBOUND_PERCENTAGE_COLUMN: Literal["offensive_rebound_percentage"] = (
    "offensive_rebound_percentage"
)
PLAYER_DEFENSIVE_REBOUND_PERCENTAGE_COLUMN: Literal["defensive_rebound_percentage"] = (
    "defensive_rebound_percentage"
)
PLAYER_TOTAL_REBOUND_PERCENTAGE_COLUMN: Literal["total_rebound_percentage"] = (
    "total_rebound_percentage"
)
PLAYER_ASSIST_PERCENTAGE_COLUMN: Literal["assist_percentage"] = "assist_percentage"
PLAYER_STEAL_PERCENTAGE_COLUMN: Literal["steal_percentage"] = "steal_percentage"
PLAYER_BLOCK_PERCENTAGE_COLUMN: Literal["block_percentage"] = "block_percentage"
PLAYER_TURNOVER_PERCENTAGE_COLUMN: Literal["turnover_percentage"] = (
    "turnover_percentage"
)
PLAYER_USAGE_PERCENTAGE_COLUMN: Literal["usage_percentage"] = "usage_percentage"
PLAYER_OFFENSIVE_RATING_COLUMN: Literal["offensive_rating"] = "offensive_rating"
PLAYER_DEFENSIVE_RATING_COLUMN: Literal["defensive_rating"] = "defensive_rating"
PLAYER_BOX_PLUS_MINUS_COLUMN: Literal["box_plus_minus"] = "box_plus_minus"
PLAYER_ACE_PERCENTAGE_COLUMN: Literal["ace_percentage"] = "ace_percentage"
PLAYER_DOUBLE_FAULT_PERCENTAGE_COLUMN: Literal["double_fault_percentage"] = (
    "double_fault_percentage"
)
PLAYER_FIRST_SERVES_IN_COLUMN: Literal["first_serves_in"] = "first_serves_in"
PLAYER_FIRST_SERVE_PERCENTAGE_COLUMN: Literal["first_serve_percentage"] = (
    "first_serve_percentage"
)
PLAYER_SECOND_SERVE_PERCENTAGE_COLUMN: Literal["second_serve_percentage"] = (
    "second_serve_percentage"
)
PLAYER_BREAK_POINTS_SAVED_COLUMN: Literal["break_points_saved"] = "break_points_saved"
PLAYER_RETURN_POINTS_WON_PERCENTGE_COLUMN: Literal["return_points_won_percentage"] = (
    "return_points_won_percentage"
)
PLAYER_WINNERS_COLUMN: Literal["winners"] = "winners"
PLAYER_WINNERS_FRONTHAND_COLUMN: Literal["winners_fronthand"] = "winners_fronthand"
PLAYER_WINNERS_BACKHAND_COLUMN: Literal["winners_backhand"] = "winners_backhand"
PLAYER_UNFORCED_ERRORS_COLUMN: Literal["unforced_errors"] = "unforced_errors"
PLAYER_UNFORCED_ERRORS_FRONTHAND_COLUMN: Literal["unforced_errors_fronthand"] = (
    "unforced_errors_fronthand"
)
PLAYER_UNFORCED_ERRORS_BACKHAND_COLUMN: Literal["unforced_errors_backhand"] = (
    "unforced_errors_backhand"
)
PLAYER_SERVE_POINTS_COLUMN: Literal["serve_points"] = "serve_points"
PLAYER_SERVES_WON_COLUMN: Literal["serves_won"] = "serves_won"
PLAYER_SERVES_ACES_COLUMN: Literal["serves_aces"] = "serves_aces"
PLAYER_SERVES_UNRETURNED_COLUMN: Literal["serves_unreturned"] = "serves_unreturned"
PLAYER_SERVES_FORCED_ERROR_PERCENTAGE_COLUMN: Literal[
    "serves_forced_error_percentage"
] = "serves_forced_error_percentage"
PLAYER_SERVES_WON_IN_THREE_SHOTS_OR_LESS_COLUMN: Literal[
    "serves_won_in_three_shots_or_less"
] = "serves_won_in_three_shots_or_less"
PLAYER_SERVES_WIDE_PERCENTAGE_COLUMN: Literal["serves_wide_percentage"] = (
    "serves_wide_percentage"
)
PLAYER_SERVES_BODY_PERCENTAGE_COLUMN: Literal["serves_body_percentage"] = (
    "serves_body_percentage"
)
PLAYER_SERVES_T_PERCENTAGE_COLUMN: Literal["serves_t_percentage"] = (
    "serves_t_percentage"
)
PLAYER_SERVES_WIDE_DEUCE_PERCENTAGE_COLUMN: Literal["serves_wide_deuce_percentage"] = (
    "serves_wide_deuce_percentage"
)
PLAYER_SERVES_BODY_DEUCE_PERCENTAGE_COLUMN: Literal["serves_body_deuce_percentage"] = (
    "serves_body_deuce_percentage"
)
PLAYER_SERVES_T_DEUCE_PERCENTAGE_COLUMN: Literal["serves_t_deuce_percentage"] = (
    "serves_t_deuce_percentage"
)
PLAYER_SERVES_WIDE_AD_PERCENTAGE_COLUMN: Literal["serves_wide_ad_percentage"] = (
    "serves_wide_ad_percentage"
)
PLAYER_SERVES_BODY_AD_PERCENTAGE_COLUMN: Literal["serves_body_ad_percentage"] = (
    "serves_body_ad_percentage"
)
PLAYER_SERVES_T_AD_PERCENTAGE_COLUMN: Literal["serves_t_ad_percentage"] = (
    "serves_t_ad_percentage"
)
PLAYER_SERVES_NET_PERCENTAGE_COLUMN: Literal["serves_net_percentage"] = (
    "serves_net_percentage"
)
PLAYER_SERVES_WIDE_DIRECTION_PERCENTAGE_COLUMN: Literal[
    "serves_wide_direction_percentage"
] = "serves_wide_direction_percentage"
PLAYER_SHOTS_DEEP_PERCENTAGE_COLUMN: Literal["shots_deep_percentage"] = (
    "shots_deep_percentage"
)
PLAYER_SHOTS_DEEP_WIDE_PERCENTAGE_COLUMN: Literal["shots_deep_wide_percentage"] = (
    "shots_deep_wide_percentage"
)
PLAYER_SHOTS_FOOT_ERRORS_PERCENTAGE_COLUMN: Literal["shots_foot_errors_percentage"] = (
    "shots_foot_errors_percentage"
)
PLAYER_SHOTS_UNKNOWN_PERCENTAGE_COLUMN: Literal["shots_unknown_percentage"] = (
    "shots_unknown_percentage"
)
PLAYER_POINTS_WON_PERCENTAGE_COLUMN: Literal["points_won_percentage"] = (
    "points_won_percentage"
)
PLAYER_TACKLES_INSIDE_50_COLUMN: Literal["tackles_inside_50"] = "tackles_inside_50"
PLAYER_TOTAL_POSSESSIONS_COLUMN: Literal["total_possessions"] = "total_possessions"
PLAYER_SCORE_INVOLVEMENTS_COLUMN: Literal["score_involvements"] = "score_involvements"
PLAYER_GOAL_ACCURACY_COLUMN: Literal["goal_accuracy"] = "goal_accuracy"
PLAYER_STOPPAGE_CLEARANCES_COLUMN: Literal["stoppage_clearances"] = (
    "stoppage_clearances"
)
PLAYER_UNCONTESTED_MARKS_COLUMN: Literal["uncontested_marks"] = "uncontested_marks"
PLAYER_DISPOSAL_EFFICIENCY_COLUMN: Literal["disposal_efficiency"] = (
    "disposal_efficiency"
)
PLAYER_CENTRE_CLEARANCES_COLUMN: Literal["centre_clearances"] = "centre_clearances"
PLAYER_ACCURATE_CROSSES_COLUMN: Literal["accurate_crosses"] = "accurate_crosses"
PLAYER_ACCURATE_LONG_BALLS_COLUMN: Literal["accurate_long_balls"] = (
    "accurate_long_balls"
)
PLAYER_ACCURATE_PASSES_COLUMN: Literal["accurate_passes"] = "accurate_passes"
PLAYER_ACCURATE_THROUGH_BALLS_COLUMN: Literal["accurate_through_balls"] = (
    "accurate_through_balls"
)
PLAYER_CROSS_PERCENTAGE_COLUMN: Literal["cross_percentage"] = "cross_percentage"
PLAYER_FREE_KICK_GOALS_COLUMN: Literal["free_kick_goals"] = "free_kick_goals"
PLAYER_FREE_KICK_PERCENTAGE_COLUMN: Literal["free_kick_percentage"] = (
    "free_kick_percentage"
)
PLAYER_FREE_KICK_SHOTS_COLUMN: Literal["free_kick_shots"] = "free_kick_shots"
PLAYER_GAME_WINNING_ASSISTS_COLUMN: Literal["game_winning_assists"] = (
    "game_winning_assists"
)
PLAYER_HEADED_GOALS_COLUMN: Literal["headed_goals"] = "headed_goals"
PLAYER_INACCURATE_CROSSES_COLUMN: Literal["inaccurate_crosses"] = "inaccurate_crosses"
PLAYER_INACCURATE_LONG_BALLS_COLUMN: Literal["inaccurate_long_balls"] = (
    "inaccurate_long_balls"
)
PLAYER_INACCURATE_PASSES_COLUMN: Literal["inaccurate_passes"] = "inaccurate_passes"
PLAYER_INACCURATE_THROUGH_BALLS_COLUMN: Literal["inaccurate_through_balls"] = (
    "inaccurate_through_balls"
)
PLAYER_LEFT_FOOTED_SHOTS_COLUMN: Literal["left_footed_shots"] = "left_footed_shots"
PLAYER_LONG_BALL_PERCENTAGE_COLUMN: Literal["long_ball_percentage"] = (
    "long_ball_percentage"
)
PLAYER_PENALTY_KICK_GOALS_COLUMN: Literal["penalty_kick_goals"] = "penalty_kick_goals"
PLAYER_PENALTY_KICK_PERCENTAGE_COLUMN: Literal["penalty_kick_percentage"] = (
    "penalty_kick_percentage"
)
PLAYER_PENALTY_KICKS_MISSED_COLUMN: Literal["penalty_kicks_missed"] = (
    "penalty_kicks_missed"
)
PLAYER_POSSESSION_PERCENTAGE_COLUMN: Literal["possession_percentage"] = (
    "possession_percentage"
)
PLAYER_POSSESSION_TIME_COLUMN: Literal["possession_time"] = "possession_time"
PLAYER_RIGHT_FOOTED_SHOTS_COLUMN: Literal["right_footed_shots"] = "right_footed_shots"
PLAYER_SHOOT_OUT_GOALS_COLUMN: Literal["shoot_out_goals"] = "shoot_out_goals"
PLAYER_SHOOT_OUT_MISSES_COLUMN: Literal["shoot_out_misses"] = "shoot_out_misses"
PLAYER_SHOOT_OUT_PERCENTAGE_COLUMN: Literal["shoot_out_percentage"] = (
    "shoot_out_percentage"
)
PLAYER_SHOT_ASSISTS_COLUMN: Literal["shot_assists"] = "shot_assists"
PLAYER_SHOT_PERCENTAGE_COLUMN: Literal["shot_percentage"] = "shot_percentage"
PLAYER_SHOTS_HEADED_COLUMN: Literal["shots_headed"] = "shots_headed"
PLAYER_SHOTS_OFF_TARGET_COLUMN: Literal["shots_off_target"] = "shots_off_target"
PLAYER_SHOTS_ON_POST_COLUMN: Literal["shots_on_post"] = "shots_on_post"
PLAYER_THROUGH_BALL_PERCENTAGE_COLUMN: Literal["through_ball_percentage"] = (
    "through_ball_percentage"
)
PLAYER_LONG_BALLS_COLUMN: Literal["long_balls"] = "long_balls"
PLAYER_TOTAL_PASSES_COLUMN: Literal["total_passes"] = "total_passes"
PLAYER_AVERAGE_RATING_FROM_EDITOR_COLUMN: Literal["average_rating_from_editor"] = (
    "average_rating_from_editor"
)
PLAYER_AVERAGE_RATING_FROM_USER_COLUMN: Literal["average_rating_from_user"] = (
    "average_rating_from_user"
)
PLAYER_DID_NOT_PLAY_COLUMN: Literal["did_not_play"] = "did_not_play"
PLAYER_DRAWS_COLUMN: Literal["draws"] = "draws"
PLAYER_GOAL_DIFFERENCE_COLUMN: Literal["goal_difference"] = "goal_difference"
PLAYER_LOSSES_COLUMN: Literal["losses"] = "losses"
PLAYER_LOST_CORNERS_COLUMN: Literal["lost_corners"] = "lost_corners"
PLAYER_MINUTES_COLUMN: Literal["minutes"] = "minutes"
PLAYER_PASS_PERCENTAGE_COLUMN: Literal["pass_percentage"] = "pass_percentage"
PLAYER_STARTS_COLUMN: Literal["starts"] = "starts"
PLAYER_SUB_INS_COLUMN: Literal["sub_ins"] = "sub_ins"
PLAYER_SUB_OUTS_COLUMN: Literal["sub_outs"] = "sub_outs"
PLAYER_SUSPENSIONS_COLUMN: Literal["suspensions"] = "suspensions"
PLAYER_TIME_ENDED_COLUMN: Literal["time_ended"] = "time_ended"
PLAYER_TIME_STARTED_COLUMN: Literal["time_started"] = "time_started"
PLAYER_WIN_PERCENTAGE_COLUMN: Literal["win_percentage"] = "win_percentage"
PLAYER_WINS_COLUMN: Literal["wins"] = "wins"
PLAYER_WON_CORNERS_COLUMN: Literal["won_corners"] = "won_corners"
PLAYER_CLEAN_SHEET_COLUMN: Literal["clean_sheet"] = "clean_sheet"
PLAYER_CROSSES_CAUGHT_COLUMN: Literal["crosses_caught"] = "crosses_caught"
PLAYER_GOALS_CONCEDED_COLUMN: Literal["goals_conceded"] = "goals_conceded"
PLAYER_PARTIAL_CLEAN_SHEET_COLUMN: Literal["partial_clean_sheet"] = (
    "partial_clean_sheet"
)
PLAYER_PENALTY_KICK_CONCEDED_COLUMN: Literal["penalty_kick_conceded"] = (
    "penalty_kick_conceded"
)
PLAYER_PENALTY_KICK_SAVE_PERCENTAGE_COLUMN: Literal["penalty_kick_save_percentage"] = (
    "penalty_kick_save_percentage"
)
PLAYER_PENALTY_KICKS_FACED_COLUMN: Literal["penalty_kicks_faced"] = (
    "penalty_kicks_faced"
)
PLAYER_PENALTY_KICKS_SAVED_COLUMN: Literal["penalty_kicks_saved"] = (
    "penalty_kicks_saved"
)
PLAYER_PUNCHES_COLUMN: Literal["punches"] = "punches"
PLAYER_SHOOT_OUT_KICKS_FACED_COLUMN: Literal["shoot_out_kicks_faced"] = (
    "shoot_out_kicks_faced"
)
PLAYER_SHOOT_OUT_KICKS_SAVED_COLUMN: Literal["shoot_out_kicks_saved"] = (
    "shoot_out_kicks_saved"
)
PLAYER_SHOOT_OUT_SAVE_PERCENTAGE_COLUMN: Literal["shoot_out_save_percentage"] = (
    "shoot_out_save_percentage"
)
PLAYER_SHOTS_FACED_COLUMN: Literal["shots_faced"] = "shots_faced"
PLAYER_SMOTHERS_COLUMN: Literal["smothers"] = "smothers"
PLAYER_UNCLAIMED_CROSSES_COLUMN: Literal["unclaimed_crosses"] = "unclaimed_crosses"
PLAYER_EFFECTIVE_CLEARANCES_COLUMN: Literal["effective_clearances"] = (
    "effective_clearances"
)
PLAYER_EFFECTIVE_TACKLES_COLUMN: Literal["effective_tackles"] = "effective_tackles"
PLAYER_INEFFECTIVE_TACKLES_COLUMN: Literal["ineffective_tackles"] = (
    "ineffective_tackles"
)
PLAYER_TACKLE_PERCENTAGE_COLUMN: Literal["tackle_percentage"] = "tackle_percentage"
PLAYER_APPEARANCES_COLUMN: Literal["appearances"] = "appearances"
PLAYER_AVERAGE_RATING_FROM_CORRESPONDENT_COLUMN: Literal[
    "average_rating_from_correspondent"
] = "average_rating_from_correspondent"
PLAYER_AVERAGE_RATING_FROM_DATA_FEED_COLUMN: Literal[
    "average_rating_from_data_feed"
] = "average_rating_from_data_feed"
PLAYER_STRIKEOUTS_PER_NINE_INNINGS_COLUMN: Literal["strikeouts_per_nine_innings"] = (
    "strikeouts_per_nine_innings"
)
PLAYER_STRIKEOUT_TO_WALK_RATIO_COLUMN: Literal["strikeout_to_walk_ratio"] = (
    "strikeout_to_walk_ratio"
)
PLAYER_TOUGH_LOSSES_COLUMN: Literal["tough_losses"] = "tough_losses"
PLAYER_CHEAP_WINS_COLUMN: Literal["cheap_wins"] = "cheap_wins"
PLAYER_SAVE_OPPORTUNITIES_PER_WIN_COLUMN: Literal["save_opportunities_per_win"] = (
    "save_opportunities_per_win"
)
PLAYER_PITCH_COUNT_COLUMN: Literal["pitch_count"] = "pitch_count"
PLAYER_STRIKE_PITCH_RATIO_COLUMN: Literal["strike_pitch_ratio"] = "strike_pitch_ratio"
PLAYER_DOUBLE_PLAYS_COLUMN: Literal["double_plays"] = "double_plays"
PLAYER_OPPORTUNITIES_COLUMN: Literal["opportunities"] = "opportunities"
PLAYER_PASSED_BALLS_COLUMN: Literal["passed_balls"] = "passed_balls"
PLAYER_OUTFIELD_ASSISTS_COLUMN: Literal["outfield_assists"] = "outfield_assists"
PLAYER_PICKOFFS_COLUMN: Literal["pickoffs"] = "pickoffs"
PLAYER_OUTS_ON_FIELD_COLUMN: Literal["outs_on_field"] = "outs_on_field"
PLAYER_TRIPLE_PLAYS_COLUMN: Literal["triple_plays"] = "triple_plays"
PLAYER_BALLS_IN_ZONE_COLUMN: Literal["balls_in_zone"] = "balls_in_zone"
PLAYER_EXTRA_BASES_COLUMN: Literal["extra_bases"] = "extra_bases"
PLAYER_OUTS_MADE_COLUMN: Literal["outs_made"] = "outs_made"
PLAYER_CATCHER_THIRD_INNINGS_PLAYED_COLUMN: Literal["catcher_third_innings_played"] = (
    "catcher_third_innings_played"
)
PLAYER_CATCHER_CAUGHT_STEALING_COLUMN: Literal["catcher_caught_stealing"] = (
    "catcher_caught_stealing"
)
PLAYER_CATCHER_STOLEN_BASES_ALLOWED_COLUMN: Literal["catcher_stolen_bases_allowed"] = (
    "catcher_stolen_bases_allowed"
)
PLAYER_CATCHER_EARNED_RUNS_COLUMN: Literal["catcher_earned_runs"] = (
    "catcher_earned_runs"
)
PLAYER_IS_QUALIFIED_CATCHER_COLUMN: Literal["is_qualified_catcher"] = (
    "is_qualified_catcher"
)
PLAYER_IS_QUALIFIED_PITCHER_COLUMN: Literal["is_qualified_pitcher"] = (
    "is_qualified_pitcher"
)
PLAYER_SUCCESSFUL_CHANCES_COLUMN: Literal["successful_chances"] = "successful_chances"
PLAYER_TOTAL_CHANCES_COLUMN: Literal["total_chances"] = "total_chances"
PLAYER_FULL_INNINGS_PLAYED_COLUMN: Literal["full_innings_played"] = (
    "full_innings_played"
)
PLAYER_PART_INNINGS_PLAYED_COLUMN: Literal["part_innings_played"] = (
    "part_innings_played"
)
PLAYER_FIELDING_PERCENTAGE_COLUMN: Literal["fielding_percentage"] = (
    "fielding_percentage"
)
PLAYER_RANGE_FACTOR_COLUMN: Literal["range_factor"] = "range_factor"
PLAYER_ZONE_RATING_COLUMN: Literal["zone_rating"] = "zone_rating"
PLAYER_CATCHER_CAUGHT_STEALING_PERCENTAGE_COLUMN: Literal[
    "catcher_caught_stealing_percentage"
] = "catcher_caught_stealing_percentage"
PLAYER_CATCHER_ERA_COLUMN: Literal["catcher_era"] = "catcher_era"
PLAYER_DEF_WARBR_COLUMN: Literal["def_warbr"] = "def_warbr"
PLAYER_WINS_ABOVE_REPLACEMENT_COLUMN: Literal["wins_above_replacement"] = (
    "wins_above_replacement"
)
PLAYER_BATTERS_HIT_COLUMN: Literal["batters_hit"] = "batters_hit"
PLAYER_SACRIFICE_BUNTS_COLUMN: Literal["sacrifice_bunts"] = "sacrifice_bunts"
PLAYER_SAVE_OPPORTUNITIES_COLUMN: Literal["save_opportunities"] = "save_opportunities"
PLAYER_FINISHES_COLUMN: Literal["finishes"] = "finishes"
PLAYER_BALKS_COLUMN: Literal["balks"] = "balks"
PLAYER_HOLDS_COLUMN: Literal["holds"] = "holds"
PLAYER_COMPLETE_GAMES_COLUMN: Literal["complete_games"] = "complete_games"
PLAYER_PERFECT_GAMES_COLUMN: Literal["perfect_games"] = "perfect_games"
PLAYER_WILD_PITCHES_COLUMN: Literal["wild_pitches"] = "wild_pitches"
PLAYER_THIRD_INNINGS_COLUMN: Literal["third_innings"] = "third_innings"
PLAYER_TEAM_EARNED_RUNS_COLUMN: Literal["team_earned_runs"] = "team_earned_runs"
PLAYER_PICKOFF_ATTEMPTS_COLUMN: Literal["pickoff_attempts"] = "pickoff_attempts"
PLAYER_RUN_SUPPORT_COLUMN: Literal["run_support"] = "run_support"
PLAYER_PITCHES_AS_STARTER_COLUMN: Literal["pitches_as_starter"] = "pitches_as_starter"
PLAYER_AVERAGE_GAME_SCORE_COLUMN: Literal["average_game_score"] = "average_game_score"
PLAYER_QUALITY_STARTS_COLUMN: Literal["quality_starts"] = "quality_starts"
PLAYER_INHERITED_RUNNERS_SCORED_COLUMN: Literal["inherited_runners_scored"] = (
    "inherited_runners_scored"
)
PLAYER_OPPONENT_TOTAL_BASES_COLUMN: Literal["opponent_total_bases"] = (
    "opponent_total_bases"
)
PLAYER_IS_QUALIFIED_SAVES_COLUMN: Literal["is_qualified_saves"] = "is_qualified_saves"
PLAYER_FULL_INNINGS_COLUMN: Literal["full_innings"] = "full_innings"
PLAYER_PART_INNINGS_COLUMN: Literal["part_innings"] = "part_innings"
PLAYER_BLOWN_SAVES_COLUMN: Literal["blown_saves"] = "blown_saves"
PLAYER_INNINGS_COLUMN: Literal["innings"] = "innings"
PLAYER_WHIP_COLUMN: Literal["whip"] = "whip"
PLAYER_CAUGHT_STEALING_PERCENTAGE_COLUMN: Literal["caught_stealing_percentage"] = (
    "caught_stealing_percentage"
)
PLAYER_PITCHES_PER_START_COLUMN: Literal["pitches_per_start"] = "pitches_per_start"
PLAYER_PITCHES_PER_INNING_COLUMN: Literal["pitches_per_inning"] = "pitches_per_inning"
PLAYER_RUN_SUPPORT_AVERAGE_COLUMN: Literal["run_support_average"] = (
    "run_support_average"
)
PLAYER_OPPONENT_AVERAGE_COLUMN: Literal["opponent_average"] = "opponent_average"
PLAYER_OPPONENT_SLUG_AVERAGE_COLUMN: Literal["opponent_slug_average"] = (
    "opponent_slug_average"
)
PLAYER_OPPONENT_ON_BASE_PERCENTAGE_COLUMN: Literal["opponent_on_base_percentage"] = (
    "opponent_on_base_percentage"
)
PLAYER_OPPONENT_OPS_COLUMN: Literal["opponent_ops"] = "opponent_ops"
PLAYER_DOUBLES_COLUMN: Literal["doubles"] = "doubles"
PLAYER_CAUGHT_STEALING_COLUMN: Literal["caught_stealing"] = "caught_stealing"
PLAYER_GAMES_STARTED_COLUMN: Literal["games_started"] = "games_started"
PLAYER_PINCH_AT_BATS_COLUMN: Literal["pinch_at_bats"] = "pinch_at_bats"
PLAYER_PINCH_HITS_COLUMN: Literal["pinch_hits"] = "pinch_hits"
PLAYER_PLAYER_RATING_COLUMN: Literal["player_rating"] = "player_rating"
PLAYER_IS_QUALIFIED_COLUMN: Literal["is_qualified"] = "is_qualified"
PLAYER_IS_QUALIFIED_STEALS_COLUMN: Literal["is_qualified_steals"] = (
    "is_qualified_steals"
)
PLAYER_TOTAL_BASES_COLUMN: Literal["total_bases"] = "total_bases"
PLAYER_PROJECTED_HOME_RUNS_COLUMN: Literal["projected_home_runs"] = (
    "projected_home_runs"
)
PLAYER_EXTRA_BASE_HITS_COLUMN: Literal["extra_base_hits"] = "extra_base_hits"
PLAYER_RUNS_CREATED_COLUMN: Literal["runs_created"] = "runs_created"
PLAYER_BATTING_AVERAGE_COLUMN: Literal["batting_average"] = "batting_average"
PLAYER_PINCH_AVERAGE_COLUMN: Literal["pinch_average"] = "pinch_average"
PLAYER_SLUG_AVERAGE_COLUMN: Literal["slug_average"] = "slug_average"
PLAYER_SECONDARY_AVERAGE_COLUMN: Literal["secondary_average"] = "secondary_average"
PLAYER_ON_BASE_PERCENTAGE_COLUMN: Literal["on_base_percentage"] = "on_base_percentage"
PLAYER_GROUND_TO_FLY_RATIO_COLUMN: Literal["ground_to_fly_ratio"] = (
    "ground_to_fly_ratio"
)
PLAYER_RUNS_CREATED_PER_27_OUTS_COLUMN: Literal["runs_created_per_27_outs"] = (
    "runs_created_per_27_outs"
)
PLAYER_BATTER_RATING_COLUNN: Literal["batter_rating"] = "batter_rating"
PLAYER_AT_BATS_PER_HOME_RUN_COLUMN: Literal["at_bats_per_home_run"] = (
    "at_bats_per_home_run"
)
PLAYER_STOLEN_BASE_PERCENTAGE_COLUMN: Literal["stolen_base_percentage"] = (
    "stolen_base_percentage"
)
PLAYER_PITCHES_PER_PLATE_APPEARANCE_COLUMN: Literal["pitches_per_plate_appearance"] = (
    "pitches_per_plate_appearance"
)
PLAYER_ISOLATED_POWER_COLUMN: Literal["isolated_power"] = "isolated_power"
PLAYER_WALK_TO_STRIKEOUT_RATIO_COLUMN: Literal["walk_to_strikeout_ratio"] = (
    "walk_to_strikeout_ratio"
)
PLAYER_WALKS_PER_PLATE_APPEARANCE_COLUMN: Literal["walks_per_plate_appearance"] = (
    "walks_per_plate_appearance"
)
PLAYER_SECONDARY_AVERAGE_MINUS_BATTING_AVERAGE_COLUMN: Literal[
    "secondary_average_minus_batting_average"
] = "secondary_average_minus_batting_average"
PLAYER_RUNS_PRODUCED_COLUMN: Literal["runs_produced"] = "runs_produced"
PLAYER_RUNS_RATIO_COLUMN: Literal["runs_ratio"] = "runs_ratio"
PLAYER_PATIENCE_RATIO_COLUMN: Literal["patience_ratio"] = "patience_ratio"
PLAYER_BALLS_IN_PLAY_AVERAGE_COLUMN: Literal["balls_in_play_average"] = (
    "balls_in_play_average"
)
PLAYER_MLB_RATING_COLUMN: Literal["mlb_rating"] = "mlb_rating"
PLAYER_OFFENSIVE_WINS_ABOVE_REPLACEMENT_COLUMN: Literal[
    "offensive_wins_above_replacement"
] = "offensive_wins_above_replacement"
PLAYER_GAMES_PLAYED_COLUMN: Literal["games_played"] = "games_played"
PLAYER_TEAM_GAMES_PLAYED_COLUMN: Literal["team_games_played"] = "team_games_played"
PLAYER_HIT_BY_PITCH_COLUMN: Literal["hit_by_pitch"] = "hit_by_pitch"
PLAYER_RBIS_COLUMN: Literal["rbis"] = "rbis"
PLAYER_SAC_HITS_COLUMN: Literal["sac_hits"] = "sac_hits"
PLAYER_STOLEN_BASES_COLUMN: Literal["stolen_bases"] = "stolen_bases"
PLAYER_WALKS_COLUMN: Literal["walks"] = "walks"
PLAYER_CATCHER_INTERFERENCE_COLUMN: Literal["catcher_interference"] = (
    "catcher_interference"
)
PLAYER_GIDPS_COLUMN: Literal["gidps"] = "gidps"
PLAYER_SAC_FLIES_COLUMN: Literal["sac_flies"] = "sac_flies"
PLAYER_GRAND_SLAM_HOME_RUNS_COLUMN: Literal["grand_slam_home_runs"] = (
    "grand_slam_home_runs"
)
PLAYER_RUNNERS_LEFT_ON_BASE_COLUMN: Literal["runners_left_on_base"] = (
    "runners_left_on_base"
)
PLAYER_TRIPLES_COLUMN: Literal["triples"] = "triples"
PLAYER_GAME_WINNING_RBIS_COLUMN: Literal["game_winning_rbis"] = "game_winning_rbis"
PLAYER_INTENTIONAL_WALKS_COLUMN: Literal["intentional_walks"] = "intentional_walks"
PLAYER_AVERAGE_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_three_point_field_goals_attempted"
] = "average_three_point_field_goals_attempted"
PLAYER_AVERAGE_FREE_THROWS_MADE_COLUMN: Literal["average_free_throws_made"] = (
    "average_free_throws_made"
)
PLAYER_AVERAGE_FREE_THROWS_ATTEMPTED_COLUMN: Literal[
    "average_free_throws_attempted"
] = "average_free_throws_attempted"
PLAYER_AVERAGE_POINTS_COLUMN: Literal["average_points"] = "average_points"
PLAYER_AVERAGE_OFFENSIVE_REBOUNDS_COLUMN: Literal["average_offensive_rebounds"] = (
    "average_offensive_rebounds"
)
PLAYER_AVERAGE_ASSISTS_COLUMN: Literal["average_assists"] = "average_assists"
PLAYER_AVERAGE_TURNOVERS_COLUMN: Literal["average_turnovers"] = "average_turnovers"
PLAYER_ESTIMATED_POSSESSIONS_COLUMN: Literal["estimated_possessions"] = (
    "estimated_possessions"
)
PLAYER_AVERAGE_ESTIMATED_POSSESSIONS_COLUMN: Literal[
    "average_estimated_possessions"
] = "average_estimated_possessions"
PLAYER_POINTS_PER_ESTIMATED_POSSESSIONS_COLUMN: Literal[
    "points_per_estimated_possessions"
] = "points_per_estimated_possessions"
PLAYER_AVERAGE_TEAM_TURNOVERS_COLUMN: Literal["average_team_turnovers"] = (
    "average_team_turnovers"
)
PLAYER_AVERAGE_TOTAL_TURNOVERS_COLUMN: Literal["average_total_turnovers"] = (
    "average_total_turnovers"
)
PLAYER_THREE_POINT_FIELD_GOAL_PERCENTAGE_COLUMN: Literal[
    "three_point_field_goal_percentage"
] = "three_point_field_goal_percentage"
PLAYER_TWO_POINT_FIELD_GOALS_MADE_COLUMN: Literal["two_point_field_goals_made"] = (
    "two_point_field_goals_made"
)
PLAYER_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "two_point_field_goals_attempted"
] = "two_point_field_goals_attempted"
PLAYER_AVERAGE_TWO_POINT_FIELD_GOALS_MADE_COLUMN: Literal[
    "average_two_point_field_goals_made"
] = "average_two_point_field_goals_made"
PLAYER_AVERAGE_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_two_point_field_goals_attempted"
] = "average_two_point_field_goals_attempted"
PLAYER_TWO_POINT_FIELD_GOAL_PERCENTAGE_COLUMN: Literal[
    "two_point_field_goal_percentage"
] = "two_point_field_goal_percentage"
PLAYER_SHOOTING_EFFICIENCY_COLUMN: Literal["shooting_efficiency"] = (
    "shooting_efficiency"
)
PLAYER_SCORING_EFFICIENCY_COLUMN: Literal["scoring_efficiency"] = "scoring_efficiency"
PLAYER_AVERAGE_48_FIELD_GOALS_MADE_COLUMN: Literal["average_48_field_goals_made"] = (
    "average_48_field_goals_made"
)
PLAYER_AVERAGE_48_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_48_field_goals_attempted"
] = "average_48_field_goals_attempted"
PLAYER_AVERAGE_48_THREE_POINT_FIELD_GOALS_MADE_COLUMN: Literal[
    "average_48_three_point_field_goals_made"
] = "average_48_three_point_field_goals_made"
PLAYER_AVERAGE_48_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_48_three_point_field_goals_attempted"
] = "average_48_three_point_field_goals_attempted"
PLAYER_AVERAGE_48_FREE_THROWS_MADE_COLUMN: Literal["average_48_free_throws_made"] = (
    "average_48_free_throws_made"
)
PLAYER_AVERAGE_48_FREE_THROWS_ATTEMPTED_COLUMN: Literal[
    "average_48_free_throws_attempted"
] = "average_48_free_throws_attempted"
PLAYER_AVERAGE_48_POINTS_COLUMN: Literal["average_48_points"] = "average_48_points"
PLAYER_AVERAGE_48_OFFENSIVE_REBOUNDS_COLUMN: Literal[
    "average_48_offensive_rebounds"
] = "average_48_offensive_rebounds"
PLAYER_AVERAGE_48_ASSISTS_COLUMN: Literal["average_48_assists"] = "average_48_assists"
PLAYER_AVERAGE_48_TURNOVERS_COLUMN: Literal["average_48_turnovers"] = (
    "average_48_turnovers"
)
PLAYER_P40_COLUMN: Literal["p40"] = "p40"
PLAYER_A40_COLUMN: Literal["a40"] = "a40"
PLAYER_AVERAGE_REBOUNDS_COLUMN: Literal["average_rebounds"] = "average_rebounds"
PLAYER_AVERAGE_FOULS_COLUMN: Literal["average_fouls"] = "average_fouls"
PLAYER_AVERAGE_FLAGRANT_FOULS_COLUMN: Literal["average_flagrant_fouls"] = (
    "average_flagrant_fouls"
)
PLAYER_AVERAGE_TECHNICAL_FOULS_COLUMN: Literal["average_technical_fouls"] = (
    "average_technical_fouls"
)
PLAYER_AVERAGE_EJECTIONS_COLUMN: Literal["average_ejections"] = "average_ejections"
PLAYER_AVERAGE_DISQUALIFICATIONS_COLUMN: Literal["average_disqualifications"] = (
    "average_disqualifications"
)
PLAYER_ASSIST_TURNOVER_RATIO_COLUMN: Literal["assist_turnover_ratio"] = (
    "assist_turnover_ratio"
)
PLAYER_STEAL_FOUL_RATIO_COLUMN: Literal["steal_foul_ratio"] = "steal_foul_ratio"
PLAYER_BLOCK_FOUL_RATIO_COLUMN: Literal["block_foul_ratio"] = "block_foul_ratio"
PLAYER_AVERAGE_TEAM_REBOUNDS_COLUMN: Literal["average_team_rebounds"] = (
    "average_team_rebounds"
)
PLAYER_TOTAL_TECHNICAL_FOULS_COLUMN: Literal["total_technical_fouls"] = (
    "total_technical_fouls"
)
PLAYER_TEAM_ASSIST_TURNOVER_RATIO_COLUMN: Literal["team_assist_turnover_ratio"] = (
    "team_assist_turnover_ratio"
)
PLAYER_STEAL_TURNOVER_RATIO_COLUMN: Literal["steal_turnover_ratio"] = (
    "steal_turnover_ratio"
)
PLAYER_AVERAGE_48_REBOUNDS_COLUMN: Literal["average_48_rebounds"] = (
    "average_48_rebounds"
)
PLAYER_AVERAGE_48_FOULS_COLUMN: Literal["average_48_fouls"] = "average_48_fouls"
PLAYER_AVERAGE_48_FLAGRANT_FOULS_COLUMN: Literal["average_48_flagrant_fouls"] = (
    "average_48_flagrant_fouls"
)
PLAYER_AVERAGE_48_TECHNICAL_FOULS_COLUMN: Literal["average_48_technical_fouls"] = (
    "average_48_technical_fouls"
)
PLAYER_AVERAGE_48_EJECTIONS_COLUMN: Literal["average_48_ejections"] = (
    "average_48_ejections"
)
PLAYER_AVERAGE_48_DISQUALIFICATIONS_COLUMN: Literal["average_48_disqualifications"] = (
    "average_48_disqualifications"
)
PLAYER_R40_COLUMN: Literal["r40"] = "r40"
PLAYER_DOUBLE_DOUBLE_COLUMN: Literal["double_double"] = "double_double"
PLAYER_TRIPLE_DOUBLE_COLUMN: Literal["triple_double"] = "triple_double"
PLAYER_FREE_THROWS_MADE_COLUMN: Literal["free_throws_made"] = "free_throws_made"
PLAYER_THREE_POINT_PERCENTAGE_COLUMN: Literal["three_point_percentage"] = (
    "three_point_percentage"
)
PLAYER_THREE_POINT_FIELD_GOALS_MADE_COLUMN: Literal["three_point_field_goals_made"] = (
    "three_point_field_goals_made"
)
PLAYER_TOTAL_TURNOVERS_COLUMN: Literal["total_turnovers"] = "total_turnovers"
PLAYER_POINTS_IN_PAINT_COLUMN: Literal["points_in_paint"] = "points_in_paint"
PLAYER_BRICK_INDEX_COLUMN: Literal["brick_index"] = "brick_index"
PLAYER_AVERAGE_FIELD_GOALS_MADE_COLUMN: Literal["average_field_goals_made"] = (
    "average_field_goals_made"
)
PLAYER_AVERAGE_FIELD_GOALS_ATTEMPTED_COLUMN: Literal[
    "average_field_goals_attempted"
] = "average_field_goals_attempted"
PLAYER_AVERAGE_THREE_POINT_FIELD_GOALS_MADE_COLUMN: Literal[
    "average_three_point_field_goals_made"
] = "average_three_point_field_goals_made"
PLAYER_AVERAGE_DEFENSIVE_REBOUNDS_COLUMN: Literal["average_defensive_rebounds"] = (
    "average_defensive_rebounds"
)
PLAYER_AVERAGE_BLOCKS_COLUMN: Literal["average_blocks"] = "average_blocks"
PLAYER_AVERAGE_STEALS_COLUMN: Literal["average_steals"] = "average_steals"
PLAYER_AVERAGE_48_DEFENSIVE_REBOUNDS_COLUMN: Literal[
    "average_48_defensive_rebounds"
] = "average_48_defensive_rebounds"
PLAYER_AVERAGE_48_BLOCKS_COLUMN: Literal["average_48_blocks"] = "average_48_blocks"
PLAYER_AVERAGE_48_STEALS_COLUMN: Literal["average_48_steals"] = "average_48_steals"
PLAYER_LARGEST_LEAD_COLUMN: Literal["largest_lead"] = "largest_lead"
PLAYER_DISQUALIFICATIONS_COLUMN: Literal["disqualifications"] = "disqualifications"
PLAYER_FLAGRANT_FOULS_COLUMN: Literal["flagrant_fouls"] = "flagrant_fouls"
PLAYER_FOULS_COLUMN: Literal["fouls"] = "fouls"
PLAYER_EJECTIONS_COLUMN: Literal["ejections"] = "ejections"
PLAYER_TECHNICAL_FOULS_COLUMN: Literal["technical_fouls"] = "technical_fouls"
PLAYER_AVERAGE_MINUTES_COLUMN: Literal["average_minutes"] = "average_minutes"
PLAYER_NBA_RATING_COLUMN: Literal["nba_rating"] = "nba_rating"
PLAYER_PLUS_MINUS_COLUMN: Literal["plus_minus"] = "plus_minus"
PLAYER_FACEOFFS_WON_COLUMN: Literal["faceoffs_won"] = "faceoffs_won"
PLAYER_FACEOFFS_LOST_COLUMN: Literal["faceoffs_lost"] = "faceoffs_lost"
PLAYER_FACEOFF_PERCENTAGE_COLUMN: Literal["faceoff_percentage"] = "faceoff_percentage"
PLAYER_UNASSISTED_GOALS_COLUMN: Literal["unassisted_goals"] = "unassisted_goals"
PLAYER_GAME_TYING_GOALS_COLUMN: Literal["game_tying_goals"] = "game_tying_goals"
PLAYER_GIVEAWAYS_COLUMN: Literal["giveaways"] = "giveaways"
PLAYER_PENALTIES_COLUMN: Literal["penalties"] = "penalties"
PLAYER_PENALTY_MINUTES_COLUMN: Literal["penalty_minutes"] = "penalty_minutes"
PLAYER_PENALTY_MINUTES_AGAINST_COLUMN: Literal["penalty_minutes_against"] = (
    "penalty_minutes_against"
)
PLAYER_MAJOR_PENALTIES_COLUMN: Literal["major_penalties"] = "major_penalties"
PLAYER_MINOR_PENALTIES_COLUMN: Literal["minor_penalties"] = "minor_penalties"
PLAYER_MATCH_PENALTIES_COLUMN: Literal["match_penalties"] = "match_penalties"
PLAYER_MISCONDUCTS_COLUMN: Literal["misconducts"] = "misconducts"
PLAYER_GAME_MISCONDUCTS_COLUMN: Literal["game_misconducts"] = "game_misconducts"
PLAYER_BOARDING_PENALTIES_COLUMN: Literal["boarding_penalties"] = "boarding_penalties"
PLAYER_UNSPORTSMANLIKE_PENALTIES_COLUMN: Literal["unsportsmanlike_penalties"] = (
    "unsportsmanlike_penalties"
)
PLAYER_FIGHTING_PENALTIES_COLUMN: Literal["fighting_penalties"] = "fighting_penalties"
PLAYER_AVERAGE_FIGHTS_COLUMN: Literal["average_fights"] = "average_fights"
PLAYER_TIME_BETWEEN_FIGHTS_COLUMN: Literal["time_between_fights"] = (
    "time_between_fights"
)
PLAYER_INSTIGATOR_PENALTIES_COLUMN: Literal["instigator_penalties"] = (
    "instigator_penalties"
)
PLAYER_CHARGING_PENALTIES_COLUMN: Literal["charging_penalties"] = "charging_penalties"
PLAYER_HOOKING_PENALTIES_COLUMN: Literal["hooking_penalties"] = "hooking_penalties"
PLAYER_TRIPPING_PENALTIES_COLUMN: Literal["tripping_penalties"] = "tripping_penalties"
PLAYER_ROUGHING_PENALTIES_COLUMN: Literal["roughing_penalties"] = "roughing_penalties"
PLAYER_HOLDING_PENALTIES_COLUMN: Literal["holding_penalties"] = "holding_penalties"
PLAYER_INTERFERENCE_PENALTIES_COLUMN: Literal["interference_penalties"] = (
    "interference_penalties"
)
PLAYER_SLASHING_PENALTIES_COLUMN: Literal["slashing_penalties"] = "slashing_penalties"
PLAYER_HIGH_STICKING_PENALTIES_COLUMN: Literal["high_sticking_penalties"] = (
    "high_sticking_penalties"
)
PLAYER_CROSS_CHECKING_PENALTIES_COLUMN: Literal["cross_checking_penalties"] = (
    "cross_checking_penalties"
)
PLAYER_STICK_HOLDING_PENALTIES_COLUMN: Literal["stick_holding_penalties"] = (
    "stick_holding_penalties"
)
PLAYER_GOALIE_INTERFERENCE_PENALTIES_COLUMN: Literal[
    "goalie_interference_penalties"
] = "goalie_interference_penalties"
PLAYER_ELBOWING_PENALTIES_COLUMN: Literal["elbowing_penalties"] = "elbowing_penalties"
PLAYER_DIVING_PENALTIES_COLUMN: Literal["diving_penalties"] = "diving_penalties"
PLAYER_TAKEAWAYS_COLUMN: Literal["takeaways"] = "takeaways"
PLAYER_EVEN_STRENGTH_SAVES_COLUMN: Literal["even_strength_saves"] = (
    "even_strength_saves"
)
PLAYER_POWER_PLAY_SAVES_COLUMN: Literal["power_play_saves"] = "power_play_saves"
PLAYER_SHORT_HANDED_SAVES_COLUMN: Literal["short_handed_saves"] = "short_handed_saves"
PLAYER_GAMES_COLUMN: Literal["games"] = "games"
PLAYER_GAME_STARTED_COLUMN: Literal["game_started"] = "game_started"
PLAYER_TIES_COLUMN: Literal["ties"] = "ties"
PLAYER_TIME_ON_ICE_PER_GAME_COLUMN: Literal["time_on_ice_per_game"] = (
    "time_on_ice_per_game"
)
PLAYER_POWER_PLAY_TIME_ON_ICE_COLUMN: Literal["power_play_time_on_ice"] = (
    "power_play_time_on_ice"
)
PLAYER_SHORT_HANDED_TIME_ON_ICE_COLUMN: Literal["short_handed_time_on_ice"] = (
    "short_handed_time_on_ice"
)
PLAYER_EVEN_STRENGTH_TIME_ON_ICE_COLUMN: Literal["even_strength_time_on_ice"] = (
    "even_strength_time_on_ice"
)
PLAYER_SHIFTS_PER_GAME_COLUMN: Literal["shifts_per_game"] = "shifts_per_game"
PLAYER_PRODUCTION_COLUMN: Literal["production"] = "production"
PLAYER_SHOT_DIFFERENTIAL_COLUMN: Literal["shot_differential"] = "shot_differential"
PLAYER_GOAL_DIFFERENTIAL_COLUMN: Literal["goal_differential"] = "goal_differential"
PLAYER_PIM_DIFFERENTIAL_COLUMN: Literal["pim_differential"] = "pim_differential"
PLAYER_RATING_COLUMN: Literal["rating"] = "rating"
PLAYER_AVERAGE_GOALS_COLUMN: Literal["average_goals"] = "average_goals"
PLAYER_YTD_GOALS_COLUMN: Literal["ytd_goals"] = "ytd_goals"
PLAYER_SHOTS_IN_FIRST_PERIOD_COLUMN: Literal["shots_in_first_period"] = (
    "shots_in_first_period"
)
PLAYER_SHOTS_IN_SECOND_PERIOD_COLUMN: Literal["shots_in_second_period"] = (
    "shots_in_second_period"
)
PLAYER_SHOTS_IN_THIRD_PERIOD_COLUMN: Literal["shots_in_third_period"] = (
    "shots_in_third_period"
)
PLAYER_SHOTS_OVERTIME_COLUMN: Literal["shots_overtime"] = "shots_overtime"
PLAYER_SHOTS_MISSED_COLUMN: Literal["shots_missed"] = "shots_missed"
PLAYER_AVERAGE_SHOTS_COLUMN: Literal["average_shots"] = "average_shots"
PLAYER_POINTS_PER_GAME_COLUMN: Literal["points_per_game"] = "points_per_game"
PLAYER_POWER_PLAY_OPPORTUNITIES_COLUMN: Literal["power_play_opportunities"] = (
    "power_play_opportunities"
)
PLAYER_POWER_PLAY_PERCENTAGE_COLUMN: Literal["power_play_percentage"] = (
    "power_play_percentage"
)
PLAYER_SHOOTOUT_ATTEMPTS_COLUMN: Literal["shootout_attempts"] = "shootout_attempts"
PLAYER_SHOOTOUT_SHOT_PERCENTAGE_COLUMN: Literal["shootout_shot_percentage"] = (
    "shootout_shot_percentage"
)
PLAYER_EMPTY_NET_GOALS_FOR_COLUMN: Literal["empty_net_goals_for"] = (
    "empty_net_goals_for"
)
PLAYER_SHUTOUTS_AGAINST_COLUMN: Literal["shutouts_against"] = "shutouts_against"
PLAYER_TOTAL_FACE_OFFS_COLUMN: Literal["total_face_offs"] = "total_face_offs"
PLAYER_AVERAGE_GOALS_AGAINST_COLUMN: Literal["average_goals_against"] = (
    "average_goals_against"
)
PLAYER_AVERAGE_SHOTS_AGAINST_COLUMN: Literal["average_shots_against"] = (
    "average_shots_against"
)
PLAYER_PENALTY_KILL_PERCENTAGE_COLUMN: Literal["penalty_kill_percentage"] = (
    "penalty_kill_percentage"
)
PLAYER_POWER_PLAY_GOALS_AGAINST_COLUMN: Literal["power_play_goals_against"] = (
    "power_play_goals_against"
)
PLAYER_SHORT_HANDED_GOALS_AGAINST_COLUMN: Literal["short_handed_goals_against"] = (
    "short_handed_goals_against"
)
PLAYER_SHOOTOUT_SAVES_COLUMN: Literal["shootout_saves"] = "shootout_saves"
PLAYER_SHOOTOUT_SHOTS_AGAINST_COLUMN: Literal["shootout_shots_against"] = (
    "shootout_shots_against"
)
PLAYER_TIMES_SHORT_HANDED_COLUMN: Literal["times_short_handed"] = "times_short_handed"
PLAYER_EMPTY_NET_GOALS_AGAINST_COLUMN: Literal["empty_net_goals_against"] = (
    "empty_net_goals_against"
)
PLAYER_OVERTIME_LOSSES_COLUMN: Literal["overtime_losses"] = "overtime_losses"
PLAYER_NET_PASSING_YARDS_PER_GAME_COLUMN: Literal["net_passing_yards_per_game"] = (
    "net_passing_yards_per_game"
)
PLAYER_NET_YARDS_PER_GAME_COLUMN: Literal["net_yards_per_game"] = "net_yards_per_game"
PLAYER_PASSING_YARDS_PER_GAME_COLUMN: Literal["passing_yards_per_game"] = (
    "passing_yards_per_game"
)
PLAYER_TOTAL_POINTS_PER_GAME_COLUMN: Literal["total_points_per_game"] = (
    "total_points_per_game"
)
PLAYER_YARDS_FROM_SCRIMMAGE_PER_GAME_COLUMN: Literal[
    "yards_from_scrimmage_per_game"
] = "yards_from_scrimmage_per_game"
PLAYER_YARDS_PER_GAME_COLUMN: Literal["yards_per_game"] = "yards_per_game"
PLAYER_ESPN_RB_RATING_COLUMN: Literal["espn_rb_rating"] = "espn_rb_rating"
PLAYER_RUSHING_YARDS_PER_GAME_COLUMN: Literal["rushing_yards_per_game"] = (
    "rushing_yards_per_game"
)
PLAYER_RECEIVING_YARDS_PER_GAME_COLUMN: Literal["receiving_yards_per_game"] = (
    "receiving_yards_per_game"
)
PLAYER_TWO_POINT_RETURNS_COLUMN: Literal["two_point_returns"] = "two_point_returns"
PLAYER_FIELD_GOAL_ATTEMPTS_COLUMN: Literal["field_goal_attempts"] = (
    "field_goal_attempts"
)
PLAYER_KICK_EXTRA_POINTS_COLUMN: Literal["kick_extra_points"] = "kick_extra_points"
PLAYER_KICK_EXTRA_POINTS_MADE_COLUMN: Literal["kick_extra_points_made"] = (
    "kick_extra_points_made"
)
PLAYER_ATTEMPTS_IN_BOX_COLUMN: Literal["attempts_in_box"] = "attempts_in_box"
PLAYER_SECOND_ASSISTS_COLUMN: Literal["second_assists"] = "second_assists"
PLAYER_QBR_COLUMN: Literal["qbr"] = "qbr"
PLAYER_ATTEMPTS_OUT_BOX_COLUMN: Literal["attempts_out_box"] = "attempts_out_box"
PLAYER_ADJUSTED_QBR_COLUMN: Literal["adjusted_qbr"] = "adjusted_qbr"
PLAYER_TURNOVER_POINTS_COLUMN: Literal["turnover_points"] = "turnover_points"
PLAYER_FANTASY_RATING_COLUMN: Literal["fantasy_rating"] = "fantasy_rating"
PLAYER_TEAM_TURNOVERS_COLUMN: Literal["team_turnovers"] = "team_turnovers"
PLAYER_SECOND_CHANCE_POINTS_COLUMN: Literal["second_chance_points"] = (
    "second_chance_points"
)
PLAYER_FAST_BREAK_POINTS_COLUMN: Literal["fast_break_points"] = "fast_break_points"
PLAYER_TEAM_REBOUNDS_COLUMN: Literal["team_rebounds"] = "team_rebounds"
PLAYER_GAINED_COLUMN: Literal["gained"] = "gained"
VERSION = DELIMITER.join(["0.0.16", ADDRESS_VERSION, OWNER_VERSION, VENUE_VERSION])


def _guess_sex(data: dict[str, Any]) -> str | None:
    name = data[PLAYER_NAME_COLUMN]
    gender_tag = GENDER_DETECTOR.get_gender(name)
    if gender_tag in MALE_GENDERS:
        return str(Sex.MALE)
    if gender_tag in FEMALE_GENDERS:
        return str(Sex.FEMALE)
    if gender_tag in UNCERTAIN_GENDERS:
        return None
    return None


def _calculate_field_goals_percentage(data: dict[str, Any]) -> float | None:
    field_goals = data.get(FIELD_GOALS_COLUMN)
    if field_goals is None:
        return None
    field_goals_attempted = data.get(FIELD_GOALS_ATTEMPTED_COLUMN)
    if field_goals_attempted is None:
        return None
    if field_goals_attempted == 0:
        return 0.0
    return float(field_goals) / float(field_goals_attempted)  # type: ignore


def _calculate_three_point_field_goals_percentage(data: dict[str, Any]) -> float | None:
    three_point_field_goals = data.get(PLAYER_THREE_POINT_FIELD_GOALS_COLUMN)
    if three_point_field_goals is None:
        return None
    three_point_field_goals_attempted = data.get(
        PLAYER_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN
    )
    if three_point_field_goals_attempted is None:
        return None
    if three_point_field_goals_attempted == 0:
        return 0.0
    return float(three_point_field_goals) / float(three_point_field_goals_attempted)  # type: ignore


def _calculate_free_throws_percentage(data: dict[str, Any]) -> float | None:
    free_throws = data.get(PLAYER_FREE_THROWS_COLUMN)
    if free_throws is None:
        return None
    free_throws_attempted = data.get(PLAYER_FREE_THROWS_ATTEMPTED_COLUMN)
    if free_throws_attempted is None:
        return None
    if free_throws_attempted == 0:
        return 0.0
    return float(free_throws) / float(free_throws_attempted)  # type: ignore


def _calculate_total_rebounds(data: dict[str, Any]) -> int | None:
    offensive_rebounds = data.get(OFFENSIVE_REBOUNDS_COLUMN)
    if offensive_rebounds is None:
        return None
    defensive_rebounds = data.get(PLAYER_DEFENSIVE_REBOUNDS_COLUMN)
    if defensive_rebounds:
        return None
    return offensive_rebounds + defensive_rebounds


class PlayerModel(BaseModel):
    """The serialisable player class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    identifier: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=PLAYER_IDENTIFIER_COLUMN,
    )
    jersey: str | None = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
    kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKS_COLUMN,
    )
    fumbles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLES_COLUMN,
    )
    fumbles_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLES_LOST_COLUMN,
    )
    field_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=FIELD_GOALS_COLUMN,
    )
    field_goals_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    offensive_rebounds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=OFFENSIVE_REBOUNDS_COLUMN,
    )
    assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ASSISTS_COLUMN,
    )
    turnovers: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=TURNOVERS_COLUMN,
    )
    name: str = Field(..., alias=PLAYER_NAME_COLUMN)
    marks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MARKS_COLUMN,
    )
    handballs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HANDBALLS_COLUMN,
    )
    disposals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DISPOSALS_COLUMN,
    )
    goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOALS_COLUMN,
    )
    behinds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BEHINDS_COLUMN,
    )
    hit_outs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HIT_OUTS_COLUMN,
    )
    tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_COLUMN,
    )
    rebounds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_REBOUNDS_COLUMN,
    )
    insides: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INSIDES_COLUMN,
    )
    clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CLEARANCES_COLUMN,
    )
    clangers: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CLANGERS_COLUMN,
    )
    free_kicks_for: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_KICKS_FOR_COLUMN,
    )
    free_kicks_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_KICKS_AGAINST_COLUMN,
    )
    brownlow_votes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BROWNLOW_VOTES_COLUMN,
    )
    contested_possessions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CONTESTED_POSSESSIONS_COLUMN,
    )
    uncontested_possessions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNCONTESTED_POSSESSIONS_COLUMN,
    )
    contested_marks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CONTESTED_MARKS_COLUMN,
    )
    marks_inside: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MARKS_INSIDE_COLUMN,
    )
    one_percenters: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ONE_PERCENTERS_COLUMN,
    )
    bounces: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BOUNCES_COLUMN,
    )
    goal_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOAL_ASSISTS_COLUMN,
    )
    percentage_played: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERCENTAGE_PLAYED_COLUMN,
    )
    birth_date: datetime.date | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_BIRTH_DATE_COLUMN
    )
    species: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL, FFILL_KEY: True},
        alias=PLAYER_SPECIES_COLUMN,
    )
    handicap_weight: float | None = Field(..., alias=PLAYER_HANDICAP_WEIGHT_COLUMN)
    father: PlayerModel | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_FATHER_COLUMN
    )
    sex: str | None = Field(
        default_factory=_guess_sex,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL, FFILL_KEY: True},
        alias=PLAYER_SEX_COLUMN,
    )
    age: int | None = Field(..., alias=PLAYER_AGE_COLUMN)
    starting_position: str | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=PLAYER_STARTING_POSITION_COLUMN,
    )
    weight: float | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_WEIGHT_COLUMN
    )
    birth_address: AddressModel | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_BIRTH_ADDRESS_COLUMN
    )
    owner: OwnerModel | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_OWNER_COLUMN
    )
    seconds_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECONDS_PLAYED_COLUMN,
    )
    field_goals_percentage: float | None = Field(
        default_factory=_calculate_field_goals_percentage,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_PERCENTAGE_COLUMN,
    )
    three_point_field_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_FIELD_GOALS_COLUMN,
    )
    three_point_field_goals_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    three_point_field_goals_percentage: float | None = Field(
        default_factory=_calculate_three_point_field_goals_percentage,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_FIELD_GOALS_PERCENTAGE_COLUMN,
    )
    free_throws: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_THROWS_COLUMN,
    )
    free_throws_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_THROWS_ATTEMPTED_COLUMN,
    )
    free_throws_percentage: float | None = Field(
        default_factory=_calculate_free_throws_percentage,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_THROWS_PERCENTAGE_COLUMN,
    )
    defensive_rebounds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_REBOUNDS_COLUMN,
    )
    total_rebounds: int | None = Field(
        default_factory=_calculate_total_rebounds,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_REBOUNDS_COLUMN,
    )
    steals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STEALS_COLUMN,
    )
    blocks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOCKS_COLUMN,
    )
    personal_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERSONAL_FOULS_COLUMN,
    )
    points: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINTS_COLUMN,
    )
    game_score: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_SCORE_COLUMN,
    )
    point_differential: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINT_DIFFERENTIAL_COLUMN,
    )
    version: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
    height: float | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_HEIGHT_COLUMN
    )
    colleges: list[VenueModel] = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=PLAYER_COLLEGES_COLUMN
    )
    headshot: str | None = Field(
        ...,
        json_schema_extra={FFILL_KEY: True, TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HEADSHOT_COLUMN,
    )
    forced_fumbles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FORCED_FUMBLES_COLUMN,
    )
    fumbles_recovered: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLES_RECOVERED_COLUMN,
    )
    fumbles_recovered_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLES_RECOVERED_YARDS_COLUMN,
    )
    fumbles_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLES_TOUCHDOWNS_COLUMN,
    )
    offensive_two_point_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_TWO_POINT_RETURNS_COLUMN,
    )
    offensive_fumbles_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN,
    )
    defensive_fumbles_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_FUMBLES_TOUCHDOWNS_COLUMN,
    )
    average_gain: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_GAIN_COLUMN,
    )
    completion_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_COMPLETION_PERCENTAGE_COLUMN,
    )
    completions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_COMPLETIONS_COLUMN,
    )
    espn_quarterback_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ESPN_QUARTERBACK_RATING_COLUMN,
    )
    interception_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INTERCEPTION_PERCENTAGE_COLUMN,
    )
    interceptions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INTERCEPTIONS_COLUMN,
    )
    long_passing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_PASSING_COLUMN,
    )
    misc_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISC_YARDS_COLUMN,
    )
    net_passing_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_PASSING_YARDS_COLUMN,
    )
    net_total_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_TOTAL_YARDS_COLUMN,
    )
    passing_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_ATTEMPTS_COLUMN,
    )
    passing_big_plays: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_BIG_PLAYS_COLUMN,
    )
    passing_first_downs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_FIRST_DOWNS_COLUMN,
    )
    passing_fumbles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_FUMBLES_COLUMN,
    )
    passing_fumbles_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_FUMBLES_LOST_COLUMN,
    )
    passing_touchdown_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWN_PERCENTAGE_COLUMN,
    )
    passing_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_COLUMN,
    )
    passing_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_YARDS_COLUMN,
    )
    passing_yards_after_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_YARDS_AFTER_CATCH_COLUMN,
    )
    passing_yards_at_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_YARDS_AT_CATCH_COLUMN,
    )
    quarterback_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_QUARTERBACK_RATING_COLUMN,
    )
    sacks: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SACKS_COLUMN,
    )
    sacks_yards_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SACKS_YARDS_LOST_COLUMN,
    )
    net_passing_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_PASSING_ATTEMPTS_COLUMN,
    )
    total_offensive_plays: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_OFFENSIVE_PLAYS_COLUMN,
    )
    total_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_POINTS_COLUMN,
    )
    total_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_TOUCHDOWNS_COLUMN,
    )
    total_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_YARDS_COLUMN,
    )
    total_yards_from_scrimmage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_YARDS_FROM_SCRIMMAGE_COLUMN,
    )
    two_point_pass: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_PASS_COLUMN,
    )
    two_point_pass_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_PASS_ATTEMPT_COLUMN,
    )
    yards_per_completion: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_COMPLETION_COLUMN,
    )
    yards_per_pass_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_PASS_ATTEMPT_COLUMN,
    )
    net_yards_per_pass_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_YARDS_PER_PASS_ATTEMPT_COLUMN,
    )
    long_rushing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_RUSHING_COLUMN,
    )
    rushing_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_ATTEMPTS_COLUMN,
    )
    rushing_big_plays: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_BIG_PLAYS_COLUMN,
    )
    rushing_first_downs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_FIRST_DOWNS_COLUMN,
    )
    rushing_fumbles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_FUMBLES_COLUMN,
    )
    rushing_fumbles_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_FUMBLES_LOST_COLUMN,
    )
    rushing_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_COLUMN,
    )
    rushing_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_YARDS_COLUMN,
    )
    stuffs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STUFFS_COLUMN,
    )
    stuff_yards_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STUFF_YARDS_LOST,
    )
    two_point_rush: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_RUSH_COLUMN,
    )
    two_point_rush_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_RUSH_ATTEMPTS_COLUMN,
    )
    yards_per_rush_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_RUSH_ATTEMPT_COLUMN,
    )
    espn_widereceiver: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ESPN_WIDERECEIVER_COLUMN,
    )
    long_reception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_RECEPTION_COLUMN,
    )
    receiving_big_plays: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_BIG_PLAYS_COLUMN,
    )
    receiving_first_downs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_FIRST_DOWNS_COLUMN,
    )
    receiving_fumbles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_FUMBLES_COLUMN,
    )
    receiving_fumbles_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_FUMBLES_LOST_COLUMN,
    )
    receiving_targets: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TARGETS_COLUMN,
    )
    receiving_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_COLUMN,
    )
    receiving_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_YARDS_COLUMN,
    )
    receiving_yards_after_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_YARDS_AFTER_CATCH_COLUMN,
    )
    receiving_yards_at_catch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_YARDS_AT_CATCH_COLUMN,
    )
    receptions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEPTIONS_COLUMN,
    )
    two_point_receptions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_RECEPTIONS_COLUMN,
    )
    two_point_reception_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_RECEPTION_ATTEMPTS_COLUMN,
    )
    yards_per_reception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_RECEPTION_COLUMN,
    )
    assist_tackles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ASSIST_TACKLES_COLUMN,
    )
    average_interception_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_INTERCEPTION_YARDS_COLUMN,
    )
    average_sack_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_SACK_YARDS_COLUMN,
    )
    average_stuff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_STUFF_YARDS_COLUMN,
    )
    blocked_field_goal_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOCKED_FIELD_GOAL_TOUCHDOWNS_COLUMN,
    )
    blocked_punt_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOCKED_PUNT_TOUCHDOWNS_COLUMN,
    )
    defensive_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_TOUCHDOWNS_COLUMN,
    )
    hurries: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HURRIES_COLUMN,
    )
    kicks_blocked: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKS_BLOCKED_COLUMN,
    )
    long_interception: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_INTERCEPTION_COLUMN,
    )
    misc_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISC_TOUCHDOWNS_COLUMN,
    )
    passes_batted_down: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_BATTED_DOWN_COLUMN,
    )
    passes_defended: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_DEFENDED_COLUMN,
    )
    quarterback_hits: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_QUARTERBACK_HITS_COLUMN,
    )
    sacks_assisted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SACKS_ASSISTED_COLUMN,
    )
    sacks_unassisted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SACKS_UNASSISTED_COLUMN,
    )
    sacks_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SACKS_YARDS_COLUMN,
    )
    safeties: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAFETIES_COLUMN,
    )
    solo_tackles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SOLO_TACKLES_COLUMN,
    )
    stuff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STUFF_YARDS_COLUMN,
    )
    tackles_for_loss: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_FOR_LOSS_COLUMN,
    )
    tackles_yards_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_YARDS_LOST_COLUMN,
    )
    yards_allowed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_ALLOWED_COLUMN,
    )
    points_allowed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINTS_ALLOWED_COLUMN,
    )
    one_point_safeties_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ONE_POINT_SAFETIES_MADE_COLUMN,
    )
    missed_field_goal_return_td: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISSED_FIELD_GOAL_RETURN_TD_COLUMN,
    )
    blocked_punt_ez_rec_td: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOCKED_PUNT_EZ_REC_TD_COLUMN,
    )
    interception_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INTERCEPTION_TOUCHDOWNS_COLUMN,
    )
    interception_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INTERCEPTION_YARDS_COLUMN,
    )
    average_kickoff_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_KICKOFF_RETURN_YARDS_COLUMN,
    )
    average_kickoff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_KICKOFF_YARDS_COLUMN,
    )
    extra_point_attempts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_POINT_ATTEMPTS_COLUMN,
    )
    extra_point_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_POINT_PERCENTAGE_COLUMN,
    )
    extra_point_blocked: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_POINT_BLOCKED_COLUMN,
    )
    extra_points_blocked_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_POINTS_BLOCKED_PERCENTAGE_COLUMN,
    )
    extra_points_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_POINTS_MADE_COLUMN,
    )
    fair_catches: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FAIR_CATCHES_COLUMN,
    )
    fair_catch_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FAIR_CATCH_PERCENTAGE_COLUMN,
    )
    field_goal_attempts_max_19_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_MAX_19_YARDS_COLUMN,
    )
    field_goal_attempts_max_29_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_MAX_29_YARDS_COLUMN,
    )
    field_goal_attempts_max_39_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_MAX_39_YARDS_COLUMN,
    )
    field_goal_attempts_max_49_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_MAX_49_YARDS_COLUMN,
    )
    field_goal_attempts_max_59_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_MAX_59_YARDS_COLUMN,
    )
    field_goal_attempts_max_99_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_MAX_99_YARDS_COLUMN,
    )
    field_goal_attempts_above_50_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_ABOVE_50_YARDS_COLUMN,
    )
    field_goal_attempt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPT_YARDS_COLUMN,
    )
    field_goals_blocked: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_BLOCKED_COLUMN,
    )
    field_goals_blocked_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_BLOCKED_PERCENTAGE_COLUMN,
    )
    field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_COLUMN,
    )
    field_goals_made_max_19_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_MAX_19_YARDS_COLUMN,
    )
    field_goals_made_max_29_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_MAX_29_YARDS_COLUMN,
    )
    field_goals_made_max_39_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_MAX_39_YARDS_COLUMN,
    )
    field_goals_made_max_49_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_MAX_49_YARDS_COLUMN,
    )
    field_goals_made_max_59_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_MAX_59_YARDS_COLUMN,
    )
    field_goals_made_max_99_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_MAX_99_YARDS_COLUMN,
    )
    field_goals_made_above_50_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_ABOVE_50_YARDS_COLUMN,
    )
    field_goals_made_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MADE_YARDS_COLUMN,
    )
    field_goals_missed_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOALS_MISSED_YARDS_COLUMN,
    )
    kickoff_out_of_bounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKOFF_OUT_OF_BOUNDS_COLUMN,
    )
    kickoff_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKOFF_RETURNS_COLUMN,
    )
    kickoff_returns_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKOFF_RETURNS_TOUCHDOWNS_COLUMN,
    )
    kickoff_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKOFF_RETURN_YARDS_COLUMN,
    )
    kickoffs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKOFFS_COLUMN,
    )
    kickoff_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICKOFF_YARDS_COLUMN,
    )
    long_field_goal_attempt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_FIELD_GOAL_ATTEMPT_COLUMN,
    )
    long_field_goal_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_FIELD_GOAL_MADE_COLUMN,
    )
    long_kickoff: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_KICKOFF_COLUMN,
    )
    total_kicking_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_KICKING_POINTS_COLUMN,
    )
    touchback_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHBACK_PERCENTAGE_COLUMN,
    )
    touchbacks: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHBACKS_COLUMN,
    )
    defensive_fumble_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_FUMBLE_RETURNS_COLUMN,
    )
    defensive_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_FUMBLE_RETURN_YARDS_COLUMN,
    )
    fumble_recoveries: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLE_RECOVERIES_COLUMN,
    )
    fumble_recovery_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FUMBLE_RECOVERY_YARDS_COLUMN,
    )
    kick_return_fair_catches: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURN_FAIR_CATCHES_COLUMN,
    )
    kick_return_fair_catch_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN,
    )
    kick_return_fumbles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURN_FUMBLES_COLUMN,
    )
    kick_return_fumbles_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURN_FUMBLES_LOST_COLUMN,
    )
    kick_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURNS_COLUMN,
    )
    kick_return_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURN_TOUCHDOWNS_COLUMN,
    )
    kick_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_RETURN_YARDS_COLUMN,
    )
    long_kick_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_KICK_RETURN_COLUMN,
    )
    long_punt_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_PUNT_RETURN_COLUMN,
    )
    misc_fumble_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISC_FUMBLE_RETURNS_COLUMN,
    )
    misc_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISC_FUMBLE_RETURN_YARDS_COLUMN,
    )
    opposition_fumble_recoveries: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPOSITION_FUMBLE_RECOVERIES_COLUMN,
    )
    opposition_fumble_recovery_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPOSITION_FUMBLE_RECOVERY_YARDS_COLUMN,
    )
    opposition_special_team_fumble_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPOSITION_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN,
    )
    opposition_special_team_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPOSITION_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN,
    )
    punt_return_fair_catches: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURN_FAIR_CATCHES_COLUMN,
    )
    punt_return_fair_catch_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURN_FAIR_CATCH_PERCENTAGE_COLUMN,
    )
    punt_return_fumbles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURN_FUMBLES_COLUMN,
    )
    punt_return_fumbles_lost: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURN_FUMBLES_LOST_COLUMN,
    )
    punt_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURNS_COLUMN,
    )
    punt_returns_started_inside_the_10: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURNS_STARTED_INSIDE_THE_10_COLUMN,
    )
    punt_returns_started_inside_the_20: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURNS_STARTED_INSIDE_THE_20_COLUMN,
    )
    punt_return_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURN_TOUCHDOWNS_COLUMN,
    )
    punt_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_RETURN_YARDS_COLUMN,
    )
    special_team_fumble_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SPECIAL_TEAM_FUMBLE_RETURNS_COLUMN,
    )
    yards_per_kick_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_KICK_RETURN_COLUMN,
    )
    yards_per_punt_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_PUNT_RETURN_COLUMN,
    )
    yards_per_return: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_RETURN_COLUMN,
    )
    average_punt_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_PUNT_RETURN_YARDS_COLUMN,
    )
    gross_average_punt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GROSS_AVERAGE_PUNT_YARDS_COLUMN,
    )
    long_punt: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_PUNT_COLUMN,
    )
    net_average_punt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_AVERAGE_PUNT_YARDS_COLUMN,
    )
    punts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_COLUMN,
    )
    punts_blocked: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_BLOCKED_COLUMN,
    )
    punts_blocked_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_BLOCKED_PERCENTAGE_COLUMN,
    )
    punts_inside_10: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_INSIDE_10_COLUMN,
    )
    punts_inside_10_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_INSIDE_10_PERCENTAGE_COLUMN,
    )
    punts_inside_20: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_INSIDE_20_COLUMN,
    )
    punts_inside_20_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_INSIDE_20_PERCENTAGE_COLUMN,
    )
    punts_over_50: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNTS_OVER_50_COLUMN,
    )
    punt_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNT_YARDS_COLUMN,
    )
    defensive_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_POINTS_COLUMN,
    )
    misc_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISC_POINTS_COLUMN,
    )
    return_touchdowns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RETURN_TOUCHDOWNS_COLUMN,
    )
    total_two_point_conversions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_TWO_POINT_CONVERSIONS_COLUMN,
    )
    passing_touchdowns_9_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_9_YARDS_COLUMN,
    )
    passing_touchdowns_19_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_19_YARDS_COLUMN,
    )
    passing_touchdowns_29_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_29_YARDS_COLUMN,
    )
    passing_touchdowns_39_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_39_YARDS_COLUMN,
    )
    passing_touchdowns_49_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_49_YARDS_COLUMN,
    )
    passing_touchdowns_above_50_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_TOUCHDOWNS_ABOVE_50_YARDS_COLUMN,
    )
    receiving_touchdowns_9_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_9_YARDS_COLUMN,
    )
    receiving_touchdowns_19_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_19_YARDS_COLUMN,
    )
    receiving_touchdowns_29_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_29_YARDS_COLUMN,
    )
    receiving_touchdowns_39_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_39_YARDS_COLUMN,
    )
    receiving_touchdowns_49_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_49_YARDS_COLUMN,
    )
    receiving_touchdowns_above_50_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_TOUCHDOWNS_ABOVE_50_YARDS_COLUMN,
    )
    rushing_touchdowns_9_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_9_YARDS_COLUMN,
    )
    rushing_touchdowns_19_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_19_YARDS_COLUMN,
    )
    rushing_touchdowns_29_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_29_YARDS_COLUMN,
    )
    rushing_touchdowns_39_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_39_YARDS_COLUMN,
    )
    rushing_touchdowns_49_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_49_YARDS_COLUMN,
    )
    rushing_touchdowns_above_50_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_TOUCHDOWNS_ABOVE_50_YARDS_COLUMN,
    )
    penalties_in_minutes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTIES_IN_MINUTES_COLUMN,
    )
    even_strength_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EVEN_STRENGTH_GOALS_COLUMN,
    )
    power_play_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_GOALS_COLUMN,
    )
    short_handed_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHORT_HANDED_GOALS_COLUMN,
    )
    game_winning_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_WINNING_GOALS_COLUMN,
    )
    even_strength_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EVEN_STRENGTH_ASSISTS_COLUMN,
    )
    power_play_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_ASSISTS_COLUMN,
    )
    short_handed_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHORT_HANDED_ASSISTS_COLUMN,
    )
    shots_on_goal: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_ON_GOAL_COLUMN,
    )
    shooting_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOTING_PERCENTAGE_COLUMN,
    )
    shifts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHIFTS_COLUMN,
    )
    time_on_ice: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIME_ON_ICE_COLUMN,
    )
    decision: str | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DECISION_COLUMN,
    )
    goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOALS_AGAINST_COLUMN,
    )
    shots_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_AGAINST_COLUMN,
    )
    saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAVES_COLUMN,
    )
    save_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAVE_PERCENTAGE_COLUMN,
    )
    shutouts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHUTOUTS_COLUMN,
    )
    individual_corsi_for_events: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INDIVIDUAL_CORSI_FOR_EVENTS_COLUMN,
    )
    on_shot_ice_for_events: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ON_SHOT_ICE_FOR_EVENTS_COLUMN,
    )
    on_shot_ice_against_events: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ON_SHOT_ICE_AGAINST_EVENTS_COLUMN,
    )
    corsi_for_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CORSI_FOR_PERCENTAGE_COLUMN,
    )
    relative_corsi_for_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RELATIVE_CORSI_FOR_PERCENTAGE_COLUMN,
    )
    offensive_zone_starts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_ZONE_STARTS_COLUMN,
    )
    defensive_zone_starts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_ZONE_STARTS_COLUMN,
    )
    offensive_zone_start_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_ZONE_START_PERCENTAGE_COLUMN,
    )
    hits: int | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD}, alias=PLAYER_HITS_COLUMN
    )
    true_shooting_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TRUE_SHOOTING_PERCENTAGE_COLUMN,
    )
    at_bats: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AT_BATS_COLUMN,
    )
    runs_scored: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_SCORED_COLUMN,
    )
    runs_batted_in: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_BATTED_IN_COLUMN,
    )
    bases_on_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BASES_ON_BALLS_COLUMN,
    )
    strikeouts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKEOUTS_COLUMN,
    )
    plate_appearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PLATE_APPEARANCES_COLUMN,
    )
    hits_at_bats: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HITS_AT_BATS_COLUMN,
    )
    obp: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OBP_COLUMN,
    )
    slg: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SLG_COLUMN,
    )
    ops: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPS_COLUMN,
    )
    pitches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PITCHES_COLUMN,
    )
    strikes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKES_COLUMN,
    )
    win_probability_added: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WIN_PROBABILITY_ADDED_COLUMN,
    )
    average_leverage_index: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_LEVERAGE_INDEX_COLUMN,
    )
    wpa_plus: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WPA_PLUS_COLUMN,
    )
    wpa_minus: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WPA_MINUS_COLUMN,
    )
    cwpa: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CWPA_COLUMN,
    )
    acli: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ACLI_COLUMN,
    )
    re24: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RE24_COLUMN,
    )
    putouts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUTOUTS_COLUMN,
    )
    innings_pitched: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INNINGS_PITCHED_COLUMN,
    )
    earned_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EARNED_RUNS_COLUMN,
    )
    home_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HOME_RUNS_COLUMN,
    )
    era: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ERA_COLUMN,
    )
    batters_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BATTERS_FACED_COLUMN,
    )
    strikes_by_contact: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKES_BY_CONTACT_COLUMN,
    )
    strikes_swinging: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKES_SWINGING_COLUMN,
    )
    strikes_looking: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKES_LOOKING_COLUMN,
    )
    ground_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GROUND_BALLS_COLUMN,
    )
    fly_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FLY_BALLS_COLUMN,
    )
    line_drives: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LINE_DRIVES_COLUMN,
    )
    inherited_runners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INHERITED_RUNNERS_COLUMN,
    )
    inherited_scores: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INHERITED_SCORES_COLUMN,
    )
    effective_field_goal_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EFFECTIVE_FIELD_GOAL_PERCENTAGE_COLUMN,
    )
    penalty_kicks_made: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_MADE_COLUMN,
    )
    penalty_kicks_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_ATTEMPTED_COLUMN,
    )
    shots_total: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_TOTAL_COLUMN,
    )
    shots_on_target: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_ON_TARGET_COLUMN,
    )
    yellow_cards: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YELLOW_CARDS_COLUMN,
    )
    red_cards: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RED_CARDS_COLUMN,
    )
    touches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHES_COLUMN,
    )
    expected_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXPECTED_GOALS_COLUMN,
    )
    non_penalty_expected_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NON_PENALTY_EXPECTED_GOALS_COLUMN,
    )
    expected_assisted_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXPECTED_ASSISTED_GOALS_COLUMN,
    )
    shot_creating_actions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOT_CREATING_ACTIONS_COLUMN,
    )
    goal_creating_actions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOAL_CREATING_ACTIONS_COLUMN,
    )
    passes_completed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_COMPLETED_COLUMN,
    )
    passes_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_ATTEMPTED_COLUMN,
    )
    pass_completion: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASS_COMPLETION_COLUMN,
    )
    progressive_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PROGRESSIVE_PASSES_COLUMN,
    )
    carries: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CARRIES_COLUMN,
    )
    progressive_carries: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PROGRESSIVE_CARRIES_COLUMN,
    )
    take_ons_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TAKE_ONS_ATTEMPTED_COLUMN,
    )
    successful_take_ons: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SUCCESSFUL_TAKE_ONS_COLUMN,
    )
    total_passing_distance: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_PASSING_DISTANCE_COLUMN,
    )
    progressive_passing_distance: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PROGRESSIVE_PASSING_DISTANCE_COLUMN,
    )
    passes_completed_short: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_COMPLETED_SHORT_COLUMN,
    )
    passes_attempted_short: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_ATTEMPTED_SHORT_COLUMN,
    )
    pass_completion_short: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASS_COMPLETION_SHORT_COLUMN,
    )
    passes_completed_medium: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_COMPLETED_MEDIUM_COLUMN,
    )
    passes_attempted_medium: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_ATTEMPTED_MEDIUM_COLUMN,
    )
    pass_completion_medium: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASS_COMPLETION_MEDIUM_COLUMN,
    )
    passes_completed_long: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_COMPLETED_LONG_COLUMN,
    )
    passes_attempted_long: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_ATTEMPTED_LONG_COLUMN,
    )
    pass_completion_long: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASS_COMPLETION_LONG_COLUMN,
    )
    expected_assists: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXPECTED_ASSISTS_COLUMN,
    )
    key_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KEY_PASSES_COLUMN,
    )
    passes_into_final_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_INTO_FINAL_THIRD_COLUMN,
    )
    passes_into_penalty_area: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_INTO_PENALTY_AREA_COLUMN,
    )
    crosses_into_penalty_area: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSSES_INTO_PENALTY_AREA_COLUMN,
    )
    live_ball_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LIVE_BALL_PASSES_COLUMN,
    )
    dead_ball_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEAD_BALL_PASSES_COLUMN,
    )
    passes_from_free_kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_FROM_FREE_KICKS_COLUMN,
    )
    through_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THROUGH_BALLS_COLUMN,
    )
    switches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SWITCHES_COLUNM,
    )
    crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSSES_COLUMN,
    )
    throw_ins_taken: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THROW_INS_TAKEN_COLUMN,
    )
    corner_kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CORNER_KICKS_COLUMN,
    )
    inswinging_corner_kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INSWINGING_CORNER_KICKS_COLUMN,
    )
    outswinging_corner_kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OUTSWINGING_CORNER_KICKS_COLUMN,
    )
    straight_corner_kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRAIGHT_CORNER_KICKS_COLUMN,
    )
    passes_offside: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_OFFSIDE_COLUMN,
    )
    passes_blocked: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_BLOCKED_COLUMN,
    )
    tackles_won: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_WON_COLUMN,
    )
    tackles_in_defensive_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_IN_DEFENSIVE_THIRD_COLUMN,
    )
    tackles_in_middle_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_IN_MIDDLE_THIRD_COLUMN,
    )
    tackles_in_attacking_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_IN_ATTACKING_THIRD_COLUMN,
    )
    dribblers_tackled: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DRIBBLERS_TACKLED_COLUMN,
    )
    dribbles_challenged: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DRIBBLES_CHALLENGED_COLUMN,
    )
    percent_of_dribblers_tackled: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERCENT_OF_DRIBBLERS_TACKLED_COLUMN,
    )
    challenges_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CHALLENGES_LOST_COLUMN,
    )
    shots_blocked: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_BLOCKED_COLUMN,
    )
    tackles_plus_interceptions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_PLUS_INTERCEPTIONS_COLUMN,
    )
    errors: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ERRORS_COLUMN,
    )
    touches_in_defensive_penalty_area: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHES_IN_DEFENSIVE_PENALTY_AREA_COLUMN,
    )
    touches_in_defensive_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHES_IN_DEFENSIVE_THIRD_COLUMN,
    )
    touches_in_middle_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHES_IN_MIDDLE_THIRD_COLUMN,
    )
    touches_in_attacking_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHES_IN_ATTACKING_THIRD_COLUMN,
    )
    touches_in_attacking_penalty_area: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUCHES_IN_ATTACKING_PENALTY_AREA_COLUMN,
    )
    live_ball_touches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LIVE_BALL_TOUCHES_COLUMN,
    )
    successful_take_on_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SUCCESSFUL_TAKE_ON_PERCENTAGE_COLUMN,
    )
    times_tackled_during_take_ons: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIMES_TACKLED_DURING_TAKE_ONS_COLUMN,
    )
    tackled_during_take_on_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLED_DURING_TAKE_ON_PERCENTAGE_COLUMN,
    )
    total_carrying_distance: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_CARRYING_DISTANCE_COLUMN,
    )
    progressive_carrying_distance: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PROGRESSIVE_CARRYING_DISTANCE_COLUMN,
    )
    carries_into_final_third: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CARRIES_INTO_FINAL_THIRD_COLUMN,
    )
    carries_into_penalty_area: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CARRIES_INTO_PENALTY_AREA_COLUMN,
    )
    miscontrols: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISCONTROLS_COLUMN,
    )
    dispossessed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DISPOSSESSED_COLUMN,
    )
    passes_received: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_RECEIVED_COLUMN,
    )
    progressive_passes_received: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PROGRESSIVE_PASSES_RECEIVED_COLUMN,
    )
    second_yellow_card: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECOND_YELLOW_CARD_COLUMN,
    )
    fouls_committed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FOULS_COMMITTED_COLUMN,
    )
    fouls_drawn: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FOULS_DRAWN_COLUMN,
    )
    offsides: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFSIDES_COLUMN,
    )
    penalty_kicks_won: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_WON_COLUMN,
    )
    penalty_kicks_conceded: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_CONCEDED_COLUMN,
    )
    own_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OWN_GOALS_COLUMN,
    )
    ball_recoveries: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALL_RECOVERIES_COLUMN,
    )
    aerials_won: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AERIALS_WON_COLUMN,
    )
    aerials_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AERIALS_LOST_COLUMN,
    )
    percentage_of_aerials_won: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERCENTAGE_OF_AERIALS_WON_COLUMN,
    )
    shots_on_target_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_ON_TARGET_AGAINST_COLUMN,
    )
    post_shot_expected_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POST_SHOT_EXPECTED_GOALS_COLUMN,
    )
    passes_attempted_minus_goal_kicks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSES_ATTEMPTED_MINUS_GOAL_KICKS_COLUMN,
    )
    throws_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THROWS_ATTEMPTED_COLUMN,
    )
    percentage_of_passes_that_were_launched: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERCENTAGE_OF_PASSES_THAT_WERE_LAUNCHED_COLUMN,
    )
    average_pass_length: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_PASS_LENGTH_COLUMN,
    )
    goal_kicks_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOAL_KICKS_ATTEMPTED_COLUMN,
    )
    percentage_of_goal_kicks_that_were_launched: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERCENTAGE_OF_GOAL_KICKS_THAT_WERE_LAUNCHED_COLUMN,
    )
    average_goal_kick_length: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_GOAL_KICK_LENGTH_COLUMN,
    )
    crosses_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSSES_FACED_COLUMN,
    )
    crosses_stopped: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSSES_STOPPED_COLUMN,
    )
    percentage_crosses_stopped: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERCENTAGE_CROSSES_STOPPED_COLUMN,
    )
    defensive_actions_outside_penalty_area: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_ACTIONS_OUTSIDE_PENALTY_AREA_COLUMN,
    )
    average_distance_of_defensive_actions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_DISTANCE_OF_DEFENSIVE_ACTIONS_COLUMN,
    )
    three_point_attempt_rate: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_ATTEMPT_RATE_COLUMN,
    )
    batting_style: str | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=PLAYER_BATTING_STYLE_COLUMN,
    )
    bowling_style: str | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=PLAYER_BOWLING_STYLE_COLUMN,
    )
    playing_roles: str | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=PLAYER_PLAYING_ROLES_COLUMN,
    )
    runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_COLUMN,
    )
    balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALLS_COLUMN,
    )
    fours: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FOURS_COLUMN,
    )
    sixes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SIXES_COLUMN,
    )
    strikerate: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKERATE_COLUMN,
    )
    fall_of_wicket_order: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FALL_OF_WICKET_ORDER_COLUMN,
    )
    fall_of_wicket_num: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FALL_OF_WICKET_NUM_COLUMN,
    )
    fall_of_wicket_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FALL_OF_WICKET_RUNS_COLUMN,
    )
    fall_of_wicket_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FALL_OF_WICKET_BALLS_COLUMN,
    )
    fall_of_wicket_overs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FALL_OF_WICKET_OVERS_COLUMN,
    )
    fall_of_wicket_over_number: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FALL_OF_WICKET_OVER_NUMBER_COLUMN,
    )
    ball_over_actual: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALL_OVER_ACTUAL_COLUMN,
    )
    ball_over_unique: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALL_OVER_UNIQUE_COLUMN,
    )
    ball_total_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALL_TOTAL_RUNS_COLUMN,
    )
    ball_batsman_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALL_BATSMAN_RUNS_COLUMN,
    )
    overs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OVERS_COLUMN,
    )
    maidens: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MAIDENS_COLUMN,
    )
    conceded: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CONCEDED_COLUMN,
    )
    wickets: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WICKETS_COLUMN,
    )
    economy: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ECONOMY_COLUMN,
    )
    runs_per_ball: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_PER_BALL_COLUMN,
    )
    dots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DOTS_COLUMN,
    )
    wides: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WIDES_COLUMN,
    )
    no_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NO_BALLS_COLUMN,
    )
    free_throw_attempt_rate: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_THROW_ATTEMPT_RATE_COLUMN,
    )
    offensive_rebound_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_REBOUND_PERCENTAGE_COLUMN,
    )
    defensive_rebound_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_REBOUND_PERCENTAGE_COLUMN,
    )
    total_rebound_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_REBOUND_PERCENTAGE_COLUMN,
    )
    assist_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ASSIST_PERCENTAGE_COLUMN,
    )
    steal_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STEAL_PERCENTAGE_COLUMN,
    )
    block_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOCK_PERCENTAGE_COLUMN,
    )
    turnover_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TURNOVER_PERCENTAGE_COLUMN,
    )
    usage_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_USAGE_PERCENTAGE_COLUMN,
    )
    offensive_rating: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_RATING_COLUMN,
    )
    defensive_rating: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEFENSIVE_RATING_COLUMN,
    )
    box_plus_minus: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BOX_PLUS_MINUS_COLUMN,
    )
    ace_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ACE_PERCENTAGE_COLUMN,
    )
    double_fault_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DOUBLE_FAULT_PERCENTAGE_COLUMN,
    )
    first_serves_in: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIRST_SERVES_IN_COLUMN,
    )
    first_serve_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIRST_SERVE_PERCENTAGE_COLUMN,
    )
    second_serve_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECOND_SERVE_PERCENTAGE_COLUMN,
    )
    break_points_saved: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BREAK_POINTS_SAVED_COLUMN,
    )
    return_points_won_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RETURN_POINTS_WON_PERCENTGE_COLUMN,
    )
    winners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WINNERS_COLUMN,
    )
    winners_fronthand: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WINNERS_FRONTHAND_COLUMN,
    )
    winners_backhand: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WINNERS_BACKHAND_COLUMN,
    )
    unforced_errors: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNFORCED_ERRORS_COLUMN,
    )
    unforced_errors_fronthand: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNFORCED_ERRORS_FRONTHAND_COLUMN,
    )
    unforced_errors_backhand: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNFORCED_ERRORS_BACKHAND_COLUMN,
    )
    serve_points: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVE_POINTS_COLUMN,
    )
    serves_won: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_WON_COLUMN,
    )
    serves_aces: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_ACES_COLUMN,
    )
    serves_unreturned: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_UNRETURNED_COLUMN,
    )
    serves_forced_error_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_FORCED_ERROR_PERCENTAGE_COLUMN,
    )
    serves_won_in_three_shots_or_less: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_WON_IN_THREE_SHOTS_OR_LESS_COLUMN,
    )
    serves_wide_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_WIDE_PERCENTAGE_COLUMN,
    )
    serves_body_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_BODY_PERCENTAGE_COLUMN,
    )
    serves_t_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_T_PERCENTAGE_COLUMN,
    )
    serves_wide_deuce_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_WIDE_DEUCE_PERCENTAGE_COLUMN,
    )
    serves_body_deuce_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_BODY_DEUCE_PERCENTAGE_COLUMN,
    )
    serves_t_deuce_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_T_DEUCE_PERCENTAGE_COLUMN,
    )
    serves_wide_ad_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_WIDE_AD_PERCENTAGE_COLUMN,
    )
    serves_body_ad_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_BODY_AD_PERCENTAGE_COLUMN,
    )
    serves_t_ad_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_T_AD_PERCENTAGE_COLUMN,
    )
    serves_net_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_NET_PERCENTAGE_COLUMN,
    )
    serves_wide_direction_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SERVES_WIDE_DIRECTION_PERCENTAGE_COLUMN,
    )
    shots_deep_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_DEEP_PERCENTAGE_COLUMN,
    )
    shots_deep_wide_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_DEEP_WIDE_PERCENTAGE_COLUMN,
    )
    shots_foot_errors_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_FOOT_ERRORS_PERCENTAGE_COLUMN,
    )
    shots_unknown_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_UNKNOWN_PERCENTAGE_COLUMN,
    )
    points_won_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINTS_WON_PERCENTAGE_COLUMN,
    )
    tackles_inside_50: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLES_INSIDE_50_COLUMN,
    )
    total_possessions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_POSSESSIONS_COLUMN,
    )
    score_involvements: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SCORE_INVOLVEMENTS_COLUMN,
    )
    goal_accuracy: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOAL_ACCURACY_COLUMN,
    )
    stoppage_clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STOPPAGE_CLEARANCES_COLUMN,
    )
    uncontested_marks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNCONTESTED_MARKS_COLUMN,
    )
    disposal_efficiency: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DISPOSAL_EFFICIENCY_COLUMN,
    )
    centre_clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CENTRE_CLEARANCES_COLUMN,
    )
    accurate_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ACCURATE_CROSSES_COLUMN,
    )
    accurate_long_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ACCURATE_LONG_BALLS_COLUMN,
    )
    accurate_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ACCURATE_PASSES_COLUMN,
    )
    accurate_through_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ACCURATE_THROUGH_BALLS_COLUMN,
    )
    cross_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSS_PERCENTAGE_COLUMN,
    )
    free_kick_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_KICK_GOALS_COLUMN,
    )
    free_kick_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_KICK_PERCENTAGE_COLUMN,
    )
    free_kick_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_KICK_SHOTS_COLUMN,
    )
    game_winning_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_WINNING_ASSISTS_COLUMN,
    )
    headed_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HEADED_GOALS_COLUMN,
    )
    inaccurate_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INACCURATE_CROSSES_COLUMN,
    )
    inaccurate_long_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INACCURATE_LONG_BALLS_COLUMN,
    )
    inaccurate_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INACCURATE_PASSES_COLUMN,
    )
    inaccurate_through_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INACCURATE_THROUGH_BALLS_COLUMN,
    )
    left_footed_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LEFT_FOOTED_SHOTS_COLUMN,
    )
    long_ball_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_BALL_PERCENTAGE_COLUMN,
    )
    penalty_kick_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICK_GOALS_COLUMN,
    )
    penalty_kick_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICK_PERCENTAGE_COLUMN,
    )
    penalty_kicks_missed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_MISSED_COLUMN,
    )
    possession_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POSSESSION_PERCENTAGE_COLUMN,
    )
    possession_time: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POSSESSION_TIME_COLUMN,
    )
    right_footed_shots: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RIGHT_FOOTED_SHOTS_COLUMN,
    )
    shoot_out_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOT_OUT_GOALS_COLUMN,
    )
    shoot_out_misses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOT_OUT_MISSES_COLUMN,
    )
    shoot_out_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOT_OUT_PERCENTAGE_COLUMN,
    )
    shot_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOT_ASSISTS_COLUMN,
    )
    shot_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOT_PERCENTAGE_COLUMN,
    )
    shots_headed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_HEADED_COLUMN,
    )
    shots_off_target: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_OFF_TARGET_COLUMN,
    )
    shots_on_post: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_ON_POST_COLUMN,
    )
    through_ball_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THROUGH_BALL_PERCENTAGE_COLUMN,
    )
    long_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LONG_BALLS_COLUMN,
    )
    total_passes: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_PASSES_COLUMN,
    )
    average_rating_from_editor: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_RATING_FROM_EDITOR_COLUMN,
    )
    average_rating_from_user: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_RATING_FROM_USER_COLUMN,
    )
    did_not_play: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DID_NOT_PLAY_COLUMN,
    )
    draws: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DRAWS_COLUMN,
    )
    goal_difference: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOAL_DIFFERENCE_COLUMN,
    )
    losses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LOSSES_COLUMN,
    )
    lost_corners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LOST_CORNERS_COLUMN,
    )
    minutes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MINUTES_COLUMN,
    )
    pass_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASS_PERCENTAGE_COLUMN,
    )
    starts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STARTS_COLUMN,
    )
    sub_ins: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SUB_INS_COLUMN,
    )
    sub_outs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SUB_OUTS_COLUMN,
    )
    suspensions: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SUSPENSIONS_COLUMN,
    )
    time_ended: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIME_ENDED_COLUMN,
    )
    time_started: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIME_STARTED_COLUMN,
    )
    win_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WIN_PERCENTAGE_COLUMN,
    )
    wins: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WINS_COLUMN,
    )
    won_corners: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WON_CORNERS_COLUMN,
    )
    clean_sheet: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CLEAN_SHEET_COLUMN,
    )
    crosses_caught: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSSES_CAUGHT_COLUMN,
    )
    goals_conceded: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOALS_CONCEDED_COLUMN,
    )
    partial_clean_sheet: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PARTIAL_CLEAN_SHEET_COLUMN,
    )
    penalty_kick_conceded: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICK_CONCEDED_COLUMN,
    )
    penalty_kick_save_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICK_SAVE_PERCENTAGE_COLUMN,
    )
    penalty_kicks_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_FACED_COLUMN,
    )
    penalty_kicks_saved: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KICKS_SAVED_COLUMN,
    )
    punches: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PUNCHES_COLUMN,
    )
    shoot_out_kicks_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOT_OUT_KICKS_FACED_COLUMN,
    )
    shoot_out_kicks_saved: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOT_OUT_KICKS_SAVED_COLUMN,
    )
    shoot_out_save_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOT_OUT_SAVE_PERCENTAGE_COLUMN,
    )
    shots_faced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_FACED_COLUMN,
    )
    smothers: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SMOTHERS_COLUMN,
    )
    unclaimed_crosses: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNCLAIMED_CROSSES_COLUMN,
    )
    effective_clearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EFFECTIVE_CLEARANCES_COLUMN,
    )
    effective_tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EFFECTIVE_TACKLES_COLUMN,
    )
    ineffective_tackles: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INEFFECTIVE_TACKLES_COLUMN,
    )
    tackle_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TACKLE_PERCENTAGE_COLUMN,
    )
    appearances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_APPEARANCES_COLUMN,
    )
    average_rating_from_correspondent: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_RATING_FROM_CORRESPONDENT_COLUMN,
    )
    average_rating_from_data_feed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_RATING_FROM_DATA_FEED_COLUMN,
    )
    strikeouts_per_nine_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKEOUTS_PER_NINE_INNINGS_COLUMN,
    )
    strikeout_to_walk_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKEOUT_TO_WALK_RATIO_COLUMN,
    )
    tough_losses: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOUGH_LOSSES_COLUMN,
    )
    cheap_wins: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CHEAP_WINS_COLUMN,
    )
    save_opportunities_per_win: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAVE_OPPORTUNITIES_PER_WIN_COLUMN,
    )
    pitch_count: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PITCH_COUNT_COLUMN,
    )
    strike_pitch_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STRIKE_PITCH_RATIO_COLUMN,
    )
    double_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DOUBLE_PLAYS_COLUMN,
    )
    opportunities: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPORTUNITIES_COLUMN,
    )
    passed_balls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSED_BALLS_COLUMN,
    )
    outfield_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OUTFIELD_ASSISTS_COLUMN,
    )
    pickoffs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PICKOFFS_COLUMN,
    )
    outs_on_field: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OUTS_ON_FIELD_COLUMN,
    )
    triple_plays: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TRIPLE_PLAYS_COLUMN,
    )
    balls_in_zone: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALLS_IN_ZONE_COLUMN,
    )
    extra_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_BASES_COLUMN,
    )
    outs_made: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OUTS_MADE_COLUMN,
    )
    catcher_third_innings_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_THIRD_INNINGS_PLAYED_COLUMN,
    )
    catcher_caught_stealing: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_CAUGHT_STEALING_COLUMN,
    )
    catcher_stolen_bases_allowed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_STOLEN_BASES_ALLOWED_COLUMN,
    )
    catcher_earned_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_EARNED_RUNS_COLUMN,
    )
    is_qualified_catcher: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_IS_QUALIFIED_CATCHER_COLUMN,
    )
    is_qualified_pitcher: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_IS_QUALIFIED_PITCHER_COLUMN,
    )
    successful_chances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SUCCESSFUL_CHANCES_COLUMN,
    )
    total_chances: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_CHANCES_COLUMN,
    )
    full_innings_played: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FULL_INNINGS_PLAYED_COLUMN,
    )
    part_innings_played: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PART_INNINGS_PLAYED_COLUMN,
    )
    fielding_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELDING_PERCENTAGE_COLUMN,
    )
    range_factor: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RANGE_FACTOR_COLUMN,
    )
    zone_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ZONE_RATING_COLUMN,
    )
    catcher_caught_stealing_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_CAUGHT_STEALING_PERCENTAGE_COLUMN,
    )
    catcher_era: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_ERA_COLUMN,
    )
    def_warbr: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DEF_WARBR_COLUMN,
    )
    wins_above_replacement: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WINS_ABOVE_REPLACEMENT_COLUMN,
    )
    batters_hit: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BATTERS_HIT_COLUMN,
    )
    sacrifice_bunts: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SACRIFICE_BUNTS_COLUMN,
    )
    save_opportunities: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAVE_OPPORTUNITIES_COLUMN,
    )
    finishes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FINISHES_COLUMN,
    )
    balks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALKS_COLUMN,
    )
    holds: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HOLDS_COLUMN,
    )
    complete_games: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_COMPLETE_GAMES_COLUMN,
    )
    perfect_games: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PERFECT_GAMES_COLUMN,
    )
    wild_pitches: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WILD_PITCHES_COLUMN,
    )
    third_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THIRD_INNINGS_COLUMN,
    )
    team_earned_runs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TEAM_EARNED_RUNS_COLUMN,
    )
    pickoff_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PICKOFF_ATTEMPTS_COLUMN,
    )
    run_support: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUN_SUPPORT_COLUMN,
    )
    pitches_as_starter: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PITCHES_AS_STARTER_COLUMN,
    )
    average_game_score: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_GAME_SCORE_COLUMN,
    )
    quality_starts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_QUALITY_STARTS_COLUMN,
    )
    inherited_runners_scored: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INHERITED_RUNNERS_SCORED_COLUMN,
    )
    opponent_total_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPONENT_TOTAL_BASES_COLUMN,
    )
    is_qualified_saves: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_IS_QUALIFIED_SAVES_COLUMN,
    )
    full_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FULL_INNINGS_COLUMN,
    )
    part_innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PART_INNINGS_COLUMN,
    )
    blown_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOWN_SAVES_COLUMN,
    )
    innings: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INNINGS_COLUMN,
    )
    whip: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WHIP_COLUMN,
    )
    caught_stealing_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CAUGHT_STEALING_PERCENTAGE_COLUMN,
    )
    pitches_per_start: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PITCHES_PER_START_COLUMN,
    )
    pitches_per_inning: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PITCHES_PER_INNING_COLUMN,
    )
    run_support_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUN_SUPPORT_AVERAGE_COLUMN,
    )
    opponent_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPONENT_AVERAGE_COLUMN,
    )
    opponent_slug_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPONENT_SLUG_AVERAGE_COLUMN,
    )
    opponent_on_base_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPONENT_ON_BASE_PERCENTAGE_COLUMN,
    )
    opponent_ops: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OPPONENT_OPS_COLUMN,
    )
    doubles: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DOUBLES_COLUMN,
    )
    caught_stealing: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CAUGHT_STEALING_COLUMN,
    )
    games_started: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAMES_STARTED_COLUMN,
    )
    pinch_at_bats: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PINCH_AT_BATS_COLUMN,
    )
    pinch_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PINCH_HITS_COLUMN,
    )
    player_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PLAYER_RATING_COLUMN,
    )
    is_qualified: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_IS_QUALIFIED_COLUMN,
    )
    is_qualified_steals: bool | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_IS_QUALIFIED_STEALS_COLUMN,
    )
    total_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_BASES_COLUMN,
    )
    projected_home_runs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PROJECTED_HOME_RUNS_COLUMN,
    )
    extra_base_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EXTRA_BASE_HITS_COLUMN,
    )
    runs_created: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_CREATED_COLUMN,
    )
    batting_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BATTING_AVERAGE_COLUMN,
    )
    pinch_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PINCH_AVERAGE_COLUMN,
    )
    slug_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SLUG_AVERAGE_COLUMN,
    )
    secondary_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECONDARY_AVERAGE_COLUMN,
    )
    on_base_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ON_BASE_PERCENTAGE_COLUMN,
    )
    ground_to_fly_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GROUND_TO_FLY_RATIO_COLUMN,
    )
    runs_created_per_27_outs: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_CREATED_PER_27_OUTS_COLUMN,
    )
    batter_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BATTER_RATING_COLUNN,
    )
    at_bats_per_home_run: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AT_BATS_PER_HOME_RUN_COLUMN,
    )
    stolen_base_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STOLEN_BASE_PERCENTAGE_COLUMN,
    )
    pitches_per_plate_appearance: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PITCHES_PER_PLATE_APPEARANCE_COLUMN,
    )
    isolated_power: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ISOLATED_POWER_COLUMN,
    )
    walk_to_strikeout_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WALK_TO_STRIKEOUT_RATIO_COLUMN,
    )
    walks_per_plate_appearance: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WALKS_PER_PLATE_APPEARANCE_COLUMN,
    )
    secondary_average_minus_batting_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECONDARY_AVERAGE_MINUS_BATTING_AVERAGE_COLUMN,
    )
    runs_produced: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_PRODUCED_COLUMN,
    )
    runs_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNS_RATIO_COLUMN,
    )
    patience_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PATIENCE_RATIO_COLUMN,
    )
    balls_in_play_average: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BALLS_IN_PLAY_AVERAGE_COLUMN,
    )
    mlb_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MLB_RATING_COLUMN,
    )
    offensive_wins_above_replacement: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OFFENSIVE_WINS_ABOVE_REPLACEMENT_COLUMN,
    )
    games_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAMES_PLAYED_COLUMN,
    )
    team_games_played: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TEAM_GAMES_PLAYED_COLUMN,
    )
    hit_by_pitch: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HIT_BY_PITCH_COLUMN,
    )
    rbis: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RBIS_COLUMN,
    )
    sac_hits: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAC_HITS_COLUMN,
    )
    stolen_bases: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STOLEN_BASES_COLUMN,
    )
    walks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_WALKS_COLUMN,
    )
    catcher_interference: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CATCHER_INTERFERENCE_COLUMN,
    )
    gidps: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GIDPS_COLUMN,
    )
    sac_flies: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SAC_FLIES_COLUMN,
    )
    grand_slam_home_runs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GRAND_SLAM_HOME_RUNS_COLUMN,
    )
    runners_left_on_base: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUNNERS_LEFT_ON_BASE_COLUMN,
    )
    triples: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TRIPLES_COLUMN,
    )
    game_winning_rbis: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_WINNING_RBIS_COLUMN,
    )
    intentional_walks: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INTENTIONAL_WALKS_COLUMN,
    )
    average_three_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_free_throws_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FREE_THROWS_MADE_COLUMN,
    )
    average_free_throws_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FREE_THROWS_ATTEMPTED_COLUMN,
    )
    average_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_POINTS_COLUMN,
    )
    average_offensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_OFFENSIVE_REBOUNDS_COLUMN,
    )
    average_assists: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_ASSISTS_COLUMN,
    )
    average_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TURNOVERS_COLUMN,
    )
    estimated_possessions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ESTIMATED_POSSESSIONS_COLUMN,
    )
    average_estimated_possessions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_ESTIMATED_POSSESSIONS_COLUMN,
    )
    points_per_estimated_possessions: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINTS_PER_ESTIMATED_POSSESSIONS_COLUMN,
    )
    average_team_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TEAM_TURNOVERS_COLUMN,
    )
    average_total_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TOTAL_TURNOVERS_COLUMN,
    )
    three_point_field_goal_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_FIELD_GOAL_PERCENTAGE_COLUMN,
    )
    two_point_field_goals_made: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    two_point_field_goals_attempted: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_two_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TWO_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    average_two_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TWO_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    two_point_field_goal_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_FIELD_GOAL_PERCENTAGE_COLUMN,
    )
    shooting_efficiency: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOTING_EFFICIENCY_COLUMN,
    )
    scoring_efficiency: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SCORING_EFFICIENCY_COLUMN,
    )
    average_48_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_FIELD_GOALS_MADE_COLUMN,
    )
    average_48_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_48_three_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_THREE_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    average_48_three_point_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_THREE_POINT_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_48_free_throws_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_FREE_THROWS_MADE_COLUMN,
    )
    average_48_free_throws_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_FREE_THROWS_ATTEMPTED_COLUMN,
    )
    average_48_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_POINTS_COLUMN,
    )
    average_48_offensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_OFFENSIVE_REBOUNDS_COLUMN,
    )
    average_48_assists: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_ASSISTS_COLUMN,
    )
    average_48_turnovers: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_TURNOVERS_COLUMN,
    )
    p40: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_P40_COLUMN,
    )
    a40: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_A40_COLUMN,
    )
    average_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_REBOUNDS_COLUMN,
    )
    average_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FOULS_COLUMN,
    )
    average_flagrant_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FLAGRANT_FOULS_COLUMN,
    )
    average_technical_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TECHNICAL_FOULS_COLUMN,
    )
    average_ejections: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_EJECTIONS_COLUMN,
    )
    average_disqualifications: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_DISQUALIFICATIONS_COLUMN,
    )
    assist_turnover_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ASSIST_TURNOVER_RATIO_COLUMN,
    )
    steal_foul_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STEAL_FOUL_RATIO_COLUMN,
    )
    block_foul_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BLOCK_FOUL_RATIO_COLUMN,
    )
    average_team_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_TEAM_REBOUNDS_COLUMN,
    )
    total_technical_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_TECHNICAL_FOULS_COLUMN,
    )
    team_assist_turnover_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TEAM_ASSIST_TURNOVER_RATIO_COLUMN,
    )
    steal_turnover_ratio: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STEAL_TURNOVER_RATIO_COLUMN,
    )
    average_48_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_REBOUNDS_COLUMN,
    )
    average_48_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_FOULS_COLUMN,
    )
    average_48_flagrant_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_FLAGRANT_FOULS_COLUMN,
    )
    average_48_technical_fouls: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_TECHNICAL_FOULS_COLUMN,
    )
    average_48_ejections: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_EJECTIONS_COLUMN,
    )
    average_48_disqualifications: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_DISQUALIFICATIONS_COLUMN,
    )
    r40: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_R40_COLUMN,
    )
    double_double: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DOUBLE_DOUBLE_COLUMN,
    )
    triple_double: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TRIPLE_DOUBLE_COLUMN,
    )
    free_throws_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FREE_THROWS_MADE_COLUMN,
    )
    three_point_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_PERCENTAGE_COLUMN,
    )
    three_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_THREE_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    total_turnovers: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_TURNOVERS_COLUMN,
    )
    points_in_paint: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINTS_IN_PAINT_COLUMN,
    )
    brick_index: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BRICK_INDEX_COLUMN,
    )
    average_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FIELD_GOALS_MADE_COLUMN,
    )
    average_field_goals_attempted: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FIELD_GOALS_ATTEMPTED_COLUMN,
    )
    average_three_point_field_goals_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_THREE_POINT_FIELD_GOALS_MADE_COLUMN,
    )
    average_defensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_DEFENSIVE_REBOUNDS_COLUMN,
    )
    average_blocks: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_BLOCKS_COLUMN,
    )
    average_steals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_STEALS_COLUMN,
    )
    average_48_defensive_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_DEFENSIVE_REBOUNDS_COLUMN,
    )
    average_48_blocks: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_BLOCKS_COLUMN,
    )
    average_48_steals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_48_STEALS_COLUMN,
    )
    largest_lead: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_LARGEST_LEAD_COLUMN,
    )
    disqualifications: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DISQUALIFICATIONS_COLUMN,
    )
    flagrant_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FLAGRANT_FOULS_COLUMN,
    )
    fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FOULS_COLUMN,
    )
    ejections: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EJECTIONS_COLUMN,
    )
    technical_fouls: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TECHNICAL_FOULS_COLUMN,
    )
    average_minutes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_MINUTES_COLUMN,
    )
    nba_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NBA_RATING_COLUMN,
    )
    plus_minus: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PLUS_MINUS_COLUMN,
    )
    faceoffs_won: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FACEOFFS_WON_COLUMN,
    )
    faceoffs_lost: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FACEOFFS_LOST_COLUMN,
    )
    faceoff_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FACEOFF_PERCENTAGE_COLUMN,
    )
    unassisted_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNASSISTED_GOALS_COLUMN,
    )
    game_tying_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_TYING_GOALS_COLUMN,
    )
    giveaways: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GIVEAWAYS_COLUMN,
    )
    penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTIES_COLUMN,
    )
    penalty_minutes: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_MINUTES_COLUMN,
    )
    penalty_minutes_against: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_MINUTES_AGAINST_COLUMN,
    )
    major_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MAJOR_PENALTIES_COLUMN,
    )
    minor_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MINOR_PENALTIES_COLUMN,
    )
    match_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MATCH_PENALTIES_COLUMN,
    )
    misconducts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_MISCONDUCTS_COLUMN,
    )
    game_misconducts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_MISCONDUCTS_COLUMN,
    )
    boarding_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_BOARDING_PENALTIES_COLUMN,
    )
    unsportsmanlike_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_UNSPORTSMANLIKE_PENALTIES_COLUMN,
    )
    fighting_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIGHTING_PENALTIES_COLUMN,
    )
    average_fights: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_FIGHTS_COLUMN,
    )
    time_between_fights: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIME_BETWEEN_FIGHTS_COLUMN,
    )
    instigator_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INSTIGATOR_PENALTIES_COLUMN,
    )
    charging_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CHARGING_PENALTIES_COLUMN,
    )
    hooking_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HOOKING_PENALTIES_COLUMN,
    )
    tripping_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TRIPPING_PENALTIES_COLUMN,
    )
    roughing_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ROUGHING_PENALTIES_COLUMN,
    )
    holding_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HOLDING_PENALTIES_COLUMN,
    )
    interference_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_INTERFERENCE_PENALTIES_COLUMN,
    )
    slashing_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SLASHING_PENALTIES_COLUMN,
    )
    high_sticking_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_HIGH_STICKING_PENALTIES_COLUMN,
    )
    cross_checking_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_CROSS_CHECKING_PENALTIES_COLUMN,
    )
    stick_holding_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_STICK_HOLDING_PENALTIES_COLUMN,
    )
    goalie_interference_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOALIE_INTERFERENCE_PENALTIES_COLUMN,
    )
    elbowing_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ELBOWING_PENALTIES_COLUMN,
    )
    diving_penalties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_DIVING_PENALTIES_COLUMN,
    )
    takeaways: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TAKEAWAYS_COLUMN,
    )
    even_strength_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EVEN_STRENGTH_SAVES_COLUMN,
    )
    power_play_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_SAVES_COLUMN,
    )
    short_handed_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHORT_HANDED_SAVES_COLUMN,
    )
    games: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAMES_COLUMN,
    )
    game_started: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAME_STARTED_COLUMN,
    )
    ties: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIES_COLUMN,
    )
    time_on_ice_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIME_ON_ICE_PER_GAME_COLUMN,
    )
    power_play_time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_TIME_ON_ICE_COLUMN,
    )
    short_handed_time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHORT_HANDED_TIME_ON_ICE_COLUMN,
    )
    even_strength_time_on_ice: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EVEN_STRENGTH_TIME_ON_ICE_COLUMN,
    )
    shifts_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHIFTS_PER_GAME_COLUMN,
    )
    production: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PRODUCTION_COLUMN,
    )
    shot_differential: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOT_DIFFERENTIAL_COLUMN,
    )
    goal_differential: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GOAL_DIFFERENTIAL_COLUMN,
    )
    pim_differential: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PIM_DIFFERENTIAL_COLUMN,
    )
    rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RATING_COLUMN,
    )
    average_goals: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_GOALS_COLUMN,
    )
    ytd_goals: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YTD_GOALS_COLUMN,
    )
    shots_in_first_period: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_IN_FIRST_PERIOD_COLUMN,
    )
    shots_in_second_period: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_IN_SECOND_PERIOD_COLUMN,
    )
    shots_in_third_period: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_IN_THIRD_PERIOD_COLUMN,
    )
    shots_overtime: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_OVERTIME_COLUMN,
    )
    average_shots: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_SHOTS_COLUMN,
    )
    points_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POINTS_PER_GAME_COLUMN,
    )
    power_play_opportunities: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_OPPORTUNITIES_COLUMN,
    )
    power_play_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_PERCENTAGE_COLUMN,
    )
    shootout_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOTOUT_ATTEMPTS_COLUMN,
    )
    shootout_shot_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOTOUT_SHOT_PERCENTAGE_COLUMN,
    )
    empty_net_goals_for: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EMPTY_NET_GOALS_FOR_COLUMN,
    )
    shutouts_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHUTOUTS_AGAINST_COLUMN,
    )
    total_face_offs: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_FACE_OFFS_COLUMN,
    )
    average_goals_against: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_GOALS_AGAINST_COLUMN,
    )
    average_shots_against: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_AVERAGE_SHOTS_AGAINST_COLUMN,
    )
    penalty_kill_percentage: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PENALTY_KILL_PERCENTAGE_COLUMN,
    )
    power_play_goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_POWER_PLAY_GOALS_AGAINST_COLUMN,
    )
    short_handed_goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHORT_HANDED_GOALS_AGAINST_COLUMN,
    )
    shootout_saves: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOTOUT_SAVES_COLUMN,
    )
    shootout_shots_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOOTOUT_SHOTS_AGAINST_COLUMN,
    )
    times_short_handed: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TIMES_SHORT_HANDED_COLUMN,
    )
    empty_net_goals_against: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_EMPTY_NET_GOALS_AGAINST_COLUMN,
    )
    overtime_losses: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_OVERTIME_LOSSES_COLUMN,
    )
    shots_missed: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SHOTS_MISSED_COLUMN,
    )
    net_passing_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_PASSING_YARDS_PER_GAME_COLUMN,
    )
    net_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_NET_YARDS_PER_GAME_COLUMN,
    )
    passing_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_PASSING_YARDS_PER_GAME_COLUMN,
    )
    total_points_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TOTAL_POINTS_PER_GAME_COLUMN,
    )
    yards_from_scrimmage_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_FROM_SCRIMMAGE_PER_GAME_COLUMN,
    )
    yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_YARDS_PER_GAME_COLUMN,
    )
    espn_rb_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ESPN_RB_RATING_COLUMN,
    )
    rushing_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RUSHING_YARDS_PER_GAME_COLUMN,
    )
    receiving_yards_per_game: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_RECEIVING_YARDS_PER_GAME_COLUMN,
    )
    two_point_returns: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TWO_POINT_RETURNS_COLUMN,
    )
    field_goal_attempts: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FIELD_GOAL_ATTEMPTS_COLUMN,
    )
    special_team_fumble_return_yards: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SPECIAL_TEAM_FUMBLE_RETURN_YARDS_COLUMN,
    )
    kick_extra_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_EXTRA_POINTS_COLUMN,
    )
    kick_extra_points_made: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_KICK_EXTRA_POINTS_MADE_COLUMN,
    )
    attempts_in_box: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ATTEMPTS_IN_BOX_COLUMN,
    )
    second_assists: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECOND_ASSISTS_COLUMN,
    )
    qbr: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_QBR_COLUMN,
    )
    attempts_out_box: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ATTEMPTS_OUT_BOX_COLUMN,
    )
    adjusted_qbr: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_ADJUSTED_QBR_COLUMN,
    )
    turnover_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TURNOVER_POINTS_COLUMN,
    )
    fantasy_rating: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FANTASY_RATING_COLUMN,
    )
    team_turnovers: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TEAM_TURNOVERS_COLUMN,
    )
    second_chance_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_SECOND_CHANCE_POINTS_COLUMN,
    )
    fast_break_points: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_FAST_BREAK_POINTS_COLUMN,
    )
    team_rebounds: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_TEAM_REBOUNDS_COLUMN,
    )
    gained: float | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=PLAYER_GAINED_COLUMN,
    )
