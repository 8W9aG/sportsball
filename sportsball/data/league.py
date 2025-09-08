"""The enumeration of the different supported leagues."""

# pylint: disable=too-many-return-statements
from enum import StrEnum


class League(StrEnum):
    """An enumeration over the different leagues."""

    AFL = "afl"
    AFLW = "aflw"
    ATP = "atp"
    EPL = "epl"
    FIFA = "fifa"
    HKJC = "hkjc"
    IPL = "ipl"
    MLB = "mlb"
    NBA = "nba"
    NCAAB = "ncaab"
    NCAAF = "ncaaf"
    NFL = "nfl"
    NHL = "nhl"
    WNBA = "wnba"
    WTA = "wta"


def long_name(league: League) -> str:
    """Find the leagues long name."""
    match league:
        case League.AFL:
            return "Australia Football League"
        case League.AFLW:
            return "Australia Football League Womens"
        case League.ATP:
            return "Association of Tennis Professionals"
        case League.EPL:
            return "English Premier League"
        case League.FIFA:
            return "Fédération Internationale de Football Association"
        case League.HKJC:
            return "Hong Kong Jockey Club"
        case League.IPL:
            return "Indian Premier League"
        case League.MLB:
            return "Major League Basketball"
        case League.NBA:
            return "National Basketball League"
        case League.NCAAB:
            return "NCAA Division I Basketball"
        case League.NCAAF:
            return "NCAA Division I Football"
        case League.NFL:
            return "National Football League"
        case League.NHL:
            return "National Hockey League"
        case League.WNBA:
            return "Womens National Basketball League"
        case League.WTA:
            return "Womens Tennis Association"


def league_from_str(league_str: str) -> League:
    """Find the league matching the string."""
    league_str = league_str.lower()
    match league_str:
        case str(League.AFL):
            return League.AFL
        case str(League.AFLW):
            return League.AFLW
        case str(League.ATP):
            return League.ATP
        case str(League.EPL):
            return League.EPL
        case str(League.FIFA):
            return League.FIFA
        case str(League.HKJC):
            return League.HKJC
        case str(League.IPL):
            return League.IPL
        case str(League.MLB):
            return League.MLB
        case str(League.NBA):
            return League.NBA
        case str(League.NCAAB):
            return League.NCAAB
        case str(League.NCAAF):
            return League.NCAAF
        case str(League.NFL):
            return League.NFL
        case str(League.NHL):
            return League.NHL
        case str(League.WNBA):
            return League.WNBA
        case str(League.WTA):
            return League.WTA
        case _:
            raise ValueError(f"Unrecognised League: {league_str}")
