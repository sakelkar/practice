//https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
//Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without 
//modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
/*
 * Definition of singly-linked list
 * struct ListNode {
 * 		int val;
 * 		ListNode *next;
 * 		ListNode() : val(0), next(nullptr) {}
 * 		ListNode(int x): val(x), next(nullptr) {}
 * 		ListNode(int x, ListNode *next): val(x), next(next) {}
 * }
*/
struct ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
	ListNode(int x, ListNode *next): val(x), next(nullptr) {}
};

class Solution {
public:
	ListNode *swapPairs(ListNode *head) {
		ListNode **pp = &head;
		ListNode *a = nullptr;
		ListNode *b = nullptr;
		while ((a = *pp) && (b = a->next)) {
			a->next = b->next;
			b->next = a;
			*pp = b;
			pp = &(a->next);
		}
		return(head);
	}
};
