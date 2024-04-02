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


class Solution2:
    """
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
