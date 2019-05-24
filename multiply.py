def products(lst):
    results = [];
    temp = 1;
    for i in range(len(lst)):
        results.append(temp);
        temp = temp * lst[i];
    temp = 1;
    for i in range(len(lst)-1,-1,-1):
        results[i] = results[i] * temp;
        temp = temp * lst[i];
    return results;


lst = [2,3,4,5];
results = products(lst);
print(results);
