## Dijkstra與Kruskal
### 資料夾目錄
* [**原理**](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW6/Dijkstra%E8%88%87Kruskal%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E7%A8%8B%E5%BC%8F%E7%A2%BC%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Dijkstra%E8%88%87Kruskal%E5%8E%9F%E7%90%86%E8%AA%AA%E6%98%8E.md)
* [**程式碼**](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW6/Dijkstra_06170235.py)
### Dijkstra簡述
* 戴克斯特拉演算法（Dijkstra's Algorithm），是一種**貪婪演算法**，如果有一個有向圖，所有邊（edge）的權重（weight）皆為非負實數（≧0），便能夠使用Dijkstra's Algorithm處理**Single-Source Shortest Path**問題。Dijkstra's Algorithm原始版本是找到兩個節點之間的最短路徑，但是更常見的變體固定了一個頂點作為源節點然後找到該頂點到圖中所有其它節點的最短路徑，產生一個**最短路徑樹**。
  * `貪婪演算法（Greedy Algorithm）`：是一種在每一步選擇中都採取在目前狀態下最好或最佳的選擇（**Optimal Solution**），從而希望導致結果是最好或最佳的演算法。
  * `單源最短路徑（Single-Source Shortest Path）`：從給定單一vertex作為起點，到圖中其它所有的vertex之最短路徑。
  * `最短路徑樹（Shortest-Path Tree）`：考慮一個連通無向圖G，一個以頂點v為根節點的最短路徑樹T是圖G滿足下列條件的生成樹－樹T中從根節點v到其它頂點u的路徑距離，在圖G中是從v到u的最短路徑距離。
* 步驟：
```
  1. 選擇某一節點當作起點
  2. 在與起點相鄰且尚未被找到的節點裡，選擇離起點距離最短的節點。
  3. 透過新增的節點更新到達其他節點的距離。
  4. 重覆步驟3，找新節點，直到所有的節點都被找到過為止。
```
### Kruskal簡述
* 克魯斯克爾演算法（Kruskal's Algorithm），是一種**貪婪演算法**，用來尋找最小生成樹的演算法。
  * `最小生成樹（MST，Minimum Spanning Tree）`：最小權重生成樹，在一張連通加權無向圖中一棵權值最小的生成樹。在一給定的無向圖G = (V, E)中，(u, v)代表連接頂點u與頂點v的邊（即(u,v)∈E），而 w(u, v) 代表此邊的權重，若存在 T 為 E 的子集（即T⊆E）且(V, T)為樹，使得![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/ea325be8060fd36f76e7bb61543a30e71b9c3b05)的w(T)最小，則此T為G的最小生成樹。

* 步驟：
```
  1. 先把所有邊照weight從小排到大。
  2. 對所有點做Disjoint Set初始化，也就是把所有點的parent設為-1。
  3. 以weight的小到大，去枚舉每條邊。
  4. 對於每條邊，看看該邊所連接的兩點，是否屬於同個set，不同就將該邊標上使用，並union他們，有的話代表會出現cycle，不union。
  5. 用步驟3的順序來重複步驟4，直到所有邊都被枚舉完。
  ＊想像每個點都是獨立的，邊不存在。
  ＊Find()操作在節點parent為-1時會回傳節點本身編號。
```

參考資料：    
[Single-Source Shortest Path：Dijkstra's Algorithm](http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html)    
[貪婪演算法- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)    
[最短路徑樹- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%91%E6%A8%B9)    
[代克思托演算法(Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)    
[[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w)        
[克魯斯克爾演算法- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)    
[最小生成樹- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91)
