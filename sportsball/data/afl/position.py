"""The enumeration of the different supported positions."""

# pylint: disable=duplicate-code
from enum import StrEnum


class Position(StrEnum):
    """An enumeration over the different positions."""

    FULL_BACK = "FB"
    HALF_BACK = "HB"
    CENTRE = "C"
    HALF_FORWARD = "HF"
    FULL_FORWARD = "FF"
    FOLLOWERS = "FOL"
    INTERCHANGE = "IC"
    EMERGENCY = "EMG"
    BACK_POCKET_LEFT = "BPL"


_POSITIONS = {str(x): x for x in Position}


def position_from_str(position_str: str) -> Position:
    """Find a position from a string."""
    position = _POSITIONS.get(position_str)
    if position is None:
        raise ValueError(f"Unrecognised position: {position_str}")
    return position
