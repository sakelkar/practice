// numOfIslands
func numOfIslands(grid [][]int) int {
	answer := 0

	for i := 0; i < len(grid); i++ {
		for j = 0; j < len(grid[i]; j++) {
			if grid[i][j] == 1 {
				dfs(grid, i, j)
				answer += 1
			}
		}
	}
}

// dfs
func dfs(grid [][]int, r, c int) {
	if r < 0 || r >= len(grid) || c < 0 || c >= grid[r] || grid[r][c] != 1 {
		return
	}
	grid[r][c] = 2
	dfs(grid, r + 1, c)
	dfs(grid, r - 1, c)
	dfs(grid, r, c + 1)
	dfs(grid, r, c - 1)
}
