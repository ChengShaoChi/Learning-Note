## Efficient Comparison
* 題目：

You would like to write a function that takes integer numbers x, y, L and R as parameters, and returns True. If x^y lies within the interval (L, R] and False otherwise. You're considering several different ways to write the conditional statement inside this function:
```
1. if L < x ** y <= R:
2. if x ** y > L and x ** y <= R:
3. if x ** y in range(L + 1, R + 1):
```
Which option would be the most efficient in terms of execution time?

- [ ] Option 1 is the most optimal one.
- [ ] Options 1 and 2 are equally good (and better than option 3).
- [ ] Option 3 is the most optimal one.
- [ ] All of these options are equally good.
* 意思：要使x ** y在L與R之間，且不包括L，包括R，要怎麼寫最有效。
* 我的理解與學習筆記：三個選項都是對的，但是選項1更有效率，因為它的運算比較少。

- [x] Option 1 is the most optimal one.
