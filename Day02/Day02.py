import os
from Day02.PilotSubmarine import PilotSubmarine


class Day02:
    def __init__(self):
        with open(f"{os.path.dirname(__file__)}/input.txt") as F:
            courses = F.read()

        ps = PilotSubmarine(courses)

        # Part 1
        ps.process_all_course_changes()
        print(f"Part1: Final horizontal: {ps.horizontal} depth: {ps.part1_depth} result: {ps.horizontal * ps.part1_depth}")

        # Part 2
        print(f"Part2: Final horizontal: {ps.horizontal} depth: {ps.part2_depth} result: {ps.horizontal * ps.part2_depth}")


if __name__ == "__main__":
    day02 = Day02()
