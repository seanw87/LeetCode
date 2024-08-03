from typing import List

"""
Most intuitive solution: {a:1..1}0{b:1..1}0{c:1..1}0{d:1...1}, sum up the lengths of 1s by turns

Most brutal solution is to calculate the length of each section between [0...0...0), and pick the biggest
Iterate the num array 
→   if meet first 0, set prev to current index; 
    if meet second 0, set cur to current index;
    next, set prev to the index of cur, set cur to current index
    repeat...
→   Now we have the duration for the calculation
→   if meet 1, check a lot of boundaries

Most concise solution(solution2) - very hard to understand: 
Just calculate the step offset (max_result = right - step_offset)
Iterate the num array
→   if meet 0, step i follows the current index;
→   if meet 1, step i stops at the left 1;
→   if meet latter 0, step i follows the offset between the current index;
→   if meet latter 1, a buffer k is needed since latter 1s may be longer than previous one;
    when moving on with these 1s, i should follow up until it meets 0, then buffer k needs decreasing
    when reaching the last 0, which means the new 1s will be longer than the previous one
"""


class Solution3:
    @staticmethod
    def longestSubarray(nums: List[int]) -> int:
        prev_len, cur_len = 0, 0
        max_len = 0
        zero_exist = False

        for num in nums:
            if num == 1:
                cur_len += 1
                max_len = max(max_len, cur_len + prev_len)
            elif num == 0:
                prev_len = cur_len
                cur_len = 0
                zero_exist = True

        if not zero_exist:
            max_len -= 1

        return max_len


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
    sliding window
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
