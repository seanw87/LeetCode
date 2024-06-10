from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        min_sum = (k*(k+1)/2)
        if n < min_sum:
            return []

        biggest = n - (min_sum - k)
        self.res = []

        def backtracking(nums, curList, k, n):
            if k == 0 and n == 0:
                self.res.append(curList)
            if k < 0 or n < 0:
                return
            for i in range(len(nums)):
                if nums[i] > biggest:
                    break
                backtracking(nums[i+1:], curList+[nums[i]], k-1, n-nums[i])

        backtracking(list(range(1, 10)), [], k, n)
        return self.res