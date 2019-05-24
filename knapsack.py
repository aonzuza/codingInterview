# def ks(weights,values,capacity,n):
#     memory = [[None for _ in range(capacity+1)] for _ in range(n+1)];
#
#     def helper(c,index):
#         if memory[index][c] is not None:
#             return memory[index][c];
#         if c == 0 or index < 0:
#             return 0;
#         if weights[index] > c:
#             result = helper(c,index -1);
#         else:
#             temp1 = helper(c,index - 1);
#             temp2 = values[index] + helper(c-weights[index],index-1);
#             result = max(temp1,temp2);
#         memory[n][c] = result;
#         return result;
#     return helper(capacity,n);
#
# weights = [2,5,5,8,9];
# values = [3,1,10,11,15];
# capacity = 9;
#
# result = ks(weights,values,capacity,len(weights)-1);
# print(result);



# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(capacity, weights, values, index):
    memory = [ [0 for _ in range(capacity+1)] for _ in range(index+1)];

    for i in range(index + 1):
        for j in range(capacity + 1):

            if i == 0 or j == 0:
                memory[i][j] = 0;
            #  previous weight exceeded.
            elif weights[i-1] > j :
            # we cannot carry the previous item
            # its value is the same as previous value
                memory[i][j] = memory[i-1][j];
            else:
                temp1 = memory[i-1][j];
                temp2 = values[i-1] + memory[i-1][j - weights[i-1]]
                memory[i][j] = max(temp1,temp2);

    return memory[index][capacity];




# Driver program to test above function
values   = [60, 100, 120]
weights  = [10, 20, 30]
capacity = 50
index = len(values)
result = knapSack(capacity, weights, values, index)
print(result);
