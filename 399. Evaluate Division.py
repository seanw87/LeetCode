from typing import List
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        def buildGraph():
            for e, v in zip(equations, values):
                a, b = e
                graph[a].append((b, v))
                graph[b].append((a, 1 / v))

        def findQuery(query):
            a, b = query

            if b not in graph or a not in graph:
                return -1.0

            queue = collections.deque([(a, 1.0)])
            visited = set()

            while queue:
                front, cur_product = queue.popleft()
                if front == b:
                    return cur_product
                visited.add(front)

                for neighbour, value in graph[front]:
                    if neighbour not in visited:
                        queue.append((neighbour, cur_product * value))

            return -1.0

        buildGraph()
        return [findQuery(q) for q in queries]


class BrilliantSolution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(collections.defaultdict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        for k in graph:
            graph[k][k] = 1.0
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]
        return [graph[x].get(y, -1.0) for x, y in queries]


print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
