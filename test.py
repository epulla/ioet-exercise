# Unit testing of util.py classes and function
# Made by Erick Pulla

# Use of a built-in testing library of python3
import unittest

from src.util import Schedule, HourRange, get_unique_pairs, format_days_to_dict, correct_time_string

class TestHourRange(unittest.TestCase):
    def test_daterange_overlapping(self):
        """
        Test if a HourRange is overlapped with another
        """
        dr1 = HourRange("10:00", "12:30")
        dr2 = HourRange("12:00", "13:00")
        self.assertTrue(dr1.is_overlapped_with(dr2), "Should be True (overlap)")
        dr3 = HourRange("13:00", "15:00")
        self.assertFalse(dr1.is_overlapped_with(dr3), "Should be False (no overlap)")

class TestSchedule(unittest.TestCase):
    def test_schedule_compare(self):
        """
        Test the number of coincidences of between two Schedules
        """
        sch1 = Schedule("DIANE", "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00")
        sch2 = Schedule("ALFONSO", "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")
        self.assertEqual(sch1.compare(sch2), 2, "Should be 2 coincidences")
        sch3 = Schedule("KIM", "MO13:00-15:00,TH02:30-04:00,SA12:00-15:00,SU21:00-22:00")
        self.assertEqual(sch1.compare(sch3), 3, "Should be 3 coincidences")

class TestGetUniquePairs(unittest.TestCase):
    def test_unique_pairs_combination(self):
        """
        Test if the function 'get_unique_pairs' is combinating pairs of unique elements (without repeated and inverted pairs)
        """
        elems = [1, 2, 3, 4]
        self.assertEqual(get_unique_pairs(elems), [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

class TestFormatDaysToDict(unittest.TestCase):
    def test_format_days_to_dict(self):
        """
        Test if the function 'format_days_to_dict' is parsing a formatted string to a dictionary (<day_code> : <HourRange>)
        """
        data = "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00"
        dicc = {'MO': HourRange("10:00", "12:00"), 'TU': HourRange("10:00", "12:00"), 'TH': HourRange("01:00", "03:00"),}
        self.assertEqual(format_days_to_dict(data), dicc)

class TestCorrectTimeString(unittest.TestCase):
    def test_correct_time_string(self):
        """
        Test if the function 'correct_time_string' is correcting a bad format of '<hours>:<minutes>'
        """
        time1 = "008:00"
        self.assertEqual(correct_time_string(time1), "10:00")
        time2 = " 18:00"
        self.assertEqual(correct_time_string(time2), "18:00")
        time3 = " 019:007 "
        self.assertEqual(correct_time_string(time3), "19:07")

if __name__ == "__main__":
    unittest.main()