//https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
//Given an integer array nums where the elements are sorted in ascending order, convert it to a
//height-balanced
//binary search tree.
using namesapce std;
#include <vector>
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(): val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {}
};

class Solution {
public:
	TreeNode *recurse(vector<int> &nums, int left, int right) {
		int middle = 0;	
		if (right < left) 
			return nullptr;

		middle = left + ((right - left)/2 
		TreeNode *root = new TreeNode(nums[middle]);
		root->left = recurse(nums, left, middle);
		root->right = recurse(nums, middle+1, right);
		return(root);

	}
	TreeNode *arr_to_bst(vector<int> &nums) {
		return recurse(nums,0, nums.size() - 1); 
	}
};
