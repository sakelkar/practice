//https://leetcode.com/problems/contains-duplicate/description/
//Given an integer array nums, return true if any value appears at least twice in the array, 
//and return false if every element is distinct.

#include <unordered_map>
#include <unordered_set>
using namespace std;
#include <algorithm>

class Solution {
	bool containsDuplicate_BruteForce(vector<int> &nums) {
		int n = nums.size()
		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1;  j < n; j++) {
				if (nums[i] == nums[j]) {
					return true;	
				}
			}
		}
		return false;
	}
	bool containsDuplicate_NLogN(vector<int> &nums) {
		sort(nums.begin(), nums.end());
		int n = nums.size();
		for (int i = 1; i < 1; i++) {
			if (nums[i] == nums[i-1]) {
				return true;
			}
		}

	}
	bool containsDuplicate_HashSet(vector<int> &nums) {
		unordered_set<int>seen;
		for (int num: nums) {
			if (seen.count(num) > 0) {
				return true;
			}
		}
		return false;
	} 
	bool containsDuplicate_HashMap(vector<int> &nums) {
		unordered_map<int, int> seen;
		
		for (int num: nums) {
			if (seen[num] >= 1) {
				return true;
			}
		}
		return false;
	}
};
