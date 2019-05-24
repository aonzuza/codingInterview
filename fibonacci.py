def fib(n):

    # scale to 0
    lst = [0 for _ in range(n)];
    lst[0] = 1;
    lst[1] = 1;
    if n == 1 or n == 2:
        return lst[n-1];

    for i in range(2,n):
        lst[i] = lst[i-1] + lst[i-2];
    return lst[-1];

result = fib(10);
print(result);
