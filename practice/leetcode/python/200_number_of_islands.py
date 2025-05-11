#https://leetcode.com/problems/number-of-islands/description/
#
#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#Example 1:
#
#Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#]
#Output: 1
#
#Example 2:
#
#Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
#Output: 3
#
#Constraints:
#
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 300
#    grid[i][j] is '0' or '1'.

class Solution:
    def numIslands_dfs(self, grid: List[List[int]]) -> int:
        #edge conditions checking 
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        answer = 0
        #dfs logic for neighbor checking and marking


        def dfs(r, c):
            #first update the current element as visited. 
            grid[r][c] = 2 

            #now check all its neighbors and recurse if any of them is 1
            for d_r, d_c in (0, 1), (1, 0), (-1, 0), (0, -1):
                new_r = d_r + r
                new_c = d_c + c
                #check the newr and newc are not falling outside of matrix
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols:
                    if grid[new_r][new_c] == 1:
                        dfs(new_r, new_c)


        #go over each and every element
        for r, rv in enumerate(grid):
            for c, cv in enumerate(rv):
                #if the element is 1, then do dfs recursively
                if cv == 1:
                    dfs(r, c)
                    answer += 1
        #update the count
        #return the count
        return answer

    def num_of_islands_dfs2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        answer = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            #visit all connected nodes and mark them as visited
            grid[r][c] = 2

            for d_r, d_c in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_r = r + d_r
                new_c = c + d_c
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols:
                    #if next node is not visited then do not recurse
                    if grid[new_r][new_c] == 1:
                        dfs(new_r, new_c)

        for r, rv in enumerate(grid):
            for c, cv in enumerate(rv):
                if cv == 1:
                    dfs(r, c)
                    answer += 1

        return answer


    def numIslands_bfs(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0

        rows, cols = len(grid), len(grid(0))
        answer = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q = collections.queue([(i, j)])
                    grid[i][j] = 2
                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                            new_x = dx + x
                            new_y = dy + y
                            if 0 <= new_x < cols and 0 <= new_y < rows and grid[new_x][new_y] == 1:
                                q.append([(new_x, new_y)])
                                grid[new_x][new_y] = 2
                    answer += 1        
        return answer
