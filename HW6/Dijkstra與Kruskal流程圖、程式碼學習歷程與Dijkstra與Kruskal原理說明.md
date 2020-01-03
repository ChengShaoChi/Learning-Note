## Dijkstra與Kruskal
### 目錄
* [Dijkstra與Kruskal流程圖](#dijkstra與kruskal流程圖)
* [程式碼學習歷程](#程式碼學習歷程)
* [Dijkstra與Kruskal原理說明](#dijkstra與kruskal原理說明)
  * [Dijkstra原理](#dijkstra原理)
  * [Kruskal原理](#kruskal原理)
### Dijkstra與Kruskal流程圖
#### Dijkstra
<div align=center>▼Dijkstra的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra%E6%B5%81%E7%A8%8B%E5%9C%96.png?raw=true"/></div>
<br />

#### Kruskal
<div align=center>▼Kruskal的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal%E6%B5%81%E7%A8%8B%E5%9C%96.png?raw=true"/></div>
<br />

### 程式碼學習歷程
參考資料：[Dijsktra's algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
```Python
import sys
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices#圖中的頂點總數。
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)]
        #創一個vertices乘vertices的矩陣，裡面都是0。column：有幾直／row：有幾橫。
        
    def minDistance(self, dist, found):#在還沒找到過的點中找到有最小距離的點
        unlm = sys.maxsize#令到還不能到的點的距離是無限大，這裡用Python中整數的最大值代替
        
        #在還沒找到過的點中找到最近的點
        for v in range(self.V):
            if dist[v] < unlm and v not in found:
                unlm = dist[v]
                unlm_index = v
        return unlm_index

    def Dijkstra(self, s):
        dist = [sys.maxsize] * self.V#令所有點與點間的距離都是無限大
        dist[s] = 0#起點到起點的距離是0
        found = []#找到過的放進去
  
        for cout in range(self.V):
            u = self.minDistance(dist, found)#在還沒找到過的點中選擇有最小距離的點，在第一次迭代中，u是起點
            found.append(u)#將最小距離的點放進found，代表找到過的了
            
            #只有在當前距離大於新距離且該頂點不在found裡時，才更新選取的頂點的相鄰頂點的距離
            for v in range(self.V):
                if self.graph[u][v] > 0 and v not in found and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        SSSP = {}
        for i in range(self.V):
            SSSP[str(i)] = dist[i]
        return SSSP
```
`sys.maxsize`：Python中整數的最大值，9223372036854775807。
### Dijkstra與Kruskal原理說明
#### Dijkstra原理
戴克斯特拉演算法（Dijkstra's Algorithm），是一種**貪婪演算法**，如果有一個有向圖，所有邊（edge）的權重（weight）皆為非負實數（≧0），便能夠使用Dijkstra's Algorithm處理**Single-Source Shortest Path**問題。Dijkstra's Algorithm原始版本是找到兩個節點之間的最短路徑，但是更常見的變體固定了一個頂點作為源節點然後找到該頂點到圖中所有其它節點的最短路徑，產生一個**最短路徑樹**。
* 貪婪演算法（Greedy Algorithm）：是一種在每一步選擇中都採取在目前狀態下最好或最佳的選擇（**Optimal Solution**），從而希望導致結果是最好或最佳的演算法。
* 單源最短路徑（Single-Source Shortest Path）：從給定單一vertex作為起點，到圖中其它所有的vertex之最短路徑。
* 最短路徑樹（Shortest-Path Tree）：考慮一個連通無向圖G，一個以頂點v為根節點的最短路徑樹T是圖G滿足下列條件的生成樹－樹T中從根節點v到其它頂點u的路徑距離，在圖G中是從v到u的最短路徑距離。
* 步驟：
```
1. 選擇某一節點當作起點
2. 在與起點相鄰且尚未被找到的節點裡，選擇離起點距離最短的節點。
3. 透過新增的節點更新到達其他節點的距離。
4. 重覆步驟3，找新節點，直到所有的節點都被找到過為止。
```
* 例子：

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra%E7%A9%BA%E7%99%BD.png?raw=true)

||⓪|1|2|3|4|5|6|7|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|∞|∞|∞|∞|∞|∞|∞|∞|

    ▲有個graph，我要對它做Dijkstra's Algorithm。選擇節點0當起點。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(1).png?raw=true)

||⓪|①|2|3|4|5|6|7|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|

    ▲與其相鄰的且沒找到過的有節點1、7，選擇最小的距離4，加入節點1。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(2).png?raw=true)

||⓪|①|2|3|4|5|6|⑦|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|

    ▲與節點1相鄰的且沒找到過的有節點2：4＋8＝12，選擇最小的距離8，加入節點7。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(3).png?raw=true)

||⓪|①|2|3|4|5|⑥|⑦|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|
|**(0, 1, 7)**|0|4|12|∞|∞|∞|9|8|15|

    ▲與節點7相鄰的且沒找到過的有節點6：8＋1＝9、8：8＋7＝15，選擇最小的距離9，加入節點6。
    
![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(4).png?raw=true)
    
||⓪|①|2|3|4|5|⑥|⑦|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|
|**(0, 1, 7)**|0|4|12|∞|∞|∞|9|8|15|
|**(0, 1, 7, 6)**|0|4|12|∞|∞|11|9|8|15|

    ▲與節點6相鄰的且沒找到過的有節點5：9＋2＝11，選擇最小的距離11，加入節點5。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(5).png?raw=true)

||⓪|①|2|3|4|⑤|⑥|⑦|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|
|**(0, 1, 7)**|0|4|12|∞|∞|∞|9|8|15|
|**(0, 1, 7, 6)**|0|4|12|∞|∞|11|9|8|15|
|**(0, 1, 7, 6, 5)**|0|4|12|25|21|11|9|8|15|

    ▲與節點5相鄰的且沒找到過的有節點3：11＋14＝25、4：11＋10＝21，選擇最小的距離12，加入節點2。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(6).png?raw=true)

||⓪|①|②|3|4|⑤|⑥|⑦|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|
|**(0, 1, 7)**|0|4|12|∞|∞|∞|9|8|15|
|**(0, 1, 7, 6)**|0|4|12|∞|∞|11|9|8|15|
|**(0, 1, 7, 6, 5)**|0|4|12|25|21|11|9|8|15|
|**(0, 1, 7, 6, 5, 2)**|0|4|12|19|21|11|9|8|14|

    ▲與節點2相鄰的都找到過了，但是要更新最短距離3：12＋7＝19，8：12＋2＝14，選擇最小的距離14，加入節點8。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(7).png?raw=true)

