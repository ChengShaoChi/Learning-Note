class ListNode:
    def __init__(self, data): 
    # 傳入一個data的值
        self.data = data
    # 指標預設是指向None
        self.next = None
        return
        
class SingleLinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        return
    def add_list_item(self, item): 
        if not isinstance(item, ListNode):
            item = ListNode(item)
    
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
    
        self.tail = item
        return

list1 = SingleLinkedList()
