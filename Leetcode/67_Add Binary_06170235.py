class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)+int(b, 2)
        x = str(x)
        x = bin(int(x, 10))
        return x[2:]
        
#轉換進位制在寫HW4時，有整理過表格，照著表格來轉換就可以了。
#一開始return x，發現輸出的結果前面會多"0b"，但是題目只要後面的數字，所以改成return x[2:]。
