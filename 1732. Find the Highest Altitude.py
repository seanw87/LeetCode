from typing import List


class Solution:
    @staticmethod
    def largestAltitude(gain: List[int]) -> int:
        ha = 0
        max_ha = 0
        glen = len(gain)

        for i in range(glen):
            ha += gain[i]
            max_ha = max(max_ha, ha)

        return max_ha


print(Solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
