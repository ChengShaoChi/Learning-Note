## Merge Sort
### 目錄
* [文字說明](#文字說明)
* [流程圖](#流程圖)
* [學習歷程](#學習歷程)
### 文字說明
#### Merge Sort（合併排序法）
* 是排序演算法的一種，使用Divide and Conquer的演算法來實作。
  * Divide and Conquer（分治法）：「分而治之」，就是把一個複雜的問題分成兩個或更多的相同或相似的子問題，直到最後子問題可以簡單的直接求解，原問題的解即子問題的解的合併。
* 分成兩個步驟／函式：    
   1.分割：遞迴地把目前陣列平均分割成兩半。    
   2.合併：在保持元素順序的同時將上一步得到的子陣列整合到一起。
* 我的理解：把陣列不斷分割到只剩一個元素後，兩個兩個進行排序並合併，直到全部合併完成。
   
參考資料：    
https://zh.wikipedia.org/wiki/%E5%88%86%E6%B2%BB%E6%B3%95    
https://emn178.pixnet.net/blog/post/87965707

### 流程圖
### 學習歷程
```Python
class Solution(object):
    def merge_sort(self, nums):
