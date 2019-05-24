
def findProducts(arr):

    prefix = [];
    suffix = [];
    results = [];

    length = len(arr);

    for i in range(0,length -1):

        if i == 0:
            prefix.append(arr[i]);
        else:
            prefix.append(prefix[-1] * arr[i]);

    for j in range(length -1, 0, -1):

        if j == length -1:
            suffix.insert(0,arr[j]);
        else:
            # print(arr[])
            suffix.insert(0,suffix[0] * arr[j]);


    print(prefix);
    print(suffix);
    for k in range(length):

        if k == 0:
            # no prefix
            results.append(suffix[0]);
        elif k == length -1:
            # no suffix
            results.append(prefix[-1]);
        else:
            results.append(prefix[k-1] * suffix[k]);

    print(results);


x = [1,2,3,4,5];
results = findProducts(x);

print(results);
