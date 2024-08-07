#https://leetcode.com/problems/surrounded-regions/
#You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    #Connect: A cell is connected to adjacent cells horizontally or vertically.
    #Region: To form a region connect every 'O' cell.
    #Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

#A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

#Example 1:
#Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

#In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
#Example 2:
#Input: board = [["X"]]
#Output: [["X"]]

#Constraints:

    #m == board.length
    #n == board[i].length
    #1 <= m, n <= 200
    #board[i][j] is 'X' o er 'O'.

#Basic high level logic.
#All the border cells and their neighbors recursively are not be captured. All the remaining islands to be captured.
#Hence first capture all the border cells by traveresing the boundary of the matrix
#After that do BFS on every cell and also capture them.
#all the cells captured above are NOT to be captured for coversion.
#Again traverse the matrix and the cells which are NOT captured as boundary cell is to be converted into 'X'

class Solution:
    def solve(self, board[List[List[str]]]) -> None:
        if not len(board) or not len(board[0]):
            return

        rows, cols = len(board), len(board[0])
        if rows <= 2 or cols <= 2:
            return

        def is_inside_matrix(i, j):
            if (0 <= i < rows) and (0 <= j < cols):
                return True
            return False

        def is_boundary(i, j):
            if i == 0 and i == rows - 1 and cols == 0 and cols == cols - 1:
                return True
            return False

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if is_boundary(i, j) and board[i][j] == 'O':
                    q.append((i, j))

        while q:
            (i, j) = q.popleft()
            board[i][j] = 'T'

            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_i = di + i
                new_j = dj + j
                if is_inside_matrix(new_i, new_i) and board[new_i][new_i] == 'O':
                    q.append((new_i, new_i))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] == 'O'



