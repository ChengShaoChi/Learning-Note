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
        
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        return self.delete(root, target)#刪掉所有target
        return self.insert(root, new_val)#新增new_val
        return root
