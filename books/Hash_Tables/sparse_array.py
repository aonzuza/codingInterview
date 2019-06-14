from collections import defaultdict;
class SparseArray:
    def __init__(self,arr,capacity):

        self.dd = defaultdict(int);
        self.capacity = capacity;

        for index,val in enumerate(arr):
            if val !=0:
                self.dd[index] = val;

    def inbound(self,index):
        return 0 <= index <= self.capacity - 1;

    def set(self,index,val):
        if self.inbound(index):
            if val !=0:
                self.dd[index] = val;
            elif index in self.dd:
                del self.dd[index];
        else:
            raise IndexError('out of range');

    def get(self,index):
        if self.inbound(index):
            return self.dd[index];
        else:
            raise IndexError('out of range');

arr = [0]*100;
# print(len(arr));
sparse_arr = SparseArray(arr,len(arr));

sparse_arr.set(9,20);
sparse_arr.set(15,21);
sparse_arr.set(18,22);
sparse_arr.set(99,23);

# print(sparse_arr.dd);
#
# sparse_arr.set(99,0);
#
# print(sparse_arr.dd);

d = {};
d["a"] = "test";
print(d["a"]);
