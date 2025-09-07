"""The enumeration of the different supported positions."""

# pylint: disable=duplicate-code
from enum import StrEnum


class Position(StrEnum):
    """An enumeration over the different positions."""

    POWER_FORWARD = "PF"
    SHORT_GUARD = "SG"
    SMALL_FORWARD = "SF"
    CENTRE = "C"
    POINT_GUARD = "PG"
    GUARD = "G"
    FORWARD = "F"
    NOT_APPLICABLE = "NA"


_POSITIONS = {str(x): x for x in Position}


def position_from_str(position_str: str) -> Position:
    """Find a position from a string."""
    position = _POSITIONS.get(position_str)
    if position is None:
        raise ValueError(f"Unrecognised position: {position_str}")
    return position
