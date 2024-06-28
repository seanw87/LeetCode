import math
from typing import List


class Solution:
    """
    Example: intervals = [[1,2],[2,3],[3,4],[1,3]]
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        right = math.inf
        overlaps = -1
        for intval in intervals:
            l = intval[0]
            r = intval[1]
            if l < right:
                overlaps += 1
                if r < right or right == math.inf:
                    right = r
            else:
                right = r

        return overlaps
