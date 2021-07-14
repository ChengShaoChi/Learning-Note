## Mex Function
* 題目：For the given set s and given an upperBound, implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.
* 意思：輸入s及upperBound，upperBound大的話就回傳不在s裡的最小非負整數，不然就直接回傳upperBound。
* 例子：For s = [0, 4, 2, 3, 1, 7] and upperBound = 10, the output should be mexFunction(s, upperBound) = 5. For s = [0, 4, 2, 3, 1, 7] and upperBound = 3, the output should be mexFunction(s, upperBound) = 3.
* 我的理解與學習筆記：```if not i in s```可以記起來用。

```Python
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found
```
