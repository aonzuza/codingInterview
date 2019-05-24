

def longest_substring_with_k_distinct_characters(s,k):
    if k == 0:
        return 0;
    #keep a running windows
    bounds = (0,0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i;
        print(h);
        if len(h) <= k :
            new_lower_bound = bounds[0]
        else:
            key_to_pop = min(h,key = h.get)
            new_lower_bound = h.pop(key_to_pop) + 1
        bounds = (new_lower_bound,bounds[1] + 1)
        max_length = max(max_length,bounds[1] - bounds[0])
    return max_length





inputs = 'abcba';
max = longest_substring_with_k_distinct_characters(inputs,2);
print(max);










#
#
#
# inputs = 'abcba';
#
# length = len(inputs);
#
#
#
# startIndex = 0;
# endIndex   = 0;
# temp = [];
# results = [];
# k = 2;
# counter = k;
#
# while endIndex < length:
#     char = inputs[endIndex];
#     print(char);
#     if char not in temp:
#         counter = counter - 1;
#     temp.append(char);
#     if counter < 0:
#         counter = k;
#         str = ''.join(temp);
#         results.append(str);
#         startIndex +=1;
#         endIndex = startIndex;
#     else:
#         endIndex = endIndex + 1;
#
# print(results);
