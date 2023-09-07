#https://leetcode.com/problems/reverse-integer/description/

#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX = pow(2,31) - 1
        MIN = -pow(2,31) - 1

        answer = 0
        while (x):
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if ((answer > (MAX//10)) or (answer == (MAX//10) and (digit >= MAX%10))):
                return(0)
            if ((answer < (MIN//10)) or (answer == (MIN//10) and (digit <= MIN%10))):
                return(0)
            answer = answer*10 + digit

        return(answer)

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -pow(2,31)
        MAX = pow(2,31)-1
        answer = 0
        while(x):
            digit = int(math.fmod(x,10))
            x = int(x/10)
            if ((answer > MAX//10) or (answer == MAX//10 and digit >= MAX % 10)):
                return(0)
            if ((answer < MIN//10) or (answer == MIN//10 and digit <= MIN % 10)):
                return(0)
            answer = answer * 10 + digit
        return(answer)
