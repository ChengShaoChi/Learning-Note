## Quick Sort
### 目錄
* [原理、筆記](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW1/Quick%20Sort.ipynb)
* [程式碼](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW1/Quick%20Sort.py)
* [流程圖](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW1/QuickSort.png)
### 簡述
* 快速排序，又稱劃分交換排序（Partition-Exchange Sort），簡稱快排，一種排序演算法。採用分割與征服（Divide and Conquer）策略從數列中挑選一個基準點，大於基準的放一邊，小於的放一邊，如此循環最後可完成排序。最壞時間複雜度Θ(n^2)，最佳時間複雜度Θ(nlogn)，平均時間複雜度	Θ(nlogn)。    
* 步驟：
1. 從數列中挑出一個元素作為基準值，稱為「基準」（pivot）。
2. 重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面（與基準值相等的數可以到任何一邊）。在這個分割結束之後，對基準值的排序就已經完成，
3. 遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。

參考資料：    
[快速排序- 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)    
[快速排序法(Quick Sort) @ 小殘的程式光廊:: 痞客邦::](https://emn178.pixnet.net/blog/post/88613503-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95(quick-sort))
