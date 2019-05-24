
class Node:
    def __init__(self, value):

        self.value = value;
        self.next  = None;


class SinglyLinkedList:
    def __init__(self):
        self.head = None;

    def add(self,val):
        new_node = Node(val);
        if self.head == None:
            self.head = new_node;
        else:
            current_node = self.head;
            while current_node.next:
                current_node = current_node.next;
            current_node.next = new_node;
    def printNode(self):
        current_node = self.head;
        while current_node:
            print(current_node.value);
            current_node = current_node.next;
    def count(self):
        return self.count_helper(self.head);
    def count_helper(self,node):
        if node == None:
            return 0;
        return 1 + self.count_helper(node.next);



def find_intersecting_node(list_a,list_b):
    dict = {};
    #  assume that list_a and list_b are not empty;
    current_node_a = list_a.head;
    while current_node_a.next:
        value = current_node_a.value;
        dict[value] = 1;
        current_node_a = current_node_a.next;
    current_node_b = list_b.head;
    while current_node_b.next:
        value = current_node_b.value;
        if value in dict:
            return current_node_b;
        current_node_b = current_node_b.next;
    return None;

list_a = SinglyLinkedList();
list_a.add(3);
list_a.add(7);
list_a.add(8);
list_a.add(10);
# node_a.printNode();


list_b = SinglyLinkedList();
list_b.add(99);
list_b.add(1);
list_b.add(8);
list_b.add(10);
list_b.add(10);
list_b.add(10);
list_b.add(10);

total = list_b.count();
print(total);

# intersecting_node = find_intersecting_node(list_a,list_b);
# print(intersecting_node);
