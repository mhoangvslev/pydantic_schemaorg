from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field
from pydantic.v1 import StrictBool

from pydantic2_schemaorg.StructuredValue import StructuredValue


class ShippingRateSettings(StructuredValue):
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is"
     "designed for publication on an URL that may be referenced via the [[shippingSettingsLink]]"
     "property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished"
     "and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

    See: https://schema.org/ShippingRateSettings
    Model depth: 4
    """

    type_: str = Field(default="ShippingRateSettings", alias="@type", const=True)
    shippingDestination: None | (
        list[DefinedRegion | str] | DefinedRegion | str
    ) = Field(
        default=None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
        "ways, e.g. postalCode ranges.",
    )
    doesNotShip: None | (
        list[StrictBool | Boolean | str] | StrictBool | Boolean | str
    ) = Field(
        default=None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    freeShippingThreshold: None | (
        list[MonetaryAmount | DeliveryChargeSpecification | str]
        | MonetaryAmount
        | DeliveryChargeSpecification
        | str
    ) = Field(
        default=None,
        description="A monetary value above (or at) which the shipping rate becomes free. Intended to be used"
        "via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching this [[ShippingRateSettings]].",
    )
    shippingLabel: list[str | Text] | str | Text | None = Field(
        default=None,
        description="Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within"
        "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    shippingRate: None | (list[MonetaryAmount | str] | MonetaryAmount | str) = Field(
        default=None,
        description="The shipping rate is the cost of shipping to the specified destination. Typically, the"
        "maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.",
    )
    isUnlabelledFallback: None | (
        list[StrictBool | Boolean | str] | StrictBool | Boolean | str
    ) = Field(
        default=None,
        description="This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]]"
        "or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]]"
        "published by the same merchant, when referenced by a [[shippingSettingsLink]] in those"
        "settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel"
        "(for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]),"
        "since this property is for use with unlabelled settings.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DefinedRegion import DefinedRegion
    from pydantic2_schemaorg.Boolean import Boolean
    from pydantic2_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic2_schemaorg.DeliveryChargeSpecification import (
        DeliveryChargeSpecification,
    )
    from pydantic2_schemaorg.Text import Text
