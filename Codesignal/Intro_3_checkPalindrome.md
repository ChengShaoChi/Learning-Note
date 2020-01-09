## checkPalindrome
* 題目：Given the string, check if it is a palindrome.
* 例子：
  * For inputString = "aabaa", the output should be checkPalindrome(inputString) = true.
  * For inputString = "abac", the output should be checkPalindrome(inputString) = false.
  * For inputString = "a", the output should be checkPalindrome(inputString) = true.
* 我的理解與學習筆記：如果字串跟字串反轉後是一樣的，返回True，如果不一樣，返回False。
  * palindrome：回文
  * 如何使字串反轉：**變數[::-1]**
```Python
def checkPalindrome(inputString):
        if inputString == inputString[::-1]:
            return True
        else:
            return False
```
