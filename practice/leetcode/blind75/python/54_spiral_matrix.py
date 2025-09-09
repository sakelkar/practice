#Given an m x n matrix, return all elements of the matrix in spiral order.
#
#Example 1:
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
#
#Example 2:
#Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 10
#    -100 <= matrix[i][j] <= 100
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        if matrix is None or len(matrix[0]) is None:
            return []

        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        while top <= bottom and left <= right:
            #left -> right movement for the current row
            for lr in range(left, right+1):
                answer.append(matrix[top][lr])
            #move top border one row below
            top += 1

            #top to bottom movement for the current column
            for tb in range(top, bottom+1):
                answer.append(matrix[tb][right])
            #move right border one column inward
            right -= 1

            if top <= bottom:
                #right -> left movement for the current row
                for rl in range(right, left-1, -1):
                    answer.append(matrix[bottom][rl])
                #move the bottom to one row up
                bottom -=1

            if left <= right:
                #bottom -> top movement for the current row
                for bt in range(bottom, top-1, -1):
                    answer.append(matrix[left][bt])
                #move the left one step inward
                left += 1
        return answer

