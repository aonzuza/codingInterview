def square_sort(arr):

    negative_numbers = list(filter( lambda x : x < 0 , arr ));
    positive_numbers = list(filter( lambda y : y >=0 , arr ));

    left_arr =  [ x ** 2 for x in reversed(negative_numbers) ];
    right_arr = list( map( lambda y: y ** 2 , positive_numbers));

    def _merged_sort(left_arr , right_arr ):

        leftIndex = 0;
        rightIndex = 0;
        results = [];
        print(left_arr);
        print(right_arr);
        print('----------');
        while leftIndex < len(left_arr) and len(right_arr):
            print(leftIndex);
            print(rightIndex);
            if left_arr[leftIndex] < right_arr[rightIndex]:

                results.append(left_arr[leftIndex]);
                leftIndex = leftIndex + 1;

            elif left_arr[leftIndex] > right_arr[rightIndex]:

                results.append(right_arr[rightIndex]);
                rightIndex = rightIndex + 1;

            else:

                results.append(left_arr[leftIndex]);
                results.append(right_arr[rightIndex]);
                leftIndex = leftIndex + 1;
                rightIndex = rightIndex + 1;

        print('xxxxxxxxxxxxxxxxxx');
        print(results);
        print('xxxxxxxxxxxxxxxxxx');
        return results + left_arr[leftIndex:] + right_arr[rightIndex:];


    return _merged_sort(left_arr, right_arr);

x = [ -3 , -2 , - 1 ,0 , 2, 3 ,5 , 10 ];

y = square_sort(x);
print(y);
