from typing import List


class DfsSolution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        city_num = len(isConnected)
        seen = set()

        prov_num = 0

        def dfs(city):
            for k, i in enumerate(isConnected[city]):
                if i == 1 and k != city and k not in seen:
                    seen.add(k)
                    dfs(k)

        for city in range(city_num):
            if city not in seen:
                seen.add(city)
                dfs(city)
                prov_num += 1

        return prov_num


class IterationSolution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        visited = {0}
        to_visit = [0]
        city_list = set(range(len(isConnected)))

        prov_num = 0

        while to_visit:
            city = to_visit.pop(0)
            print(city)
            for k, i in enumerate(isConnected[city]):
                if k != city and i == 1 and k not in visited:
                    print(k, city, i)
                    visited.add(k)
                    to_visit.append(k)

            if not to_visit:
                prov_num += 1
                if city_list - visited:
                    city = list((city_list - visited))[0]
                    visited.add(city)
                    to_visit.append(city)

        return prov_num


class BfsSolution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        prov_num = 0
        visited = set()

        for c in range(len(isConnected)):
            if c not in visited:
                to_visit = [c]
                visited.add(c)

                while to_visit:
                    city = to_visit.pop(0)
                    for k, i in enumerate(isConnected[city]):
                        if k != city and i == 1 and k not in visited:
                            visited.add(k)
                            to_visit.append(k)

                prov_num += 1

        return prov_num


print(BfsSolution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
