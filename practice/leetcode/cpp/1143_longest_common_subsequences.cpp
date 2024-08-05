//https://leetcode.com/problems/longest-common-subsequence/description/
//
//Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
//A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
//For example, "ace" is a subsequence of "abcde".
//A common subsequence of two strings is a subsequence that is common to both strings.

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	int longestCommonSubsequence(string &s, string &t) {
		vector<vector<int>>dp(s.length()+1, vector<int>(t.length()+1, 0));

		for (int i = 0; i < s.length(); i++) {
			for (int j = 0; j < t.length(); j++) {
				dp[i+1][j+1] = ((s[i] == t[j]) ? (dp[i-1][j-1] + 1) : (max(dp[i+1][j], dp[i][j+1]))); 
			}
		}
		return(dp[s.size()][t.size()]);
	}
};
