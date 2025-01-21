class Node():
    def __init__(self, data, next=None):
        self.data=data
        self.next=next



class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0

    def display(self):
        node=self.head
        while node is not None:
            print(node.data, end="->")
            node=node.next
        print('None')

    #my implementation
    def findAt1(self, i):
        node=self.head
        cur_i=0
        while node is not None:
            if cur_i==i:
                return node 
            node=node.next
            cur_i+=1
        return None
    
    def findAt2(self, i):
        node=self.head
        if not node:
            return None
        while i>0: 
            i-=1
            node=node.next
            if not node:
                return None
        return node
    
    def insert_at_back(self, data):
        new_node=Node(data)
        curr_node=self.head
        if not curr_node:
            self.head=new_node
        while curr_node.next:
            curr_node=curr_node.next
        curr_node.next=new_node
        self.size+=1
    
    def insert_at_front(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def insert(self, i, data):
        new_node=Node(data)

        #1st case: insert at start
        if self.head is None or i==0:
            new_node.next=self.head
            self.head=new_node
            self.size+=1
            return True

        curr=self.head
        while i>1:
            curr=curr.next
            if not curr:
                print("It is out of range")
                return False
            i-=1
        new_node.next=curr.next
        curr.next=new_node
        self.size+=1
        return True

    #this is the stupid way
    def size2(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
    
    #using size attribute
    def find(self, i):
        if i<0 or i>self.size:
            return None
        curr=self.head
        while i>0:
            curr=curr.next
            i-=1
        return curr
    
    #new insert function using find function
    def insert2(self, i, data):
        new_node=Node(data)
        #check if within bounds
        if i<0 or i>self.size:
            return False

        #insert at the front
        if i==0:
            new_node.next=self.head
            self.head=new_node
            self.size+=1
            return True
        #insert at the middle
        prev=self.find(i-1)
        new_node.next=prev.next
        prev.next=new_node        
        self.size+=1
        return True
    
    def remove(self, i):
        if i==0:
            temp=self.head 
            self.head=self.head.next
            temp.next=None
            return True
        curr=self.head
        while i>1:
            i-=1
            curr=curr.next
            if not curr:
                return False
        temp=curr.next
        curr.next=temp.next
        temp.next=None
        return True
l=LinkedList()
l.insert_at_front(3)
l.insert_at_back(4)
l.insert(2, 3.5)
l.insert2(3, 2)
l.remove(3)
print(l.findAt1(0).data, '\n')
print(l.size)
l.display()