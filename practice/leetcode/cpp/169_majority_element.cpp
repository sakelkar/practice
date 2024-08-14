//https://leetcode.com/problems/majority-element/description/
//Given an array nums of size n, return the majority element.
//The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
//Example 1:
//Input: nums = [3,2,3]
//Output: 3
//Example 2:
//Input: nums = [2,2,1,1,1,2,2]
//Output: 2

#include <vector>
using namespace std;

class Solution {
	int majorityElement(vector<int> &nums) {
		int maj = nums[0];
		int maj_count = 1;
		for (int i = 1; i < nums.size(); i++) {
			if (nums[i] == maj) {
				maj_count++;
			} else {
				maj_count--;
				if (maj_count == 0) {
					maj = nums[i];
					maj_count = 1;
				}
			}
		}
		return(maj);
	}
};

