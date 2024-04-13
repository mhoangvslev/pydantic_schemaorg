from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.Audience import Audience


class EducationalAudience(Audience):
    """An EducationalAudience.

    See: https://schema.org/EducationalAudience
    Model depth: 4
    """

    type_: str = Field(default="EducationalAudience", alias="@type", const=True)
    educationalRole: list[str | Text] | str | Text | None = Field(
        default=None,
        description="An educationalRole of an EducationalAudience.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
