class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev
