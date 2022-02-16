from datetime import datetime, timedelta


class TimeInterval:
    def __init__(self, start: datetime, end: datetime):
        if end < start:
            raise ValueError("Start should be before the end (start <= end)")
        self._start = start
        self._end = end

    def intersects(self, other: 'TimeInterval') -> bool:
        return self._end > other._start and other._end > self._start

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def end(self) -> datetime:
        return self._end

    @property
    def duration(self) -> timedelta:
        return self._end - self._start

    @staticmethod
    def at(start: datetime, duration: timedelta) -> 'TimeInterval':
        return TimeInterval(start, start + duration)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TimeInterval):
            return False
        return self._start == other._start and self._end == other._end

    def __repr__(self) -> str:
        return f'Interval(start={self._start}, end={self._end})'

    def __hash__(self) -> int:
        return hash((self._start, self._end))

    def __gt__(self, other: 'TimeInterval') -> bool:
        if self.intersects(other):
            raise ValueError("Can't compare intersected intervals")
        return self._start > other._end

    def __lt__(self, other: 'TimeInterval') -> bool:
        if self.intersects(other):
            raise ValueError("Can't compare intersected intervals")
        return self._end < other._start
