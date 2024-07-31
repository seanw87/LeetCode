from typing import List


class Solution1:
    """
    traditional way
    not the most efficient (additional zero_num rounds of iteration)
    """
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        zero_num = total_zero_num = 0

        for i in range(nums_len):
            if nums[i] == 0:
                zero_num += 1
                total_zero_num += 1
            else:
                nums[i - zero_num] = nums[i]

        for j in range(total_zero_num):
            nums[nums_len - j - 1] = 0

        print(nums)


print(Solution1.moveZeroes([1, 0, 0, 2, 3, 0, 4, 0, 0, 6]))


class Solution2:
    """
    snowball method
    """
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        zero_num = 0

        for i in range(nums_len):
            if nums[i] == 0:
                zero_num += 1
            elif zero_num > 0:
                nums[i - zero_num] = nums[i]
                nums[i] = 0

        print(nums)


print(Solution2.moveZeroes([1, 0, 0, 1, 1, 0, 1]))


class Solution3:
    """
    fast-slow pointer
    """
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow: int = 0
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

        print(nums)


print(Solution3.moveZeroes([1, 0, 0, 1, 1, 0, 1]))
