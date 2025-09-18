"""The enumeration of the different supported positions."""

from enum import StrEnum


class Position(StrEnum):
    """An enumeration over the different positions."""

    DEFENSEMAN = "D"
    CENTRE = "C"
    GOALTENDER = "G"
    LEFT_WING = "LW"
    RIGHT_WING = "RW"
    FORWARD = "F"
    UNASSIGNED = "UN"
