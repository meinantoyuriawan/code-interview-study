class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# base linked list definition
# single linked list

class LL:
    def __init__(self):
        self.head = None

    def insertEnd(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def insertBeginning(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # kinda rigged but ok
    def insertMiddle(self, val, index):
        new_node = Node(val)
        current_node = self.head
        position = 0

        if position == index:
            self.insertBeginning(val)
        else:
            while (current_node != None) and (position+1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None :
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("index not present")
