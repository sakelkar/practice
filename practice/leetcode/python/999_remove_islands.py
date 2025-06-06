from typing import List
class Solution:
    def removeIslands(self, matrix: List[List[int]]):
        def border_island_key(i, j):
            return ('{}{}'.format(i, j))
        def is_outside_matrix(new_i, new_j):
            if new_i < 0 and new_j < 0 or new_i > (len(matrix) - 1) or new_j > (len(matrix[0]) - 1):
                return(True)
            return(False)

        border_islands = {}
        #rec will just look up, left, right, and down to see of the element is == 1
        #if Yes and if the new element is alreadu not in border_island then it will 
        #going
        def rec(i, j):
            steps =
            [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0)
            ]
            for (ix, jx) in steps: 
                new_i = ix + i
                new_j = jx + j
                #check for out of bound neighbor elements and skip those coordinates
                #run logic for the all other coordinates
                if is_outside_matrix(new_i, new_j):
                    continue
                neigh = matrix[new_i][new_i]
                key = border_island_key(new_i, new_i)
                if neigh == 1 and not key in border_islands:
                    border_islands[key] = True
                    rec(new_i, new_i)

        def is_border(i, row_length, j, col_length):
            if i == 0 or i == row_length or j == 0 or j == col_length:
                return True
            
            return False

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == 1 and is_border(i, len(matrix) - 1, j, len(row) - 1):
                    border_islands[border_island_key(i, j)] = True
                    #now recurse for all the adjacent members of current i and j
                    rec(i, j)

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                key = border_island_key(i, j)
                if value == 1 and not key in border_islands:
                    matrix[i][j] = 0

        return matrix
