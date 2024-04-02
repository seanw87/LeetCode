from typing import List


class Solution1:
    """
    traditional way
    """

    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res1 = []
        res2 = []

        for num in nums1_set:
            if num not in nums2_set:
                res1.append(num)
        for num in nums2_set:
            if num not in nums1_set:
                res2.append(num)

        return [res1, res2]


print(Solution1.findDifference([1, 2, 3], [2, 4, 6]))


class Solution2:
    """
    use python set.difference()
    """
    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return [nums1_set.difference(nums2_set), nums2_set.difference(nums1_set)]

