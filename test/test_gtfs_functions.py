import pytest
from importlib.resources import files
from gtfs_functions import Feed


@pytest.fixture
def gtfs_path():
    return files("test.data") / "sample-feed.zip"


def test_compute_line_freq(gtfs_path):
    time_windows = [0, 6, 9, 15.5, 19, 22, 24]

    feed = Feed(
        str(gtfs_path),
        time_windows=time_windows,
    )
    line_freq = feed.lines_freq


def test_compute_bus_segments(gtfs_path):
    time_windows = [0, 6, 9, 15.5, 19, 22, 24]

    feed = Feed(
        str(gtfs_path),
        time_windows=time_windows,
    )
    with pytest.raises(ValueError, match="No shapes"):
        segments_gdf = feed.segments
