from collections import defaultdict

class Graph:
    def __init__(self):#用Adjacency List表示法表示有向圖。
        self.graph = defaultdict(list)#用defaultdict來儲存圖，並以一個list產生。
        
    def addEdge(self,u,v):#為圖加上邊。
        self.graph[u].append(v)
        
    def BFS(self, s):
        iffound = []#創一個iffound，如果是找到過的就放進去。
        queue = []#創一個queue，放被找到的，且最前面的當起點。
        found = []#創一個found，放被移除queue的。
        
        queue.append(s)#把起點放進queue裡，
        iffound.append(s)#並標記為找到過了的。
        
        while queue:#當queue裡有點，
            s = queue.pop(0)#把它最前面的移除（當起點），
            found.append(s)#並加到found。
            
            for i in self.graph[s]:#找到與其相鄰的（ex：這題的2的相鄰的就是0、3），
                if i not in iffound:#如果是還沒找到過的，
                    queue.append(i)#將其放進queue裡，
                    iffound.append(i)#並標記為找到過了的。
                    
        return found
    
    def DFS(self, s):
        iffound = []#創一個iffound，如果是找到過的就放進去。
        stack = []#創一個stack，放被找到的，且最上面的當起點
        found = []#創一個found，放被移除stack的
        
        found.append(s)#先把s放進found，
        iffound.append(s)#並標記為找到過了的。
        
        for i in self.graph[s]:#找到與其相鄰的（ex：這題的2的相鄰的就是0、3），
            if i not in iffound:#如果是還沒找到過的（False），
                stack.append(i)#將其放進stack裡，
                iffound.append(i)#並標記為找到過了的。
                
        while stack:#當stack裡有點，
            s = stack.pop(-1)#把它最上面的移除（當起點），
            found.append(s)#並加到found。
            
            for i in self.graph[s]:
                if i not in iffound:
                    stack.append(i)
                    iffound.append(i)
                    
        return found
