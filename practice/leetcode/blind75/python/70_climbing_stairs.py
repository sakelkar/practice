#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many *****distinct***** ways can you climb to the top?
#
#Example 1:
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps

#Example 2:
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#3. 2 steps + 1 step

#2. 1 step + 2 steps
#
#Constraints:
#    1 <= n <= 45
#Similar questions:
#https://leetcode.com/problems/decode-ways
#https://leetcode.com/problems/unique-paths/
#https://leetcode.com/problems/fibonacci-number/
#Practice them in a row for better understanding 😉

#Beginner Questions once have a look:
#
#    Two Sum
#    Roman to Integer
#    Palindrome Number
#    Maximum Subarray
#    Remove Element
#    Contains Duplicate
#    Add Two Numbers
#    Majority Element
#    Remove Duplicates from Sorted Array

#    Valid Anagram
#    Group Anagrams
#    Practice them in a row for better understanding and please Upvote for more questions.
from functools import lru_cache

class Solution:
    #the most important thing in this proble in difference between step and ways
    #way is the path or progression
    #step is the actual physicaly movement in that way

    #so now when you want to go step 3, there are following ways possible
    #way1. Step 2 + 1 step
    #way2. Step 1 + 1 step + 1 step
    #way3. Step 1 + 2 step

    #extending this logic further we can say that, to reach step(i) we have logically following number of ways
    #1 step + step(i-1)
    #2 steps + step(i-2)
    #3 step(i-2) + 1 step + 1 step is also another way but its not distinct since #1 covers that way
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs2(n-1) + self.climbStairs2(n-2)

    def climbStairs3(self, n: int) -> int:
        memo = {}

        def recurse(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]

            memo[n] = recurse(n-1) + recurse(n-2)
            return memo[n]

        return recurse(n)
