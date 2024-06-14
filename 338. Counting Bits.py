from typing import List
import math
from math import sqrt


class Solution:
    """
    TC: O(nlogn)
    Got MLE since "cur" and "prev_start" are both SC(O(n))
    """

    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        prev_start = start = [1, 2]
        m = n // 2
        for _ in range(1, m):
            cur = prev_start + [x + 1 for x in prev_start]
            start += cur
            prev_start = cur
        drop_num = int(math.pow(2, m + 1)) - n - 1
        return [0, 1] + start[:(len(start) - drop_num)]


print(Solution().countBits(8))


class BitSolution:
    """
    for each i in n:
        "0 1" "10 11" "100 101 110 111" "1000 1001 1010 1011 1100 1101 1110 1111"
        shift one bit to the right, then we can get the num of bits of the previous round,
        the last bit can be easily check with & 1
    """

    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res


print(BitSolution().countBits(8))


class DPSolution:
    """
    similar idea with big solution,
    just turn the bit action to the offset action (move bit to right equals minus offset*2)
    """

    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            res[i] = res[i - offset] + 1
        return res
