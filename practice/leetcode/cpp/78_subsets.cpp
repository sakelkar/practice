//https://leetcode.com/problems/subsets/description/
//Given an integer array nums of unique elements, return all possible
//subset (the power set).
//The solution set must not contain duplicate subsets. Return the solution in any order.

#include <vector>
using namespace std;

class Solutions {
public:
	vector<vector<int>> subsets(vector<int> &nums) {
		vector<vector<int>> answer;
		vector<int> row;
		
		for (int i = 0; i < (1 << nums.size()); i++) {
			int j = i;
			int indexcnt = 0;
			while(j) {
				if (j & 1) {
					row.push_back(nums[indexcnt]);
				}
				indexcnt++;
				j >>= 1;
			}
			row.clear();
			answer.push_back(row);
		}
		return(answer);
	} 
};
