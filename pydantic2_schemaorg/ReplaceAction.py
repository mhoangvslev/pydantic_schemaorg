from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.UpdateAction import UpdateAction


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object.

    See: https://schema.org/ReplaceAction
    Model depth: 4
    """

    type_: str = Field(default="ReplaceAction", alias="@type", const=True)
    replacee: list[Thing | str] | Thing | str | None = Field(
        default=None,
        description="A sub property of object. The object that is being replaced.",
    )
    replacer: list[Thing | str] | Thing | str | None = Field(
        default=None,
        description="A sub property of object. The object that replaces.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Thing import Thing
