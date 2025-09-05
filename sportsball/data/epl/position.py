"""The enumeration of the different supported positions."""

from enum import StrEnum


class Position(StrEnum):
    """An enumeration over the different positions."""

    GOALKEEPER = "G"
    CENTRE_DEFENDER_LEFT = "CD-L"
    CENTRE_DEFENDER_RIGHT = "CD-R"
    LEFT_BACK = "LB"
    RIGHT_BACK = "RB"
    ATTACKING_MIDFIELDER = "AM"
    CENTRAL_MIDFIELDER = "CM"
    LEFT_MIDFIELDER = "LM"
    RIGHT_MIDFIELDER = "RM"
    CENTRAL_MIDFIELDER_LEFT = "CM-L"
    FORWARD = "F"
    LEFT_FORWARD = "LF"
    CENTRE_DEFENDER = "CD"
    ATTACKING_MIDFIELDER_LEFT = "AM-L"
    RIGHT_FORWARD = "RF"
    ATTACKING_MIDFIELDER_RIGHT = "AM-R"
    SUBSTITUTE = "SUB"
    CENTRE_MIDFIELDER_RIGHT = "CM-R"
    DEFENSIVE_MIDFIELDER = "DM"
    CENTRE_FORWARD_LEFT = "CF-L"
    CENTRE_FORWARD_RIGHT = "CF-R"
    SWEEPER = "SW"
    MIDFIELDER = "M"
    RIGHT_CENTRAL_MIDFIELDER = "RCM"


_POSITIONS = {str(x): x for x in Position}


def position_from_str(position_str: str) -> Position:
    """Find a position from a string."""
    position = _POSITIONS.get(position_str)
    if position is None:
        raise ValueError(f"Unrecognised position: {position_str}")
    return position
