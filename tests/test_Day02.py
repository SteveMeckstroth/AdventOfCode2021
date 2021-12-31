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
        self.assertEqual(self.ps.depth, 5, "Incorrect positive depth change")

        self.ps.process_course_change("up", 3)
        self.assertEqual(self.ps.depth, 2, "Incorrect negative depth change")

    
