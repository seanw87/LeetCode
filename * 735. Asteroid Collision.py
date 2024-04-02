from typing import List


class Solution:
    """
    an additional nested interation is needed because asteroids collides with each other again and again
    """

    @staticmethod
    def asteroidCollision(asteroids: List[int]) -> List[int]:
        la = len(asteroids)
        res = []

        for i in range(la):
            # only when a positive value on the left and a negative value on the right may cause the collision
            while len(res) > 0 and asteroids[i] < 0 < res[-1]:
                if res[-1] == -asteroids[i]:
                    res.pop()
                    break
                elif res[-1] > -asteroids[i]:
                    break
                elif res[-1] < -asteroids[i]:
                    res.pop()
                    continue
            else:
                res.append(asteroids[i])

        return res


print(Solution.asteroidCollision([5, 10, -5]))


class Solution_w:
    """
    deprecated: wrong idea
    """

    @staticmethod
    def asteroidCollision(asteroids: List[int]) -> List[int]:
        la = len(asteroids) - 1
        res = []

        while la >= 0:
            res_lastval = None if len(res) == 0 else res[len(res) - 1]
            if res_lastval and 0 > res_lastval and abs(asteroids[la]) >= abs(res_lastval):
                res.pop()
            if res_lastval and 0 > res_lastval and abs(asteroids[la]) <= abs(res_lastval):
                la -= 1
            else:
                res.append(asteroids[la])
                la -= 1

        return list(reversed(res))


print(Solution.asteroidCollision([10, 2, -5]))
