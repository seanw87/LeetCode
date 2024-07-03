class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(1))
print(obj.next(2))
print(obj.next(3))
print(obj.next(4))
print(obj.next(3))
print(obj.next(5))
