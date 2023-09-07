#https://leetcode.com/problems/zigzag-conversion/

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number of rows:

#string convert(string s, int numRows);
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        answer = ""
        for rowNo in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(rowNo, len(s), increment):
                answer += s[i]
                if ((rowNo > 0) and (rowNo < (numRows - 1)) and (((i + increment) - (2 * rowNo)) < len(s))):
                    answer += s[((i + increment) - (2 * rowNo))]
        return(answer)
