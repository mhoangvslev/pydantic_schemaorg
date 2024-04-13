from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import AnyUrl
from pydantic.v1 import Field
from pydantic.v1 import StrictBool
from pydantic.v1 import StrictFloat
from pydantic.v1 import StrictInt

from pydantic2_schemaorg.FinancialProduct import FinancialProduct


class LoanOrCredit(FinancialProduct):
    """A financial product for the loaning of an amount of money, or line of credit, under agreed"
     "terms and charges.

    See: https://schema.org/LoanOrCredit
    Model depth: 5
    """

    type_: str = Field(default="LoanOrCredit", alias="@type", const=True)
    renegotiableLoan: None | (
        list[StrictBool | Boolean | str] | StrictBool | Boolean | str
    ) = Field(
        default=None,
        description="Whether the terms for payment of interest can be renegotiated during the life of the loan.",
    )
    loanType: None | (
        list[AnyUrl | URL | str | Text] | AnyUrl | URL | str | Text
    ) = Field(
        default=None,
        description="The type of a loan or credit.",
    )
    gracePeriod: list[Duration | str] | Duration | str | None = Field(
        default=None,
        description="The period of time after any due date that the borrower has to fulfil its obligations before"
        "a default (failure to pay) is deemed to have occurred.",
    )
    currency: list[str | Text] | str | Text | None = Field(
        default=None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
        'currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker'
        "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies,"
        'e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'
        '(LETS) and other currency types, e.g. "Ithaca HOUR".',
    )
    loanRepaymentForm: None | (
        list[RepaymentSpecification | str] | RepaymentSpecification | str
    ) = Field(
        default=None,
        description="A form of paying back money previously borrowed from a lender. Repayment usually takes"
        "the form of periodic payments that normally include part principal plus interest in"
        "each payment.",
    )
    loanTerm: None | (list[QuantitativeValue | str] | QuantitativeValue | str) = Field(
        default=None,
        description="The duration of the loan or credit agreement.",
    )
    recourseLoan: None | (
        list[StrictBool | Boolean | str] | StrictBool | Boolean | str
    ) = Field(
        default=None,
        description="The only way you get the money back in the event of default is the security. Recourse is"
        "where you still have the opportunity to go back to the borrower for the rest of the money.",
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
    requiredCollateral: None | (list[str | Text | Thing] | str | Text | Thing) = Field(
        default=None,
        description="Assets required to secure loan or credit repayments. It may take form of third party pledge,"
        "goods, financial instruments (cash, securities, etc.)",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Duration import Duration
    from pydantic2_schemaorg.RepaymentSpecification import RepaymentSpecification
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic2_schemaorg.Thing import Thing
