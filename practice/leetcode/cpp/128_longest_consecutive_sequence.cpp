//https://leetcode.com/problems/longest-consecutive-sequence/description/
//Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
//You must write an algorithm that runs in O(n) time.
#include <algorithm>
#include <vector>
using namespace std;
#include <unordered_set>

class Solution {
public:
	int longestConsecutive(vector<int> &nums) {
		int best = 0;
		int start = 0;
		unordered_set<int> set;
		
		//converting to unordered set make the list only having unique elements
		//but its not ordered.
		for (int num: nums) {
			set.insert(num);
		}
		
		for (int num: nums) {
			//find the element such that its previous is not present in the set
			if (set.find(num - 1) == set.end()) {
				start = num;
				//now move forward 
				while ( set.find(start + 1) != set.end()) {
					start++;
				}
				best = max(best, start - num);
			}
 		}
		return(best);
 	}
	int longestConsecutiveSequenceLength(vector<int> &nums) {
		unordered_set<int> set(nums.begin(), nums.end());
		int start = 0;
		int best = 0;

		for (auto n: nums) {
			if (set.find(n-1) == set.end()) {
				start = n;
				while (set.find(start) != set.end()) {
					start++;
				}
				best = max(best, start - n);
			}
		}
		return(best);
	}
	// longrstConsecutiveSequenceLength2
	int longrstConsecutiveSequenceLength2(vector<int> &nums) {
		//create unordered set
		unordered_set<int> set(nums.begin(), nums.end());
		int start = 0;
		int best = 0;

		//now loop through the array
		for (auto n: nums) {
			//for current element if its present in the set then
			if (set.find(n-1) == set.end()) {
				start = n;
				while (set.find(start) != set.end()) {
					start++;
				}
				best = max(best, start - n);
			}
			//that is the new start
			//now find if the + 1 is present if yes then move the start
			//
		}
		return(best);
	}
};
