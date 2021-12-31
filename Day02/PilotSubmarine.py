

class PilotSubmarine:
    horizontal = 0
    depth = 0
    
    def __init__(self, input: str):
        self.depths = [tuple(d.split(' ')) for d in input.split('\n')]
        print(self.depths)

    def process_course_change(self, direction: str, unit: int):
        self.horizontal += unit if direction == "forward" else 0
        self.depth += unit if direction == "down" else 0
        self.depth -= unit if direction == "up" else 0