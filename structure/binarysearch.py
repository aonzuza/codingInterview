
def binary_search(arr,val):

    low = 0;
    high = len(arr) - 1;

    while high >= low :
        mid_point = high + low // 2;

        if arr[mid_point] == val:
            return True;
        elif arr[mid_point] < val:
            low = mid_point + 1;
        else:
            high = mid_point -1;

    return False;

def binary_search_recursion(arr,val):

    def _helper(arr, val, low , high):

        mid_point = high + low // 2;

        if high < low:
            return False;

        if arr[mid_point] == val:
            return True;
        elif arr[mid_point] > val:
            return _helper( arr,val,low,mid_point - 1);
        else:
            return _helper(arr ,val, mid_point + 1 , high );

    return _helper(arr,val, 0 , len(arr) - 1);










arr = [2,4,6,7,8,10,15];
val = 15;
x = binary_search_recursion(arr, val);
print(x);
