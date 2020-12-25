## Hash Table
### 目錄
* [Hash Table與Hash function原理](#hash-table與hash-function原理)
  * [Hash Table原理](#hash-table原理)
  * [Hash function原理](#hash-function原理)
* [Hash Table](#hash-table)
  * [流程圖](#流程圖)
  * [學習歷程](#學習歷程)


### Hash Table與Hash function原理
#### Hash Table原理
雜湊表，也叫哈希表，是根據 **鍵（Key）** 直接查詢在內存存儲位置的資料結構。也就是說，它透過 **雜湊函數（[Hash Function](#hash-function)）** ，將所需查詢的數據映射到表中一個位置來查詢記錄，加快了查找速度。    

參考資料：[雜湊表- 維基百科，自由的百科全書 - Wikipedia ](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)
* **規則**    
我的資料不一定是數字，也有可能是**文字**，因此每個字串被塞進去時要先得到一個唯一的、不重複的`編碼`，編碼完之後，讓array的長度當作mode的值，並取**餘數**，餘數就是要對應回到array的哪一格，那為了避免餘數相同的資料被覆蓋、`衝突`，要用linked list去串，這樣如果已經有第一筆餘數為a的資料，下一筆餘數也為a的資料就擺在它後面（next）。

* **使用時機**    
資料量很大的時候，想要很快速地查到某特定筆資料放在什麼位置。

* **優點**    
如果有很多筆資料，要找到某特定筆資料，把它mode完後餘多少，就去編號是那個餘數的抽屜（array的哪一格）找，不用把每個linked list都走訪一次。

* **衝突**    
Collision，發生不只一筆資料被存進同一個抽屜裡的情況。解決方法是用**linked list**去把那些會被存進同一個抽屜裡的資料串起來。

* **步驟**    
```
1. 將一筆文字資料透過數學模式轉換成16進位制的編碼。
2. 將編碼轉換成10進位制。
3. 用10進位制的系統提取餘數。
4. 把資料insert進去／知道放在array的第幾格（餘數多少，就是第幾格）。
5. 為了避免衝突，用linked list去串。
```

* **三種功能**    
```
1. add：新增。
2. remove：刪除。
3. contains：是否包含。
```

* **不同進位間的轉換**    

|轉⮮|2進位制|8進位制|10進位制|16進位制|
|:---:|:---:|:---:|:---:|:---:|
|**2進位制**|－|bin(int(x, 8))|bin(int(x, 10))|bin(int(x, 16))|
|**8進位制**|oct(int(x, 2))|－|oct(int(x, 10))|oct(int(x, 16))|
|**10進位制**|int(x, 2)|int(x, 8)|－|int(x, 16)|
|**16進位制**|hex(int(x, 2))|hex(int(x, 8))|hex(int(x, 10))|－|

#### Hash function原理
雜湊函數，也叫雜湊演算法，是將**不固定長度訊息**的輸入，演算成**固定長度雜湊值**的輸出。雜湊函數在資訊安全技術上所扮演的角色非常重要，應用範圍很廣泛。一般雜湊函數必須具備以下功能：
```
1. 雜湊函數必須對任意長度的訊息輸入，都產生固定長度的雜湊值輸出。
2. 對於任意訊息 M，雜湊函數可以輕易的計算出雜湊值 H(M)，並且可經由硬體或軟體來實現。
3. 如果給予雜湊值 h，在計算上無法找出原訊息 M，使其符合 h = H(M)，此特性稱之為「單向雜湊（One-way Hash）」。
4. 對於一個訊息 M1，在計算上無法找出另一個訊息 M2 （≠ M1），使得 H(M1) = H(M2)。也就是說，給定一個雜湊值H(M1)，
    須無法找出另一個訊息M2，使得 H(M1) = H(M2)。
5. 就兩訊息 M1、M2 而言，若他們的雜湊值相等，則 M1 與 M2 也一定相等；同理，若 H(M1)≠H(M2)，則 M1≠M2。也就是說，
    給定一個明文與雜湊值，須無法找出另一個訊息來產生相等的雜湊值。
```

* **雜湊值**    
不同明文所計算出來的雜湊值必須是不相同的，甚至只改變明文中任何一個字元時，雜湊值的輸出也必須有很大的差異。雜湊值就像是一個無法冒充的識別碼，每一份文件都有其特殊的雜湊值，且無法被偽造，故有「數位指紋（Digital Fingerprint）」之稱。計算出來的雜湊值必須符合以下條件：
```
1. 由雜湊值是無法反推出原來的訊息。
2. 雜湊值必須隨明文改變而改變。
```

參考資料：[第四章雜湊與亂數演算法 - 翻轉工作室 ](http://www.tsnien.idv.tw/Security_WebBook/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E9%9B%9C%E6%B9%8A%E8%88%87%E4%BA%82%E6%95%B8%E6%BC%94%E7%AE%97%E6%B3%95.html)

* **MD5**    
這次作業規定使用MD5，MD5 Message-Digest Algorithm，一種被廣泛使用的密碼雜湊函式，可以產生出一個128位元（16位元組）的雜湊值（hash value），用於確保資訊傳輸完整一致。    

參考資料：[MD5 - 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/MD5)

* **編碼**    
編碼有非常多種，例如MD5、SHA-1、Adler32、CRC32等，它們都跟餘數、質數的概念有關（細節在密碼學相關的課程教）。編碼直接呼叫Python裡面的編碼工具，叫MD5，而在做編碼工具時，會微調一些function裡面的細節，這次用的MD5，規定用以下這個套件產生出來：
```Python
from Crypto.Hash import MD5
```

#### 流程圖
<div align=center>▼圖一、Hash Table</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Hash%20Table.png?raw=true"/></div>
<br />

* **新增**

<br />
<div align=center>▼圖二、add</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Hash%20Table%20Insert.png?raw=true"/></div>
<br />

* **刪除**

<br />
<div align=center>▼圖三、remove</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Hash%20Table%20Remove.png?raw=true"/></div>
<br />

* **是否包含**

<br />
<div align=center>▼圖四、contains</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Hash%20Table%20Contains.png?raw=true"/></div>
<br />

#### 學習歷程
* **新增**    
這裡我參考了[Hash Tables - OmarElGabry's Blog - Medium](https://medium.com/omarelgabrys-blog/hash-tables-2fec6870207f)，他的put的架構，結合[Linked List | Set 2 (Inserting a node) - GeeksforGeeks](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/)，他的push的架構（讓新的node加在最前面）：
```Python
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        d = int(h.hexdigest(), 16) % self.capacity
        node = self.data[d]
        while node != None:
            if node.val == h:
                return
            node = node.next
        new = ListNode(h)
        new.next = self.data[d]
        self.data[d] = new
```
結果出來是錯的，沒有成功加進去。但是如果加的是key，是成功的，代表是h那裡出了問題，之後我查了資料並print了以下的程式才了解：
```Python
h.update("dog".encode("utf-8"))
```
▲這是**更新**MD5雜湊值，這時會回傳的h是hash的**位置**，而不是雜湊碼本身。
```Python
h = h.hexdigest()
```
▲這是**取得**MD5雜湊值，這樣才會**以字串形式回傳雜湊碼**。
```Python
h = int(h, 16)
```
▲在轉10進位制時，要改成這樣。
```Python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        d = int(h, 16) % self.capacity#取餘數當作第幾格抽屜
        node = self.data[d]
        while node != None:
            if node.val == h:
                return
            node = node.next
        new = ListNode(h)
        new.next = self.data[d]
        self.data[d] = new
```
這樣就成功了。
* **刪除**    
這裡我參考了[Linked List | Set 3 (Deleting a node) - GeeksforGeeks](https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/)，他的deleteNode的架構：
```Python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        d = int(h, 16) % self.capacity
        node = self.data[d]
        if node != None:
            if node.val == h:
                self.data[d] = node.next
                node = None
                return
        while node != None:
            if node.val == h:
                break
            prev = node
            node = node.next
        if node == None:
            return
        prev.next = node.next
        node = None
```
* **是否包含**    
這裡我參考了[Search an element in a Linked List (Iterative and Recursive) - GeeksforGeeks](https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/)，他的search的架構：
```Python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        d = int(h , 16) % self.capacity
        node = self.data[d]
        while node != None:
            if node.val == h:
                return True
            node = node.next
        return False
```
