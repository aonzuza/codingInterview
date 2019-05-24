def is_palindrom_number(input):

    if input < 0:
        return False;
    temp = input;
    palindrom = 0;

    while temp > 0:
        palindrom = palindrom * 10 + ( temp % 10);
        temp = temp / 10;
    return input == palindrom;

def validPalindrome(s):
    length = len(s);
    decreasing_index = length - 1;
    increasing_index = 0;
    is_first_mistake = False;

    while increasing_index < decreasing_index:

        if s[increasing_index] == s[decreasing_index]:
            increasing_index += 1;
            decreasing_index -= 1;
        else:
            decreasing_index -= 1;

    return is_palindrom;

input = 'abca';
is_palindrom = validPalindrome(input);
print(is_palindrom);
# print(10/10);
# a = 6;
# b = a;
# b = b +5;
# print(b);
