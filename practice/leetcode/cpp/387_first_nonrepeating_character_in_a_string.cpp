//https://leetcode.com/problems/first-unique-character-in-a-string/solutions/

//Given a string s, find the first non-repeating character in it and return its index.
//If it does not exist, return -1

#include <string>
#include <unordered_map>
#include <utility>
using namespace std;

class Solution {
public:
	int firstUniqueChar(string s) {
		int min_index = s.length();
		unordered_map<char, pair<int, int>>map;
		for (int i = 0; i < s.length(); i++) {
			map[s[i]].first++;
			map[s[i]].second = i;
		}
		for (const auto [c, p] : map) {
			if (p.first == 1) {
				min_index = min(min_index, p.second);
			}
		}
		return(min_index < s.length() ? min_index : -1);

	}
	//
	int firstUniqueChar2(string s) {
		unordered_map<char, int>	 map;
		for (const auto c: s) {
			map[c]++;
		}
		for (int i = 0; i < s.length(); i++) {
			if (map[s[i]] == 1) {
				return(i);
			}
		}
		return(-1);
	}
};
