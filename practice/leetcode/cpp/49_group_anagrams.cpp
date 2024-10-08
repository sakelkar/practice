//https://leetcode.com/problems/group-anagrams/description/

//Given an array of strings strs, group the anagrams together. You can return the answer in any order.
//An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
//Example 1:
//Input: strs = ["eat","tea","tan","ate","nat","bat"]
//Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//Example 2:
//Input: strs = [""]
//Output: [[""]]
//Example 3:
//Input: strs = ["a"]
//Output: [["a"]]

#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
	vector<vector<string>> groupAnagrams(vector<string> &strs) {
		unordered_map<string, vector<string>> map;

		for (auto x: strs) {
			string word = x;
			sort(word.begin(), word.end());
			map[word].push_back(x);
		}
		vector<vector<string>> answer;
		for (auto x: map) {
			answer.push_back(x.second);
		}
		return answer;
	}
};
