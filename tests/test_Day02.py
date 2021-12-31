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

    
