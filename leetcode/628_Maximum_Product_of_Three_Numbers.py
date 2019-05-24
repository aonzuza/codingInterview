

def find_max_of_three_numbers(inputs):
    sorted = inputs;
    sorted.sort();
    return max(sorted[0] * sorted[1] * sorted[2], sorted[-1]*sorted[-2] *sorted[-3]);


inputs = [1,2,3,4];

max_product = find_max_of_three_numbers(inputs);
print(max_product);




# def find_Product(arr,count):
#     def findPro(arr,mul,count):
#         if len(arr)==count == 1:
#             return mul*arr[0]
#         if count == 1:
#             return max(mul*arr[0],find_Product(arr[1:],mul,count))
#         if len(arr)==count:
#             return find_Product(arr[1:] ,mul*arr[0] ,count-1)
#
#         return max(find_Product(arr[1:] ,mul*arr[0] ,count-1) ,find_Product(arr[1:] ,mul ,count))
#
#     return findPro(arr,1,count)
#
# arr = [-100,-10,-3,-4,-1]
# count = 3
# print(find_Product(arr,count))
#
