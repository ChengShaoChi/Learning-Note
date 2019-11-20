# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:#如果沒有root，
            return TreeNode(val)#輸入的val就當root
        elif val < root.val:#如果輸入的val比root的值小
            root.left = self.insertIntoBST(root.left, val)#就把左邊當root
        else:#如果輸入的val比root的值大
            root.right = self.insertIntoBST(root.right, val)#就把右邊當root
        return root
        
#參考資料：https://blog.csdn.net/fuxuemingzhu/article/details/82385503
