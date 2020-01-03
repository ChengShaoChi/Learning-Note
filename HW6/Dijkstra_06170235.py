import sys
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices#圖中的頂點總數。
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)]
        #創一個vertices乘vertices的矩陣，裡面都是0。column：有幾直／row：有幾橫。
        
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w]) 
        
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
      
      
      
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
      
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def Kruskal(self):
        result =[]
        i = 0
        e = 0
        self.graph = sorted(self.graph,key = lambda item:item[2]) 
        parent = [] ; rank = [] 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V -1:
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
                
        MST = {}
        for u, v, weight in result:
            MST[str(u)+'-'+str(v)] = weight
        return MST
      
#參考資料：
#https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
#https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
