

def is_even(x):
    if x & 1 == 0:
        return True;
    return False;
def is_nth_set(x,n):
    if x & (1<<n):
        return True;
    return False;

def set_nth(x,n):
    return x | (1 << n );

def toggle_nth(x,n):
    return x ^ (1 << n );

x = 60;
# n = 4;
# y = toggle_nth(x,n);
print(bin(~(1<<5)));
# #
# print(bin(~(1<<5)));
