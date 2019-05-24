class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data;
        self.prev = prev;
        self.next = next;

class DoublyLinkedList:
    def __init__(self):
        self.head = None;
    def append(self,data):
        newNode = Node(data);
        if self.head == None:
             newNode.prev = None;
             newNode.next = None;
             self.head = newNode;
        currentNode = self.head;
        while currentNode.next:
            currentNode = currentNode.next;
        currentNode.next = newNode;
        newNode.prev     = currentNode;
        newNode.next     = None;

    def prepend(self,data):
        newNode = Node(data);
        if self.head == None:
            newNode.prev = None;
            newNode.next = None;
            self.head    = newNode;
        else:
            self.head.prev = newNode;
            newNode.next   = self.head;
            newNode.prev   = None;
            self.head = newNode;
    def reverse(self):
        previousNode = None;
        currentNode = self.head;
        while currentNode:
            nextNode = currentNode.next;
            currentNode.next = previousNode;
            currentNode.prev = nextNode;
            previousNode = currentNode;
            currentNode  = nextNode;
        self.head = previousNode;

    def removeDuplicate(self):
        # create a dict
        dict = {};
        current = self.head;
        while current:
            if current.data not in dict:
                dict[current.data] = 1;
            else:
                # remove data here
                # print("repeated");
            current = current.next;
        return dict;

    def show(self):
        currentNode = self.head;
        while currentNode:
            print(currentNode.data);
            currentNode = currentNode.next;

lst = DoublyLinkedList();
lst.append(1);
lst.append(2);
lst.append(3);
lst.append(4);
lst.append(4);
lst.append(5);
lst.append(6);
lst.append(5);
lst.append(7);
lst.append(0);

# lst.show();
dict = lst.removeDuplicate();
print(dict);
# lst.reverse();
# print("-------------------");
# lst.show();
