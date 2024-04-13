from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.SoftwareApplication import SoftwareApplication


class WebApplication(SoftwareApplication):
    """Web applications.

    See: https://schema.org/WebApplication
    Model depth: 4
    """

    type_: str = Field(default="WebApplication", alias="@type", const=True)
    browserRequirements: list[str | Text] | str | Text | None = Field(
        default=None,
        description="Specifies browser requirements in human-readable text. For example, 'requires HTML5"
        "support'.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
