
#binary search
from bisect import bisect_left;

def binary_search(lst,target):
    lo = 0 ;
    hi = len(lst);

    index = bisect_left(lst,target);
    return index;


def find_sum(lst, K ):
    lst.sort();
    for i in range(len(lst)):

        target = K - lst[i];
        index = binary_search(lst, target);

        # if index is not i , it means the target exists in our list
        # if index + 1 is not out of range and is equal to target , return true
        if index != i :
            return True;
        elif index + 1 < len(lst) and lst[index + 1] == target :
            return True;
        elif index - 1 >= 0 and lst[index -1]  == target :
            return True;
    return False;




# main code starts here...
result = 30;
lst = [5,10,15,20,99];


index = binary_search(lst,100);
print(index);







# best method
# def two_sum(lst,sum):
#     # if two member in a list can sum uo to sum , return true , else return false.
#
#     pocket = [];
#
#     for i  in range(len(lst)) :
#         target = sum - lst[i];
#
#         if target in pocket :
#             return True;
#         else:
#             pocket.append(lst[i]);
#     return False;
#
# sum = 16;
# lst = [0,8,30,8,50];
# isFound = two_sum(lst,sum);
#
# print(isFound);
