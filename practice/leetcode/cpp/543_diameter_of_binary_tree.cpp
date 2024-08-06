//https://leetcode.com/problems/diameter-of-binary-tree/description/
//Given the root of a binary tree, return the length of the diameter of the tree.
//The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
//This path may or may not pass through the root.
//The length of a path between two nodes is represented by the number of edges between them.
#include <algorithm>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(): val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {}
};

int max_diameter;

class Solution {
public:
	int maxHeightOfRoot(TreeNode *root) {
		int diam = 0;
		int height_left = 0;
		int height_right = 0;

		if (root == nullptr) {
			return(0);
		}
		height_left = maxHeightOfRoot(root->left);
		height_right = maxHeightOfRoot(root->right);
		//Update the max diameter
		max_diameter = max((height_left + height_right), max_diameter);
		//return max height for the current root
		return (1 + max(height_left, height_right)); 
	}
	int diameterOfBinaryTree(TreeNode *root) {
		maxHeightOfRoot(root);
		return(max_diameter);
	}
};
