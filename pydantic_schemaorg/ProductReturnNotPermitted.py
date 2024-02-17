from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ProductReturnEnumeration import ProductReturnEnumeration


class ProductReturnNotPermitted(ProductReturnEnumeration):
    """ProductReturnNotPermitted: product returns are not permitted.

    See: https://schema.org/ProductReturnNotPermitted
    Model depth: 5
    """
    type_: str = Field(default="ProductReturnNotPermitted", alias='@type', const=True)
    
