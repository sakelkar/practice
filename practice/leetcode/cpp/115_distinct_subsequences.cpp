//https://leetcode.com/problems/distinct-subsequences/description/
//Given two strings s and t, return the number of distinct subsequences of s which equals t.
//The test cases are generated so that the answer fits on a 32-bit signed integer.
using namespace std;
#include <string>
#include <vector>
class Solution {
public:
	int recur(string s, string t, int n, int m) {
		if (n == 0 && m == 0) {
			return 1;
		}
		if (n == 0) {
			return 0;
		}
		if (m == 1) {
			return 1;
		}
		if (s[n-1] == t[m-1]) {
			return recur(s, t, n-1, m-1) + recur(s, t, n-1, m);
		}
		return recur(s, t, n-1, m);
	}
	int numDistinctSubsequences_Recursive(string s, string t) {
		int n = s.size();
		int m = t.size();
		return recur(s, t, n, m);
		
	}
	int recur_memoization(string &s, string &t, int n, int m, vector<vector<int>>dp) {
		if (n == 0 && m == 0) {
			return 1;
		}
		if (m == 0) {
			return 1;
		}
		if (n == 0) {
			return 0;
		}
		if (dp[n][m] != -1) {
			return dp[n][m];
		}
		if (s[n-1] == t[m-1]) {
			return dp[n][m] = recur_memoization(s, t, n-1, m-1, dp) + recur_memoization(s, t, n-1, m, dp);
		}
		return dp[n][m] = recur_memoization(s, t, n-1, m, dp);
	}
    int numDistinctSubsequences_Memoization(string s, string t) {
		int  n = s.size();
		int m = t.size();
		vector<vector<int>>dp(n+1, vector<int>(m+1,-1));
		return recur_memoization(s, t, n, m, dp);
    }
	int numDistinctSubsequences_Tabulation(string s, string t) {
		int n = s.size();
		int m = t.size();
		vector<vector<double>> dp(n+1, vector<double>(m+1, 0));

		int i, j;

		for (int i = 0; i <= n; i++) {
			dp[i][0] = 1;
		}

		for (i = 1; i <= n; i++) {
			for (j = 1; j <= m; j++) {
				if (s[i-1] == t[j-1]) {
					dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
				} else {
					dp[i][j] = dp[i-1][j];
				}
			}
		}
		return(dp[n][m]);
	}
};
