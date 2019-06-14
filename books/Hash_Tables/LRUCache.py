class Node:
    def __init__(self,key,val):

        self.key = key;
        self.val = val;
        self.next = None;
        self.prev = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = Node('','head');
        self.tail = Node('','tail');

        self.head.next = self.tail;
        self.tail.prev = self.head;

    def count(self):

        def _count(current):

            if not current.next:
                return 0;
            return 1 + _count(current.next);

        return _count(self.head.next);


    def get_first_node(self):
        return self.head.next;

    def get_last_node(self):
        return self.tail.prev;

    def append(self,node):

        prev = self.tail.prev;
        prev.next = node;
        node.prev = prev;
        node.next = self.tail;
        self.tail.prev = node;

    def remove(self,node):
        prev = node.prev;
        next = node.next;
        prev.next = next;
        next.prev = prev;


class LRUCache:
    def __init__(self,size):
        self.size = size;
        self.dict = {};
        self.list  = DoublyLinkedList();

    def current_size(self):
        return self.list.count();

    def set(self, key, val):
        if key in self.dict:
            # if we have a hit, we remove and add to cache again to maintain LRU Eviction policy
            node = self.dict[key];
            self.list.remove(node);
            del self.dict[key];

        node = Node(key,val);
        self.list.append(node);
        self.dict[key] = node;

        if len(self.dict) > self.size:
            #get first node
            firstNode = self.list.head.next;
            self.list.remove(firstNode);
            del self.dict[firstNode.key];


    def get(self,key):

        if key in self.dict:
            # hit
            node = dict[key];
            self.list.remove(node);
            self.list.append(node);
            return node.val;

cache = LRUCache(3);
cache.set('A',1);
cache.set('B',2);
print(cache.current_size());
print('-------------------');
cache.set('A',2);
cache.set('C',2);
cache.set('D',2);
cache.set('E',2);
print(cache.current_size());
