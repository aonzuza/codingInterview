def create_anagram(word):

    if len(word) == 1:
        # considered permutated
        return [word];
    else:
        permutated = [];
        for perm in create_anagram(word[1:]):
            # start permutaing a char with others from create_anagram
            for anchor in range(len(word)):
                permutated.append(perm[:anchor] + word[0]  + perm[anchor:]);
        return permutated;


def create_anagram_2(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in create_anagram(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]



word = 'abcd';
string = 'abxba';


anagram_lst = list(create_anagram(word));
