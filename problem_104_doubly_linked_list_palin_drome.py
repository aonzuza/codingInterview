class Node:
    def __init__(self,val):
        self.val  = val;
        self.next = None;
        self.prev = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = None;
    def append(self,val):
        newNode = Node(val);
        if self.head == None:
            self.head = newNode;
        else:
            current = self.head;
            while current.next:
                current = current.next;
            current.next = newNode;
            newNode.prev = current;
            newNode.next = None;
    def prepend(self,val):
        newNode = Node(val);
        if not self.head:
            self.head = newNode;
        else:
            headNode = self.head;
            headNode.prev = newNode;
            newNode.next = headNode;
            self.head = newNode;

    def show(self):
        current = self.head;
        while current:
            print(current.val);
            current = current.next;

    def count(self):
            current = self.head;
            def _count(current):
                if not current.next:
                    return 1;
                return 1 + _count(current.next);
            return _count(current);

    def is_palindrom(self):
        firstNode = self.head;
        lastNode = self.head;
        while lastNode.next:
            lastNode = lastNode.next;

        while True:

            if firstNode.val != lastNode.val:
                return False;
            if firstNode.next == lastNode.prev:
                return True;
            firstNode = firstNode.next;
            lastNode = lastNode.prev;
    def is_palindrom_2(self):
            current = self.head;
            length  = self.count();
            middle  = (length - 1) / 2;
            # print(middle);
            isOdd  = True if length % 2 != 0 else False;
            cached  = [];
            index   = 0;
            while current:

                if index <= middle:
                    cached.append(current.val);
                else:
                    if index == middle and isOdd == True:
                        print('wasted');
                        cached.pop(-1);

                    if cached.pop(-1) != current.val:
                        return False;

                index   = index + 1;
                current = current.next;

            return True;
    def generate_array(self):
        current = self.head;
        arr = [];
        while current:
            arr.append(current.val);
            current = current.next;
        return arr;

    def is_palindrom_3(self):
        arr = self.generate_array();
        reversed_arr = reversed(arr);
        return all( x == y for x,y in zip(arr,reversed_arr));


doubly_linked_list = DoublyLinkedList();
doubly_linked_list.append(1);
doubly_linked_list.append(2);
doubly_linked_list.append(5);
doubly_linked_list.append(2);
doubly_linked_list.append(1);

x = doubly_linked_list.is_palindrom_3();

print(x);
