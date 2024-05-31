import heapq


class HeapqSmallestInfiniteSet:

    def __init__(self):
        self.hq = list(range(1, 1001))
        heapq.heapify(self.hq)
        self.popped = set()

    def popSmallest(self) -> int:
        res = -1
        if len(self.hq) > 0:
            res = heapq.heappop(self.hq)
            self.popped.add(res)
        return res

    def addBack(self, num: int) -> None:
        if num in self.popped:
            heapq.heappush(self.hq, num)
            self.popped.remove(num)


class PointerSmallestInfiniteSet:
    def __init__(self):
        self.s = set()
        self.p = 0

    def popSmallest(self) -> int:
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        self.p += 1
        return self.p

    def addBack(self, num: int) -> None:
        if num < 1 or num > 1000:
            return
        if num <= self.p:
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = HeapqSmallestInfiniteSet()
param_1 = obj.popSmallest()
obj.addBack(1)
print(param_1)

obj2 = PointerSmallestInfiniteSet()
param_2 = obj2.popSmallest()
obj.addBack(2)
print(param_2)