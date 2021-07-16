## Feedback Review
* 題目： Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:
* 意思：輸入一數，整數就回傳除以2的餘數，非整數就回傳-1。
* 例子：For feedback = "This is an example feedback" and size = 8, the output should be feedbackReview(feedback, size) = ["This is", "an", "example", "feedback"]
* 我的理解與學習筆記：`textwrap`文本換行與填充。

```Python
import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)
```
參考資料：    
[textwrap --- 文本自动换行与填充— Python 3.7.11 文档](https://docs.python.org/zh-cn/3.7/library/textwrap.html#textwrap.TextWrapper.wrap)    
[python textwrap的使用- 慢行厚积- 博客园](https://www.cnblogs.com/wanghui-garcia/p/10664186.html)
