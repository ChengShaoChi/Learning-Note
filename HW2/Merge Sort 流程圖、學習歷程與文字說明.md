## Merge Sort
### 目錄
* [文字說明](#文字說明)
* [流程圖](#流程圖)
* [學習歷程](#學習歷程)
### 文字說明
#### Merge Sort（合併排序法）
* 是排序演算法的一種，使用Divide and Conquer的演算法來實作。
  * Divide and Conquer（分治法）：「分而治之」，就是把一個複雜的問題分成兩個或更多的相同或相似的子問題，直到最後子問題可以簡單的直接求解，原問題的解即子問題的解的合併。
* 分成兩個步驟：    
   1.分割：遞迴地把目前陣列平均分割成兩半。    
   2.合併：在保持元素順序的同時將上一步得到的子陣列整合到一起。    
   <div align=center>▼圖一、Merge Sort步驟</div>    
   <div align=center><img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif"/></div>    
   圖片來源：[合併排序- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)
* 我的理解：把陣列不斷分割到只剩一個元素後，兩個兩個進行排序並合併，直到全部合併完成。
   
參考資料：    
[分治法- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%88%86%E6%B2%BB%E6%B3%95)    
[合併排序法(Merge Sort) @ 小殘的程式光廊:: 痞客邦::](https://emn178.pixnet.net/blog/post/87965707)

### 流程圖
### 學習歷程
```Python
class Solution(object):
    def merge_sort(self, nums):
