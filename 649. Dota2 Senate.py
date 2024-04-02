import collections


class Solution1:
    """
    Attention: low efficiency solution: O(nlogn)
    """

    @staticmethod
    def predictPartyVictory(senate: str) -> str:
        rd = {"R": "D", "D": "R"}
        rd_fullname = {"R": "Radiant", "D": "Dire"}
        sq = collections.deque(list(senate))  # or [*senate]

        while len(set(sq)) == 2:
            t = sq.popleft()
            # for s in sq:
            #     if s == rd[t]:
            #         sq.remove(s)
            #         break
            sq.remove(rd[t])  # remove the first occurence of s (TC should be O(n)
            sq.append(t)

        return rd_fullname[sq[0]]


print(Solution1.predictPartyVictory("RRDDDD"))


class Solution2:
    """
    TC: O(n)
    """

    @staticmethod
    def predictPartyVictory(senate: str) -> str:
        np = len(senate)
        ri = collections.deque()
        di = collections.deque()
        for i in range(np):
            ri.append(i) if senate[i] == "R" else di.append(i)

        while len(ri) > 0 and len(di) > 0:
            np += 1
            if (rindex := ri.popleft()) < (dindex := di.popleft()):
                ri.append(np)
            else:
                di.append(np)

        return "Radiant" if len(ri) > 0 else "Dire"
