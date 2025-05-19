func numOfIslands(grid [][]int) int {
	answer := 0
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[r]); c++ {
			if grid[r][c] == 1 {
				dfs(grid, i, j)
				answer += 1
			}
		}
	}
}

func dfs(grid [][]int, r, c int) {
	if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[r]) || grid[r][c] != 1 {
		return
	}
	dfs(grid, r+1, c)
	dfs(grid, r-1, c)
	dfs(grid, r, c+1)
	dfs(grid, r, c-1)
}
