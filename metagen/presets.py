from enum import Enum


class BackgroundMapsPreset(Enum):
    CartoDB_LightNoLabels = {
        "key": "cartoDB_LightNoLabels",
        "type": "wmts",
        "options": {
            "url": "https://{s}.basemaps.cartocdn.com/rastertiles/light_nolabels/{z}/{x}/{y}{r}.png"
        }}


class MapSynchronizationPreset(Enum):
    AllTrue = {"roll": True,
               "tilt": True,
               "range": True,
               "center": True,
               "heading": True,
               "boxRange": True}


class MapSettingViewPreset(Enum):
    Europe = {"center": {"lat": 45.77, "lon": 14.77}, "boxRange": 2103667}
