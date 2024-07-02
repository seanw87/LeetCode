import math
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)  # points.sort(key = lambda x: x[0])
        res = 0

        right = math.inf

        for point in points:
            l, r = point[0], point[1]
            if l > right or right == math.inf:
                res += 1
                right = r
            else:
                right = min(right, r)

        return res


print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
