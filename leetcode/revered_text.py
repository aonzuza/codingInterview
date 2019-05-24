def reversed_text(arr):
    reversed_list = [];
    def _reversed(arr, reversed_list):
            if len(arr) == 0 :
                return;
            reversed_list.append(arr[-1]);
            _reversed(arr[:-1],reversed_list);

    _reversed(arr,reversed_list);
    return reversed_list;


x = [1,2,3,4,5];
y = reversed_text(x);
print(y);

# x = [1];
# print(len(x[:]));
