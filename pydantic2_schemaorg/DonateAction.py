from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.TradeAction import TradeAction


class DonateAction(TradeAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic"
     "reasons.

    See: https://schema.org/DonateAction
    Model depth: 4
    """

    type_: str = Field(default="DonateAction", alias="@type", const=True)
    recipient: None | (
        list[Organization | Audience | ContactPoint | Person | str]
        | Organization
        | Audience
        | ContactPoint
        | Person
        | str
    ) = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Organization import Organization
    from pydantic2_schemaorg.Audience import Audience
    from pydantic2_schemaorg.ContactPoint import ContactPoint
    from pydantic2_schemaorg.Person import Person
