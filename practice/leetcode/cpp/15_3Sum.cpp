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
		int numsSize = 0

		numsSize = nums.size()
		if (numsSize < 3)
			return answer
		sort(nums.begin(), nums.end())
		if (nums[i] > 0) 
			return answer

		for (int i = 0; i < numsSize; i++) {
			map[nums[i]] = i
		}
		for (int i = 0; i < numsSize - 2; i++) {
	   		if i != 0 and nums[i] == nums[i-1] continue;
	   		
	   		if nums[i] > 0 break
	    	
	   		for (int j = i + 1; j < numsSize - 1; j++) {

		    	if j != i + 1 and nums[j] == nums[j-1] contunue
		   		
		   		key = -1*(nums[i] + nums[j])

	   			if ((map.find(key) != map.end()) and (map[key] != j)) {
		   			answer.push_back({nums[i], nums[j], map[key]})
		   		}
		   	}
	    }
	   return(answer)
	}
};
