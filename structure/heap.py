class MinHeap:
    def __init__(self):
        self.heap = [];
    def show(self):
        print(self.heap);

    def peek(self):
        # return mininmun value;
        return self.heap[0] if len(self.heap) >=0 else 5555;
    def swap(self,index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2] , self.heap[index_1];
    def push(self,value):
        # add the new value to Heap;
            # add value to the end of the heap (right most leaf node)
            # heapify up - parent value is always less than children
        self.heap.append(value);
        index = len(self.heap) - 1;
        parentIndex = self.parentIndex(index);
        hasParent = self.hasParent(parentIndex);

        print('valus is' + str(value));
        print('parent Index is' + str(parentIndex));
        # print(hasParent);

        while hasParent and self.heap[index] < self.heap[parentIndex]:
            # swap
            # check parent
            # update index
            print('prentIndex is' + str(parentIndex) + ' swap ' + str(self.heap[index]) + ' with ' + str(self.heap[parentIndex]) );
            self.swap(index,parentIndex);
            index = parentIndex;
            parentIndex = self.parentIndex(index);
            hasParent = self.hasParent(parentIndex);


    def pop(self):
        # remove the min value
        # replace the root with the leaf node ( the depest and most right node)
        # heapify down
        size = len(self.heap);
        if size:
            # swap root with the last node
            self.swap(-1,0);
            #  remove the last node
            self.heap.pop(-1);
            # heapify dow
            index = 0;
            leftIndex = self.leftChildIndex(index);
            hasLeftChild = self.hasLeftChild(leftIndex);
            rightIndex = self.rightChildIndex(index);
            hasRightChild = self.hasRightChild(rightIndex);

            while hasLeftChild:

                if hasRightChild and self.heap[rightIndex] < self.heap[leftIndex]:
                    leftIndex = rightIndex;

                if self.heap[index] > self.heap[leftIndex]:
                    self.swap(leftIndex,index);
                    index = leftIndex;
                    leftIndex = self.leftChildIndex(index);
                    hasLeftChild = self.hasLeftChild(leftIndex);
                else:
                    break;


    def parentIndex(self,index):
        # index - 1 // 2
        return (index - 1) // 2;
    def hasParent(self,parentIndex):

        # parentIndex = self.parentIndex(Index);
        size = len(self.heap);
        return True if  0 <= parentIndex < size else False;

    def leftChildIndex(self,index):
        return (index * 2) + 1;

    def hasLeftChild(self,leftIndex):
        # leftIndex = self.leftChildIndex(index);
        size = len(self.heap);
        return True if 0 <= leftIndex < size else False;

    def rightChildIndex(self,index):
        return (index *2) + 2;

    def hasRightChild(self,rightChildIndex):
        # rightIndex = self.rightChildIndex(index);
        size = len(self.heap);
        return True if 0 <= rightChildIndex < size else False;

class MaxHeap():
    def __init__(self):
        self.heap = [];
    def show(self):
        print(self.heap);
    def swap(self,a,b):
        self.heap[a] , self.heap[b] = self.heap[b] , self.heap[a];

    def peek(self):
        return self.heap[0] if len(self.heap) >= 0 else 5555;
    def pop(self):
        # move root node to the right most child position...
        if self.heap:
            self.swap(0, -1);
            self.heap.pop(-1);
            index = 0;
            leftIndex = self.leftChildIndex(index);
            hasLeftChild = self.hasLeftChild(leftIndex);
            rightIndex = self.rightChildIndex(index);
            hasRightChild = self.hasRightChild(rightIndex);
            while hasLeftChild:

                if hasRightChild and self.heap[rightIndex] > self.heap[leftIndex]:
                    leftIndex = rightIndex;
                if self.heap[index] < self.heap[leftIndex]:
                    self.swap(index,leftIndex);
                    index = leftIndex;
                    leftIndex = self.leftChildIndex(index);
                    hasLeftChild = self.hasLeftChild(leftIndex);
                else:
                    break;
    def push(self,value):
        self.heap.append(value);
        index = len(self.heap) - 1;
        # heapify up
        parentIndex = self.parentIndex(index);
        hasParent   = self.hasParent(parentIndex);

        while hasParent and self.heap[index] > self.heap[parentIndex]:

            # print('prentIndex is' + str(parentIndex) + ' swap ' + str(self.heap[index]) + ' with ' + str(self.heap[parentIndex]) );
            self.swap(index,parentIndex);
            index = parentIndex;
            parentIndex = self.parentIndex(index);
            hasParent = self.hasParent(parentIndex);

    def parentIndex(self,index):
        return (index - 1) //2;

    def hasParent(self,index):
        return True if 0 <= index < len(self.heap) else False;

    def leftChildIndex(self,index):
        return (index * 2) + 1;
    def hasLeftChild(self,index):
        return True if 0 <= index < len(self.heap) else False;

    def hasRightChild( self,index):
        return True if 0 <= index < len(self.heap) else False;

    def rightChildIndex(self,index):
        return (index * 2) + 2;



heap = MaxHeap();
heap.push(2);
heap.push(5);
heap.push(8);
heap.push(7);
heap.push(10);
heap.push(11);
# expected 3,4,8,9
heap.show();
heap.pop();
heap.show();
# print(x);
