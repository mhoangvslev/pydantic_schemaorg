from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.Intangible import Intangible


class GeospatialGeometry(Intangible):
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions"
     "from Geo-Spatial best practices.

    See: https://schema.org/GeospatialGeometry
    Model depth: 3
    """

    type_: str = Field(default="GeospatialGeometry", alias="@type", const=True)
    geoCoveredBy: None | (
        list[Place | GeospatialGeometry | str] | Place | GeospatialGeometry | str
    ) = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
        "a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoContains: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
        'a containing geometry to a contained geometry. "a contains b iff no points of b lie in'
        'the exterior of a, and at least one point of the interior of b lies in the interior of a".'
        "As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoOverlaps: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
        "a geometry to another that geospatially overlaps it, i.e. they have some but not all points"
        "in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoCrosses: None | (
        list[Place | GeospatialGeometry | str] | Place | GeospatialGeometry | str
    ) = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
        'a geometry to another that crosses it: "a crosses b: they have some but not all interior'
        "points in common, and the dimension of the intersection is less than that of at least one"
        'of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).',
    )
    geoIntersects: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
        "have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoWithin: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
        "a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined"
        "in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoDisjoint: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
        'are topologically disjoint: "they have no point in common. They form a set of disconnected'
        'geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)',
    )
    geoEquals: None | (
        list[Place | GeospatialGeometry | str] | Place | GeospatialGeometry | str
    ) = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
        "are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."
        '"Two geometries are topologically equal if their interiors intersect and no part of'
        'the interior or boundary of one geometry intersects the exterior of the other" (a symmetric'
        "relationship).",
    )
    geoCovers: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
        'a covering geometry to a covered geometry. "Every point of b is a point of (the interior'
        'or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).',
    )
    geoTouches: None | (
        list[GeospatialGeometry | Place | str] | GeospatialGeometry | Place | str
    ) = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
        'touch: "they have at least one boundary point in common, but no interior points." (A'
        "symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Place import Place
