"""ESPN game model."""

# pylint: disable=too-many-arguments,duplicate-code
import datetime
from typing import Any, Dict

import pytest_is_running
import requests_cache
from dateutil.parser import parse

from ...cache import MEMORY
from ..game_model import VERSION as GAME_VERSION
from ..game_model import GameModel, localize
from ..google.google_news_model import create_google_news_models
from ..league import League
from ..odds_model import OddsModel
from ..season_type import SeasonType
from ..team_model import VERSION as TEAM_VERSION
from ..team_model import TeamModel
from ..umpire_model import UmpireModel
from ..venue_model import VERSION as VENUE_VERSION
from ..venue_model import VenueModel
from ..x.x_social_model import create_x_social_model
from .espn_bookie_model import create_espn_bookie_model
from .espn_odds_model import MONEYLINE_KEY, create_espn_odds_model
from .espn_player_model import create_espn_player_model
from .espn_team_model import ID_KEY, create_espn_team_model
from .espn_umpire_model import create_espn_umpire_model
from .espn_venue_model import create_espn_venue_model


def _create_espn_team(
    competitor: Dict[str, Any],
    odds_dict: Dict[str, Any],
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
    positions_validator: dict[str, str],
) -> TeamModel:
    if competitor["type"] == "athlete":
        player = create_espn_player_model(
            session=session,
            player=competitor,
            dt=dt,
            positions_validator=positions_validator,
        )
        return TeamModel(
            identifier=player.identifier,
            name=player.name,
            location=None,
            players=[player],
            odds=[],
            points=int(competitor["winner"]),
            ladder_rank=None,
            news=create_google_news_models(player.name, session, dt, league),
            social=create_x_social_model(player.identifier, session, dt),
            field_goals=None,
            coaches=[],
            lbw=None,
            end_dt=None,
            runs=None,
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
            tackles_inside_50=None,
            total_possessions=None,
            uncontested_marks=None,
            disposal_efficiency=None,
            centre_clearances=None,
            stoppage_clearances=None,
            goal_accuracy=None,
            rushed_behinds=None,
            touched_behinds=None,
            left_behinds=None,
            left_posters=None,
            right_behinds=None,
            right_posters=None,
            total_interchange_count=None,
            interchange_count_q1=None,
            interchange_count_q2=None,
            interchange_count_q3=None,
            interchange_count_q4=None,
            game_winning_goals=None,
            headed_goals=None,
            inaccurate_crosses=None,
            inaccurate_long_balls=None,
            inaccurate_passes=None,
            inaccurate_through_balls=None,
            left_footed_shots=None,
            longball_percentage=None,
            offsides=None,
            penalty_kick_goals=None,
            penalty_kick_percentage=None,
            penalty_kick_shots=None,
            penalty_kicks_missed=None,
            possession_percentage=None,
            possession_time=None,
            right_footed_shots=None,
            shoot_out_goals=None,
            shoot_out_misses=None,
            shoot_out_percentage=None,
            shot_assists=None,
            shot_percentage=None,
            shots_headed=None,
            shots_off_target=None,
            shots_on_post=None,
            shots_on_target=None,
            through_ball_percentage=None,
            total_crosses=None,
            total_goals=None,
            total_long_balls=None,
            total_passes=None,
            total_shots=None,
            total_through_balls=None,
            draws=None,
            sub_outs=None,
            suspensions=None,
            time_ended=None,
            time_started=None,
            win_percentage=None,
            wins=None,
            won_corners=None,
            yellow_cards=None,
            clean_sheet=None,
            crosses_caught=None,
            goals_conceded=None,
            partial_clean_sheet=None,
            penalty_kick_conceded=None,
            penalty_kick_save_percentage=None,
            penalty_kicks_faced=None,
            penalty_kicks_saved=None,
            punches=None,
            saves=None,
            shoot_out_kicks_faced=None,
            shoot_out_kicks_saved=None,
            shoot_out_save_percentage=None,
            shots_faced=None,
            smothers=None,
            unclaimed_crosses=None,
            accurate_crosses=None,
            accurate_long_balls=None,
            accurate_passes=None,
            accurate_through_balls=None,
            cross_percentage=None,
            free_kick_goals=None,
            free_kick_percentage=None,
            free_kick_shots=None,
            game_winning_assists=None,
            blocked_shots=None,
            effective_clearances=None,
            effective_tackles=None,
            ineffective_tackles=None,
            interceptions=None,
            tackle_percentage=None,
            appearances=None,
            average_rating_from_correspondent=None,
            average_rating_from_data_feed=None,
            average_rating_from_editor=None,
            average_rating_from_user=None,
            did_not_play=None,
            fouls_committed=None,
            fouls_suffered=None,
            goal_difference=None,
            losses=None,
            lost_corners=None,
            minutes=None,
            own_goals=None,
            pass_percentage=None,
            red_cards=None,
            starts=None,
            sub_ins=None,
            pitch_count=None,
            strikes=None,
            strike_pitch_ratio=None,
            games_played=None,
            team_games_played=None,
            double_plays=None,
            opportunities=None,
            errors=None,
            passed_balls=None,
            outfield_assists=None,
            pickoffs=None,
            putouts=None,
            outs_on_field=None,
            triple_plays=None,
            balls_in_zone=None,
            extra_bases=None,
            outs_made=None,
            catcher_third_innings_played=None,
            catcher_caught_stealing=None,
            catcher_stolen_bases_allowed=None,
            catcher_earned_runs=None,
            is_qualified_catcher=None,
            is_qualified_pitcher=None,
            successful_chances=None,
            total_chances=None,
            full_innings_played=None,
            part_innings_played=None,
            fielding_percentage=None,
            range_factor=None,
            zone_rating=None,
            catcher_caught_stealing_percentage=None,
            catcher_era=None,
            def_warbr=None,
            perfect_games=None,
            wild_pitches=None,
            third_innings=None,
            team_earned_runs=None,
            shutouts=None,
            pickoff_attempts=None,
            run_support=None,
            pitches_as_starter=None,
            quality_starts=None,
            inherited_runners=None,
            inherited_runners_scored=None,
            opponent_total_bases=None,
            is_qualified_saves=None,
            full_innings=None,
            part_innings=None,
            blown_saves=None,
            innings=None,
            era=None,
            whip=None,
            caught_stealing_percentage=None,
            pitches_per_start=None,
            pitches_per_inning=None,
            run_support_average=None,
            opponent_average=None,
            opponent_slug_average=None,
            opponent_on_base_percentage=None,
            opponent_ops=None,
            save_percentage=None,
            strikeouts_per_nine_innings=None,
            strikeout_to_walk_ratio=None,
            tough_losses=None,
            cheap_wins=None,
            save_opportunities_per_win=None,
            runs_created=None,
            batting_average=None,
            pinch_average=None,
            slug_average=None,
            secondary_average=None,
            on_base_percentage=None,
            ops=None,
            ground_to_fly_ratio=None,
            runs_created_per_27_outs=None,
            batter_rating=None,
            at_bats_per_home_run=None,
            stolen_base_percentage=None,
            pitches_per_plate_appearance=None,
            isolated_power=None,
            walk_to_strikeout_ratio=None,
            walks_per_plate_appearance=None,
            secondary_average_minus_batting_average=None,
            runs_produced=None,
            runs_ratio=None,
            patience_ratio=None,
            balls_in_play_average=None,
            mlb_rating=None,
            offensive_wins_above_replacement=None,
            wins_above_replacement=None,
            earned_runs=None,
            batters_hit=None,
            sacrifice_bunts=None,
            save_opportunities=None,
            finishes=None,
            balks=None,
            batters_faced=None,
            holds=None,
            complete_games=None,
            hit_by_pitch=None,
            ground_balls=None,
            strikeouts=None,
            rbis=None,
            sac_hits=None,
            hits=None,
            stolen_bases=None,
            walks=None,
            catcher_interference=None,
            gidps=None,
            sacrifice_flies=None,
            at_bats=None,
            home_runs=None,
            grand_slam_home_runs=None,
            runners_left_on_base=None,
            triples=None,
            game_winning_rbis=None,
            intentional_walks=None,
            doubles=None,
            fly_balls=None,
            caught_stealing=None,
            pitches=None,
            games_started=None,
            pinch_at_bats=None,
            pinch_hits=None,
            player_rating=None,
            is_qualified=None,
            is_qualified_steals=None,
            total_bases=None,
            plate_appearances=None,
            projected_home_runs=None,
            extra_base_hits=None,
            average_game_score=None,
            version=TEAM_VERSION,
        )

    team_dict = competitor
    if "team" in competitor:
        team_response = session.get(competitor["team"]["$ref"])
        team_response.raise_for_status()
        team_dict = team_response.json()

    odds: list[OddsModel] = []
    if odds_dict:
        if "homeAway" in competitor:
            odds_key = competitor["homeAway"] + "TeamOdds"
            odds = [  # pyright: ignore
                create_espn_odds_model(
                    x[odds_key],
                    create_espn_bookie_model(x["provider"]),
                )
                for x in odds_dict["items"]
                if odds_key in x and MONEYLINE_KEY in x[odds_key]
            ]

    roster_dict = {}
    if "roster" in competitor:
        roster_response = session.get(competitor["roster"]["$ref"])
        roster_response.raise_for_status()
        roster_dict = roster_response.json()

    score_dict = {}
    if "score" in competitor:
        score_response = session.get(competitor["score"]["$ref"])
        score_response.raise_for_status()
        score_dict = score_response.json()

    statistics_dict = {}
    if "statistics" in competitor:
        statistics_response = session.get(competitor["statistics"]["$ref"])
        statistics_response.raise_for_status()
        statistics_dict = statistics_response.json()

    return create_espn_team_model(
        session,
        team_dict,
        roster_dict,
        odds,
        score_dict,
        dt,
        league,
        positions_validator,
        statistics_dict=statistics_dict,
    )


