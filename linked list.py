# Linked list
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def setHead(self,val):
        self.head = Node(val)

    def insert(self,val):
        if self.head is None:
            self.setHead(val)
            return None
        n=self.head
        while n.next:
            n = n.next
        n.next = Node(val)

    def insertBefore(self,val,input):
        if self.head is None:
            self.setHead(input)
            return None
        if self.head.val == val:
            temp = self.head
            self.head = Node(input)
            self.head.next = temp
            return 0
        newNode = Node(input)
        prev = self.head
        n = self.head.next
        while n is not None:
            if n.val == val:
                prev.next = newNode
                newNode.next = n
                return 0
            prev = prev.next
            n=n.next
        print("element not found")

    def insertAfter(self,val,input):
        if self.head is None:
            print("list empty")
            return None
        n=self.head
        newNode = Node(input)
        while n:
            if n.val == val:
                temp = n.next
                n.next = newNode
                newNode.next = temp
                return 0
            n=n.next
        
    def insertByIdx(self,idx,input):
        if self.head is None:
            self.setHead(input)
            return 0
        if idx == 0:
            temp = self.head
            self.head = Node(input)
            self.head.next = temp
            return 0
        i=1
        newNode = Node(input)
        prev = self.head
        n=self.head.next
        while n is not None:
            if i==idx:
                prev.next = newNode
                newNode.next = n
                return 0
            i+=1
            prev = prev.next
            n=n.next
        print("Element not found")
                    
    def removeByVal(self,target):
        if self.head is None:
            return "list is empty"
        if target == self.head.val:
            self.head = self.head.next
            return 0
        prev = self.head
        n = self.head.next
        while n is not None:
            if n.val== target:
                prev.next = n.next
                return 0
            prev = prev.next
            n = n.next
        print("element not found")

    def removeByIdx(self,idx):
        if self.head is None:
            return "List is empty"
        if idx==0:
            self.head = self.head.next
            return 0
        i=1
        prev = self.head
        n=self.head.next
        while n is not None:
            if i==idx:
                prev.next = n.next
                return 0
            i+=1
            prev = prev.next
            n=n.next
        print("Element not found")

    def printList(self):
        n=self.head
        while n:
            print(n.val)
            n=n.next

ll = LinkedList()
ll.setHead(5)
ll.insert(10)
ll.insert(15)
ll.insertBefore(5,2)
ll.insertAfter(5,7)
ll.insertByIdx(3,99)
ll.removeByVal(10)
ll.removeByIdx(2)
ll.printList()
