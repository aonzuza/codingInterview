def max_subarray_sum(arr):

    max_seen = max_ending_here = 0 ;

    for num in arr:
        max_ending_here = max( num , max_ending_here + num);
        max_seen = max( max_seen , max_ending_here );

    return max_seen;

def min_subarray_sum(arr):

    min_seen = min_ending_here = 0;

    for num in arr:

        min_ending_here = min(num , num + min_ending_here);
        min_seen = min(min_seen,min_ending_here);


    return min_seen;



def max_subarray_wrap_around(arr):

    max_wrap_around = sum(arr) - min_subarray_sum(arr);


    return max(max_subarray_sum(arr) , max_wrap_around );


arr = [34,-50,42,14,-5,86];
max_sub = max_subarray_wrap_around(arr);


lst = [8,-1,3,4];
max_circular = max_subarray_wrap_around(lst);
print(max_circular);
