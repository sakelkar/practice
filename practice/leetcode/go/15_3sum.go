//https://leetcode.com/problems/3sum/
//Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
//Notice that the solution set must not contain duplicate triplets.

//Basic logic
//Boundary conditions
//Check the length < 3 return []
//Sort
//Check if the first number > 0 after sorting return []

//Create a hashMap[] and update the highest index for the given value of the number

//for loop to find first non-repeating number
//run 2nd for loop to find second non-repeating number
//negate the sum of find1 and find2
//search in hashMap above and insert into list of lists
//return
import (
	"sort"
)

func threeSum(nums []int) [][]int {
	var result [][]int
	//sort the array
	sort.Ints(nums)
	
	//
	for i = 0; i < len(nums) - 2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue;
		}
		target, left, right = -1*nums[i], i + 1, len(nums) - 1
		while (left < right) {
			sum := nums[left] + nums[right]
			if sum == target {
				results = append(result, []int{nums[i], nums[left], nums[right]})
				left++
				right--
				for left < right && nums[left] == nums[left - 1] {
					left++
				}
				for right > left && nums[right] = nums[right+1] {
					right--
				}
			} else if sum > target {
				right--
			} else {
				left++
			}
		}
	}
	return(answer)
}
