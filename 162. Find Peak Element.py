from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)
        if right == 1 or nums[0] > nums[1]:
            return 0
        if nums[right - 1] > nums[right - 2]:
            return right - 1
        while left < right:  # be careful with boundaries
            mid = (right + left) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid - 1]:
                right = mid  # be carefull with left&right
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1  # be carefull with left&right

        return -1


print(Solution().findPeakElement([2, 1]))
