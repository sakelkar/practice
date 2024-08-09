//https://leetcode.com/problems/reverse-nodes-in-k-group/
//Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
//k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
//You may not alter the values in the list's nodes, only nodes themselves may be changed.

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(): val(0), next(nullptr) {}
	ListNode(int x): val(x), next(nullptr) {}
	ListNode(int x, ListNode *next): val(x), next(next) {}
};

class Solution {
private:
	int ll_length(ListNode *head) {
		int N = 0;
		while (head) {
			N += 1;
			head = head->next;
		}
		return(N);
	}
public:
	ListNode *reverseKGroup(ListNode *head, int K) {
		if (!head)
			return head;

		int N = ll_length(head);
		if (N < K) {
			return head;
		}

		ListNode dummy = new ListNode(0);
		ListNode *prev = &dummy;
		dummy.next = head;

		for (int i = 0; i < N/K; i++) {
			for (int j = 0; j < K; j++) {
				ListNode *temp = prev->next;
				prev->next = head->next;
				head->next = head->next->next;
				prev->next->next = temp;
			}
			prev = head;
			head = head.next;
		}
		return(dummy.next);
	}
};
