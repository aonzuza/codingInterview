class Node:

    def __init__(self,val = None ,next = None):
        self.val = val;
        self.next = next;


class SinglyLikedList:

    def __init__(self):
        self.head = None;

    def append(self,val):
        new_node = Node(val);

        if not self.head:
            self.head = new_node;
        else:
            current = self.head;
            while current.next:
                current = current.next;
            current.next = new_node;

    def show(self):
        current = self.head;
        if self.head:
            while current:
                print(current.val);
                current = current.next;
        else:
            print('it is empty');


    def count(self):
        current = self.head;
        counter = 0;

        while current:
            counter = counter + 1;
            current = current.next;
        return counter;

    def count_recursive(self):

        def _count(node):
            if not node:
                return 0;
            return 1 + _count(node.next);

        return _count(self.head);

    def reverse(self):
        prev = None;
        current = self.head;
        while current:
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        self.head = prev;

    def empty(self):
        self.head = None;

    def prepend(self,val):

        if not self.head:

            newNode = Node(val);
            self.head = newNode;

        else:
            current = self.head;
            newNode = Node(val);
            while current.next:
                current = current.next;

            current.next = newNode;
            # newNode.next = None;

    def insertAt(self,index,val):
        newNode = Node(val);

        if index == 0:
            newNode.next = self.head;
            self.head = newNode;
        else:
            current = self.head;
            # count = 1 because we start at the head.
            count = 1;
            while count < index:
                current = current.next;
                count = count + 1;
            temp = current.next;
            current.next = newNode;
            newNode.next = temp;

    def sortHighLow(self):

        if self.count() > 1:
            left = self.head;
            right = self.head.next;
            # keep low at left position
            lowLeft = True;

            while right:

                if left.val > right.val and lowLeft:
                    left.val , right.val = right.val,left.val;
                if left.val < right.val and not lowLeft:
                    left.val , right.val = right.val,left.val;

                left = right;
                right = right.next;
                lowLeft = not lowLeft;



def sum_list(list1,list2):

    results = SinglyLikedList();
    current1 = list1.head;
    current2 = list2.head;
    carrier  = 0;

    while current1 or current2:

        a = current1.val if current1 else 0;
        b = current2.val if current2 else 0;
        sum = a + b + carrier;

        carrier = 0 if sum < 10 else 1;
        sum = sum % 10;

        results.append(sum);
        current1 = current1.next if current1 else None;
        current2 = current2.next if current2 else None;

    if carrier:
        results.append(carrier);

    return results;




lst1 = SinglyLikedList();
lst1.append(1);
lst1.append(2);
lst1.append(3);
lst1.append(4);
lst1.append(5);
lst1.append(3);
lst1.sortHighLow();
lst1.show();
