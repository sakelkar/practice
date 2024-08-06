//https://leetcode.com/problems/merge-two-binary-trees/description

//You are given two binary trees root1 and root2.
//Imagine that when you put one of them to cover the other, some nodes of the two trees are 
//overlapped while the others are not. You need to merge the two trees into a new binary tree. 
//The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
//Otherwise, the NOT null node will be used as the node of the new tree.
//Return the merged tree.
//Note: The merging process must start from the root nodes of both trees.

#include <utility>
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
	TreeNode *mergeTree(TreeNode *t1, TreeNode *t2) {
		if (!t1) {
			return t2;
		} 
		if (!t2) {
			return t1;
		}
		t1->val += t2->val;
		if (t2->left) {
			t1->left = mergeTree(t1->left, t2->left);
		} 
		if (t2->right) {
			t2->right = mergeTree(t2->right, t2->right);
		}
		return(t1);
	}
	TreeNode *mergeTrees_BFS_Queues(TreeNode *t1, TreeNode *t2) {
		if (!t1 && !t2) return nullptr;
		if (!t1) return t2;
		if (!t2) return t1;

		queue<pair<TreeNode *, TreeNode *>> que;
		que.push({t1, t2});
		while (!que.empty()) {
			auto node = que.front();
			que.pop();
			node.first->val += node.second->val;

			if (node.first->left && node.second->left) {
				que.push({node.first->left, node.second->right});
			} else if (node.second->left) {
				node.first->left = node.second->left;
			}

			if (node.first->right && node.second->right) {
				que.push({node.first->right, node.second->right});
			} else if (node.second->right) {
				node.first->right = node.second.right;
			}
		}
		return(t1);
	}
};
