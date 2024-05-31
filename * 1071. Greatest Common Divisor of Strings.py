"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

import math


class Solution1:
    """
    use prefix string
    """
    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        for i in range(min(len1, len2), 0, -1):
            if len1 % i > 0 or len2 % i > 0:
                continue
            n1, n2 = len1 // i, len2 // i  # 地板除
            base = str1[:i]
            if str1 == base * n1 and str2 == base * n2:
                return base
        return ""


print(Solution1().gcdOfStrings("ABAABAABAABA", "ABAABA"))
print(Solution1().gcdOfStrings("ABABABAB", "ABAB"))


class Solution2:
    """
    gcd solution
    """
    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_val = math.gcd(len(str1), len(str2))
        return str1[:gcd_val]


print(Solution2().gcdOfStrings("ABAABAABAABA", "ABAABA"))
