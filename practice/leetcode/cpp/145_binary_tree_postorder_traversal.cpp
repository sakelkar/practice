//https://leetcode.com/problems/binary-tree-postorder-traversal/description/
//Given the root of a binary tree, return the postorder traversal of its nodes' values.

#include <queue>
#include <stack>
#include <vector>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(): val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
private:
	void postOrder(TreeNode *root, vector<int>	&answer) {
		if (!root) {
			return;
		}
		postOrder(root->left, answer);
		postOrder(root->right, answer);
		answer.push_back(root->val);
		return;
	}
public:
	vector<int> postOrder_Recurse(TreeNode *root) {
		vector<int> answer;
		if (!root) {
			return answer;
		}
		postOrder(root, answer);
		return(answer);
	}
	vector<int> postOrder_Iterative(TreeNode *root) {
		stack<TreeNode *> st;
		vector<int> answer;
		TreeNode *last = nullptr, *temp = nullptr;

		if (!root) {
			return answer;
		}
		//iterative loop
		while (root || !st.empty()) {
			if (root) {
				st.push(root);
				root = root->left;
			} else {
				temp = st.top();
				//
				if ((temp->right != nullptr) && (temp->right != last)) {
					root = temp->right;
				} else {
					answer.push_back(temp->val);
					last = temp;
					st.pop();
				}
			}
		}
		return(answer);
	}
};
