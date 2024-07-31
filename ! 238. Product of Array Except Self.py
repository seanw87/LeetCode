from typing import List

"""
e.g. [1, 2, 3, 4]
pre_val: [1, 1, 2, 6, 24]  # accumulative multiply from left to right
post_val: [1, 4, 12, 24, 24]  # accumulative multiply from right to left
res = [pre[3] * post[0], pre[2] * post[1], pre[1] * post[2], pre[0] * post[3]]
"""
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
