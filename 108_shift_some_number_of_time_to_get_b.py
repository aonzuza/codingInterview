def is_match(a,b):
    length = len(a);
    while length > 0:
        a = a[1:] + a[0];
        length = length - 1;
        if a == b:
            return True;
    return False;


a = "abc";
b = "acb";

x =is_match(a,b);
