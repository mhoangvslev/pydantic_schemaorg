from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field
from pydantic.v1 import StrictFloat
from pydantic.v1 import StrictInt

from pydantic2_schemaorg.Grant import Grant


class MonetaryGrant(Grant):
    """A monetary grant.

    See: https://schema.org/MonetaryGrant
    Model depth: 4
    """

    type_: str = Field(default="MonetaryGrant", alias="@type", const=True)
    funder: None | (
        list[Organization | Person | str] | Organization | Person | str
    ) = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
        "contribution.",
    )
    amount: None | (
        list[StrictInt | StrictFloat | Number | MonetaryAmount | str]
        | StrictInt
        | StrictFloat
        | Number
        | MonetaryAmount
        | str
    ) = Field(
        default=None,
        description="The amount of money.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
