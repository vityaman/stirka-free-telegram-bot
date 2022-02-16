import unittest

from src.main.time.time import interval, time
from src.main.time.timeinterval import TimeInterval
from src.main.time.timetable import TimeTable


class TestTimeTable(unittest.TestCase):
    period = interval('00:00', '23:00')

    def test_creation(self):
        table = TimeTable(self.period)
        self.assertEqual(table.period, self.period)

    def test_insertion(self):
        a = interval('00:00', '02:00')
        b = interval('05:00', '10:00')
        table = TimeTable(self.period, [a, b])

        self.assertEqual([a, b], [i for i in table])

    def test_insertion_exception(self):
        a = interval('00:00', '02:00')
        b = interval('01:00', '10:00')
        table = TimeTable(self.period, [a])

        with self.assertRaises(ValueError):
            table.insert(b)

        b = TimeInterval(b.start, time('23:30'))

        with self.assertRaises(ValueError):
            table.insert(b)

    def test_remove(self):
        a = interval('00:00', '02:00')
        b = interval('04:00', '15:00')
        c = interval('15:01', '20:00')
        table = TimeTable(self.period, [a, b, c])

        table.remove(b)

        self.assertEqual([a, c], [i for i in table])

    def test_gaps(self):
        a = interval('00:00', '02:00')
        b = interval('04:00', '15:00')
        c = interval('15:00', '20:00')
        table = TimeTable(self.period, [a, b, c])

        gaps = [i for i in table.gaps()]
        want = [TimeInterval(a.end, b.start),
                TimeInterval(c.end, table.period.end)]

        self.assertEqual(gaps, want)

    def test_gaps_empty(self):
        table = TimeTable(self.period)

        a = TimeInterval(table.period.start, table.period.end)
        table.insert(a)

        self.assertEqual([i for i in table.gaps()], [])

    def test_intersects_with_false(self):
        table = TimeTable(self.period, [
            interval('00:00', '02:00'),
            interval('04:00', '15:00'),
            interval('15:00', '20:00')
        ])

        self.assertTrue(table.intersects_with(interval('13:00', '17:00')))
        self.assertFalse(table.intersects_with(interval('03:00', '03:30')))

    def test_intersections_with(self):
        a = interval('00:00', '02:00')
        b = interval('04:00', '15:00')
        c = interval('15:00', '20:00')
        table = TimeTable(self.period, [a, b, c])

        intersections = [i for i in table.intersections_with(interval('13:00', '17:00'))]

        self.assertEqual(
            [b, c],
            intersections
        )


if __name__ == '__main__':
    unittest.main()

