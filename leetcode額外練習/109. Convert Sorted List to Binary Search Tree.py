# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        middle = len(nums)//2
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])
        return root
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        if head:
            while head:
                nums.append(head.val)
                head = head.next
            return self.sortedArrayToBST(nums)

#參考資料：https://blog.csdn.net/qqxx6661/article/details/76168244
