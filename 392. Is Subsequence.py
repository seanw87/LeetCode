class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if s == "":
            return True

        sp = 0

        for i in range(len(t)):
            if t[i] == s[sp]:
                sp += 1

            if sp == len(s):
                return True

        return False


print(Solution.isSubsequence('abc', 'aababdrgabcakdf'))
