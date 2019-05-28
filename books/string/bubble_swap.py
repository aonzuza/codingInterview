def bubble_swap(string,i,j):
    string = list(string);
    # rotate so that i is at the begining.
    while i > 0:
        string = string[1:] + string[:1];
        i -=1;
        print(string);

    # move the first two letters to the end in reversed order
    string = string[:1] + string[2:] + string[1:2];
    print('first move',string);
    string = string[1:] + string[:1];
    print('secod move',string);

    #rotate back to the initial position
    while len(string) > j + 1:
        string = string[1:] + string[:1];
        j += 1;
        print('rotate back',string);
    return ''.join(string);

def get_best_word(string,k):
    string = list(string);
    print('word',string);
    if k == 1:
        best = string;
        for i in range(1,len(string)):
            newly_rotated_string = string[i:] + string[:i];
            if newly_rotated_string < best:
                best = newly_rotated_string;

        return ''.join(best);
    else:
        return ''.join(sorted(string));

def char_swapper(string,k):
    string = list(string);

    for index in range(100000):
        index = index %  ( len(string) -1 );

        if string[index] > string[index+1]:
            string[index], string[index+1] = string[index+1],string[index];
        string = string[1:] + string[:1];
        print(string);


string = "gfedcba";

print('word',list(string));
# best1 = bubble_swap(string,2,1);
# best2 = get_best_word(string,1);
char_swapper(string,2);
# print('bubble_swap:', best1);
# print('get_best_word:', best2);
