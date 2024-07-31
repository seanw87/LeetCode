"""
another solution: using stack and a string, iterate s to append to string until a space is met,
then push to the stack, ignore the consective space by setting a flag, iterate this process.
At last, pop out the stack with FILO and generate the string
TC: O(n)
SC: O(n)
"""


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


