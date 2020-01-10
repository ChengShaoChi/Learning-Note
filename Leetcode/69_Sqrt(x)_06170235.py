import math
class Solution:
    def mySqrt(self, x: int):
        y = math.sqrt(x)
        y = int(y)
        return y
        
#sqrt()：返回數字的平方根，要先import math，返回的會包含小數點。
#但是題目只要整數部分，所以最後轉成int。
