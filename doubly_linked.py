class Node():
    def __init__(self, data, next=None, prev=None):
        self.__data=data
        self.next=next
        self.prev=prev
    
    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data=data

    def getNext(self):
        return self.__next
    
    def getPrevious(self):
        return self.__prev
    
    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.__next=node
        else:
            raise Exception("Must be Node")

    def setPrev(self, node):
        if node is None or isinstance(node, Node):
            self.__prev=node
        else:
            raise Exception("Must be Node")
    def __str__(self):
        return str(self.__data)

class DoublyLinked():
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def getFirst(self):
        return self.__head
    
    def getLast(self):
        return self.__tail
    
    def insertFirst(self, node):
        if node is None or isinstance(node, Node):
            node.next=self.head
            if self.head:
                self.head.prev=node
            self.head=node
            if not self.tail:
                self.tail=node
        else:
            raise Exception("Not a Node")
        
    def insertLast(self, node):
        if node is None or isinstance(node, Node):
            if self.tail:
                self.tail.next=node
                node.prev=self.tail
                self.tail=node
            else:
                self.head=node
                #need to add this also
                self.tail=node
        else:
            raise Exception("Not a Node")
    
    def deleteFirst(self):
        if self.head:
            curr=self.head
            self.head=curr.next
            curr.next=None
            return True
        else:
            return False
    
    def deleteLast(self):
        if self.tail:
            curr=self.tail.prev
            curr.next=None
            self.tail=curr
            return True        
        else:
            return False
        
    def delete(self, i):
        if not self.head or i<0:
            return False
        #First edge case: Removing the head 
        if i==0:
            curr=self.head
            self.head=curr.next
            curr.next=None
            return True
        curr=self.head
        while i>1:
            curr=curr.next
            if not curr:
                return False
            i-=1
        #removing the tail
        if not curr.next:
            curr=self.tail.prev
            curr.next=None
            self.tail=curr
            return True
        nx1=curr.next
        nx2=nx1.next
        curr.next=nx2
        nx1.prev=None
        nx2.prev=curr
        return True
        