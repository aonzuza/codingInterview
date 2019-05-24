def isAdvanced(lst):

    finish = 0;
    for i in range(len(lst)):
        current = i;
        temp = current + lst[current];

        if temp > finish:
            finish = temp;
        if current == finish:
            return 'false'
    return 'true';

lst = [3,0,1];
result = isAdvanced(lst);
print(result);
