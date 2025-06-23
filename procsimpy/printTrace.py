from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from procsimpy.EventData import EventData

# TODO format spaceing based on maxSimTime


# If this remains this small just move to Base
# May be changeing to using logger instead of printing
# and only file will make more sense
def printTrace(event: EventData) -> None:
    timecode = f'@T:{event.time:>4.2f}'
    print(f'{timecode} -> {event.phrase()}')
