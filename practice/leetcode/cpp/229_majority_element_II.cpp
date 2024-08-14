////https://leetcode.com/problems/majority-element-ii/description/
//Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
//Example 1:
//Input: nums = [3,2,3]
//Output: [3]
//Example 2:
//Input: nums = [1]
//Output: [1]
//Example 3:
//Input: nums = [1,2]
//Output: [1,2]

#include <vector>
using namespace std;

class Solution {
public:
	vector<int> majorityElementII(vector<int> nums) {
		int m1 = 0;
		int m2 = 0;
		int cm1 = 0;
		int cm2 = 0;
		vector<int> answer;

		for (int n: nums) {
			if (n == m1) {
				cm1++;
			} else if (n == m2) {
				cm2++;
			} else if (cm1 == 0) {
				cm1 = 1;
				m1 = n;
			} else if (cm2 == 0) {
				cm2 = 1;
				m2 = n;
			} else {
				cm1--;
				cm2--;
			}
		}
		cm1 = 0;
		cm2 = 0;

		for (int n : nums) {
			if (n == m1) {
				cm1++;
			} else if (n == m2) {
				cm2++;
			}
		}
		if (cm1 > nums.size()/3) {
			answer.push_back(m1);
		}
		if (cm2 > nums.size()/3) {
			answer.push_back(m2);
		}
		return(answer);
	}
};
