def products(nums):
    # suffix products

    count = len(nums);
    #  default value = 1
    outputs = [1] * count;
    k = 1;
    for i in range(count-1,-1,-1):

        if i + 1 < count:
            k = k * inputs[i+1];
        outputs[ i ] = k;


    m = 1;

    for j in range(count):

        if j - 1 >= 0:
            m = m * inputs[j -1];

        outputs[j] = outputs[j] * m;

    print(outputs);

inputs = [1,2,3,4,5];

products(inputs);
#
# print(outputs);

# print(inputs[-]);


#second method
# input = [2,3,4,5,6];
#
# output = [];
#
# x = 1;
# for i in range(len(input)):
#     x = x * input[i];
#
#
# for j in range(len(input)):
#     k = x / input[j];
#     output.append(int(k));
#
# print(output);









#  worst way to do
# input = [2,3,4,5,6];
#
# output = [];
#
# for i in range(len(input)):
#     x = input[i];
#     k = 1;
#     for j in range(len(input)):
#         y = input[j];
#         if i != j :
#             k = k * y;
#     output.append(k);
# print(output);
