import math


class Solution1:
    """
    2024-07-04 Some Reflection:
    Key point: use iteration to check whether they have common base
    TIME: O(n)

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
    2024-07-04 Reflection:
    Key assumption: AB = BA, suppose len(A) >= len(B), then A = Bxxx...B → AB = Bxxx...BB → A = Bxxx...BB → ...
    Conslusion: A and B must share a common base!
    problem turns into: n * base = m * base, here base is the greatest common divisor

    gcd solution
    """

    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_val = math.gcd(len(str1), len(str2))
        return str1[:gcd_val]


print(Solution2().gcdOfStrings("ABAABAABAABA", "ABAABA"))
