#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class solution {
public:
	vector<vector<int>> threeSum(vector<int> nums) {
		vector<vector<int>> answer;
		unordered_map<int, int> map;
		int key;
		int numsSize = 0;

		numsSize = nums.size();
		if (numsSize < 3)
			return(answer);

		sort(nums.begin(), nums.end());

		// Check for basic edge case that if there are all postivive integers then return immediately
		if (nums[0] > 0) {
			return(answer);
		}

		for (int i = 0; i < numsSize; i++) {
			map[nums[i]] = i;
		}

		for (int i = 0; i < numsSize - 2; i++) {
			//Get first unique number
	   		if ((i != 0) and (nums[i] == nums[i-1])) {
				continue;
			}
			// If the first unique number is non zero then stop and return immediately
	   		if (nums[i] > 0) {
				break;
			}
			// now work for 2nd and third number
	   		for (int j = i + 1; j < numsSize - 1; j++) {
		    	if ((j != i + 1) and (nums[j] == nums[j-1])) {
					continue;
				}
		   		key = -1*(nums[i] + nums[j]);
	   			if ((map.find(key) != map.end()) and (map[key] != j)) {
		   			answer.push_back({nums[i], nums[j], map[key]});
		   		}
		   	}
	    }
	   return(answer);
	}
};

class Solution {
public:
	vector<vector<int>> threeSum(vector<int> nums) {
		vector<vector<int>> answer;
		unordered_map<int, int>map;
		int key;
		int numsSize;

		// get the size
		numsSize = nums.size();
		// is size < 3
		if (numsSize < 3) {
			return(answer);
		}
		// sort
		sort(nums.begin(), nums.end());
		// is first number > 0 then exit immediately.
		if (nums[0] > 0) {
			return(answer);
		}
		// Create a map
		for (int i = 0; i < numsSize; i++) {
			map[nums[i]] = i;
		}
		// Loop
		// 		First find the first intenger
		// 		First integer always has to be < 0 if its not then break
		//		first 2nd number
		//		find the complment of sum of first and 2nd number
		//		Check whether that key exists in the map
		//		if yes then append to the array
		for (int i = 0; i < numsSize - 2; i++) {
			if ((i != 0) && (nums[i] == nums[i-1])) {
				continue;
			}
			if (nums[i] > 0) {
				break;
			}
			for (int j = i + 1; i < numsSize - 1; j++) {
				if ((j != i) && (nums[j] == nums[j-1])) {
					continue;
				}
				//now you have i and j figured out, now check 
				//if the complement of nums[i] + nums[j] exist 
				//in the map
				key = -1 * (nums[i] + nums[j]);
				if ((map.find(key) != map.end()) && (map[key] != j)) {
					answer.push_back({nums[i], nums[j], map[key]});
				}
			}

		}
		return(answer);
	}
};
