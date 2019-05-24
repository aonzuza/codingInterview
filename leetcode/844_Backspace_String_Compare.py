

def backspaceCompare(s,t):

    result1 = '';
    for char in s:
        if char != '#':
            result1 += char;
        else:
            result1 = result1[0:-1];

    result2 = '';
    for char in t:
        if char != '#':
            result2 += char;
        else:
            result2 = result2[0:-1];

    print(result1);
    print(result2);
    return result1 == result2;


s,t = "a##c","#a#c";

isEqual = backspaceCompare(s,t);

print(isEqual);
