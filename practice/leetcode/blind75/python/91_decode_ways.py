#You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
#
#"1" -> 'A'
#"2" -> 'B'
#
#...
#"25" -> 'Y'
#"26" -> 'Z'
#
#However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").
#
#For example, "11106" can be decoded into:
#    "AAJF" with the grouping (1, 1, 10, 6)
#    "KJF" with the grouping (11, 10, 6)
#    The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
#
#Note: there may be strings that are impossible to decode.
#Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
#The test cases are generated so that the answer fits in a 32-bit integer.

#possible encodings are A = 1 and Z = 26
#so at any position there are two possible ways
#next character if its not zero, and next 2 characters if the next character is not zero
#ways[i]

#s can have zeros or leading zeros
#so first go past all the leading zeros
#you cannot sort s since that will change the s itself and interpretation of s will not be correct

#so at each step i, decoding two ways is possible if i not equal to 0
#and s[i-1:i+1] is between 10 and 26
from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == 0:
                return 0

            res = dfs(i+1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            return(res)

        return(dfs(0))

#start from index 0
#at every index, there are two ways and you need to accumulate count received from both the ways.
#those two ways are, take the current index and move forward: way 1. get the number from way1
#take next two character and move forward: way 2. get the number from way2

from functools import lru_cache

class Solution2:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0

            #way 1
            res = dfs(i+1)

            #way 2, next two characters at current index. so take i and i+1
            if (i+1) < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            return(res)

        return(dfs(0))

    def numDecodings2(self, s: str) -> int:
        def dfs(i):
            if i == len(i):
                return 1
            if int(s[i]) == 0:
                return 0

            res = dfs(i+1)

            if (i+1) > len(s) and 10 <= int(s[i]) <= 26:
                res += dfs(i+2)

            return(res)
        return(dfs(0))

    def numDecodings3(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0

            res = dfs(i+1)

            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            memo[i] = res
            return memo[i]
        return(dfs(0))
