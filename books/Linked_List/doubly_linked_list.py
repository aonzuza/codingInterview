class Node:
    def __init__(self, val,next = None , prev = None):
        self.val = val;
        self.next = next;
        self.prev = prev;


class DoublyLinkedList:

    def __init__(self):
        self.head = None;

    def count(self):

        def _count(current):
            count = 0;
            while current:
                current = current.next;
                count = count + 1;
            return count;

        return _count(self.head);

    def append(self, val):

        current = self.head;
        newNode = Node(val);

        if not current:
            self.head = newNode;
        else:
            while current.next:
                current = current.next;
            current.next = newNode;
            newNode.prev = current;

    def insertAt(self,index,val):
        current = self.head;
        newNode = Node(val);
        prev = None;
        counter = 0;
        if index == 0:
            newNode.next = current;
            current.prev = newNode;
            self.head = newNode;
        elif index >= (self.count() - 1):
            while current.next:
                current = current.next;
            current.next = newNode;
            newNode.prev = current;

        else:
            while counter < index:
                prev = current;
                current = current.next;
                counter = counter + 1;
            prev.next = newNode;
            newNode.prev = prev;
            newNode.next = current;
            current.prev = newNode;

    def removeAt(self,index):
        counter = 0;
        count = self.count();
        if not 0 <= index <= count - 1:
            return;

        if index == 0:
            if count < 2:
                self.head = None;
            elif count > 1:
                current = self.head;
                next = current.next;
                next.prev = None;
                self.head = next;
        # elif index == count - 1:
        #     pass
        else:
            current = self.head;
            prev  = None;
            while counter < index:
                prev = current;
                current = current.next;
                counter = counter + 1;

            # prev.next = current.next if current.next else None;
            if current.next:
                next = current.next;
                prev.next = next;
                next.prev = prev;

                current.prev = None;
                current.next = None;

            else:
                prev.next = None;
                current.prev = None;





    def show(self):

        current = self.head;
        while current:
            print(current.val);
            current = current.next;


dll = DoublyLinkedList();
dll.append(1);
dll.append(2);
dll.append(3);
dll.append(4);
dll.append(5);

dll.show();
print('------------------');
dll.removeAt(4);

dll.show();
