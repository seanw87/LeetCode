from typing import List


class Solution1:
    """
    use prefix string
    """
    @staticmethod
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for num_candies in range(len(candies)):
            res.append(candies[num_candies] + extraCandies >= max_candies)

        return res


print(Solution1().kidsWithCandies([1, 2, 3, 4, 5, 6, 7], 5))
