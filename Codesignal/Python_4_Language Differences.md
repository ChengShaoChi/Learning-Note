## Language Differences
* 題目：

Your friend is an experienced coder who just started learning Python. Since she is already proficient in Java and C++, she decided to write all of her snippets in all three languages, in order to ensure the Python code was
working as expected. Here's the very first function your friend wrote in Python and Java (the C++ version is the same as Java one):

`● Python:`

```Python
def division(x, y):
    return x // y
```
`● Java:`
```Java
int division(int x, int y){
    return x / y;
}
```
You noticed that the functions aren't quite the same: they won't produce the same result for some valid values of x and y . For which of the following example inputs would these two versions produce different outputs?
- [ ] x = 15, y = -4
- [ ] x = -10, y = -3
- [ ] x = 5, y = 10
- [ ] x = 17, y = 13
* 意思：輸入哪個選項後，這兩個版本將產生不同的輸出？
* 我的理解與學習筆記：去查了Java中的"**/**"，它的運算也是如果兩個運算數都是整數，那麼除法運算符的運算結果就是整數，並且會省略一切小數點後的值（或者說是兩個整數相除得到的商），跟Python中的"**//**"一樣。但是當被除數和除數是一正一負時，
Java的商（負的）會**向上**取整數，而Python會**向下**。所以答案是x = 15, y = -4，Java的輸出結果會是-3，Python會是-4。
- [x] x = 15, y = -4

參考資料：    
[Java/運算符- 維基教科書，自由的教學讀本 - Wikibooks](https://zh.wikibooks.org/zh-tw/Java/%E8%BF%90%E7%AE%97%E7%AC%A6)
