//https://leetcode.com/problems/binary-tree-level-order-traversal/description/
//Given the root of a binary tree, return the level order traversal of its nodes' values. 
//(i.e., from left to right, level by level).

#include <queue>
#include <utility>
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
	vector<vector<int>> levelOrder(TreeNode *root) {
		if (!root) {
			return {};
		} 
		
		vector<vector<int>> answer;
		queue<TreeNode *> que;
		TreeNode *temp;

		que.push(root);
		while (!que.empty()) {
			vector<int> level;

			for (int i = que.size(); i; i--) {
				level.push_back(que.front()->val);
				temp = que.front();
				que.pop();
				if (temp->left) {
					que.push(temp->left);
				}
				if (temp->right) {
					que.push(temp->right);
				}
			}
			answer.push_back(std::move(level));
 		}
  		return(answer);
	}
};
