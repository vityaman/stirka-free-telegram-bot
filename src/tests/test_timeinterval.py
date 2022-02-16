import unittest

from src.main.time.time import time
from src.main.time.timeinterval import TimeInterval


class TestTimeInterval(unittest.TestCase):
    def test_creation(self):
        start = time('00:00')
        end = time('05:00')
        duration = end - start

        a = TimeInterval(start, end)

        self.assertEqual(a.start, start)
        self.assertEqual(a.end, end)
        self.assertEqual(a.duration, duration)

    def test_intersection(self):
        a = TimeInterval(time('00:00'), time('05:00'))
        b = TimeInterval(time('02:00'), time('06:00'))

        self.assertTrue(a.intersects(b))
        self.assertTrue(b.intersects(a))
        self.assertTrue(a.intersects(a))

    def test_equality(self):
        a = TimeInterval(time('02:00'), time('06:00'))
        b = TimeInterval(time('02:00'), time('06:00'))

        self.assertTrue(a == b)

    def test_comparison_no_exception(self):
        a = TimeInterval(time('00:00'), time('05:00'))
        b = TimeInterval(time('06:00'), time('10:00'))

        self.assertTrue(a < b)
        self.assertFalse(a > b)

    def test_comparison_exception(self):
        a = TimeInterval(time('00:00'), time('05:00'))
        b = TimeInterval(time('02:00'), time('10:00'))
        with self.assertRaises(ValueError):
            a_is_less_than_b = a < b
        with self.assertRaises(ValueError):
            a_is_greater_than_b = a > b


if __name__ == '__main__':
    unittest.main()

