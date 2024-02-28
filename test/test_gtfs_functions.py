import pytest
from importlib.resources import files
from gtfs_functions import Feed
from pathlib import Path


@pytest.fixture
def gtfs_path():
    # return files("test.data") / "sample-feed.zip"
    return Path("/media/jung/P590/where2share/sollfahrplan/fernverkehr.zip")


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
