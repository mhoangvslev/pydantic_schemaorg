from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic_schemaorg.Trip import Trip


class TrainTrip(Trip):
    """A trip on a commercial train line.

    See: https://schema.org/TrainTrip
    Model depth: 4
    """
    type_: str = Field(default="TrainTrip", alias='@type', const=True)
    departurePlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The platform from which the train departs.",
    )
    trainNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unique identifier for the train.",
    )
    trainName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name of the train (e.g. The Orient Express).",
    )
    arrivalStation: Optional[Union[List[Union['TrainStation', str]], 'TrainStation', str]] = Field(
        default=None,
        description="The station where the train trip ends.",
    )
    arrivalPlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The platform where the train arrives.",
    )
    departureStation: Optional[Union[List[Union['TrainStation', str]], 'TrainStation', str]] = Field(
        default=None,
        description="The station from which the train departs.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.TrainStation import TrainStation
