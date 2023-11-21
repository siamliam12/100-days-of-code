class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:# check if the head is an empty node or not
            # if the head is empty then we make the new_node as head and return
            self.head = new_node
            return
        else:
            # we insert the head at the next new_node and make the head equal to new_node.
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        positions = 0
        if positions == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and positions +1 != index):
                positions = positions+1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present!")

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def updateNode(self,val,index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node!=None and position != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print("Index not Present")
        
    def remove_first_node(self):
        if(self.head ==None):
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self,index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node!= None and position +1 != index):
                position = position +1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not found")

    def remove_node(self, data):
        current_node = self.head
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next


    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while(current_node) :
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
        
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()
llist.insertAtBegin('a')
llist.insertAtBegin('b')
llist.insertAtBegin('c')
llist.insertAtBegin('d')
llist.insertAtBegin('e')
llist.insertAtBegin('f')
llist.insertAtEnd('g')
llist.insertAtIndex('h',5)
llist.remove_first_node()
llist.remove_last_node()
llist.remove_at_index(5)
llist.remove_node('g')
print("node data")
llist.printLL()