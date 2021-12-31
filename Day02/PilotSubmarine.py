

class PilotSubmarine:
    horizontal = 0
    part1_depth = 0
    part2_depth = 0
    aim = 0
    
    def __init__(self, input: str):
        self.course_changes = [tuple(d.split(' ')) for d in input.split('\n')]

    def process_course_change(self, direction: str, unit: int):
        self.horizontal += unit if direction == "forward" else 0
        self.part1_depth += unit if direction == "down" else 0
        self.part1_depth -= unit if direction == "up" else 0

        self.aim += unit if direction == "down" else 0
        self.aim -= unit if direction == "up" else 0
        self.part2_depth += self.aim * unit if direction == "forward" else 0

    def process_all_course_changes(self):
        for direction, unit in self.course_changes:
            self.process_course_change(direction, int(unit))