from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field
from pydantic.v1 import StrictFloat
from pydantic.v1 import StrictInt

from pydantic2_schemaorg.OrganizationRole import OrganizationRole


class EmployeeRole(OrganizationRole):
    """A subclass of OrganizationRole used to describe employee relationships.

    See: https://schema.org/EmployeeRole
    Model depth: 5
    """

    type_: str = Field(default="EmployeeRole", alias="@type", const=True)
    baseSalary: None | (
        list[
            (
                StrictInt
                | StrictFloat
                | Number
                | PriceSpecification
                | MonetaryAmount
                | str
            )
        ]
        | StrictInt
        | StrictFloat
        | Number
        | PriceSpecification
        | MonetaryAmount
        | str
    ) = Field(
        default=None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    salaryCurrency: list[str | Text] | str | Text | None = Field(
        default=None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217))"
        "used for the main salary information in this job posting or for this employee.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.PriceSpecification import PriceSpecification
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic2_schemaorg.Text import Text
