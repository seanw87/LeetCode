class Solution1:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        slen = len(s)
        if k > slen:
            return False

        vl = [1 for i in range(k) if s[i] in ['a', 'e', 'i', 'o', 'u']]
        max_vowel_num = vowel_num = sum(vl)

        for i in range(k, slen):
            if s[i-k] in ['a', 'e', 'i', 'o', 'u']:
                vowel_num -= 1
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel_num += 1
            max_vowel_num = max(max_vowel_num, vowel_num)

        return max_vowel_num


class Solution2:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        slen = len(s)
        if k > slen:
            return False

        vl = [1 for i in range(k) if s[i] in vowels]
        max_vowel_num = vowel_num = sum(vl)

        for i in range(k, slen):
            if s[i-k] in vowels:
                vowel_num -= 1
            if s[i] in vowels:
                vowel_num += 1
            max_vowel_num = max(max_vowel_num, vowel_num)

        return max_vowel_num
