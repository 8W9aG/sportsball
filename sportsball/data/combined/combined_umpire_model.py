"""Combined umpire model."""

from typing import Any

from ..umpire_model import VERSION, UmpireModel
from .ffill import ffill
from .most_interesting import more_interesting


def create_combined_umpire_model(
    umpire_models: list[UmpireModel],
    identifier: str,
    umpire_ffill: dict[str, dict[str, Any]],
) -> UmpireModel:
    """Create an umpire model by combining many umpire models."""
    name = None
    sex = None
    birth_date = None
    age = None
    birth_address = None
    high_school = None
    for umpire_model in umpire_models:
        name = more_interesting(name, umpire_model.name)
        sex = more_interesting(sex, umpire_model.sex)
        birth_date = more_interesting(birth_date, umpire_model.birth_date)
        age = more_interesting(age, umpire_model.age)
        birth_address = more_interesting(birth_address, umpire_model.birth_address)
        high_school = more_interesting(high_school, umpire_model.high_school)
    if name is None:
        raise ValueError("name is null")

    umpire_model = UmpireModel.model_construct(
        identifier=identifier,
        name=name,
        sex=sex,
        birth_date=birth_date,
        age=age,
        birth_address=birth_address,
        high_school=high_school,
        version=VERSION,
    )

    ffill(umpire_ffill, identifier, umpire_model)

    return umpire_model
