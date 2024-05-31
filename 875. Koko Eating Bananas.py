from typing import List
import math


class InsufficientSolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        if h < len(piles):
            return -1
        elif h == len(piles):  # NOTE for the boundary check!
            return right
        res = right

        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours <= h:
                res = min(res, mid)
                right = mid
            elif hours > h:
                left = mid + 1

        return res


class Solution:
    """
    Instead of calculating min(mid), use left value
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        if h < len(piles):
            return -1
        elif h == len(piles):  # NOTE for the boundary check!
            return right

        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours <= h:
                right = mid
            elif hours > h:
                left = mid + 1

        return left


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
