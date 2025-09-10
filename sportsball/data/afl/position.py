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
    BACK_POCKET_RIGHT = "BPR"
    HALF_BACK_FLANK_LEFT = "HBFL"
    CENTRE_HALF_BACK = "CHB"
    HALF_BACK_FLANK_RIGHT = "HBFR"
    RUCK_ROVER = "RR"
    RUCK = "R"
    HALF_FORWARD_FLANK_LEFT = "HFFL"
    CENTRE_HALF_FORWARD = "CHF"
    HALF_FORWARD_FLANK_RIGHT = "HFFR"
    FRONT_POCKET_LEFT = "FPL"
    FRONT_POCKET_RIGHT = "FPR"


_POSITIONS = {str(x): x for x in Position}


def position_from_str(position_str: str) -> Position:
    """Find a position from a string."""
    position = _POSITIONS.get(position_str)
    if position is None:
        if position_str == "INT":
            return Position.INTERCHANGE
        raise ValueError(f"Unrecognised position: {position_str}")
    return position
