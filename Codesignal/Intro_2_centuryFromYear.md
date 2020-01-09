## centuryFromYear
* 題目：Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
* 例子：
  * For year = 1905, the output should be centuryFromYear(year) = 20.
  * For year = 1700, the output should be centuryFromYear(year) = 17.
* 我的理解與學習筆記：如果除以100等於0，代表能整除（1700、1800...），直接返回，如果不等於0，代表是下一個世紀，返回加1。
  * 只取整數的除法：**//**
  * 如何判斷是否能整除：**取餘數等於0**
  * 如何取餘數：**%**
```Python
def centuryFromYear(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
```
