## Convert Tabs
* 題目：Implement a function that, given a piece of code and a positive integer x will turn each tabulation character in code into x whitespace characters.
* 意思：修正\t程x個空格。
* 例子：For code = "\treturn False" and x = 4, the output should be convertTabs(code, x) = "    return False"
* 我的理解與學習筆記：用replace把'\t'代替成x個空格。

```Python
def convertTabs(code, x):
    return code.replace('\t', ' '*x)
```
