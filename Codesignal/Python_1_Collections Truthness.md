## Collections Truthness
* 題目：

What will be the value of res after the following snippet is executed:
```Python
xs = [()]
res = [False] * 2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True
```
- [ ] [False, True]
- [ ] [True, True]
- [ ] [True, False]
- [ ] [False, False]
* 意思：執行以下程式碼後，res的值是多少。
* 我的理解與學習筆記：    
  * 我要確認xs那樣到底算有沒有包含東西（看看它的長度）和包含什麼，執行以下程式碼後返回1和()，代表算不為空，包含一個()，但是它是空元組，不算元素，所以res[0]就會變True，res[1]還是False。
    
```Python
xs = [()]
print(len(xs),xs[0])
```
- [x] [True, False]
