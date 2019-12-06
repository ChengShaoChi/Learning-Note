from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        h = MD5.new()#建立MD5物件
        h.update(key.encode("utf-8"))#更新MD5雜湊值，回傳hash的位置
        h = h.hexdigest()#取得MD5雜湊值，以字串形式回傳雜湊碼
        d = int(h, 16) % self.capacity
        #將16進位制轉換成10進位制，並取餘數當作第幾格抽屜
        node = self.data[d]
        while node != None:
            if node.val == h:
                return
            node = node.next
        new = ListNode(h)
        new.next = self.data[d]
        self.data[d] = new
        
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        d = int(h, 16) % self.capacity
        node = self.data[d]
        #如果self.data[d]本身就是要刪除的，
        if node != None:
            if node.val == h:
                self.data[d] = node.next
                node = None
                return
        #先找到要刪除的，
        while node != None:
            if node.val == h:
                break
            prev = node#要刪除的前一個節點
            node = node.next
        #找不到要刪除的，
        if node == None:
            return
        prev.next = node.next#prev接到node.next
        node = None
        
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        d = int(h, 16) % self.capacity
        node = self.data[d]
        while node != None:
            if node.val == h:
                return True
            node = node.next
        return False
    
#參考資料：
#https://medium.com/omarelgabrys-blog/hash-tables-2fec6870207f
#https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
#https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
#https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
