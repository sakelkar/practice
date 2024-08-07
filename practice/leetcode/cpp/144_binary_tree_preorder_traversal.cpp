//https://leetcode.com/problems/binary-tree-preorder-traversal/description/
//Given the root of a binary tree, return the preorder traversal of its nodes' values.

#include <algorithm>
#include <vector>
using namespace std;

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
	vector<int> preOrderTraversal_Morris(TreeNode *root) {
		if (!root) {
			return {};
		}

		vector<int> answer;
		TreeNode *pre;
		while (root) {
			if (!root->left) {
				answer.push_back(root->val);
				root = root->right;
			} else {
				pre = root->left;
				while ((pre->right != nullptr) && (pre->right != root)) {
					pre = pre->right;
				}
				if (pre->right == nullptr) {
					pre->right = root;
					answer.push_back(root->val);
					root = root->left;
				} else {
					pre->right = nullptr;
					root = root->right;
				}
			}
		}
		return(answer);
	}
};
