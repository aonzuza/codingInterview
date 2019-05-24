def capacity(arr):
    if not arr:
        return 0

    total = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for num in arr[1:max_i]:
        left_max = max(left_max, num)
        total += left_max - num

    right_max = arr[-1]
    for num in arr[-2:max_i:-1]:
        right_max = max(right_max, num)
        total += right_max - num

    return total

# def capacity(arr):
#     n = len(arr)
#     left_maxes = [0 for _ in range(n)]
#
#     right_maxes = [0 for _ in range(n)]
#
#     current_left_max = 0
#     for i in range(n):
#         current_left_max = max(current_left_max, arr[i])
#         left_maxes[i] = current_left_max
#
#     current_right_max = 0
#     for i in range(n - 1, -1, -1):
#         current_right_max = max(current_right_max, arr[i])
#         right_maxes[i] = current_right_max
#     print(right_maxes);
#     total = 0
#     for i in range(n):
#         total += min(left_maxes[i], right_maxes[i]) - arr[i]
#     return total


arry = [3,0,5,0,4];
print(arry);
result = capacity(arry);
print(result);
