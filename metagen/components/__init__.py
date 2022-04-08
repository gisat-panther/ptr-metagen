from pydantic import BaseModel
from typing import Optional
from metagen.components.map import Maps


class ViewComponent(BaseModel):
    longDescription: str


class TimelineComponents(BaseModel):
    timelinePeriod: dict
    timelineLayers: dict


class StateComponents(BaseModel):
    View: Optional[ViewComponent]
    Timeline: Optional[TimelineComponents]


class State(BaseModel):
    maps: Optional[Maps]
    components: Optional[StateComponents]
