from typing import List


class BfsSolution:
    """
    Here's the key prompt: "you can take all of them with you to unlock the other rooms"
    NOT exactly BFS, but more for Iterative
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        keys = [0]
        seen = set(keys)

        while keys:
            i = keys.pop(0)
            for key in rooms[i]:  # to ensure the seen keys are in the order of the seen rooms
                if key not in seen:
                    keys.append(key)
                    seen.add(key)
                    if len(seen) == len(rooms):
                        return True

        return len(seen) == len(rooms)


class SetIterSolution:
    """
    Use Set to iterate
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        keys = {0}
        seen = set(keys)

        while keys:
            i = keys.pop()
            seen.add(i)
            keys |= set(rooms[i]) - seen

        return len(seen) == len(rooms)


class DfsSolution:
    res = False

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        seen = set()

        def dfs(curRoom):
            if curRoom not in seen:
                seen.add(curRoom)
                for key in rooms[curRoom]:
                    dfs(key)

        dfs(0)
        return len(seen) == len(rooms)


# Iterative space-optimized with a use of 1000-bit integer to track visited rooms

# Iterative with a list of visited rooms


print(DfsSolution().canVisitAllRooms([[1], [2], [], [3]]))
