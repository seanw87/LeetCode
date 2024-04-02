from typing import List


class Solution:
    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        ksum = 0
        # for i in range(k):
        #     ksum += nums[i]
        mksum = ksum = sum(nums[:k])

        for i in range(k, len(nums)):   # pay attention to the boundary value
            ksum = ksum - nums[i - k] + nums[i]
            mksum = max(mksum, ksum)

        return mksum/float(k)


print(Solution.findMaxAverage([0, 4, 0, 3, 2], 1))
