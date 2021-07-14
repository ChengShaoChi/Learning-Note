## Fix Message
* 題目： Implement a function that will change the very first symbol of the given message to uppercase, and make all the other letters lowercase.
* 意思：輸入一句子，修正大小寫。
* 例子：For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1", the output should be fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1".
* 我的理解與學習筆記：Python大小寫轉換用法如下：

|one Two thrEe|轉換|結果|
|:---:|:---:|:---:|
|**.upper()**|全大寫|ONE TWO THREE|
|**.lower()**|全小寫|one two three|
|**.capitalize()**|句子第一個詞字首大寫|One two three|
|**.title()**|每個詞字首大寫|One Two Three|

```Python
def fixMessage(message):
    return message.capitalize()
```
參考資料：    
[Python来作大小写转换_杰瑞的专栏-CSDN博客](https://blog.csdn.net/Jerry_1126/article/details/81349187)
