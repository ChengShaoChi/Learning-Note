## Is Word Palindrome
* 題目：Given a word, check whether it is a palindrome or not.
* 意思：判斷字串是否回文。
* 例子：
  * For word = "aibohphobia", the output should be isWordPalindrome(word) = true
  * For word = "hehehehehe", the output should be isWordPalindrome(word) = false.
* 我的理解與學習筆記：在另一個練習[checkPalindrome](https://github.com/ChengShaoChi/Learning-Note/blob/master/Codesignal/Intro_3_checkPalindrome.md)中有使用過判斷回文的方法 `[::-1]`。

```Python
def isWordPalindrome(word):
    return word == word[::-1]
```
