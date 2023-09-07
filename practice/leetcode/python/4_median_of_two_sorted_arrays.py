#https://leetcode.com/problems/median-of-two-sorted-arrays/

#Given two sorted arrays nums1 and nums2 of size m and n respectively, 
#return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

from typing import List

class Solution:
    def findMedianOfSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #let A and B be the two arrays
        A, B = nums1, nums2
        #let A be the smallest among the two arrays and you will run bianry search on the smallest arrays
        if len(B) < len(A):
            A, B = B, A

        #find out the total length and median length
        total = len(A) + len(B)
        half = total // 2

        #define left and right pointer
        l, r = 0, len(A) - 1
        #parse through the smallest array a
        while True:
            #check for left and right partitions based on the median
            i = (l + r) // 2
            j = half - i - 2

            #Get the values of edge elements around the i an j in both A and B arrays
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i + 1 <= len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j + 1 < len(B) else float("infinity")

            #adjust partions based on the comparison and take care of out of bound edge cases
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

