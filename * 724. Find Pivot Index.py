from typing import List


class Solution:
    """
    ! wrong solution: 左右累加的量不一定会递增，反而可能会递减，所以不能用双指针根据值的大小来判断滑动方向
    """
    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        lnums = len(nums)
        lindex, rindex = 0, lnums - 1
        lsum, rsum = 0, nums[rindex]

        while lindex < rindex - 1:
            if lsum + nums[lindex] > rsum:
                rindex -= 1
                rsum += nums[rindex]
            elif lsum + nums[lindex] <= rsum:
                lsum += nums[lindex]
                lindex += 1
            if lsum == rsum and lindex == rindex - 1:
                return lindex

        return -1


print(Solution.pivotIndex([2, 1, -1]))


class Solution2:
    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)

        for i in len(nums):
            rsum -= nums[i]
            if rsum == lsum:
                return i
            lsum += nums[i]
        return -1