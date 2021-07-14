## List Beautifier
* 題目：Given a list a, your task is to chop off its first and its last element until it becomes beautiful. Implement a function that will make the given a beautiful as described, and return the resulting list as an answer.
* 意思：輸入一數，第一及最後的數字若佈一樣則移除至一樣為止回傳。
* 例子：For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be listBeautifier(a) = [4, 38, 4]. For a = [1, 4, -5], the output should be listBeautifier(a) = [4].
* 我的理解與學習筆記：提示提供[Extended Iterable Unpacking](https://www.python.org/dev/peps/pep-3132/)用法可使用，範例如下：

```Python
a, *b, c = range(5)
a = 0
c = 4
b = [1, 2, 3]
```
* range(5)是0、1、2、3、4，a即為第一個數0，c即為最後一個數4，而b即為除了第一及最後的數之外的所有數。
```Python
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        m, *res, n = res
    return res
```
