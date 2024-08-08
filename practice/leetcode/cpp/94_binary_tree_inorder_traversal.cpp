//https://leetcode.com/problems/binary-tree-inorder-traversal/description/
//Given the root of a binary tree, return the inorder traversal 
//of its nodes' values.

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
	void inOrder(TreeNode *root, vector<int> answer) {
		if (!root) {
			return;
		}
		inOrder(root->left, answer);
		answer.push_back(root->val);
		inOrder(root->right, answer);
	}
public:
	//using stack data structure
	vector<int> inOrder_iterartive(TreeNode *root) {
		vector<int> answer;
		stack<TreeNode *> st;

		while (root || !st.empty()) {
			while (root) {
				st.push(root->left);
				root = root->left;
			}
			root = st.top();
			st.pop();
			answer.push_back(root->val);
			root = root->right;
		}
		return(answer);

	}
	vector<int> inorderTraversal_Recurse(TreeNode *root) {
		vector<int> answer;
		inOrder(root, answer);
		return(answer);
	}
	vector<int> inorderTraversal_Morris(TreeNode *root) {
		vector<int> answer;
		TreeNode *pre;

		if (!root) {
			return {};
		}

		while (root) {
			if (!root->left) {
				//take the current as per inorder rule
				answer.push_back(root->val);
				//now travere right as per inorder
				root = root->right;
			} else {
				pre = root->left;
				//first find the inorder predecessor of the current root
				//inorder predecessor is the right-most element in the left sub-tree
				while (pre->right != nullptr && pre->right != root) {
					pre = pre->right;
				}
				//set up backtracking link from predecessor to current root
				if (pre->right == nullptr) {
					pre->right = root;
					root = root->left;
				} else {
					//take current root and move to the successor
					pre->right = nullptr;
					answer.push_back(root->val);
					root = root->right;
				}
			}
		}
		return(answer);
	}
};
