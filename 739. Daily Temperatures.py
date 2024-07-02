import math
from typing import List


class WrongSolution:
    """
    Using sorted array here is low efficient in Time and brings extra complexity!
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        for i, temp in enumerate(temperatures):
            temperatures[i] = [temp, i]

        temperatures.sort(key=lambda x: x[0])

        prev_temp = math.inf
        offset = 0
        res = []
        for i in range(len(temperatures), 0, -1):  # 1..len(array)
            if temp >= prev_temp:
                offset += 1
                new_index = i + offset
            elif temp < prev_temp:
                new_index = i if prev_temp != math.inf else 0
                offset = 0
            res.append(new_index)
            prev_temp = temp

        return res


print(WrongSolution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # iterate the stack, if ele in the stack(forehead with order) is smaller, then store the distance;
            # otherwise, the result value would be 0(no ele on the right is bigger)
            while stack and temperatures[stack[-1]] < temp:
                cur = stack.pop()
                ans[cur] = i - cur
            # iterate and put ele into stack
            stack.append(i)
        return ans
