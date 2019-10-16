#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedlist = []

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.linkedlist.insert(0,val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.linkedlist.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < len(self.linkedlist):
            self.linkedlist.insert(index,val)
        elif index == len(self.linkedlist):
            self.linkedlist.append(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < len(self.linkedlist):
            return self.linkedlist.pop(index)

