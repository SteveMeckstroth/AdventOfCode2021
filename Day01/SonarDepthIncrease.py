import pandas as pd


class SonarDepthIncrease:
    increased_count = 0

    def __init__(self, input: list):
        self.depths = [int(d) for d in input]

    def count_depth_increases(self, depths = None):
        depths = self.depths if depths is None else depths
        self.increased_count = 0

        for i in range(1, len(depths)):
            self.increased_count += 1 if depths[i] > depths[i-1] else 0

    def rolling_sum_depth_increases(self, window_size: int = 3):
        s = pd.Series(self.depths)
        rolling = s.rolling(window_size).sum()
        self.rolling_sums = rolling.tolist()

