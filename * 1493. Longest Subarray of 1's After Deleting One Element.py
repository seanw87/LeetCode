from typing import List


class Solution1:
    @staticmethod
    def longestSubarray(nums: List[int]) -> int:
        zk = {'prev': -1, 'cur': -1}
        mon = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                if -1 == zk['prev']:
                    zk['prev'] = right
                elif -1 == zk['cur']:
                    zk['cur'] = right
                else:
                    zk['prev'] = zk['cur']
                    zk['cur'] = right

            if nums[right] == 1:
                if zk['cur'] != -1:
                    on = right - zk['prev'] - 1
                else:
                    on = right + 1 if zk['prev'] == -1 else right
                mon = max(mon, on)

        if zk['prev'] == zk['cur'] == -1:
            mon = max(0, mon - 1)

        return mon


print(Solution1.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))


class Solution2:
    """
    sliding window:
    i: 1 before first 0
    j: 1 after second 0
    """
    @staticmethod
    def longestSubarray(nums: List[int]) -> int:
        k = 1
        i = 0
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i


print(Solution2.longestSubarray([1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]))
