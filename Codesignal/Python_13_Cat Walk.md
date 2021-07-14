## Cat Walk
* 題目：To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given line of your code with single ones. In addition, all leading and trailing whitespaces should be removed.
* 意思：輸入一句子，修正句子空格。
* 例子：For line = "def      m   e  gaDifficu     ltFun        ction(x):" the output should be catWalk(line) = "def m e gaDifficu ltFun ction(x):".
* 我的理解與學習筆記：
  * .join()：將容器物件拆分並以指定的字元將列表內的元素連線起來，返回字串。
  * .split()：以指定的字元將字串分割為單個元素（字元）並加入list中，返回一個list。

```Python
def catWalk(code):
    return ' '.join(code.split())
```
參考資料：    
[关于python：删除字符串中多个空格的简单方法？ | 码农家园](https://www.codenong.com/1546226/)</br>
[深入淺析Python中join 和split詳解(推) | 程式前沿](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/368516/)
