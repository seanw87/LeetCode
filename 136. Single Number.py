from typing import List
import numpy


class NotProperSolution:
    """
    Problem of this solution: the res represents the value of 2^n, in which I should get n,
    yet it seems not accurate to do the sqrt in python (**0.5, math.sqrt(), cmath.sqrt() all tried)
    """

    def singleNumber(self, nums: List[int]) -> int:
        res = 0b0

        def setBit(bit, offset):
            return bit | (1 << offset)

        def clearBit(bit, offset):
            return bit & ~(1 << offset)

        for num in nums:
            if (res >> num) & 1 == 1:
                res = clearBit(res, num)
            else:
                res = setBit(res, num)
            print(num, res)

        return res**0.5 if res > 1 else 1


print(NotProperSolution().singleNumber([1, 1, 5, 3, 3, 6, 6, 10, 10]))


class Solution:
    """
    Bit-wise XOR(exclusive OR) operation
    """
    def singleNumber(self, nums: List[int]) -> int:
        res = 0b0
        for num in nums:
            res ^= num
        return res


print(Solution().singleNumber([1, 1, 5, 3, 3, 6, 6, 10, 10]))


class SetSolution:
    """
    Not most efficient for SC because we don't know how many elements we need to store in the set
    """
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.add(num)
        return res.pop()
