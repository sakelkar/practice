#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#Example 1:
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true
#
#Example 2:
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#Output: true
#
#Example 3:
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#Output: false
#
#Constraints:
#    m == board.length
#    n = board[i].length
#    1 <= m, n <= 6
#    1 <= word.length <= 15
#    board and word consists of only lowercase and uppercase English letters.
from typing import List

class Solution:
    def word_search(self, board: List[List[str]], word: str) -> bool:
        #if the matrix is empty then return False
        if not len(board) == 0 or not len(board[0]) == 0:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= rows or j < 0 or j > cols or board[i][j] != word[k] or board[i][j] == '#':
                return False

            temp = board[i][j]
            board[i][j] = '#'

            found = dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
            board[i][j] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0) == True:
                    return True
        return False

