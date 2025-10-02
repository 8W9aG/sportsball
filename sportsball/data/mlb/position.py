"""The enumeration of the different supported positions."""

from enum import StrEnum


class Position(StrEnum):
    """An enumeration over the different positions."""

    LEFT_FIELD = "LF"
    RIGHT_FIELD = "RF"
    SECOND_BASEMAN = "2B"
    CATCHER = "C"
    SHORTSTOP = "SS"
    DESIGNATED_HITTER = "DH"
    FIRST_BASEMAN = "1B"
    CENTRE_FIELDER = "CF"
    THIRD_BASEMAN = "3B"
    PINCH_RUNNER = "PR"
    PITCHER = "P"
    PINCH_HITTER = "PH"
    RELIEF_PITCHER = "RP"
    OUTFIELDER = "OF"
