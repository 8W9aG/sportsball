"""Combined coach model."""

from typing import Any

from ..coach_model import VERSION, CoachModel
from .ffill import ffill
from .most_interesting import more_interesting


def create_combined_coach_model(
    coach_models: list[CoachModel],
    identifier: str,
    coach_ffill: dict[str, dict[str, Any]],
) -> CoachModel:
    """Create a coach model by combining many coach models."""
    name = None
    birth_date = None
    age = None
    sex = None
    for coach_model in coach_models:
        name = more_interesting(name, coach_model.name)
        birth_date = more_interesting(birth_date, coach_model.birth_date)
        age = more_interesting(age, coach_model.age)
        sex = more_interesting(sex, coach_model.sex)
    if name is None:
        raise ValueError("name is null.")
    coach_model = CoachModel.model_construct(
        identifier=identifier,
        name=name,
        birth_date=birth_date,
        age=age,
        version=VERSION,
        sex=sex,
    )

    ffill(coach_ffill, identifier, coach_model)

    return coach_model
