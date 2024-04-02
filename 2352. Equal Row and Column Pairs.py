import collections
from typing import List


class Solution1:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        # srow = []
        mcol = {}
        # scol = []
        mcrow = {}
        # mccol = {}
        res = 0

        for row in grid:
            # srow.append(tuple(row)) # list is not hashable, so cannot be added into set, but tuple works
            if tuple(row) not in mcrow:  # list can neither be added into map, but tuple can
                mcrow[tuple(row)] = 0
            mcrow[tuple(row)] += 1
            for i in range(len(row)):
                if i not in mcol:
                    mcol[i] = []
                mcol[i].append(row[i])
        for ele in mcol:
            # scol.append(tuple(mcol[ele]))
            # if ele not in mccol:
            #     mccol[ele] = 0
            # else:
            #     mccol[ele] += 1

            if tuple(mcol[ele]) in mcrow:
                res += mcrow[tuple(mcol[ele])]
        return res

        # set will deduplicate, should avoid using
        # srow = set(srow)
        # scol = set(scol)
        # return len(srow.intersection(scol))


print(Solution1.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))


class Solution2:
    """
    use defaultdict() to create and initialize the dictionary automatically
    """

    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        m = collections.defaultdict(int)  # initialize the dict with default value type (here is int)
        mcol = collections.defaultdict(list)  # initialize the dict with default value type (here is list)
        res = 0

        for row in grid:
            m[str(row)] += 1
            for i in range(len(row)):
                mcol[i].append(row[i])

        for ele in mcol:
            if str(mcol[ele]) in m:
                res += m[str(mcol[ele])]
        return res


print(Solution2.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
