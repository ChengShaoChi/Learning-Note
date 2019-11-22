## Binary Search Tree
### 目錄
* [原理](#原理)
* [流程圖與學習歷程](#流程圖與學習歷程)
  * [新增](#新增)
  * [刪除](#刪除)
  * [查詢](#查詢)
  * [修改](#修改)

### 原理
* Binary Search Tree（二元搜尋樹）：也稱為ordered binary tree（有序二元樹）或sorted binary tree（排序二元樹），是指一棵空樹或者具有下列性質的二元樹：    
  1.若任意節點的左子樹不空，則左子樹上所有節點的值均小於其根節點的值。    
  2.若任意節點的右子樹不空，則右子樹上所有節點的值均大於其根節點的值。    
  3.任意節點的左、右子樹也分別都是Binary Search Tree。    
  4.沒有鍵值相等的節點。    
  
  * 二元搜尋樹相比於其他資料結構的優勢在於尋找、插入的時間複雜度較低，為O(logn)。    
  * 搜尋、新增、刪除的複雜度等於樹高，平均O(logn)，最差O(n)。    
  * 時間與空間複雜度：    
  
    ||平均|最差|
    |:---:|:---:|:---:|
    |空間|O(n)|O(n)|
    |時間|O(logn)|O(n)|
<br />
<div align=center>▼圖一、三層的二元搜尋樹</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BST(2).png?raw=true"/></div>    
<br />

參考資料：[二元搜尋樹- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)
   
### 流程圖與學習歷程
#### 新增
我先參考[【LeetCode】701. Insert into a Binary Search Tree 解题报告（Python & C++）](https://blog.csdn.net/fuxuemingzhu/article/details/82385503)寫了leetcode上的[701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)，並修改成規定的函數名稱：
```Python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:#如果沒有root，
            return TreeNode(val)#就創一個node輸入val。
        if val <= root.val:#如果輸入的val比root的值小或一樣大，
            if root.left is None:#且如果左邊沒有node，
                root.left = TreeNode(val)#就在左邊創一個node輸入val
            else:#如果左邊有node了，
                self.insert(root.left, val)#就把左邊當root再跑一次insert
        else:#如果輸入的val比root的值大，
            if root.right is None:#且如果右邊沒有node，
                root.right = TreeNode(val)#就在右邊創一個node輸入val
            else:#如果右邊有node了，
                self.insert(root.right, val)#就把右邊當root再跑一次insert
        return root
```
之後我用簡報裡的測資，先創一棵樹：
```Python
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(-5)
Node3 = TreeNode(8)
Node4 = TreeNode(7)
Node5 = TreeNode(6)
Node6 = TreeNode(10)
root.left = Node1
root.right = Node3
Node1.left = Node2
Node3.left = Node4
Node3.right = Node6
Node4.left = Node5
```
新增4：
```Python
import copy
root1 = copy.deepcopy(root)
Solution().insert(root1,4)
print(Solution().insert(root1,4) == root1.left.right)
```
4應該會新增到root1.left.right，但是這裡print(Solution().insert(root1,4) == root1.left.right)出來的結果False，檢查print(Solution().insert(root1,4).val)，**出來的結果是5**，而print(root1.left.right.val)是4，代表確實是有新增進去，但是insert完return的是root。    
修改如下：
```Python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:#如果沒有root，
            return TreeNode(val)#就創一個node輸入val。
        if val <= root.val:#如果輸入的val比root的值小或一樣大，
            if root.left is None:#且如果左邊沒有node，
                root.left = TreeNode(val)#就在左邊創一個node輸入val。
                return root.left
            else:#如果左邊有node了，
                return self.insert(root.left, val)#就把左邊當root再跑一次insert。
        else:#如果輸入的val比root的值大，
            if root.right is None:#且如果右邊沒有node，
                root.right = TreeNode(val)#就在右邊創一個node輸入val。
                return root.right
            else:#如果右邊有node了，
                return self.insert(root.right, val)#就把右邊當root再跑一次insert。
```
這裡print(Solution().insert(root1,4).val)出來的結果是4，print(root1.left.right.val)也是4，但是print(Solution().insert(root1,4) == root1.left.right)還是False。
<div align=center>▼圖一、新增4的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Insert4.png?raw=true"/></div>
<br />
   
#### 刪除
我先參考[python recursive soluton](https://leetcode.com/problems/delete-node-in-a-bst/discuss/290949/python-recursive-soluton)寫了leetcode上的[450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)，並修改成規定的函數名稱：
```Python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:#如果沒有root，
            return None#回傳None。
        if target == root.val:#如果target跟root的值一樣大，
            if root.left is None and root.right is None:#且root的左右邊都沒有小孩，
                return None#回傳None。
            if root.left is None:#如果左邊沒有小孩，
                return root.right#回傳右邊小孩。
            if root.right is None:#如果右邊沒有小孩，
                return root.left#回傳左邊小孩。
            #如果root的左右邊都有小孩，
            left = root.left
            right = root.right
            p = right
            while p.left:#當root的右邊的左邊有小孩，
                p = p.left#就讓root的右邊變成root的右邊的左邊的小孩
            p.left = left#讓root的右邊的左邊變成root的左邊的小孩
            return right
        if target > root.val:#如果target比root的值大，
            root.right = self.delete(root.right, target)#就把右邊當root再跑一次delete。
        else:#如果target比root的值小，
            root.left = self.delete(root.left, target)#就把左邊當root再跑一次delete。
        return root
```
刪除3：
```Python
root2 = copy.deepcopy(root)
root2 = Solution().delete(root2,3)
print(root2.val==5 and root2.left.val==3 and root2.right.val==8
      and root2.left.left.val==-5 and root2.right.left.val==7 
      and root2.right.right.val==10 and root2.right.left.left.val==6)
```
出來的結果是True。    
測試後發現，如果樹裡有重複的值就會出錯，只刪了較靠近root的那個，但還是畫了我的想法，如圖二，應該是錯在少了第2步的程式：
<div align=center>▼圖二、刪除3的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Delete3.png?raw=true"/></div>
<br />

#### 查詢
我先參考[【LeetCode】700. Search in a Binary Search Tree 解题报告（Python）](https://blog.csdn.net/fuxuemingzhu/article/details/81015754)寫了leetcode上的[700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)，並修改成規定的函數名稱：
```Python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:#如果沒有root，
            return None#回傳None
        elif target == root.val:#如果輸入的val跟root的值一樣大
            return root#直接回傳root
        elif target < root.val:#如果輸入的val比root的值小
            return self.search(root.left, target)#就把左邊當root再跑一次search
        else:#如果輸入的val比root的值大
            return self.search(root.right, target)#就把右邊當root再跑一次search
```
查詢10：
```Python
root2 = copy.deepcopy(root)
print(Solution().search(root2,10) == root2.right.right)
```
出來的結果是True。
<div align=center>▼圖三、查詢10的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Search10.png?raw=true"/></div>
<br />

#### 修改
```Python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        return self.delete(root, target)
        return self.insert(root, new_val)
```
<div align=center>▼圖四、把12改成4的流程圖</div>    
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Modify12.png?raw=true"/></div>
<br />
