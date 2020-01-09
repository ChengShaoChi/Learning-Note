## shapeArea
* 題目：Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n. A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Area.png?raw=true"/></div>

* 意思：算面積。
* 例子：
  * For n = 2, the output should be shapeArea(n) = 5.
  * For n = 3, the output should be shapeArea(n) = 13.
* 我的理解與學習筆記：有數學遞迴關係。
```Python
def shapeArea(n):
    return (n*n*2 - n*2 + 1)
```
