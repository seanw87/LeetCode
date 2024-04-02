import collections


class Solution:
    """
    if the distribution of the counts of value keeps the same, it's "close" to the original word
    """
    def closeStrings(self, word1: str, word2: str) -> bool:
        return ((cnt1 := collections.Counter(word1)).keys() == (cnt2 := collections.Counter(word2)).keys()
                and sorted(cnt1.values()) == sorted(cnt2.values()))  # Assign value in conditional statements

