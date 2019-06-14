def find_add_up_to_k(lst,k):

    seen = {};

    for number in lst:
        key = k - number;
        if key in seen:
            return True;

        else:
            seen[number] = 1;

    return False;


k = -5;
lst = [-4,15,9,-2];

result = find_add_up_to_k(lst,k);

print(result);
