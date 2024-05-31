from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:  # NOTE for doundary check! Otherwise, the return value will be [""] rather than []
            return []

        dig_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backTracking(dg):
            if dg == "":
                return [""]
            digit = dg[0]
            dg = dg[1:]

            return [e[0] + e[1] for e in
                    list(itertools.product(dig_letter_map[digit], backTracking(dg)))]

        return backTracking(digits)


print(Solution().letterCombinations("23"))
