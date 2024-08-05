#https://leetcode.com/problems/longest-common-subsequence/description/
#
#Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#For example, "ace" is a subsequence of "abcde".
#A common subsequence of two strings is a subsequence that is common to both strings.
class Solution:
    #return length of longerst common subsequence
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.lcs_memoized(s, t, 0, 0, dp)

    def lcs_memoized(self, s, t, i, j, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == s.length() or j == t.length():
            dp[i][j] = 0;
           
        if s[i] == t[j]:
            dp[i][j] = 1 + self.lcs_memoized(s, t, i+1, j+1, dp)
        else:
            dp[i][j] = max(self.lcs_memoized(s, t, i+1, j, dp), self.lcs_memoized(s, t, i, j+1, dp))
        return dp[i][j]

