class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        res = []

        sl = s.split(" ")
        for i in range(len(sl), 0, -1):
            if len(sl[i-1]) > 0:
                res.append(sl[i-1])

        if len(res) == 0:
            return ""
        return " ".join(res)


print(Solution.reverseWords("a good   example"))


