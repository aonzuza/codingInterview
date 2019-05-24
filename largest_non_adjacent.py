# def largest_non_adjacent(arr):
#     if not arr:
#         return 0;
#     return max(largest_non_adjacent(arr[1:]), arr[0] + largest_non_adjacent(arr[2:]))\


# def largest_non_adjacent(arr):
#     if len(arr) <=2:
#         return max(arr);
#
#     max_excluding_last = arr[0];
#     max_including_last = max(max_excluding_last,arr[1])
#
#     for num in arr[2:]:
#         prev_max_including_last = max_including_last;
#
#         max_including_last = max(max_including_last,max_excluding_last + num)
#         max_excluding_last = prev_max_including_last;
#
#     return max(max_including_last,max_excluding_last);


def find_max_sum(arr):
    if len(arr) <=2:
        return max(arr);

    max_excluding_last = arr[0];
    max_including_last = max(arr[0],arr[1]);

    for num in arr[2:]:

        temp = max_including_last;
        max_including_last = max(num + max_excluding_last, num , max_including_last);
        max_excluding_last = temp;
    return max_including_last

ary = [5, 5, 10, 100, 10, 5,200]

result = find_max_sum(ary);

print(result);
