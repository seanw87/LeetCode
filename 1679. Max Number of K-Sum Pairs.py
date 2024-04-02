from typing import List


class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:
        d = {}
        hit = 0

        for num in nums:
            if num in d and d[num] > 0:
                hit += 1
                d[num] -= 1
            else:
                if (k-num) not in d:
                    d[k - num] = 1
                else:
                    d[k - num] += 1

        return hit


print(Solution.maxOperations([3, 1, 3, 4, 3], 6))
