class BubbleSort:
    def __init__(self, arr):
        self.arr = arr;

    def sort_asc(self):

        def _sorter(arr,endIndex):
            if endIndex == 0:
                return;
            for current_index in range(0,endIndex):

                if arr[current_index] > arr[current_index + 1]:
                        # swap
                        arr[current_index], arr[current_index + 1] = arr[current_index + 1] , arr[current_index];

            _sorter(arr,endIndex - 1);

        _sorter(self.arr,len(self.arr) -1 );

    def sort_desc(self):

        def _sorter(arr, endIndex):
            if endIndex == (len(arr) -1):
                return;
            for index in range(len(arr)-1, endIndex -1 , -1):
                if arr[index] > arr[index -1]:
                    arr[index],arr[index-1] = arr[index-1] , arr[index];
            _sorter(arr,endIndex + 1);

        _sorter(self.arr, 0);



arr = [12,0,8,16,8,5,3,15];
bubble = BubbleSort(arr);
bubble.sort_desc();
print(bubble.arr);

bubble.sort_asc();
print(bubble.arr);
