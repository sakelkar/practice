//https://leetcode.com/problems/valid-anagram/description/

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
	bool isAnagram(string s, string t) {
		vector<int> charCount(26, 0);
		if (s.length() != t.length()) {
			return false;
		}
		for (int i = 0; i < s.length(); i++) {
			charCount[s[i] - 'a']++;
			charCount[t[i] - 'a']--;
		}
		return all_of(charCount.begin(), charCount.end(), [] (int x) { return x == 0;});
	} 
};
