//https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
//Given an unsorted array of integers nums, return the length of the longest 
//continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
//A continuous increasing subsequence is defined by two indices l and r (l < r) 
//such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

#include <algorithm>
using namespace std;
#include <vector>

class Solution {
public:
	int findLengthOfLCIS(vector<int> &nums) {
		int max_len = 1;
		int running_len = 1;

		if (nums.size() <= 1) {
			return nums.size();
		}
		
		for (int i = 1; i < nums.size(); i++) {
			if (nums[i] > nums[i-1]) {
				running_len += 1;
			} else {
				max_len = max(max_len, running_len);
				running_len = 1;
			}
		}
		return(max(max_len, running_len));
	}
};
