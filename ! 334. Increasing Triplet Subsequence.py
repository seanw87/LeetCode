from typing import List
import math

"""
solution: value pass
if right value is smaller than left value, then assign a to the smaller value
if right value is not smaller than a and smaller than b, then assign b to the smaller value
else (right value is bigger than b, and b is bigger than a) return true 
"""
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
