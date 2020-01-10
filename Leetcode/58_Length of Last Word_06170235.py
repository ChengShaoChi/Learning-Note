class Solution:
    def lengthOfLastWord(self, s: str):
        s = s.rstrip()
        s = s.split(' ')
        return len(s[-1])
        
#參考資料：https://blog.csdn.net/coder_orz/article/details/51702268

#rstrip()：刪除字串末端的指定字符，默認是空格。
  #這題用來處理當輸入的字串都是空格或末端有空格時的問題，先把空格都刪掉。
#split():以指定分隔符把字串分開成好幾個字串。
  #這題把s以空格分開。
