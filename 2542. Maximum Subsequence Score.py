from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        hq = []
        total = res = 0

        for b, a in sorted(zip(nums2, nums1), key=lambda sk: -sk[0]):
            heapq.heappush(hq, a)
            total += a

            if len(hq) > k-1:
                total -= heapq.heappop(hq)

            if len(hq) == k-1:
                res = max(res, total*b)

        return res


print(Solution().maxScore([2, 6, 3, 5, 8, 4], [6, 9, 3, 1, 6, 3], 1))
