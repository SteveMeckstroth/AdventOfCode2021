import unittest
from Day02.PilotSubmarine import PilotSubmarine


class TestDay02(unittest.TestCase):
    input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    def setUp(self):
        self.ps = PilotSubmarine(self.input)

    def test_process_course_change(self):
        self.ps.process_course_change("forward", 5)
        self.assertEqual(self.ps.horizontal, 5, "Incorrect forward change")

        self.ps.process_course_change("down", 5)
        self.assertEqual(self.ps.part1_depth, 5, "Incorrect positive depth change")

        self.ps.process_course_change("up", 3)
        self.assertEqual(self.ps.part1_depth, 2, "Incorrect negative depth change")

    def test_process_all_course_changes(self):
        self.ps.process_all_course_changes()
        self.assertEqual(self.ps.horizontal, 15, "Incorrect processing of horizontal changes")
        self.assertEqual(self.ps.part1_depth, 10, "Incorrect processing of depth changes for Part1")
        self.assertEqual(self.ps.part2_depth, 60, "Incorrect processing of depth for Part2")

    
