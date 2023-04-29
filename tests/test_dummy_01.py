"""Test dummy_01"""

import unittest
import dummy.dummy_01 as dummy


class MyTestCase(unittest.TestCase):
    """
    TestCase class
    """
    def test_lab_booking_intro(self):
        """
        Test lab booking introduction
        :return:
        """
        introduction = "Hello Users"
        self.assertEqual(introduction, dummy.lab_booking_intro())  # add assertion here


if __name__ == '__main__':
    unittest.main()
