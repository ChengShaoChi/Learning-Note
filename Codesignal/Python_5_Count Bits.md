## Count Bits
* 題目：Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.
* 意思：輸入一整數，回傳該整數的二進位制有幾位。
* 例子：For n = 50, the output should be countBits(n) = 6.
* 我的理解與學習筆記：原本想法是以轉二進位的方式來寫，即除以2至商數為0，讀餘數從下讀到上。但題目規定除了可修改範圍外不可多加程式碼，因此使用了別的方式。

* 原本想法：
```Python
def countBits(n):
    count = 0
    while n >= 1:
        count += 1
        n = n // 2
    return count
```
* 依題目規定：
```Python
def countBits(n):
    return n.bit_length()
```
參考資料：    
[二進位- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%BF%9B%E5%88%B6)
