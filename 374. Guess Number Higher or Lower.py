import math


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    # suppose n==10
    if num > 6:
        return -1
    elif num < 6:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        gn = math.ceil(n / 2)  # NOTE! floor division cannot be used here! Use ceil division to avoid keeping still!
        gr = guess(gn)
        while gr != 0:
            if gr == -1:
                right = gn
            elif gr == 1:
                left = gn
            gn = left + math.ceil((right - left) / 2)
            gr = guess(gn)
        return gn


print(Solution().guessNumber(10))
