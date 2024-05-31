from typing import List
import heapq
import random


class SortedSolution:
    """
    Most obvious solution: use Sorted function
    TC: O(nlogn)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k > len(nums):
            return -1
        sorted_num = sorted(nums, reverse=True)
        return sorted_num[k - 1]


class HeapqSolution:
    """
    Heapq or priority queue, min-heap by default
    TC: O(nlogn)
    NOT most efficient to use heapq.nlargest!
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return list(heapq.nlargest(k, nums))[k - 1]


class HeapqEfficientSolution:
    """
    heapq: push k elements to heapq then push the rest of elements(heappush) and pop the smallest at the same time(heappushpop)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for n in nums:
            if len(h) == k:
                heapq.heappushpop(h, n)
            else:
                heapq.heappush(h, n)

        return h[0]


class QuickSortSolution:
    """
    Manually sort the list using quick sort
    Although shuffled the nums, still got TLE
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        random.shuffle(nums)
        low, high = 0, len(nums) - 1

        # Quicksort example: [20, 10, 30, 90, 40, 60]
        # pivot==60, i==0, j==0: [20, 10, 30, 90, 40, 60]
        # pivot==60, i==1, j==1: [20, 10, 30, 90, 40, 60]
        # pivot==60, i==2, j==2: [20, 10, 30, 90, 40, 60]
        # pivot==60, i==2, j==3: [20, 10, 30, 90, 40, 60]
        # pivot==60, i==3, j==4: [20, 10, 30, 40, 90, 60]
        # pivot==60, i==3, j==4, exchange arr[i+1] and arr[high]: [20, 10, 30, 40, 60, 90]
        # i+1 == 4
        # right side [90]
        # left side [20, 10, 30, 40]
        # right side [40]
        # left side [20, 10, 30]
        # right side [30]
        # left side [20, 10]
        # pivot==10, i==0, j==0: [20, 10]
        # pivot==10, i==0, j==0, exchange arr[i+1] and arr[high]: [10, 20]
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quicksort(arr, low, high):
            if low < high:
                # Element smaller than pivot are on the left
                # Element bigger than pivot are on the right
                pivot = partition(arr, low, high)
                quicksort(arr, low, pivot - 1)
                quicksort(arr, pivot + 1, high)
            return arr

        sorted_num = quicksort(nums, low, high)
        return sorted_num[high - k + 1]


print(SortedSolution().findKthLargest([5, 2, 8, 4, 6, 2, 5], 2))
print(HeapqSolution().findKthLargest([5, 2, 6, 4, 8, 2, 5], 2))
print(QuickSortSolution().findKthLargest([20, 10, 30, 90, 40, 60], 2))
