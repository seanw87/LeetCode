import math
from typing import List
import bisect


class InsufficientSolution:
    """
    There's no need to compare the success value in each pv vs. success condition
    Not clear logic!
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        potions_len = len(potions)
        res = []

        for k, spell in enumerate(spells):
            mid = (potions_len - 1) // 2
            pl, pr = 0, potions_len - 1
            res.append(0)
            while pl <= pr:
                pv = spell * potions[mid]
                if pv >= success:
                    if (mid > 0 and spell * potions[mid - 1] < success) or mid == 0:
                        res[k] = potions_len - mid
                        break
                    pr = mid
                    mid = pl + (pr - pl) // 2
                else:
                    if (mid < potions_len - 1 and spell * potions[mid + 1] >= success) or mid == potions_len - 1:
                        res[k] = potions_len - mid - 1
                        break
                    pl = mid
                    mid = pl + (pr + 1 - pl) // 2
                if pl == pr:
                    break
        return res


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        start, end = 0, len(potions)
        potions.sort()
        for i in range(len(spells)):
            while start <= end:
                mid = int((start + end) / 2)  # key for binary search
                if potions[mid] * spells[i] < success:
                    start = mid + 1  # key for binary search
                else:
                    end = mid - 1  # key for binary search
            spells[i] = len(potions) - start
        return spells


class BisectSolution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        m = len(potions)
        for spell in spells:
            pairs.append(m - bisect.bisect_left(potions, math.ceil(success / spell)))  # bisect approach
        return pairs


print(InsufficientSolution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
