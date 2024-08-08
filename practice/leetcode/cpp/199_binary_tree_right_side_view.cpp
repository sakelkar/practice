//https://leetcode.com/problems/binary-tree-right-side-view/description/
//Given the root of a binary tree, imagine yourself standing on the right side 
//of it, return the values of the nodes you can see ordered from top to bottom.

#include <queue>
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
	vector<int> rightSideView(TreeNode *root) {
		queue<TreeNode *>q;
		vector<int> answer;
		TreeNode *temp;

		if (!root) {
			return(answer);
		}

		q.push(root);
		while (!q.empty()) {
			answer.push_back(q.front()->val);
			for (int i = q.size(); i; i--) {
				temp = q.front(); 
				q.pop();
				if (temp->right) {
					q.push(temp->right);
				}
				if (temp->left) {
					q.push(temp->left);
				}
			}
		}
		return(answer);
	}
};
