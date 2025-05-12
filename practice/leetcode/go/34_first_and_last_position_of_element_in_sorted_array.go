//#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description
//Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
//of a given target value
//If target is not found in the array, return [-1, -1]
//You must write an algorithm with O(log n) runtime complexity
//Example 1:

//Input: nums = [5,7,7,8,8,10], target = 8
//Output: [3,4]
//Example 2:

//Input: nums = [5,7,7,8,8,10], target = 6
//Output: [-1,-1]
//Example 3:

//Input: nums = [], target = 0
//Output: [-1,-1]

// searchRange
func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	return []int{binaryLeft(nums, target), binaryRight(nums, target)}
}

// binaryLeft
func binaryLeft(nums []int, target int) int {
	left, right := 0, len(nums) - 1
}

// binaryRight
func binaryLeft(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for left < right {
		mid := (left + (right - left)/2)
		if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}
	if nums[left] == target 
		return mid
	else 
		return -1
}
// binaryRight
func binaryRight(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for left < right {
		mid := (left + (right - left)/2)
		if nums[mid] > target {
			right = mid - 1
		} else {
			left = mid
		}
	}
	if nums[left] == target {
		return left 
	} else {
		return -1 
	} 
}
