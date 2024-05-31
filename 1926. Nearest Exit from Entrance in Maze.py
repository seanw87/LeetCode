from functools import lru_cache
from typing import List
import math
from collections import deque


class WrongDfsSolution:
    """
    Using memoization here(@lru_cache(None)) is not right because it denies the result from other route
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze or not entrance or maze[entrance[0]][entrance[1]] == "+":
            return 0
        # up, down, left, right - four direction detection
        left, top = (0, 0)
        right = len(maze[0]) - 1
        bottom = len(maze) - 1

        @lru_cache(None)
        def dfs(r, c):
            if r < 0 or c < 0 or r > bottom or c > right or maze[r][c] == "+":
                return math.inf

            if (r != entrance[0] or c != entrance[1]) and (r in (top, bottom) or c in (left, right)):
                return 0

            maze[r][c] = "+"
            ans = 1 + min(dfs(r, c - 1), dfs(r, c + 1), dfs(r - 1, c),
                          dfs(r + 1, c))
            maze[r][c] = "."
            return ans

        res = dfs(entrance[0], entrance[1])
        return -1 if res >= math.inf else res


class TleDfsSolution:
    """
    Not using memoization will cause Time Limit Exceeded(TLE) error, yet the logic is right, it's just not efficient.
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze or not entrance or maze[entrance[0]][entrance[1]] == "+":
            return 0
        # up, down, left, right - four direction detection
        left, top = (0, 0)
        right = len(maze[0]) - 1
        bottom = len(maze) - 1

        def dfs(r, c):
            if r < 0 or c < 0 or r > bottom or c > right or maze[r][c] == "+":
                return math.inf

            if (r != entrance[0] or c != entrance[1]) and (r in (top, bottom) or c in (left, right)):
                return 0

            maze[r][c] = "+"
            ans = 1 + min(dfs(r, c - 1), dfs(r, c + 1), dfs(r - 1, c),
                          dfs(r + 1, c))
            maze[r][c] = "."
            return ans

        res = dfs(entrance[0], entrance[1])
        return -1 if res >= math.inf else res


class BfsSolution:
    """
    Best solution here.
    Each process contains at most four steps, the shortest path is with the minimum amount of the processes.
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n, infi = len(maze), len(maze[0]), int(1e5)
        reached = lambda p, q: (not p==x or not q==y) and (p==0 or q==0 or p==m-1 or q==n-1)
        q, ans = deque(), 0
        q.append((x, y, ans))
        directions = [1, 0, -1, 0, 1]
        while q:
            row, col, ans = q.popleft()
            for i in range(4):
                r, c = row + directions[i], col + directions[i+1]
                if r<0 or c<0 or r==m or c==n or maze[r][c]=='+':
                    continue
                if reached(r, c):  # one step each call, the first to reach the exit is the shortest path
                    return ans+1
                maze[r][c] = '+'
                q.append((r, c, ans+1))
        return -1


print(DfsSolution().nearestExit(
    [[".", "+", "+", "+", ".", ".", ".", "+", "+"], [".", ".", "+", ".", "+", ".", "+", "+", "."],
     [".", ".", "+", ".", ".", ".", ".", ".", "."], [".", "+", ".", ".", "+", "+", ".", "+", "."],
     [".", ".", ".", ".", ".", ".", ".", "+", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "+", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "+"],
     ["+", ".", ".", ".", "+", ".", ".", ".", "."]], [5, 6]))
