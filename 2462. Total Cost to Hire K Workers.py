from typing import List
import heapq, math


class InefficientSolution:
    """
    the cause of inefficiency is due to the list operation for remain (TC: pop the last ele: O(1);
        pop the first ele: O(n));
    also the frequent heappop and heappush is not that necessary (using index value instead)
    """

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        fc = costs[:candidates]
        lc = costs[-candidates:]
        remain = costs[candidates:(len(costs) - len(lc))]
        cost = 0
        if len(fc) + len(lc) > len(costs) or len(costs) < candidates:
            fc = costs
            lc = []
            remain = []
        # print("remain: ", remain, "fc: ", fc, "lc: ", lc)
        heapq.heapify(fc)
        heapq.heapify(lc)
        for i in range(k):
            fcs = heapq.heappop(fc) if len(fc) > 0 else math.inf
            lcs = heapq.heappop(lc) if len(lc) > 0 else math.inf
            if fcs <= lcs:
                cost += fcs
                heapq.heappush(lc, lcs)
                if len(remain) > 0:
                    heapq.heappush(fc, remain.pop(0))
            else:
                cost += lcs
                heapq.heappush(fc, fcs)
                if len(remain) > 0:
                    heapq.heappush(lc, remain.pop())
            # print("-", i, fcs, lcs, cost)
        return cost


class EfficientSolution:
    """
    Use the two pointer to remain the list operation
    """
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        l, r = candidates, max(n - candidates - 1, candidates - 1)
        fc = costs[:candidates]
        lc = costs[max(n - candidates, candidates):]
        heapq.heapify(fc)
        heapq.heapify(lc)
        cost = 0
        for _ in range(k):
            if not fc:
                cost += heapq.heappop(lc)
                continue
            if not lc:
                cost += heapq.heappop(fc)
                continue
            if fc[0] <= lc[0]:
                cost += heapq.heappop(fc)
                if l <= r:
                    heapq.heappush(fc, costs[l])
                    l += 1
            else:
                cost += heapq.heappop(lc)
                if l <= r:
                    heapq.heappush(lc, costs[r])
                    r -= 1
        return cost


print(InefficientSolution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))
print(InefficientSolution().totalCost([1, 2, 4, 1], 3, 3))
