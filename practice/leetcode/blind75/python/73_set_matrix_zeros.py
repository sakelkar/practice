#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#You must do it in place.
#
#Example 1:
#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#Example 2:
#Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#Constraints:
#    m == matrix.length
#    n == matrix[0].length
#    1 <= m, n <= 200
#    -231 <= matrix[i][j] <= 231 - 1
#
#Follow up:
#
#    A straightforward solution using O(mn) space is probably a bad idea.
#    A simple improvement uses O(m + n) space, but still not the best solution.
#    Could you devise a constant space solution?
from typing import List


class Solution:
    def setZeros(self, matrix: List[List[int]]):
        #note inner cells if they have zeros
        #note perimeter cells if they have zeros
        #O(m*n) solution is where we can store the i and j value for rows and column in separate set
        #Once sets are populated then traverse the matrix again and based on set value make cells 0
        rows, cols = set(), set()
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        pass

    def setZeros2(self, matrix: List[List[int]]):
        #O(1) space solution is where you maintain the status of rows and columns
        #in some tertiary variable
        #and then based on the variable set the cells to zero
        r, c = len(matrix), len(matrix[0])
        firstRowZero = any(matrix[0][j] == 0 for j in range(c))
        firstColZero = any(matrix[i][0] == 0 for i in range(r))

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        if firstRowZero:
            for j in range(c):
                matrix[0][c] = 0

        if firstColZero:
            for i in range(r):
                matrix[i][0] = 0

    def setZero1(self, matrix: List[List[int]]):
        rowIndex, colIndex = set(), set()
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rowIndex.add(i)
                    colIndex.add(j)

        for i in range(r):
            for j in range(c):
                if i in rowIndex or j in colIndex:
                    matrix[i][j] = 0

    def setZero3(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        #set if the first row and column zero
        firstRowZero = any(matrix[0][j] == 0 for j in range(c))
        firstColZero = any(matrix[i][0] == 0 for i in range(r))

        #set the marker for internal cells in first row and column
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        #now do the setting of cells based on markers
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        #set the first row
        if firstRowZero:
            for i in range(c):
                matrix[0][i] = 0

        #set the first column
        if firstColZero:
            for j in range(r):
                matrix[j][0] = 0
