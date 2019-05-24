
def is_palindrome(word):
    return word == word[::-1];

def palindrome_pair(lst):

    dict = {};
    results = [];
    for index, word in enumerate(lst):
        dict[word] = index;

    # print(dict);

    for word_index,word in enumerate(lst):

        for index in range(len(word)):

            prefix = word[:index];
            suffix = word[index:];

            reversed_prefix = prefix[::-1];
            reversed_suffix = suffix[::-1];


            if is_palindrome(prefix) == True and reversed_suffix in dict:

                if word_index != dict[reversed_suffix]:
                    results.append([word_index,dict[reversed_suffix]]);

            if is_palindrome(suffix) == True and reversed_prefix in dict:

                if word_index != dict[reversed_prefix]:
                    results.append([word_index,dict[reversed_prefix]]);





    return results;





lst =['code','edoc','da','d'];

results = palindrome_pair(lst);

print(results);
