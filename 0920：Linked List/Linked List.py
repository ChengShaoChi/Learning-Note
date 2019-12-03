class ListNode:
    def __init__(self, data): 
    # 建立一個節點，並傳入一個data的值
        self.data = data
    # 指標預設是指向None
        self.next = None
        return
        
class SingleLinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        return
    #在建立list的一開始，我們預設裡面是沒有節點的。而linked list本身帶有head跟tail兩個屬性。當我們加入一個新的節點時：
        #若list本身還沒有任何節點，則head以及tail都會變成新的節點
        #若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。
    
    def add_list_item(self, item): 
        if not isinstance(item, ListNode):#判斷item是否為節點，如果不是，
            item = ListNode(item)#就使用ListNode(item)建立一個帶有item資料的節點
    
        if self.head is None:#如果原本沒有head
            self.head = item#那head就是item
        else:#如果有頭
            self.tail.next = item#那就讓item接在tail後面
    
        self.tail = item#tail就是item
        return
    #在取得item之後，要檢查item是否是一個節點，若不是的話則使用ListNode(item)建立一個帶有item資料的節點。
    
#參考資料：https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d
