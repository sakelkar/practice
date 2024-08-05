//https://leetcode.com/problems/balanced-binary-tree/description/
//Given a binary tree, determine if it is #height-balanced
//
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};

using namespace std;
int height(struct TreeNode *root) {
	int left_height;
	int right_height;
	int diff;

	if (!root) {
		return(0);
	}
	left_height = height(root->left);
	if (left_height == -1) {
		return(-1);
	}
	right_height = height(root->right);
	if (right_height == -1) {
		return(-1);
	}
	diff = (left_height - right_height) ? (left_height - right_height) : (right_height - left_height);
	if (diff > 1) {
		return(-1);
	} else {
		return left_height > right_height ? left_height + 1 : right_height + 1;
	}
}
bool isBalanced(struct TreeNode *root) {
	if (!root) {
		return(true);
	} else {
		return(height(root) != -1);
	}
}
