"""
Stack way is opposite to the normal way in terms of the direction of iteraction
"""


class Solution2:
    """
    Stack way
    """

    @staticmethod
    def removeStars(s: str) -> str:
        ans = []
        for i in s:
            if i == "*":
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)


class Solution1:
    """
    traditional iterating way
    """

    @staticmethod
    def removeStars(s: str) -> str:
        l = len(s) - 1
        d = 0
        res = []

        while l >= 0:
            if s[l] == "*":
                d += 1
            elif d > 0:
                d -= 1
            else:
                res.append(s[l])
            l -= 1

        return "".join(list(reversed(res)))


print(Solution1.removeStars("leet**cod*e"))