||⓪|①|②|3|4|⑤|⑥|⑦|⑧|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|
|**(0, 1, 7)**|0|4|12|∞|∞|∞|9|8|15|
|**(0, 1, 7, 6)**|0|4|12|∞|∞|11|9|8|15|
|**(0, 1, 7, 6, 5)**|0|4|12|25|21|11|9|8|15|
|**(0, 1, 7, 6, 5, 2)**|0|4|12|19|21|11|9|8|14|
|**(0, 1, 7, 6, 5, 2, 8)**|0|4|12|19|21|11|9|8|14|

    ▲與節點8相鄰的都找到過了，選擇最小的距離19，加入節點3。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(8).png?raw=true)

||⓪|①|②|③|4|⑤|⑥|⑦|⑧|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|∞|∞|∞|∞|∞|8|∞|
|**(0, 1)**|0|4|12|∞|∞|∞|∞|8|∞|
|**(0, 1, 7)**|0|4|12|∞|∞|∞|9|8|15|
|**(0, 1, 7, 6)**|0|4|12|∞|∞|11|9|8|15|
|**(0, 1, 7, 6, 5)**|0|4|12|25|21|11|9|8|15|
|**(0, 1, 7, 6, 5, 2)**|0|4|12|19|21|11|9|8|14|
|**(0, 1, 7, 6, 5, 2, 8)**|0|4|12|19|21|11|9|8|14|
|**(0, 1, 7, 6, 5, 2, 8, 3)**|0|4|12|19|21|11|9|8|14|

    ▲與節點8相鄰的都找到過了，而且更新4：19＋9＝28，沒有比較小，維持4：21，選擇最小的距離21，加入節點4。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Dijkstra(9).png?raw=true)

