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
    def remove(self,data):
        current = self.head;
        prev    = None;
        while current:
            if current.data == data:
                if prev == None:
                    self.head = current.next;
                    current.next = None;
                    return;
                # delete the node
                prev.next = current.next;
                current.next = None;
                return;
            prev    = current;
            current = current.next;
    def removeAt(self,k):
        counter  = 1;
        current  = self.head;
        previous = None;

        while current:
            if counter == k:
                # it's the head
                if previous == None:
                    self.head = current.next;
                    current.next = None;
                else:
                    previous.next = current.next;
                    current.next  = None;
            previous = current;
            current  = current.next;
            counter  = counter + 1 ;

    def deleteFromLast(self,k):
         current = self.head;
         prev    = self.head;
         while k > 0:
            current = current.next;
            k = k - 1;
         temp = None;
         while current:
            current = current.next;
            temp    = prev;
            prev    = prev.next;
         if temp:
             temp.next = prev.next;
             prev.next = None;
         else:
             self.head = prev.next;
             prev.next = None;
    def removeDuplicate(self):
        # dict
        dict = {};
        current = self.head;
        previous = None;
        while current:
            if current.data in dict:
                previous.next = current.next;
                current.next  = None;
                current = previous.next;
            else:
                dict[current.data] = 1;
                previous = current;
                current = current.next;
    def reverse(self):
        current = self.head;
        previous    = None;
        while current:
            next = current.next;
            current.next = previous;
            previous = current;
            self.head = previous;
            current  = next;
    def recursiveReverse(self):
        def _reverse(current,previous):
            if current:
                next = current.next;
                current.next = previous;
                previous = current;
                self.head = previous;
                current = next;
                _reverse(current,previous);
        _reverse(self.head,None);

def mergeSortedList(list_A,list_B):
        current_A =  list_A.head;
        current_B =  list_B.head;
        while current_B:

            if current_B.data >= current_A.data and current_A.next == None:
                # do something
                nextB = current_B.next;
                current_B.next = current_A.next;
                current_A.next = current_B;
                current_A = current_B;
                current_B = nextB;
                list_B.head = current_B;
            elif current_B.data >= current_A.data and current_B.data <= current_A.next.data:
                nextB = current_B.next;
                current_B.next = current_A.next;
                current_A.next = current_B;
                current_A = current_B;
                current_B = nextB;
                list_B.head = current_B;
            else:
                # move to another number;
                current_A = current_A.next;
        return list_A;


lst_A = LinkedList();

lst_A.append(1);
lst_A.append(8);
lst_A.append(8);
lst_A.append(11);


lst_B = LinkedList();
lst_B.append(6);
lst_B.append(7);
lst_B.append(8);
lst_B.append(12);
lst_B.append(13);

mergedList = mergeSortedList(lst_A,lst_B);
mergedList.show();
