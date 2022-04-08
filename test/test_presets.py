import pytest
from metagen.presets import BackgroundMaps
from metagen.components.map import BackgroundLayer


def test_background_preset():
    assert BackgroundLayer.from_presets(BackgroundMaps.CartoDB_LightNoLabels)