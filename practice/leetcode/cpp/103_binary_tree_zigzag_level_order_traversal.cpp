//https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
//Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
//(i.e., from left to right, then right to left for the next level and alternate between).

#include <algorithm>
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
	vector<vector<int>> levelOrderZigZagTraversal(TreeNode *root) {
		vector<vector<int>> answer;
		vector<int> level;
		int x = 0;
		queue<TreeNode *> que;
		TreeNode *temp;

		que.push(root);
		while (!que.empty()) {
			int levelSize = que.size();

			for (int k = 0; k < levelSize; k++) {
				TreeNode *temp = que.front();
				que.pop();
				level.push_back(temp->val);

				if (temp->left)
					que.push(temp->left);
				if (temp->right)
					que.push(temp->right);
			}
			if (x % 2 == 0) {
				answer.push_back(level);
			} else {
				reverse(level.begin(), level.end());
				answer.push_back(level);
			}
		}
		return(answer);
	}
};
