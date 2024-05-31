from typing import List
from collections import deque
import math


class BfsSolution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh_cnt = 0
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or yy < 0 or xx == rows or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        return minutes_passed if fresh_cnt == 0 else -1


class DefectiveSolution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        left, top, right, bottom = (0, 0, len(grid[0]) - 1, len(grid) - 1)

        def bfs(i, j):
            q = deque([(i, j, 0)])
            reached = lambda p, q: (p != i or q != j) and (p in (top, bottom) or q in (left, right) or (
                    [grid[p - 1][q], grid[p + 1][q], grid[p][q - 1], grid[p][q + 1]] != [1, 1, 1, 1]))
            directions = [1, 0, -1, 0, 1]
            while q:
                r, c, minutes = q.popleft()
                for z in range(len(directions)):
                    row, col = r + directions[z], c + directions[z + 1]
                    if row < 0 or col < 0 or row == bottom or col == right or grid[row][col] != 1:
                        continue
                    if reached(row, col):
                        return minutes + 1
                    grid[row][col] = 2
                    q.append(row, col, minutes + 1)
            return -1

        ans = math.inf
        for i in range(bottom + 1):
            for j in range(right + 1):
                if grid[i][j] == 1:
                    ans = min(ans, bfs(i, j))
        return ans


print(BfsSolution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
