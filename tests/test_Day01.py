import unittest
from Day01.SonarDepthIncrease import SonarDepthIncrease


class TestDay01(unittest.TestCase):
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def setUp(self):
        self.sdi = SonarDepthIncrease(self.input)

    def test_part1_increased_count(self):
        self.sdi.count_depth_increases()
        self.assertEqual(self.sdi.increased_count, 7, "Incorrect depth count")

    def test_part2_rolling_sum(self):
        self.sdi.rolling_sum_depth_increases(window_size=3)
        self.sdi.count_depth_increases(self.sdi.rolling_sums)
        self.assertEqual(self.sdi.increased_count, 5)
