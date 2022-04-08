from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from enum import Enum
from metagen.base import BaseModelWithDynamicKey


class MapDefinitions(BaseModel):
    key: str
    data: dict
    name: Optional[str]


class Map(BaseModelWithDynamicKey):
    __root__: Dict[str, MapDefinitions]


class MapSynchronizationSetting(BaseModel):
    roll: bool
    tilt: bool
    range: bool
    center: bool
    heading: bool
    boxRange: bool

    @classmethod
    def from_presets(cls, preset: Enum):
        return cls.parse_obj(preset.value)


class BackgroundLayer(BaseModel):
    key: str
    type: str
    options: dict

    @classmethod
    def from_presets(cls, preset: Enum):
        return cls.parse_obj(preset.value)


class MapViewSetting(BaseModel):
    center: dict
    boxrange: int

    @classmethod
    def from_presets(cls, preset: Enum):
        return cls.parse_obj(preset.value)


class MapSetDefinitionsData(BaseModel):
    backgroundLayer: Optional[BackgroundLayer]
    view: Optional[MapViewSetting]
    viewLimits: dict = Field(default={})


class MapSetDefinitions(BaseModel):
    key: str
    data: dict
    maps: List[str]
    sync: Optional[MapSynchronizationSetting]


class MapSet(BaseModelWithDynamicKey):
    __root__: Dict[str, MapDefinitions]


class Maps(BaseModel):
    maps: Optional[Map]
    sets: Optional[MapSet]
    activeSetKey: Optional[str]