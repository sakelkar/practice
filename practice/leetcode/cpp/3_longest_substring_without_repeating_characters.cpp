//https://leetcode.com/problems/longest-substring-without-repeating-characters/

//Given a string s, find the length of the longest
//substring without repeating characters.

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		unordered_set<char> charSet;
		int left;
		int max_length = 0;
		//traverse the string
		for (int right = 0; right < s.length(); right++) {
			if (charSet.count(s[right]) == 0) {
				charSet.insert(s[right]);
				max_length = max(max_length, right - left + 1);
			} else {
				while (charSet.count(s[right])) {
					charSet.erase(s[right]);
					left++;
				}
				charSet.insert(s[right]);
			}
		}
		return(max_length);
	}	
	//lengthOfLongestSubstring2
	int lengthOfLongestSubstring2(string s) {
		unordered_map<char, int> map;
		int left = 0;
		int max_length = 0;

		for (int right = 0; right < s.length(); right++) {
			if (map.count(s[right]) > 0) {
				left = max(left, map[s[right]] + 1);
			}
			map[s[right]] = right;
			max_length = max(max_length, right - left + 1);
		}
		return(max_length);

	}
};
