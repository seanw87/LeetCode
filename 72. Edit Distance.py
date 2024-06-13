class Solution:
    """
    For this question, the purpose of "dp" is to get the minimum operations required to convert s1 to s2
    the actions are:
        insert(pos+1), delete(pos-1), replace(pos no change)
    the states:
        dp[i][j] represents the result, in which contains dim i for s1 and dim j for s2
    the state machine(how dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1] turn into dp[i][j]):
        INSERT(insert the char of s2[j-1] to s1[i]):
            dp[i][j-1] + 1
        DELETE(delete s1[i-1]):
            dp[i-1][j] + 1
        REPLACE(replace s1[i-1] with s2[i-1]):
            dp[i-1][j-1] + 1
        NO ACTION(when dp[i][j] == dp[i-1][j-1])
    In conclusion:
        dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
                 = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    Initial state:
        dp[i][0] = i
        dp[0][j] = j
    """

    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for c in range(len2 + 1):
            dp[0][c] = c
        for r in range(len1 + 1):
            dp[r][0] = r

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[len1][len2]


print(Solution().minDistance("horse", "ros"))


class DPSCOptimizedSolution:
    """
    SC optimization tips: on the i-th step only dp[i] and dp[i-1] are needed
    """
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        prev = list(range(len2 + 1))
        cur = [0] * (len2 + 1)

        for i in range(1, len1 + 1):
            cur[0] = i
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = min(prev[j-1], prev[j], cur[j-1]) + 1
            prev = cur
            cur = [0] * (len2 + 1)

        return prev[-1]

