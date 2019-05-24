
def find_max_product_of_three(arr):

        arr.sort();
        return max(arr[0] * arr[1] * arr[2] , arr[-1] * arr[-2] * arr[-3]);

# - 10 ,2,5,6,10
x = [-10,10,2,5,6];
max = find_max_product_of_three(x);
print(max);
