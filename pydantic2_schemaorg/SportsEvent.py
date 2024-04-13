from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from pydantic.v1 import Field

from pydantic2_schemaorg.Event import Event


class SportsEvent(Event):
    """Event type: Sports event.

    See: https://schema.org/SportsEvent
    Model depth: 3
    """

    type_: str = Field(default="SportsEvent", alias="@type", const=True)
    homeTeam: None | (
        list[SportsTeam | Person | str] | SportsTeam | Person | str
    ) = Field(
        default=None,
        description="The home team in a sports event.",
    )
    sport: None | (list[AnyUrl | URL | str | Text] | AnyUrl | URL | str | Text) = Field(
        default=None,
        description="A type of sport (e.g. Baseball).",
    )
    competitor: None | (
        list[SportsTeam | Person | str] | SportsTeam | Person | str
    ) = Field(
        default=None,
        description="A competitor in a sports event.",
    )
    awayTeam: None | (
        list[SportsTeam | Person | str] | SportsTeam | Person | str
    ) = Field(
        default=None,
        description="The away team in a sports event.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.SportsTeam import SportsTeam
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
