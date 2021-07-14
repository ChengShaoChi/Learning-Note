## Base Conversion
* 題目：Implement a function that, given an integer number n and a base x, converts n from base x to base 16.
* 意思：輸入n及x，將x進位的n轉成16進位回傳。
* 例子：For n = "1302" and x = 5, the output should be baseConversion(n, x) = "ca".
* 我的理解與學習筆記：在之前做[HW4](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW4/Hash%20Table%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%20Table%E8%88%87Hash%20function%E5%8E%9F%E7%90%86.md)有筆記過**不同進位間的轉換**的表格如下。

|轉⮮|2進位制|8進位制|10進位制|16進位制|
|:---:|:---:|:---:|:---:|:---:|
|**2進位制**|－|bin(int(x, 8))|bin(int(x, 10))|bin(int(x, 16))|
|**8進位制**|oct(int(x, 2))|－|oct(int(x, 10))|oct(int(x, 16))|
|**10進位制**|int(x, 2)|int(x, 8)|－|int(x, 16)|
|**16進位制**|hex(int(x, 2))|hex(int(x, 8))|hex(int(x, 10))|－|

```Python
def baseConversion(n, x):
    return hex(int(str(int(n, x)), 10))[2:]
```
