//https://leetcode.com/problems/invert-binary-tree/description/
//Given the root of a binary tree, invert the tree, and return its root.

#include <cmath>
#include <utility>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(0), left(left), right(right) {}
};

class Solution {
public:
	TreeNode *invertTree_recursive(TreeNode *root) {
		if (root) {
			invertTree(root->right);
			invertTree(root->left);
			std::swap(root->left, root->right);
		}
		return(root);
	}
	TreeNode *invertTree_iterative(TreeNode *root) {
		stack<TreeNode *> st;
		st.push(root);

		while (!st.empty()) {
			TreeNode *tmp = st.top();
			st.pop();
			if (tmp) {
				st.push(tmp->left);
				st.push(tmp->right);
				std::swap(tmp->left, tmp->right);
			}
		}
		return(root);
	}
};
