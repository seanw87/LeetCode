from typing import List
import collections


class NotEfficientSolution:
    """
    NOT Efficient: each recursion TC: O(n), total TC: O(n^2)
    cause: the routes in connections contains repeated nodes(cities)
    resolution: map the routes into {node: [associated_node1, ...]}
    """
    ans = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if not connections:
            return 0

        visited_routes = []

        def dfs(city):
            for route in connections:
                if city in route:
                    if route not in visited_routes:
                        visited_routes.append(route)

                        if city == route[0]:
                            self.ans += 1
                            dfs(route[1])
                        else:
                            dfs(route[0])

        dfs(0)
        return self.ans


class DfsSolution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)  # no need to initialize
        directed = set()
        visited = set()
        for a, b in connections:
            # exchange space for time
            adjList[a].append(b)
            adjList[b].append(a)
            directed.add((a, b))

        def dfs(node):
            if node in visited:
                return 0
            res = 0
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited and (neighbor, node) not in directed:
                    res += 1
                res += dfs(neighbor)
            return res

        return dfs(0)


class DfsWithUVSolution:
    """
    build the graph first
    """
    def __init__(self):
        self.res = None

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)

        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)

        dfs(0, -1)
        return self.res


print(DfsSolution().minReorder(3, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
