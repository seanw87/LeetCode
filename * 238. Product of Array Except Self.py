from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        pre_val = post_val = 1
        res = []

        for i in range(len(nums)):
            res.append(pre_val)
            pre_val *= nums[i]
        for j in range(len(nums), 0, -1):
            res[j-1] *= post_val
            post_val *= nums[j - 1]
        return res


print(Solution.productExceptSelf([1, 2, 3, 4]))
