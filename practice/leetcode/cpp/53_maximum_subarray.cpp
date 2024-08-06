//https://leetcode.com/problems/maximum-subarray/description/
//Given an integer array nums, find the subarray
//with the largest sum, and return its sum.

using namespace std;
#include <vector>

class Solution {
public:
	int maxSubArraySum(vector<int> &nums) {
		int maxSum = INT_MIN;
		int currentSum = 0;
		for (int i = 0; i < nums.size(); i++) {
			currentSum += nums[i];
			if (currentSum > maxSum) {
				maxSum = currentSum;
			}
			if (currentSum < 0) {
				currentSum = 0;
			}	
		}
		return(maxSum);

	}
};


