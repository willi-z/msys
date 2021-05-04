import pytest
from mdd.core import Metadata, Point


@pytest.mark.core
@pytest.mark.parametrize(
    "expected,json",
    [({}, Metadata()),
     ({"name": "test"}, Metadata("test")),
     ({"color": "blue"}, Metadata(color="blue")),
     ({"pos": {"x": 1.0, "y": 42.0}}, Metadata(pos=Point(1.0, 42.0))),
     pytest.param({"name": "test", "color": "blue", "pos": {"x": 1.0, "y": 42.0}}, Metadata(), marks=pytest.mark.xfail)],
)
def test_to_dict(json, expected):
    res = json.to_dict()
    assert res == expected


@pytest.mark.core
@pytest.mark.parametrize(
    "json, expected",
    [({}, Metadata()),
     ({"name": "test"}, Metadata("test")),
     ({"color": "blue"}, Metadata(color="blue")),
     ({"pos": {"x": 1.0, "y": 42.0}}, Metadata(pos=Point(1.0, 42.0))),
     pytest.param({"name": "test", "color": "blue", "pos": {"x": 1.0, "y": 42.0}}, Metadata(),
                  marks=pytest.mark.xfail)],
)
def test_from_dict(json, expected):
    res = Metadata()
    res.from_dict(json)
    assert res.to_dict() == expected.to_dict()

