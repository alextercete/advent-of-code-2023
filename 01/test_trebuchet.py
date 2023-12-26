import unittest

from trebuchet import recover_calibration

class RecoverCalibrationTests(unittest.TestCase):
    def test_two_digit_number(self):
        value = recover_calibration("13")
        self.assertEqual(value, 13)

    def test_long_number(self):
        value = recover_calibration("123456")
        self.assertEqual(value, 16)

    def test_alphanumeric(self):
        value = recover_calibration("abc123def")
        self.assertEqual(value, 13)

    def test_single_digit(self):
        value = recover_calibration("1abcde")
        self.assertEqual(value, 11)

    def test_spelled_out(self):
        value = recover_calibration("one2three")
        self.assertEqual(value, 13)

    def test_spelled_out_overlapped(self):
        value = recover_calibration("eighthree")
        self.assertEqual(value, 83)