||⓪|①|②|③|④|⑤|⑥|⑦|⑧|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|0|4|12|19|21|11|9|8|14|

    ▲所有結點都找到過了，Dijkstra's Algorithm完成。

參考資料：    
[Single-Source Shortest Path：Dijkstra's Algorithm](http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html)    
[貪婪演算法- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)    
[最短路徑樹- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%91%E6%A8%B9)    
[代克思托演算法(Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)    

#### Kruskal原理
克魯斯克爾演算法（Kruskal's Algorithm），是一種**貪婪演算法**，用來尋找最小生成樹的演算法。
* 最小生成樹（MST，Minimum Spanning Tree）：最小權重生成樹，在一張連通加權無向圖中一棵權值最小的生成樹。在一給定的無向圖G = (V, E)中，(u, v)代表連接頂點u與頂點v的邊（即(u,v)∈E），而 w(u, v) 代表此邊的權重，若存在 T 為 E 的子集（即T⊆E）且(V, T)為樹，使得![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/ea325be8060fd36f76e7bb61543a30e71b9c3b05)的w(T)最小，則此T為G的最小生成樹。

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
* 例子：

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal%E7%A9%BA%E7%99%BD.png?raw=true)

    ▲有個graph，我要對它做Kruskal's Algorithm。把所有點的parent設為-1。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(1).png?raw=true)

|Edge|76|
|:---:|:---:|
|**Weight**|**1**|

    ▲第一條邊76，7的findroot是7，6的findroot是6，兩個不一樣，把兩個union，並把6的parent改成7。
    
![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(2).png?raw=true)

|Edge|76|82|
|:---:|:---:|:---:|
|**Weight**|**1**|**2**|

    ▲第二條邊82，8的findroot是8，2的findroot是2，兩個不一樣，把兩個union，並把2的parent改成8。
    
![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(3).png?raw=true)

|Edge|76|82|65|
|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|

    ▲第三條邊65，6的findroot是7，5的findroot是5，兩個不一樣，把兩個union，並把5的parent改成6再改成7。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(4).png?raw=true)

|Edge|76|82|65|01|
|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|

    ▲第四條邊01，0的findroot是0，1的findroot是1，兩個不一樣，把兩個union，並把1的parent改成0。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(5).png?raw=true)

|Edge|76|82|65|01|25|
|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|

    ▲第五條邊25，2的findroot是8，5的findroot是7，兩個不一樣，把兩個union，並把5的parent改成2再改成8。
     另外6、7的parent原本是7也要改成8。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(6).png?raw=true)

|Edge|76|82|65|01|25|
|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|

    ▲第六條邊86，8的findroot是8，6的findroot也是8，兩個一樣，不能union。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(7).png?raw=true)

|Edge|76|82|65|01|25|23|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|**7**|

    ▲第七條邊23，2的findroot是8，3的findroot是3，兩個不一樣，把兩個union，並把3的parent改成2再改成8。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(8).png?raw=true)

|Edge|76|82|65|01|25|23|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|**7**|

    ▲第八條邊78，7的findroot是8，8的findroot也是8，兩個一樣，不能union。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(9).png?raw=true)

|Edge|76|82|65|01|25|23|07|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|**7**|**8**|

    ▲第九條邊07，0的findroot是0，7的findroot是8，兩個不一樣，把兩個union，並把7的parent改成0。
     另外2、3、5、6、8的parent原本是8也要改成0。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(10).png?raw=true)

|Edge|76|82|65|01|25|23|07|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|**7**|**8**|

    ▲第十條邊12，1的findroot是0，2的findroot也是0，兩個一樣，不能union。
    
![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(11).png?raw=true)

|Edge|76|82|65|01|25|23|07|34|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**Weight**|**1**|**2**|**2**|**4**|**4**|**7**|**8**|**9**|

    ▲第十一條邊34，3的findroot是0，4的findroot是4，兩個不一樣，把兩個union，並把4的parent改成3再改成0。
     總共連成8個邊就代表結束，因為此graph有9個點，而邊至多只能有點減一條，也就是E＝V－1。
     Kruskal's Algorithm完成。

![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Kruskal(12).png?raw=true)

參考資料：    
[[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w)        
[克魯斯克爾演算法- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)    
[最小生成樹- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91)
