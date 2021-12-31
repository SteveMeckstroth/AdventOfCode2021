import os
from Day01.SonarDepthIncrease import SonarDepthIncrease


class Day02:
    def __init__(self):
        with open(f"{os.path.dirname(__file__)}/input.txt") as F:
            depths = F.readlines()

        sdi = SonarDepthIncrease(depths)

        # Part 1
        sdi.count_depth_increases()
        print(f"Part1: Total number of times depth increased: {sdi.increased_count}")

        # Part 2
        sdi.rolling_sum_depth_increases(window_size=3)
        sdi.count_depth_increases(sdi.rolling_sums)
        print(f"Part2: Total number of times rolling sum increased: {sdi.increased_count}")


if __name__ == "__main__":
    day01 = Day01()
