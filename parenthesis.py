def isBalanced(msg):
    counter = 0;
    for char in msg:
        if char == '{':
            counter = counter + 1;
        else:
            counter = counter - 1;
    return 'True' if counter == 0 else 'False';



msg = '}}}}{{{}}}{{}}{{{{{{}}}}}{{';
result = isBalanced(msg);

print(result);
