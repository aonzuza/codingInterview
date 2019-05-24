class QuickSort:

    def __init__(self, arr):
        self.arr = arr;

    def sort(self):
        first = 0;
        last  = len(self.arr) - 1;
        self.sortHelper(first,last);

    def sortHelper(self, first, last):
        if first < last :
            # partition the self.array;
            # find a correct position for the pivot
            correctPivotIndex = self.patitioning(first,last);

            # left side
            self.sortHelper( first, correctPivotIndex -1);
            # right side
            self.sortHelper( correctPivotIndex + 1 , last);


    def patitioning(self, first, last):

        # pivotIndex = 0;
        # pivotValue = self.arr[pivotIndex];
        pivotIndex = first;
        pivotValue = self.arr[first];
        done = False;

        leftIndex = first + 1;
        rightIndex = last;



        while not done:

            while leftIndex <= rightIndex and self.arr[leftIndex] <= pivotValue:

                leftIndex = leftIndex + 1;


            while self.arr[rightIndex] >= pivotValue and leftIndex <= rightIndex:

                rightIndex = rightIndex - 1;

            # the swapping is still in process
            if leftIndex > rightIndex:
                done = True;
            else:
                self.arr[leftIndex] , self.arr[rightIndex] = self.arr[rightIndex] , self.arr[leftIndex];

        self.arr[pivotIndex] , self.arr[rightIndex] = self.arr[rightIndex] , self.arr[pivotIndex];


        return rightIndex;




arr = [54,26,93,17,77,31,44,55,20];

sorter = QuickSort(arr);
sorter.sort();
print(sorter.arr);
