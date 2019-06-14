class Node:
    def __init__(self,key = None, val = None):
        self.key = key;
        self.val = val;
        self.next = None;
        self.prev = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None,'head');
        self.tail = Node(None,'tail');

        self.head.next = self.tail;
        self.tail.prev = self.head;

    def get_first_node(self):
        return self.head.next;

    def get_last_node(self):
        return self.tail.prev;

    def append(self, new_node):
        last_node = self.tail.prev;
        last_node.next = new_node;
        new_node.prev = last_node;
        new_node.next = self.tail;
        self.tail.prev = new_node;

    def remove(self,current):
        prev_node = current.prev;
        next_node = current.next;
        prev_node.next = next_node;
        next_node.prev = prev_node;
        current.prev = None;
        current.next = None;

class LRUCache:
    def __init__(self,capacity = 1):
        self.capacity = capacity;
        self.hash_table = dict();
        self.dlst = DoublyLinkedList();

    def get(self,key):
        # hit
        if key in self.hash_table:
            node = self.hash_table[key];
            self.dlst.remove(node);
            # del self.hash_table[key];
            self.dlst.append(node);
            # self.hash_table[key] = node;
            return self.hash_table[key].val;


    def set(self,key,val):
        # hit
        if key in self.hash_table:
            node = self.hash_table[key];
            self.dlst.remove(node);
            del self.hash_table[key];

        new_node = Node(key,val);
        self.dlst.append(new_node);
        self.hash_table[key] = new_node;


        if len(self.hash_table) > self.capacity:
            first_node = self.dlst.get_first_node();
            self.dlst.remove(first_node);
            del self.hash_table[first_node.key];


cache = LRUCache(3);
cache.set('A',1);
cache.set('B',2);
cache.set('C',2);
cache.set('D',2);



node = cache.dlst.head;

while node:
    print(node.key,node.val);
    node = node.next;

cache.set('A',3);
print('b',cache.get('B'));

node = cache.dlst.head;
print('---------------');
while node:
    print(node.key,node.val);
    node = node.next;
