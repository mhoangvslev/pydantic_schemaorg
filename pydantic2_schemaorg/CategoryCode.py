from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from pydantic.v1 import Field

from pydantic2_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See: https://schema.org/CategoryCode
    Model depth: 4
    """

    type_: str = Field(default="CategoryCode", alias="@type", const=True)
    codeValue: list[str | Text] | str | Text | None = Field(
        default=None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: None | (
        list[AnyUrl | URL | CategoryCodeSet | str]
        | AnyUrl
        | URL
        | CategoryCodeSet
        | str
    ) = Field(
        default=None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.CategoryCodeSet import CategoryCodeSet
