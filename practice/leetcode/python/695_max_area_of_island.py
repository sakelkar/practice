#https://leetcode.com/problems/max-area-of-island/description/
#You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#The area of an island is the number of cells with a value 1 in the island.
#Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j):
            curr_area = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_i = di + i
                new_j = dj + j
                if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_i] == 1:
                    grid[new_i][new_i] = 2
                    curr_area += dfs(new_i, new_i)

            return curr_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    max_area = max(dfs(i, j), max_area)

        return max_area
