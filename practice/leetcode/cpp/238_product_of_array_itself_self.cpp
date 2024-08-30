//https://leetcode.com/problems/product-of-array-except-self/description/
//
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> productExceptSelt(vector<int> &nums) {
		int n = nums.size();
		vector<int> result(n, 1);
		//in first pass calculate the left multiplication
		for (int i = 1; i < n; i++) {
			result[i] = result[i-1]*nums[i-1];
		} 
		//in swcond pass calculate the right multiplication on the same array modified above
		int right = 1;
		for (int i = n-2; i >= 0; i--) {
			right *= nums[i+1];
			result[i] *= right;
		}
		return(result);

	}
};
