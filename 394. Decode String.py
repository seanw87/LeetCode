class Solution:
    @staticmethod
    def decodeString(s: str) -> str:
        stack = []

        snum = ""
        ss = ""
        for l in s:
            if l.isnumeric():
                snum += l
            if l.isalpha():
                ss += l
            if l == "[":
                # or use tuple (ss, int(snum)) so that only one operation of append and pop is needed
                stack.append(ss)
                stack.append(int(snum))
                ss = ""
                snum = ""
            if l == "]":
                tssn = stack.pop()
                pss = stack.pop()
                ss = pss + tssn * ss
        return ss


print(Solution.decodeString("3[a2[bc]]"))
