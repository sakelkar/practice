//https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
//Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
	ListNode(int x, ListNode *next): val(x), next(next) {}
};

class Solution {
public:
	ListNode *removeDuplicates(ListNode *head) {
		ListNode *curr = head;
		while (curr) {
			if ((curr->next) && (curr->val == curr->next->val)) {
				curr->next = curr->next->next;
			} else {
				curr = curr->next;
			}
		}
		return(head);
	}
};
