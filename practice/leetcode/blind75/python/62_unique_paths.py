#There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#The test cases are generated so that the answer will be less than or equal to 2 * 109.
#Example 1:
#Input: m = 3, n = 7
#Output: 28
#
#Example 2:
#Input: m = 3, n = 2
#Output: 3
#Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#1. Right -> Down -> Down
#2. Down -> Down -> Right
#3. Down -> Right -> Down
#
#Constraints:
#    1 <= m, n <= 100
from collections import defaultdict
from typing import Optional, Tuple

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths_memo(self,
                         m: int,
                         n: int,
                         memo: Optional[defaultdict[Tuple[int, int], int]] = None) -> int:
        if memo is None:
            memo = {}
        if m == 1 or n == 1:
            return 1
        if (m, n) in memo:
            return memo[(m,n)]
        memo[(m,n)] = self.uniquePaths_memo(m-1, n, memo) + self.uniquePaths_memo(m, n-1, memo)
        return memo[(m,n)]

    #uniquePaths_dp2d
    def uniquePaths_dp2d(self, m: int, n: int) -> int:
        dp = [[] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
