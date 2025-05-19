from typing import List
class Solution:
    def numOfIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        answer = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '2'

            for d_r, d_c in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_r = r + d_r
                new_c = c + d_c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1':
                    dfs(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    answer += 1

        return answer
