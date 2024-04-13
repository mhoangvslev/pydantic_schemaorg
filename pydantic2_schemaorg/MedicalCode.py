from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.CategoryCode import CategoryCode
from pydantic2_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    See: https://schema.org/MedicalCode
    Model depth: 4
    """

    type_: str = Field(default="MedicalCode", alias="@type", const=True)
    codeValue: list[str | Text] | str | Text | None = Field(
        default=None,
        description="A short textual code that uniquely identifies the value.",
    )
    codingSystem: list[str | Text] | str | Text | None = Field(
        default=None,
        description="The coding system, e.g. 'ICD-10'.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
