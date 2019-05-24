class Node:
    def __init__(self,data):
         self.data = data;
         self.next = None;
class LinkedList:
    def __init__(self):
        self.head = None;
    def show(self):

        curNode = self.head;
        while curNode:
            print(curNode.data);
            curNode = curNode.next;

    def append(self,data):
        newNode = Node(data);

        if self.head is None:
            self.head = newNode;
            return;
        lastNode = self.head;
        while lastNode.next :
            lastNode = lastNode.next;
        lastNode.next = newNode;
    # insert at the very begining
    def prepend(self,data):
        newNode = Node(data);
        newNode.next = self.head;
        self.head = newNode;
    def empty(self):
        self.head = None;
    def count(self):
        counter = 0;
        if self.head is None:
            return counter;
        nextNode = self.head;
        while nextNode:
            nextNode = nextNode.next;
            counter = counter + 1;
        return counter;
    def insertAt(self,index,data):
        newNode = Node(data);
        counter = 0;
        currentNode = self.head;
        previousNode = None;

        while currentNode:
           if index == 0:
               newNode.next = self.head;
               self.head = newNode;
               return;
           elif counter == index:
               previousNode.next = newNode;
               newNode.next = currentNode;
               return;
           previousNode = currentNode;
           currentNode  = currentNode.next;
           counter = counter + 1;

    def reverse(self):
        previousNode = None;
        currentNode  = self.head;
        while currentNode:
            tempNode = currentNode.next;
            currentNode.next = previousNode;
            #self.head = currentNode;
            previousNode = currentNode;
            currentNode =  tempNode;
        self.head = previousNode;

    def recursiveReverse(self):
        def _recursiveReverse(previousNode,currentNode):
            if currentNode is None:
                self.head = previousNode;
                return;
            tempNode = currentNode.next;
            currentNode.next = previousNode;
            previousNode = currentNode;
            currentNode  = tempNode;
            _recursiveReverse(previousNode,currentNode);
        _recursiveReverse( None ,self.head);

    def remove(self,data):
        currentNode = self.head;
        previousNode = None;
        while currentNode:
            if currentNode.data == data:
                if previousNode is None:
                    #do something
                    # this is the head
                    #self.head = None;
                    self.head.next = None;
                    self.head = currentNode.next;
                    return;
                else:
                    previousNode.next = currentNode.next;
                    return;

            previousNode = currentNode;
            currentNode  = currentNode.next;



lst = LinkedList();
lst.append(0);
lst.append(1);
lst.append(2);
lst.append(3);
lst.append(4);
# #lst.show();
#
# lst.prepend(5);
lst.show();

# lst.reverse();
# lst.recursiveReverse();
# lst.show();
