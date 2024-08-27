//#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description
//Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
//of a given target value
//If target is not found in the array, return [-1, -1]
//You must write an algorithm with O(log n) runtime complexity
//Example 1:

//Input: nums = [5,7,7,8,8,10], target = 8
//Output: [3,4]
//Example 2:

//Input: nums = [5,7,7,8,8,10], target = 6
//Output: [-1,-1]
//Example 3:

//Input: nums = [], target = 0
//Output: [-1,-1]

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
	int my_lower_bound(vector<int> &nums, int low, int high, int target) {
		int mid = 0;
		while (low <= high) {
			mid = (low + (high - low)/2);
			if (nums[mid] < target) {
				low = mid + 1;
			} else {
				high = mid;
			}
		}
		return(low);
	}
public:
	vector<int>	 searchRange(vector<int> nums, int target) {
		int low = 0, high = nums.size() - 1;
		int starting_position = my_lower_bound(nums, low, high, target);
		int ending_position = my_lower_bound(nums, low, high, target + 1);
		if (starting_position < nums.size() and nums[starting_position] == target) {
			return {starting_position, ending_position};
		}
		return {-1, -1};
	}
	vector<int> searchRange2(vector<int> nums, int target) {
		int starting_position = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
		int ending_position = lower_bound(nums.begin(), nums.end(), target+1) - nums.begin();
		if (starting_position == ending_position) {
			return {-1, -1};
		} else {
			return {starting_position, ending_position - 1};
		}
	}
};


