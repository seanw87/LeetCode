from typing import List
import math


class Solution:
    @staticmethod
    def increasingTriplet(nums: List[int]) -> bool:
        a = b = math.inf

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True

        return False
