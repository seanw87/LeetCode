"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false
otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List


class Solution1:
    @staticmethod
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_flowerbed = len(flowerbed)

        if len_flowerbed == 1:
            if (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0):
                return True
            else:
                return False

        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n = n - 1

        for i in range(1, len_flowerbed - 1):
            if flowerbed[i-1] == flowerbed[i] == 1:
                return False

            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n = n - 1

        if flowerbed[len_flowerbed-2] == flowerbed[len_flowerbed-1] == 0:
            flowerbed[len_flowerbed-1] = 1
            n = n - 1

        if n <= 0:
            return True


class Solution2:
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        len_flowerbed = len(flowerbed)
        count = 0

        for i in range(len_flowerbed):
            # Pay attention for boundary check
            left_empty_flowerbed = i == 0 or flowerbed[i - 1] == 0
            right_empty_flowerbed = i == len_flowerbed - 1 or flowerbed[i + 1] == 0

            if flowerbed[i] == 0:
                if left_empty_flowerbed and right_empty_flowerbed:
                    flowerbed[i] = 1
                    count += 1
                    if count == n:
                        return True
            else:
                # Issue: the original flowerbed should be confirmed whether following the "no-adjacent-flowers" rule.
                if ((i != 0 and not left_empty_flowerbed) or
                        (i != len_flowerbed-1 and not right_empty_flowerbed)):
                    return False

        return count >= n
