from typing import Union, Type, Any, Literal, Callable, List
from pydantic import validator, Field
from shapely.geometry import MultiPolygon, MultiPoint, MultiLineString, shape, Polygon, Point, LineString, LinearRing
from shapely.geometry.base import BaseMultipartGeometry
from dataclasses import dataclass
from warnings import warn

from metagen.base import BaseModelArbitrary


@dataclass
class ShapeCollection:
    collection: List[BaseMultipartGeometry]

    @property
    def type(self):
        geom_type = set([shape.type for shape in self.collection])
        if len(geom_type) == 1:
            return geom_type.pop()
        else:
            raise ValueError(f'Geometry collection is heterogenus. Multiple geometry types {geom_type}')

    @property
    def convex_hull(self) -> Polygon:
        """Return convex hull of the collection"""
        if self.type in ['Polygon', 'MultiPolygon']:
            return MultiPolygon(self.collection).convex_hull
        elif self.type in ['LineString', 'MultiLineString', 'LinearRing']:
            return MultiLineString(self.collection).convex_hull
        elif self.type in ['Point', 'MultiPoint']:
            return MultiPoint(self.collection).convex_hull


def feature_collection(interface: dict) -> Polygon:
    """returns polygon of externa boundary from feature collection"""
    collection = ShapeCollection([shape(feature['geometry']) for feature in interface['features']])
    return collection.convex_hull


def geometry_collection(interface: dict) -> Polygon:
    collection = ShapeCollection([shape(geometry) for geometry in interface['geometries']])
    return collection.convex_hull


def polygon(interface: dict) -> Polygon:
    return shape(interface)


convert_func = {'FeatureCollection': feature_collection,
                'Polygon': polygon,
                'GeometryCollection': geometry_collection}


class Geometry(BaseModelArbitrary):
    """
    Helper class to extract geometry from inpur geodata.
    input:
        data: any type that have __geo_interface__ like shaply, geopandas etc. Works for geometry types
        FeatureCollection, Multipolygons, Polygon, Point. It do not works for heterogenic collection of shapes
    """
    data: Any

    @property
    def geom_type(self):
        return self.data.__geo_interface__['type']

    @property
    def convert_func(self) -> Callable:
        return convert_func[self.geom_type]

    @validator('data', pre=True)
    def has_geo_interface(cls, value):
        if hasattr(value, '__geo_interface__'):
            return value
        else:
            raise AttributeError('Input data has not __geo_interface__')

    def bbox(self) -> dict:
        warn('Method "geometry" called insted of "box". Pathner Place do not support plain bbox')
        return self.geometry()

    def geometry(self) -> dict:
        return self.convert_func(self.data.__geo_interface__).__geo_interface__