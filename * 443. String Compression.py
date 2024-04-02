from typing import List


class Solution:
    @staticmethod
    def compress(chars: List[str]) -> int:
        cnt, chars_pos, charslen = 1, 0, len(chars)

        if charslen == 1:
            return charslen

        for i in range(1, charslen):
            if chars[i] == chars[i - 1]:
                cnt += 1

            a, b = chars[i], chars[i - 1]   # !
            if a != b or i == charslen - 1:
                chars[chars_pos] = b
                chars_pos += 1
                if cnt > 1:
                    for num_str in str(cnt):
                        chars[chars_pos] = num_str
                        chars_pos += 1
                cnt = 1

                if chars_pos <= i == charslen - 1 and a != b:
                    chars[chars_pos] = a
                    chars_pos += 1

        return chars_pos


print(Solution.compress(["a", "b", "c"]))


class Solution2:
    """
    double pointer solution
    """
    @staticmethod
    def compress(chars: List[str]) -> int:
        walker, runner = 0, 0
        while runner < len(chars):

            chars[walker] = chars[runner]
            count = 1

            while runner + 1 < len(chars) and chars[runner] == chars[runner + 1]:
                runner += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[walker + 1] = c
                    walker += 1

            runner += 1
            walker += 1

        return walker


print(Solution2.compress(["a", "b", "c"]))

