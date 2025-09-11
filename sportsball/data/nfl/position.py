"""The enumeration of the different supported positions."""

from enum import StrEnum


class Position(StrEnum):
    """An enumeration over the different positions."""

    LINE_BACKER = "LB"
    DEFENSIVE_TACKLE = "DT"
    QUARTER_BACK = "QB"
    DEFENSIVE_LINESMAN = "DL"
    OFFENSIVE_LINESMAN = "OL"
    SAFETY = "S"
    WIDE_RECEIVER = "WR"
    GUARD = "G"
    RUNNING_BACK = "RB"
    TIGHT_END = "TE"
    OFFENSIVE_TACKLE = "OT"
    CORNER_BACK = "CB"
    DEFENSIVE_BACK = "DB"
    DEFENSIVE_END = "DE"
    EDGE_RUSHER = "EDGE"
    PUNTER = "P"
    LONG_SNAPPER = "LS"
    PLACE_KICKER = "PK"
    CENTER = "C"
    FULL_BACK = "FB"
    NOSE_TACKLE = "NT"
    ATHLETE = "ATH"
    KICK_RETURNER = "KR"
    PUNT_RETURNER = "PR"
    SETTER = "SETTER"
