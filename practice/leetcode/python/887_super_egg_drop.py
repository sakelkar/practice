#https://leetcode.com/problems/super-egg-drop/

#You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.
#You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
#Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. 
#However, if the egg does not break, you may reuse it in future moves.
#Return the minimum number of moves that you need to determine with certainty what the value of f is.
#k Eggs
#n Floors
import math
class Solution:
    def recursion(self, dp, k: int, n: int) -> float: 
        #innitialize the dp array 
        #if we have only one egg then in the worst case we need to take n moves = number of floors
        if k == 1:
            return(n)

        #if we have only one floor then also max n moves are possible
        if n <= 1:
            return(n)

        if dp[k][n] != -1:
            return dp[k][n]

        ans = math.inf
        for floor in range(n):
            #if egg breaks, then you have one less egg and you will go one floow down, so call recursion by reducing both n and k
            ans_breaks = 1 + self.recursion(dp, k - 1, floor - 1) 
            #if egg does not break, then you have same number of eggs and you will go up until n, so call recursion by accordingly 
            ans_not_breaks = 1 + self.recursion(dp, k, n - floor) 
            ans = min(ans, max(ans_breaks, ans_not_breaks))

        dp[k][n] = ans
        return ans

    def superEggDrop(self, k: int, n: int) -> float:
        dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
        return self.recursion(dp, k, n)
