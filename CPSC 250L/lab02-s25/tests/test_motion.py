import unittest
import copy
from src import motion


class TestMotion(unittest.TestCase):
    """
        Test Class for motion.py
    """

    def test_motion_empty(self):
        start = (1, 2)
        motions = []
        end = motion.motion(start, motions)
        self.assertEqual(start, end, msg="Empty motions - stay at start")

    def test_motion_zero(self):
        start = (1, 2)
        motions = [(0, 0)]
        end = motion.motion(start, motions)
        self.assertEqual(start, end, msg="Zero motions - stay at start")

    def test_motion_one_dx(self):
        start = (1, 2)
        motions = [(1, 0)]
        end = motion.motion(start, motions)
        self.assertEqual((2, 2), end, msg="One motion - move")

    def test_motion_one_dy(self):
        start = (1, 2)
        motions = [(0, 1)]
        end = motion.motion(start, motions)
        self.assertEqual((1, 3), end, msg="One motion - move")

    def test_motion_two(self):
        start = (1, 2)
        motions = [(0, 1), (1, 0)]
        end = motion.motion(start, motions)
        self.assertEqual((2, 3), end, msg="Two motions - move")

    def test_motion_three(self):
        start = (1, 2)
        motions = [(0, 1), (1, 0), (2, 3)]
        end = motion.motion(start, motions)
        self.assertEqual((4, 6), end, msg="Three motions - move")

    def test_motion_four(self):
        start = (1, 2)
        motions = [(0, 1), (0, 0), (2, 4), (-1, -1)]
        end = motion.motion(start, motions)
        self.assertEqual((2, 6), end, msg="Four motions - move")

    def test_motion_four2(self):
        start = (1, 2)
        motions = [(0, -1), (0, -1), (-2, 0), (0, -1)]
        end = motion.motion(start, motions)
        self.assertEqual((-1, -1), end, msg="Four motions - move")


if __name__ == '__main__':
    unittest.main()
