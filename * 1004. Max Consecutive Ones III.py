from typing import List


class Solution1:
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        nums_len = len(nums)
        max_con = 0

        for i in range(nums_len):
            if (i == 0 and nums[i] == 1) or (i > 0 and nums[i - 1] == 0 and nums[i] == 1):
                j = 0
                con = 0
                while i + con < nums_len:
                    if nums[i + con] == 0:
                        j += 1
                        if j == k + 1:
                            break
                    con += 1
                max_con = max(max_con, con)

        j = 0
        con = 0
        for i in range(nums_len - 1, -1, -1):
            if nums[i] == 0:
                j += 1
                if j == k + 1:
                    break
                if i == 0:
                    con += 1
                    break
            if j <= k:
                con += 1
        max_con = max(max_con, con)
        return max_con


print(Solution1.longestOnes([0, 0, 0, 1], 4))


class Solution2:
    """
    sliding window!
    """
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1


print(Solution1.longestOnes([0, 0, 0, 1], 4))
