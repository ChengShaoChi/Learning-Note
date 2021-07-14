## Modulus
* 題目：Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.
* 意思：輸入一數，整數就回傳除以2的餘數，非整數就回傳-1。
* 例子：For n = 15, the output should be modulus(n) = 1; For n = 23.12, the output should be modulus(n) = -1.
* 我的理解與學習筆記：除以1的餘數為0即為整數。

```Python
def modulus(n):
    if n % 1 == 0:
        return n % 2
    else:
        return -1
```
參考資料：    
[python 如何判断一个数为整数？（判断整数，没有小数）（取余）判断整型 isinstance()](https://blog.csdn.net/Dontla/article/details/106956452)
