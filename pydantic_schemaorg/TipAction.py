from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic_schemaorg.TradeAction import TradeAction


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    See: https://schema.org/TipAction
    Model depth: 4
    """
    type_: str = Field(default="TipAction", alias='@type', const=True)
    recipient: Optional[Union[List[Union['Organization', 'Audience', 'ContactPoint', 'Person', str]], 'Organization', 'Audience', 'ContactPoint', 'Person', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Person import Person
