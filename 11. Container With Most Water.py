from typing import List


class Solution:
    """
    clue:
          |
    |   | |
    | | | |
    →     ←
    in order to let the inner area be bigger than the outer area,
    the height of the inner element should be bigger,
    which means the smaller one of (left_value, right_value) should move in order
    to cover the possible maximum areas.
    """
    @staticmethod
    def maxArea(height: List[int]) -> int:
        hsize = len(height)
        left, right = 0, hsize - 1
        water_capacity_max = 0

        while left < right:
            lh = height[left]
            rh = height[right]

            water_capacity = (right-left) * min(lh, rh)
            water_capacity_max = max(water_capacity_max, water_capacity)
            if lh > rh:
                right -= 1
            else:
                left += 1

        return water_capacity_max


print(Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

