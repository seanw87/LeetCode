class Solution:
    @staticmethod
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        word1_len = len(word1)
        word2_len = len(word2)
        for i in range(word1_len):
            merged += word1[i]

            if i <= word2_len - 1:
                merged += word2[i]

        if word2_len > word1_len:
            for j in range(word2_len - word1_len):
                merged += word2[word1_len + j]

        return merged


print(Solution().mergeAlternately("abasdfasdfasdfc", ""))


class Solution1(object):
    """
    One Pointer Solution
    """
    @staticmethod
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)


print(Solution1().mergeAlternately("abasdfasdfasdfc", ""))