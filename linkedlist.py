class Node():
    def __init__(self, datum, next=None):
        self.__data=datum
        self.__next=next
    
    def get_data(self):
        return self.__data
    
    def set_data(self, datum):
        self.__data=datum

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next=node
    
    def isLast(self):
        return self.get_next is None
    
    def __str__(self):
        return str(self.get_data())


class LinkedList():
    def __init__(self):
        self.__first=None

    def getFirst(self):
        return self.__first
    
    def setFirst(self, node):
        self.__first=node

    def isEmpty(self):
        return self.getFirst() is None
    
    def insert(self, datum):
        node = Node(datum, self.getFirst())
        self.setFirst(node)
    
    def find(self, goal):
        node=self.getFirst()
        while node is not None:
            if node.get_data()==goal:
                return node
            node=node.get_next()
l=LinkedList()
l.insert("a")
l.insert("b")
l.insert("c")
print(l.getFirst())
print(l.find("a"))
