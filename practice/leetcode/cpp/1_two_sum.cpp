//https://leetcode.com/problems/two-sum/

//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//You may assume that each input would have exactly one solution, and you may not use the same element twice.
//You can return the answer in any order.

#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int> &nums, int target) {
		unordered_map<int, int> prevMap;
		vector<int> answer;
		int complement;
		int n = nums.size();

		for (int i = 0; i < n; i++) {
			complement = target - nums[i];
			if (prevMap.find(complement) != prevMap.end()) {
				answer.push_back(prevMap[complement]);
				answer.push_back(i);
				break;
			} else {
				prevMap.insert({nums[i], i});
			}
		}
		return(answer);
	}
};
