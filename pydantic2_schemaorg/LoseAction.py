from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.AchieveAction import AchieveAction


class LoseAction(AchieveAction):
    """The act of being defeated in a competitive activity.

    See: https://schema.org/LoseAction
    Model depth: 4
    """

    type_: str = Field(default="LoseAction", alias="@type", const=True)
    winner: list[Person | str] | Person | str | None = Field(
        default=None,
        description="A sub property of participant. The winner of the action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
