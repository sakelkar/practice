//https://leetcode.com/problems/reverse-linked-list/
//Given the head of a singly linked list, reverse the list, and return the reversed list.

//Definition of singly linked list
//class ListNode:
//   def __init__(self, val=0, next=None)
//       self.val = val
//       self.next = next
//typing module is create to support gradual typing as per PEP 484
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
};

class Solution {
public:
	ListNode *reverseLinkedList(ListNode *head) {
		ListNode *prev = nullptr;
		ListNode *curr = head;
		ListNode *next = nullptr;
		while (curr) {
			next = curr->next;
			curr->next = prev;
			prev = curr;
			curr = next;
		}
		return(curr);
	}
};
