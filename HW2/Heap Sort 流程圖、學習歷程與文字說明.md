## Heap Sort
### 目錄
* [文字說明](#文字說明)
   * Heap
   * Heap Sort
* [流程圖](#流程圖)
* [學習歷程](#學習歷程)
### 文字說明
#### Heap（堆積）
* 是電腦科學中的一種特別的樹狀資料結構，且是Complete Binary Tree。可以分為「**Min Heap**」與「**Max Heap**」兩種。兄弟節點的大小不重要。在堆積中最頂端的那一個節點，稱作**根節點（root node）**，根節點本身沒有母節點（parent node）。    
    * Complete Binary Tree（完全二元樹）：是一種二元樹，只有最底下那層的節點數量不必填滿，且必須由左至右填入，其他的每個父節點都有兩個子節點。有 **parent-child** 關係，index(i)的left child必定在index(2i+1)，right child必定在index(2i+2)，parent必定在index((i-1)//2)。
    * Min Heap（最小堆積）：由大到小**遞減**排序，上層節點的值必會小於下層節點的值。    
    * Max Heap（最大堆積）：由小到大**遞增**排序，上層節點的值必會大於下層節點的值。

#### Heap Sort（堆積排序法）
* 利用Heap結構來完成排序。
* 分成兩個步驟／函式：    
   1.heapify：把陣列製作成Min Heap或Max Heap。    
   2.heapSort：利用Min Heap或Max Heap來進行排序。    
   
   以Max Heap為例：    
   ![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/HeapSortUnderstandingtheCode.png?raw=true)        
   截圖自：[Heap Sort | GeeksforGeeks - YouTube](https://youtu.be/MtQL_ll5KhQ)    
* 我的理解：先把陣列製作成Max Heap，讓 **從下面數來第一個有小孩的節點（index = n//2-1）** 開始跟它的左右小孩比，比小孩小就交換，製造完Max Heap後，開始排序，方式是把array的第一個值跟最後一個值交換，一換完，最大值跑到array的最後一位，就不用管它了（array的長度減1），其他的要再跑heapify一次，讓第一個節點（index = 0）跟它的小孩比。比完再換位置，循環。
   
參考資料：    
[堆積- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%A0%86%E7%A9%8D)    
[堆積排序(Heap Sort)演算法，利用完全二元樹來排序的演算法](https://magiclen.org/heap-sort/)   
[Comparison Sort: Heap Sort(堆積排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
### 流程圖
### 學習歷程
```Python
class Solution(object):
    def heap_sort(self, nums):
