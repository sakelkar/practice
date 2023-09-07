#https://leetcode.com/problems/regular-expression-matching/
#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#    '.' Matches any single character.​​​​
#    '*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(n, m):
            if (n, m) in cache:
                return cache[(n,m)]
            if n >= len(s) and m >= len(p):
                return True
            if m >= len(p):
                return False
            match = ((m < len(p)) and ((p[m] == s[n]) or (p[m] == '.'))) 
            if ((m+1 < len(p)) and (p[m+1] == '*')):
                cache[(n, m)] = ((dfs(n, m+2)) or ((match) and (dfs(n+1, m))))
                return cache[(n, m)]
            if match:
                cache[(n, m)] = dfs(n+1, m+1) 
                return cache[(n, m)]
            cache[(n, m)] = False
            return False
        return(dfs(0, 0))
