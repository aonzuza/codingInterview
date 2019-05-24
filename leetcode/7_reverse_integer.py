
def reverse(x):
    revered_list = str(x)[::-1];
    return int(revered_list[:]) if x > 0 else int(revered_list[:-1]) * -1

inputs =  23456;
y =reverse(inputs);
print(y);


k = [1,2,3,4,5,6,7,8,9,10];
print(k[::-2]);