def _create_venue(
    event: dict[str, Any],
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel | None:
    venue = None
    if "venue" in event:
        venue = create_espn_venue_model(
            venue=event["venue"], session=session, dt=dt, version=version
        )
    if venue is None and "venues" in event:
        venues = event["venues"]
        if venues:
            venue_url = event["venues"][0]["$ref"]
            venue_response = session.get(venue_url)
            venue_response.raise_for_status()
            venue = create_espn_venue_model(
                venue=venue_response.json(), session=session, dt=dt, version=version
            )
    return venue  # pyright: ignore


def _create_teams(
    event: dict[str, Any],
    session: requests_cache.CachedSession,
    venue: VenueModel | None,
    dt: datetime.datetime,
    league: League,
    positions_validator: dict[str, str],
) -> tuple[list[TeamModel], int | None, datetime.datetime | None, list[UmpireModel]]:
    # pylint: disable=too-many-locals
    teams = []
    attendance = None
    end_dt = None
    umpires = []
    for competition in event["competitions"]:
        odds_dict = {}
        if "odds" in competition:
            odds_response = session.get(competition["odds"]["$ref"])
            odds_response.raise_for_status()
            odds_dict = odds_response.json()

        for competitor in competition["competitors"]:
            if competitor[ID_KEY] in {"-1", "-2"}:
                continue
            teams.append(
                _create_espn_team(
                    competitor, odds_dict, session, dt, league, positions_validator
                )
            )
        attendance = competition.get("attendance")
        if "situation" in competition:
            situation_url = competition["situation"]["$ref"]
            situation_response = session.get(situation_url)
            situation_response.raise_for_status()
            situation = situation_response.json()
            if "lastPlay" in situation:
                last_play_response = session.get(situation["lastPlay"]["$ref"])
                last_play_response.raise_for_status()
                last_play = last_play_response.json()
                if "wallclock" in last_play:
                    end_dt = parse(last_play["wallclock"])
        if venue is not None and end_dt is not None:
            end_dt = localize(venue, end_dt)

        if "officials" in competition:
            officials_response = session.get(competition["officials"]["$ref"])
            officials_response.raise_for_status()
            officials_dict = officials_response.json()
            for official in officials_dict["items"]:
                umpires.append(
                    create_espn_umpire_model(
                        session=session, url=official["$ref"], dt=dt
                    )
                )

    return teams, attendance, end_dt, umpires


def _create_espn_game_model(
    event: dict[str, Any],
    week: int | None,
    game_number: int,
    session: requests_cache.CachedSession,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
    positions_validator: dict[str, str],
    version: str,
) -> GameModel:
    dt = parse(event["date"])
    venue = _create_venue(event, session, dt, VENUE_VERSION)
    if venue is not None:
        dt = localize(venue, dt)
    teams, attendance, end_dt, umpires = _create_teams(
        event, session, venue, dt, league, positions_validator
    )
    return GameModel(
        dt=dt,
        week=week,
        game_number=game_number,
        venue=venue,
        teams=teams,
        end_dt=end_dt,
        attendance=attendance,
        league=str(league),
        year=year,
        season_type=season_type,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        umpires=umpires,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_espn_game_model(
    event: dict[str, Any],
    week: int | None,
    game_number: int,
    session: requests_cache.CachedSession,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
    positions_validator: dict[str, str],
    version: str,
) -> GameModel:
    return _create_espn_game_model(
        event=event,
        week=week,
        game_number=game_number,
        session=session,
        league=league,
        year=year,
        season_type=season_type,
        positions_validator=positions_validator,
        version=version,
    )


def create_espn_game_model(
    event: dict[str, Any],
    week: int | None,
    game_number: int,
    session: requests_cache.CachedSession,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
    positions_validator: dict[str, str],
) -> GameModel:
    """Creates an ESPN game model."""
    dt = parse(event["date"])
    if (
        not pytest_is_running.is_running()
        and dt.date() < datetime.datetime.now().date() - datetime.timedelta(days=7)
    ):
        return _cached_create_espn_game_model(
            event=event,
            week=week,
            game_number=game_number,
            session=session,
            league=league,
            year=year,
            season_type=season_type,
            positions_validator=positions_validator,
            version=GAME_VERSION,
        )
    with session.cache_disabled():
        return _create_espn_game_model(
            event=event,
            week=week,
            game_number=game_number,
            session=session,
            league=league,
            year=year,
            season_type=season_type,
            positions_validator=positions_validator,
            version=GAME_VERSION,
        )
