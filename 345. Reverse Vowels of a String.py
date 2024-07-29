class Solution2:
    """
    Use double-pointer
    """

    @staticmethod
    def reverseVowels(s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        start, end = 0, len(s) - 1

        while start < end:
            if s[start].lower() not in vowels:
                start += 1
            elif s[end].lower() not in vowels:
                end -= 1
            else:
                # s[start], s[end] = s[end], s[start]  # Error: 'str' object does not support item assignment
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return "".join(s)


class Solution1:
    @staticmethod
    def reverseVowels(s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        last_pos = str_len = len(s)

        res_list = list(s)

        for i in range(str_len):
            if res_list[i].lower() in vowels:
                for j in range(last_pos, 0, -1):
                    if i >= j:
                        return "".join(res_list)

                    if res_list[j - 1].lower() in vowels:
                        tmp_val = res_list[j - 1]
                        res_list[j - 1] = res_list[i]
                        res_list[i] = tmp_val
                        last_pos = j - 1
                        break

        return "".join(res_list)



