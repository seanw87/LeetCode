import collections
from typing import List


class Solution1:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        arr_set = {}
        rev_arr_set = {}
        for ele in arr:
            if ele in arr_set:
                arr_set[ele] += 1
            else:
                arr_set[ele] = 0

        for ele in arr_set:
            rev_arr_set[arr_set[ele]] = ele

        if len(arr_set) == len(rev_arr_set):
            return True
        else:
            return False


class Solution2:
    """
    use python3 collections.Counter()
    not very efficient
    """
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))


class Solution3:
    """
    use python3 collections.Counter() with another way(directly check the counts of each element)
    """
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        seen = set()
        for freq in collections.Counter(arr).values():
            if freq in seen:
                return False
            seen.add(freq)
        return True
