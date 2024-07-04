from typing import List


class BetterSolution:
    """
    2024-07-04 reflection:
    note for the boundary check!
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flen = len(flowerbed)
        for i in range(flen):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == flen - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


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
            if flowerbed[i - 1] == flowerbed[i] == 1:
                return False

            if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n = n - 1

        if flowerbed[len_flowerbed - 2] == flowerbed[len_flowerbed - 1] == 0:
            flowerbed[len_flowerbed - 1] = 1
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
                        (i != len_flowerbed - 1 and not right_empty_flowerbed)):
                    return False

        return count >= n
