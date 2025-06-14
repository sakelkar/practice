#There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
#The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
#The island is partitioned into a grid of square cells. 
#You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
#The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west 
#if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
#Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
from typing import List

class Solution:
    def matrixGraphTemplate(self, matrix: List[List[int]]):
        answer = []
        visited = set()

        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        dirs = ((0,1),(1,0),(0,-1),(-1,0))

        def dfs(r, c):
            if (r, c) in visited:
                return

            visited.add((r, c))
            for dir in dirs:
                next_r, next_c = r + dir[0], c + dir[1]
                if 0 <= next_r < rows and 0 <= next_c < cols:
                    dfs(next_r, next_c)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(heights), len(heights[0])
        dirs = ((0,1),(1,0),(-1,0),(0,-1))

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r,c))
            for dir in dirs:
                new_r, new_c = r + dir[0], c + dir[1]
                if 0 <= new_r < rows and 0 <= new_c < cols and heights[new_r][new_c] > heights[r][c]:
                    dfs(new_r, new_c, visited)

        #pacific col = 0 and all rows
        #atlantic col = cols - 1 and all rows
        for row in range(rows):
            dfs(row, 0, p_visited)
            dfs(row, cols - 1, a_visited)

        #pacific row = 0 and all columns
        #atlantic row = rows - 1 and all cols
        for col in range(cols):
            dfs(0, col, p_visited)
            dfs(rows -1, col, a_visited)

        return list(p_visited & a_visited)





