

class PilotSubmarine:
    horizontal = 0
    depth = 0
    
    def __init__(self, input: str):
        self.depths = [tuple(d.split(' ')) for d in input]
        print(self.depths)

    def process_course_change(direction: str, unit: int):
        horizontal += unit if direction == "forward" else 0
        depth += unit if direction == "down" else 0
        depth -= unit if direction == "up" else 0