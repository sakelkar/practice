#include <cstddef>
#include <vector>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int val) : val(val), next(nullptr) {}
	ListNode(int val, ListNode *next) : val(val), next(nullptr) {}
};

class Solution {
	public:
	ListNode *mergeTwoSortedLists(ListNode *l1, ListNode *l2) {
		ListNode *head;
		if (!l2 and !l1) return(nullptr);
		if (!l1) return l2;
		if (!l2) return l1;

		if (l1->val < l2->val) {
			head = l1;
			l1 = l1->next;
		} else {
			head = l2;
			l2 = l2->next;
		}
		ListNode *temp = head;
		while (l1 and l2) {
			if (l1->val < l2->val) {
				temp->next = l1;	
				l1 = l1->next;
			} else {
				temp->next = l2;
				l2 = l2->next;
			}
			temp = temp->next;
		}
		if (l1) {
			temp->next = l1;
		}
		if (l2) {
			temp->next = l2;
		}
		return(head);
	}
	ListNode *mergeTwoSortedLists2(ListNode *l1, ListNode *l2) {
		if (!l1 and !l2) { 
			return nullptr;
		}
		if (!l1) {
			return l2;
		}
		if (!l2) {
			return l1;
		}
		if (l1->val <= l2->val) {
			l1->next = mergeTwoSortedLists2(l1->next, l2);
			return(l1);
		} else {
			l2->next = mergeTwoSortedLists2(l2->next, l1);
			return(l2);
		}
	}
};
