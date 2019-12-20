## BFS與DFS
### 目錄
* [BFS與DFS流程圖](#bfs與dfs流程圖)
* [程式碼學習歷程](#程式碼學習歷程)
* [BFS與DFS原理與比較](#bfs與dfs原理與比較)
  
### BFS與DFS流程圖
#### BFS
<div align=center>▼圖一、BFS的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BFS%E6%B5%81%E7%A8%8B%E5%9C%962.png?raw=true"/></div>
<br />

#### DFS
<div align=center>▼圖二、DFS的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/DFS%E6%B5%81%E7%A8%8B%E5%9C%962.png?raw=true"/></div>
<br />

### 程式碼學習歷程
```Python
from collections import defaultdict
```
第一行就看不懂，去查了資料並補充如下：    
`dict`：字典（Dictionary），是一種可變容器模型，且可以儲存任意類型的對象。    
`defaultdict`：collections提供的defaultdict，對於我們調用一個不存在的key值，它會先建立一個default（默認）值給我們，而這個default值必須由一個可呼叫的函數產生，在我們初始化一個defaultdict時，必須先指定一個產生default值的函數，例如以一個list()方法產生。

參考資料：    
[Python 字典(Dictionary) | 菜鸟教程](https://www.runoob.com/python/python-dictionary.html)    
[collections雜談之一 ——— dict的key值存不存在乾我屁事](https://ithelp.ithome.com.tw/articles/10193094)

```Python
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
```
如上述說的要先指定一個產生default值的函數，這裡**讓default值以一個list產生**。

```Python
    def addEdge(self,u,v):
        self.graph[u].append(v)
```
這裡是**為點加上邊**的功能，為點u加上點v，讓點u和點v之間有邊連接。有點像multidict，用defaultdict實現multidict。    
`multidict`：在字典中，某個鍵可能對應多個值，可以將這些值存入一個列表中，以後遍歷訪問。

參考資料：    
[Python MultiDict 的实现 - 站在巨人的肩上](http://matrix.ac.cn/blog/article/90/)    
[tuple inside list for finding values - Stack Overflow](https://stackoverflow.com/questions/3977635/tuple-inside-list-for-finding-values)

接著，我參考了[Breadth First Search or BFS for a Graph - GeeksforGeeks](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)，寫了BFS：
1. 創一個iffound，判斷每個點是否被找到過，如果是找到過的就放進去，一開始就將起點（s）放進去。
2. 創一個queue，把當下被找到的放進去，且最前面的當起點，最後會清空。
3. 創一個found，放被移除queue的，最後要回傳的。
4. 把起點放進queue裡，並加進iffound，代表被找到過的。
5. 把queue裡最前面的移除並加到found，並把它當成起點找它的鄰點。
6. 如果鄰點是還沒找到過的（不在iffound），就將其放進queue裡，並加進iffound。
```Python
    def BFS(self, s):
        iffound = []
        queue = []
        found = []
        
        queue.append(s)
        iffound.append(s)
        
        while queue:
            s = queue.pop(0)
            found.append(s)
            
            for i in self.graph[s]:
                if i not in iffound:
                    queue.append(i)
                    iffound.append(i)
                    
        return found
```
之後，我直接用BFS的概念去改成DFS：
1. 創一個iffound，判斷每個點是否被找到過，如果是找到過的就放進去，一開始就將起點（s）放進去。
2. 創一個stack，把當下被找到的放進去，且最上面的當起點，最後會清空。
3. 創一個found，放被移除stack的，最後要回傳的。
4. 把起點s放進found，並加進iffound，代表被找到過的。
5. 找它的鄰點，如果鄰點是還沒找到過的（不在iffound），就將其放進stack裡，並加進iffound。
6. 把stack裡最上面的移除並加到found，並把它當成起點找它的鄰點。
7. 如果鄰點是還沒找到過的，就將其放進stack裡，並加進iffound。
```Python
    def DFS(self, s):
        iffound = []
        stack = []
        found = []
        
        found.append(s)
        iffound.append(s)
        
        for i in self.graph[s]:
            if i not in iffound:
                stack.append(i)
                iffound.append(i)
                
        while stack:
            s = stack.pop(-1)
            found.append(s)
            
            for i in self.graph[s]:
                if i not in iffound:
                    stack.append(i)
                    iffound.append(i)
                    
        return found
```
### BFS與DFS原理與比較
#### Graph（圖）    
* 圖就是進階版的樹（tree），它們都有點跟邊，但是樹不能有loop，且一定是由上而下；而圖可以有loop，且可以往回，其資料型態很像hash table。    
* 圖用於表示物件與物件之間的關係，有多種變體，大體上有二元組和三元組這兩種定義方式。當一張圖G是一個**二元組**(V,E)，其中V或V(G)稱為頂點（vertex）集，E或E(G)稱為邊（edge）集。E的元素是一個二元組數對，用(x,y)表示，其中x,y ∈ V。    
* 圖根據edge是否具有「方向性」，可分成`directed graph（有向圖）`和`undirected graph（無向圖）`。    
* 圖一般有兩種常用的「表示法」，`Adjacency Matrix（相鄰矩陣）`和`Adjacency List（相鄰串列）`。    
  * Adjacency List：先以一個一維陣列列出所有的vertex，再以linked list表示所有與vertex相連的vertex（vertex接進linked list的順序不重要），如下圖三。這次作業使用這種表示法。
<div align=center>▼圖三、Adjacency List</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BFS%E7%A9%BA%E7%99%BD%E6%97%81%E9%82%8A%E6%9C%89.png?raw=true"/></div>
<br />

* 圖的「遍歷方法」有[`BFS`](#bfs原理)和[`DFS`](#dfs原理)。

參考資料：    
[圖(數學) - 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%9B%BE_(%E6%95%B0%E5%AD%A6))    
[Graph: Intro(簡介)](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)


#### BFS原理
Breadth-First Search，**廣度**優先搜尋，也稱為**寬度**優先搜尋或**橫向**優先搜尋，是一種用於遍歷或搜尋樹或圖的演算法。各個點相對於root有其對應的level，BFS是按照level，由小到大依序對點進行走訪。如果所有的點均被存取，則演算法中止。level代表點與root的「距離」，以graph的語言來說，距離便是路徑的length（長度）／distance（距離）。
<div align=center>▼圖四、有個graph</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BFS%E7%A9%BA%E7%99%BD.png?raw=true"/></div>
<br />

我要對圖四的graph做BFS()：    
1. 選擇**E**作為起點，把E放進queue，以queue的最前面的當作新的起點搜尋，新的起點就是E，與其相鄰的有**B、C、F**，它們被E找到了，按照找到的順序，把它們依序放進queue裡，並把E移除queue。    
2. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**B**，與其相鄰的有A、E，E已經被找到過了，所以B只能找到**A**，把A放進queue裡，並把B移除queue。    
3. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**C**，與其相鄰的有A、E、F、G、H，A、E、F已經被找到過了，所以C只能找到**G、H**，按照找到的順序，把它們依序放進queue裡，並把C移除queue。    
4. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**F**，與其相鄰的有E、C、I，E、C已經被找到過了，所以F只能找到**I**，把I放進queue裡，並把F移除queue。    
5. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**A**，與其相鄰的有B、C、D，B、C已經被找到過了，所以A只能找到**D**，把D放進queue裡，並把A移除queue。    
6. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**G**，與其相鄰的有H、C、I，它們都已經被找到過了，直接把G移除queue。    
7. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**H**，與其相鄰的有D、C、G，它們都已經被找到過了，直接把H移除queue。    
8. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**I**，與其相鄰的有F、G，它們都已經被找到過了，直接把I移除queue。    
9. 繼續以queue的最前面的當作新的起點搜尋，新的起點就是**D**，與其相鄰的有A、H，它們都已經被找到過了，直接把D移除queue。    
10. queue裡所有的node都被移除了，表示它們都被當作起點搜尋過其相鄰的node，也代表BFS()完成了。

<div align=center>▼圖五、步驟的動圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BFS.gif?raw=true"/></div>
<br />

參考資料：    
[广度优先搜索- 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)    
[Graph: Breadth-First Search(BFS，廣度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

#### DFS原理
Depth-First Search，**深度**優先搜尋，是一種用於遍歷或搜尋樹或圖的演算法。先遇到的點就先尋訪，並且以先遇到的點作為新的搜尋起點，直到所有有邊相連的點都被探索過。
<div align=center>▼圖六、有個graph</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BFS%E7%A9%BA%E7%99%BD.png?raw=true"/></div>
<br />

我要對圖六的graph做DFS()：
1. 選擇**G**作為起點，與其相鄰的有**E**，把E放進stack裡。
2. 繼續以stack的最上面的當作新的起點搜尋，新的起點就是**E**，與其相鄰的有**B、F**，把它們放進stack裡，並把E移除stack。
3. 繼續以stack的最上面的當作新的起點搜尋，新的起點就是**F**，與其相鄰的有**A**，把A放進stack裡，並把F移除stack。
4. 繼續以stack的最上面的當作新的起點搜尋，新的起點就是**A**，與其相鄰的有B、D，B已經被找到過了，所以把**D**放進stack裡，並把A移除stack。
5. 繼續以stack的最上面的當作新的起點搜尋，新的起點就是**D**，與其相鄰的有F，它已經被找到過了，直接把D移除stack。
6. 繼續以stack的最上面的當作新的起點搜尋，新的起點就是**B**，與其相鄰的有**C**，把C放進stack裡，並把B移除stack。
7. 繼續以stack的最上面的當作新的起點搜尋，新的起點就是**C**，與其相鄰的有E、G，它們都已經被找到過了，直接把C移除stack。
8. stack裡所有的node都被移除了，表示它們都被當作起點搜尋過其相鄰的node，也代表DFS()完成了。

<div align=center>▼圖七、步驟的動圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/DFS.gif?raw=true"/></div>
<br />

參考資料：    
[深度優先搜尋- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)    
[Graph: Depth-First Search(DFS，深度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

#### BFS與DFS比較
||BFS|DFS|
|:---:|:---:|:---:|
|英文|**Breadth**-First Search|**Depth**-First Search|
|中文|**廣度**優先搜尋|**深度**優先搜尋|
|基於|點|邊|
|資料結構|Queue|Stack|
|記憶體使用|較多|較少|
|空間複雜度|O(V+E)|O(V+E)|
|時間複雜度|O(V+E)|O(V+E)|
|找最短路徑|✓||

＊ 使用Adjacency List表示法。    
＊ V是節點的數目，E是邊的數目。

參考資料：    
[Difference Between BFS and DFS](https://techdifferences.com/difference-between-bfs-and-dfs.html)
