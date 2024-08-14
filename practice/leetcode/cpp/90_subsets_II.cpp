//https://leetcode.com/problems/subsets-ii/description/
//Given an integer array nums that may contain duplicates, return all possible
//subsets (the power set).
//The solution set must not contain duplicate subsets. Return the solution in any order.
//Example 1:
//Input: nums = [1,2,2]
//Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
//Example 2:
//Input: nums = [0]
//Output: [[],[0]]

#include <algorithm>
#include <string>
#include <strings.h>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
private:
	void helper(vector<int> &nums, vector<vector<int>> &answer, vector<int> &curr, int idx) {
		answer.push_back(curr);
		for (int i = idx; i < nums.size(); i++) {
			if (i > idx && nums[i] == nums[i-1]) continue;
			curr.push_back(nums[i]);
			helper(nums, answer, curr, i+1);
			curr.pop_back();
		}
	}
public:
	vector<vector<int>> subsetWithDup(vector<int> &nums) {
		vector<vector<int>> answer;
		vector<int> row;
		unordered_set<string> subset_sign;
		int indexcnt;
		string row_string;
		int j;

		sort(nums.begin(), nums.end());
		for (int i = 0; i < (1 << nums.size()); i++) {
			j = 1;
			indexcnt = 0;
			row_string = "";
			while (j) {
				if (j & 1) {
					row.push_back(nums[indexcnt]);
					row_string += to_string(nums[indexcnt]) + ',';
				}
			}
			//check whether the row_string exists already
			if (!subset_sign.count(row_string)) {
				answer.push_back(row);
				subset_sign.insert(row_string);
			}
		}
		return(answer);
	}
	//subsetWithDup_Backtracking using backtracking method
	vector<vector<int>> subsetWithDup_Backtracking(vector<int> &nums) {
		vector<vector<int>> answer;
		vector<int> curr;
		sort(nums.begin(), nums.end());
		helper(nums, answer, curr, 0);
		return(answer);
	}
};

