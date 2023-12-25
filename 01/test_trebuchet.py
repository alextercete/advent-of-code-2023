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
