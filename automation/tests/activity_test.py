import sys
from icalevents.icalevents import events

projpath = "/Users/devin/Sandbox/dsl/automation"
sys.path.append(projpath)

from src.activity import Activity


def test_activity_init():
    assert 1 == 1

