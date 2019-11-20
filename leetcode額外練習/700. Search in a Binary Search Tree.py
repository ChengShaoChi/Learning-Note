# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:#如果沒有root，
            return None
        elif val == root.val:#如果輸入的val跟root的值一樣大
            return root#直接回傳root
        elif val < root.val:#如果輸入的val比root的值小
            return self.searchBST(root.left, val)
        else:#如果輸入的val比root的值大
            return self.searchBST(root.right, val)

#參考資料：https://blog.csdn.net/fuxuemingzhu/article/details/81015754
