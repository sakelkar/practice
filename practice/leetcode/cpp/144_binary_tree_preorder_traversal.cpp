//https://leetcode.com/problems/binary-tree-preorder-traversal/description/
//Given the root of a binary tree, return the preorder traversal of its nodes' values.

#include <algorithm>
#include <stack>
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
private:
	//preOrder
	void preOrder(TreeNode *root, vector<int> &answer) {
		if (!root) {
			return;
		}
		answer.push_back(root->val);
		preOrder(root->left, answer);
		preOrder(root->right, answer);
		return;
	}
public:
	vector<int> preOrder_Iterative(TreeNode *root) {
		vector<int> answer;
		stack<TreeNode *> st;

		while (root || !st.empty()) {
			if (root) {
				answer.push_back(root->val);
				st.push(root->right);
				root = root->left;
			} else {
				root = st.top();
				st.pop();
			}
		}
		return(answer);
	}
	vector<int> preOrderTraversal_Recurse(TreeNode *root) {
		vector<int> answer;
		preOrder(root, answer);
		return(answer);

	}
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
