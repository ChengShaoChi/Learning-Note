## Heap Sort

**Heap（堆積）**
* 是電腦科學中的一種特別的樹狀資料結構，且是Complete Binary Tree（完全二元樹），可以分為「**最小堆積（Min Heap）**」與「**最大堆積（Max Heap）**」兩種。在堆積中最頂端的那一個節點，稱作**根節點（root node）**，根節點本身沒有母節點（parent node）。    
    * Complete Binary Tree：是一種二元樹，它只允許最底下那層的節點數量不必填滿。有 **parent-child** 關係，index(i)的left child必定在index(2i)，right child必定在index(2i+1)，parent必定在index(i/2)。
    * Min Heap：由大到小**遞減**排序，上層節點數值必會小於下層節點數值。    
    * Max Heap：由小到大**遞增**排序，上層節點數值必會大於下層節點數值。

**Heap Sort（堆積排序法）**
* 利用Heap結構來完成排序。    
    
   

參考資料：    
https://magiclen.org/heap-sort/   
http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
