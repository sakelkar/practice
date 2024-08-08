//https://leetcode.com/problems/reverse-linked-list-ii/description/
//Given the head of a singly linked list and two integers left and right where left <= right, 
//reverse the nodes of the list from position left to position right, and return the reversed list.

struct ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
	ListNode(int x, ListNode *next): val(x), next(next) {}
};

class Solution {
public:
	ListNode *reverseBetween(ListNode *head, int left, int right) {
		ListNode dummy = ListNode(0);
		ListNode *prev = &dummy;
		ListNode *curr = nullptr;

		for (int i = 0; i < left - 1; i++) {
			prev = prev->next;
		}

		curr = prev->next;
		for (int i = 0; i < right - left; i++) {
			ListNode *temp = prev->next;
			prev->next = curr->next;
			curr->next = curr->next->next;
			prev->next->next = temp;
		}
		return(dummy.next);
	}
};
