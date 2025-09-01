from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return(dp[m][n])

    def longestCommonSubsequence2(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[] * (n+1) for _ in range(m+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return(dp[m][n])

    def longesetCommonSubsequence3(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[j-1][i])
        return dp[m][n]

    def longestCommonSubsequnce4(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * len(n+1) for _ in range(m+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

#+-------------------------+-----------------+---------------------+
#| Approach                | Time Complexity | Space Complexity    |
#+-------------------------+-----------------+---------------------+
#| Brute Force             | O(2^(m+n))      | O(m+n) (stack)      |
#| Memoization (Top-Down)  | O(m * n)        | O(m*n) + stack      |
#| Tabulation (Bottom-Up)  | O(m * n)        | O(m*n)              |
#| Space-Optimized DP      | O(m * n)        | O(min(m, n))        |
#+-------------------------+-----------------+---------------------+
    def lcs_bruteforce(self, s1: str, s2: str) -> int:
        def dfs(i, j):
            if len(s1) == i or len(s2) == j:
                return 0
            if s1[i] == s2[j]:
                return(1 + dfs(i+1, j+1))
            return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0,0)

    def lcs_memo(self, s1: str, s2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s1[i] == s2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[(i,j)]
        return dfs(0,0)

    def lcs_memo_lru_cache(self, s1: str, s2: str) -> int:
#        What @lru_cache(None) does
#        It wraps the function dfs(i, j) with an internal hash map (dictionary).
#        Every time you call dfs(i, j), Python checks if (i, j) is already in the cache:
#        If yes → returns the cached result (no recursion).
#        If no → computes it, stores it in the cache, then returns it.
#        So in effect, the memo table is hidden inside the cache.
#        Keys are (i, j) (the function arguments), values are the LCS lengths computed.
        @lru_cache(None)
        def dfs(i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + dfs(i+1, j+1)
            return max(dfs(i, j+1), dfs(i+1, j))
        return dfs(0,0)

    def lcs_tabulation(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

    def lcs_tabulation_space_optimized(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        prev = [0] * (n+1)

        #range(start, stop, step)
        #start = inclusive
        #stop = stop before this index
        #step = if negative then move backward and if possitive move forward
        for i in range(m-1, -1, -1):
            curr = [0] * (n+1)
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(prev[j], curr[j+1])
            prev = curr

        return prev[0]



