class MergeSort:

    def divider(self,arr):
        if len(arr) == 1:
            return arr;
        center = len(arr) // 2;
        left_arr =  self.divider(arr[0:center]);
        right_arr = self.divider(arr[center:]);
        return self.sorter(left_arr,right_arr);

    def sorter(self,left_arr,right_arr):

        results = [];
        i = 0;
        j = 0;
        while i < len(left_arr) and j < len(right_arr):

            x = left_arr[i];
            y = right_arr[j];

            if x < y:
                results.append(x);
                i = i + 1;
            elif x > y:
                results.append(y);
                j = j + 1;
            else:
                results.append(x);
                results.append(y);
                i = i + 1;
                j = j + 1;
        return results + left_arr[i:] + right_arr[j:];

x = [-25,4,7,810,0,15,-32,3,1,13,26,-300,2,1];
ms = MergeSort();
y = ms.divider(x);
print(x);
