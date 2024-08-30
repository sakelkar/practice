//https://leetcode.com/problems/n-queens/description/
//The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
//Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
//Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
//both indicate a queen and an empty space, respectively.
#include <string>
#include <vector>
using namespace std;

class Solution {
private:
	bool isSafePlace(int n, vector<string> nQueens, int rowNum, int col) {
		//existing row: all columns should not have Q
		for (int i = 0; i < n; i++) {
			if (nQueens[i][rowNum] == 'Q') {
				return false;
			}
		}
		//existing cols: all rows should not have Q
		for (int i = 0; i < n; i++) {
			if (nQueens[col][i] == 'Q') {
				return false;
			}
		}
		//positive diagonal should not have Q. Check all the previous positions on the diagonal from current r:c
		for (int r = rowNum-1, c = col -1; r >= 0 && c >= 0; r--, c--) {
			if (nQueens[r][c] == 'Q') {
				return false;
			}
		}
		//negative diagonal should not have Q. Check all the previous positions on the diagonal from current r:c
		for (int r = rowNum-1, c = col+1; r >= 0 && c >= 0; r--, c++) {
			if (nQueens[r][c] == 'Q') {
				return false;
			}
		}
		return true;
	}
	void solveNQueens(int n, vector<vector<string>> &output, vector<string> &nQueens, int rowNum) {
		if (rowNum == n) {
			output.push_back(nQueens);
			return;
		}
		for (int col = 0; col < n; col++) {
			if (isSafePlace(n, nQueens, rowNum, col)) {
				nQueens[rowNum][col] = 'Q';
				solveNQueens(n, output, nQueens, rowNum+1);
				nQueens[rowNum][col] = '.';
			}
		}
	}
public:
	vector<vector<string>> solveNQueens(int n) {
		vector<vector<string>> output;
		vector<string> nQueens(n, string(n, '.'));
		solveNQueens(n, output, nQueens, 0);
		return output;

	}
};
class Solution2 {
private:
	bool isSafePlace(int n, vector<string> nQueens, int rowNum, int col) {
		//check row for all columns
		int r, c;
		for (int i = 0; i < n; i++) {
			if (nQueens[rowNum][i] == 'Q') {
				return false;
			}
		}
		//check column for all rows
		for (int i = 0; i < n; i++) {
			if (nQueens[i][col] == 'Q') {
				return false;
			}
		}
		//check positive diagonal
		for (r = rowNum - 1, c = col - 1; r >= 0 && c >= 0; r--, c--) {
			if (nQueens[r][c] == 'Q') {
				return false;
			}
		}
		//check negative diagonal
		for (r = rowNum - 1, c = col + 1; r >= 0 && c >= 0; r--, c++) {
			if (nQueens[r][c] == 'Q') {
				return false;
			}
		}
		return true;
	}
	void solveNQueens(int n, vector<vector<string>> &output, vector<string> &nQueens, int rowNum) {
		if (rowNum == n) {
			output.push_back(nQueens);
			return;
		}
		for (int col = 0; col < n; col++) {
			if (isSafePlace(n, nQueens, rowNum, col)) {
				nQueens[rowNum][col] = 'Q';
				solveNQueens(n, output, nQueens, rowNum+1);
				nQueens[rowNum][col] = '.';
			}
		}

	}
public:
	vector<vector<string>> solveNQueens(int n) {
		vector<vector<string>> output;
		vector<string> nQueens(n, string(n, '.'));
		solveNQueens(n, output, nQueens, 0);
		return output;
	}
};
