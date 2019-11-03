## Heap Sort

**Heap（堆積）**
* 是電腦科學中的一種特別的樹狀資料結構，且是Complete Binary Tree（完全二元樹）。可以分為「**最小堆積（Min Heap）**」與「**最大堆積（Max Heap）**」兩種。在堆積中最頂端的那一個節點，稱作**根節點（root node）**，根節點本身沒有母節點（parent node）。    
    * Complete Binary Tree：是一種二元樹，它只允許最底下那層的節點數量不必填滿，且最後一階層的節點必須由左至右填入。有 **parent-child** 關係，index(i)的left child必定在index(2i+1)，right child必定在index(2i+2)，parent必定在index((i-1)//2)。
    * Min Heap：由大到小**遞減**排序，上層節點數值必會小於下層節點數值。    
    * Max Heap：由小到大**遞增**排序，上層節點數值必會大於下層節點數值。

**Heap Sort（堆積排序法）**
* 利用Heap結構來完成排序。    
* 分成兩個步驟：    
    1. 把要排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。
    2. 利用最大堆積和最小堆積來進行排序。
    
   

參考資料：    
https://zh.wikipedia.org/wiki/%E5%A0%86%E7%A9%8D
https://magiclen.org/heap-sort/   
http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
