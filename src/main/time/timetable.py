from bisect import insort
from typing import List, Generator, Iterable

from src.main.time.timeinterval import TimeInterval


class TimeTable:
    def __init__(self, period: TimeInterval,
                 initial_intervals: Iterable[TimeInterval]=None):

        if initial_intervals is None:
            initial_intervals = []

        self._period = period

        self._intervals: List[TimeInterval] = []
        for interval in initial_intervals:
            self.insert(interval)

    @property
    def period(self) -> TimeInterval:
        return self._period

    def __iter__(self):
        return iter(self._intervals)

    def insert(self, interval: TimeInterval):
        if not self._period.intersects(interval):
            raise ValueError("Interval must be in TimeTable period")
        if self.intersects_with(interval):
            raise ValueError("Interval conflicts with timetable")

        insort(self._intervals, interval)

    def remove(self, interval: TimeInterval):
        self._intervals.remove(interval)

    def gaps(self) -> Generator[TimeInterval, None, None]:
        starts = [self._period.start] + [i.end for i in self._intervals]
        ends = [i.start for i in self._intervals] + [self._period.end]
        for start, end in zip(starts, ends):
            gap = TimeInterval(start, end)
            if gap.duration.total_seconds() != 0:
                yield gap

    def intersects_with(self, other: TimeInterval) -> bool:
        for interval in self:
            if other.intersects(interval):
                return True
        return False

    def intersections_with(self, other: TimeInterval) -> Generator[TimeInterval, None, None]:
        was_intersection = False
        for interval in self:
            if other.intersects(interval):
                was_intersection = True
                yield interval
            elif was_intersection:
                break
