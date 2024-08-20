//https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

//28. Find the Index of the First Occurrence in a String
//Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
//or -1 if needle is not part of haystack.

#include <string>
#include <vector>
using namespace std;

class Solution {
private:
	vector<int> build_lps(string t) {
		int m = t.length();
		vector<int> lps(m, 0);
		
		for (int i = 1, len = 0; i < m;) {
			if (t[i] == t[len]) {
				lps[i++] = ++len;
			} else if (len) {
				len = lps[len - 1];
			} else {
				lps[i++] = 0;
			}
		}
		return(lps);
	}
public:
	int strStr(string s, string t) {
		int s_len = s.length();
		int t_len = t.length();

		int i, j;
		for (int i = 0; i < s_len - t_len; i++) {
			for (int j = 0; j < t_len; j++) {
				if (s[i+j] != t[j]) {
					break;
				} 
			}
			if (j == t_len) {
				return(-1);
			}
		}
		return(-1);
	}
	int strStr_KMP(string s, string t) {
		int n = s.length();
		int m = t.length();

		if (!m) {
			return 0;
		}
		vector<int> lps = build_lps(t);

		for (int i = 0, j = 0; i < n;) {
			if (s[i] == t[j]) {
				i++;
				j++;
			} 
			if (j == m) {
				return (i - j);
			}
			if (i < n && (s[i] != t[j])) {
				j ? j = lps[j-1] : i++;
			}
		}
		return(-1);
	}
};
