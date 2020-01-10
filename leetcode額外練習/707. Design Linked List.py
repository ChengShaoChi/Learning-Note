class MyLinkedList:
    def __init__(self):
        self.linkedlist = []

    #返回linked list中第index個節點的值。
    #如果index無效（小於0或大於等於linked list的長度），則返回-1。
    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    #在linked list的第一個元素之前添加一個值節點。插入後，新節點將成為linked list的第一個節點。
    def addAtHead(self, val: int) -> None:
        self.linkedlist.insert(0,val)

    #將值節點添加到linked list的最後一個元素。
    def addAtTail(self, val: int) -> None:
        self.linkedlist.append(val)

    #在linked list的第index個節點之前添加一個值節點。
    #如果index等於linked list的長度，則添加到末端。
    #如果index大於linked list的長度，則不會插入。
    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.linkedlist):
            self.linkedlist.insert(index,val)
        elif index == len(self.linkedlist):
            self.linkedlist.append(val)

    #如果index有效（大於等於0和小於linked list的長度），則刪除linked list中第index個節點。
    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index < len(self.linkedlist):
            return self.linkedlist.pop(index)
