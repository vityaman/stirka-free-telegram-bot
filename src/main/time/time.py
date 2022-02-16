from datetime import datetime

from src.main.time.timeinterval import TimeInterval


def time(iso_time: str, iso_date='2012-12-12') -> datetime:
    return datetime.fromisoformat(iso_date + ' ' + iso_time)


def interval(iso_time_start: str, iso_time_end: str, iso_date='2012-12-12'):
    return TimeInterval(
        start=time(iso_time_start, iso_date),
        end=time(iso_time_end, iso_date)
    )
