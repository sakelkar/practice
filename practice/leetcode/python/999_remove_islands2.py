from typing import List

class Solution:
    def removeIslands(self, matrix: List[List[int]]):
        border_islands = {}
        rows, cols = len(matrix), len(matrix[0])

        def isOutsideMatrix(i, j):
            if i < 0 or i > rows or j < 0 or j > cols:
                return False
            return True

        def isBorder(i, j):
            if ((i == 0 or i == rows) and (j == 0 or j == cols)):
                return True
            return False

        def islandKey(i, j):
            #return(f'{i}{j}')
            return('{}{}'.format(i, j))

        def rec(i, j):
            steps = [(0,1), (1,0), (0,-1), (-1,0)]
            for (ix, jx) in steps:
                new_i = ix + i
                new_j = jx + j
                if isOutsideMatrix(new_i, new_i):
                    continue
                key = islandKey(new_i, new_i)
                if matrix[new_i][new_i] == 1 and not key in border_islands:
                    border_islands[key] = True
                    rec(new_i, new_j)

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 1 and isBorder(i, j):
                    border_islands[islandKey(i, j)] = True
                    rec(i, j)

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                key = islandKey(i, j)
                if val == 1 and not key in border_islands:
                    matrix[i][j] = 0

        return matrix
