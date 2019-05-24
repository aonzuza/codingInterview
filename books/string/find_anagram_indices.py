from collections import defaultdict;
from collections import Counter;


def find_my_anagram(word,string):

    freq = defaultdict(int);
    results = [];

    for char in word:
        freq[char] = freq[char] - 1;

    for char in string[:len(word)]:
        freq[char] = freq[char] + 1;
        delete_if_zero(freq,char);



    for index in range(0, len(string) - len(word) + 1 ):

        startChar = string[index - 1] ;
        endChar   = string[index + len(word) - 1];

        if index !=0:

            freq[endChar] = freq[endChar] + 1;
            delete_if_zero(freq,endChar);
            freq[startChar] = freq[startChar] - 1;
            delete_if_zero(freq,startChar);
            # print(freq);
        if not freq:
            results.append(index);

    print(results);




def find_my_anagram_2(word,text):
    freq = defaultdict(int);

    for char in word:
        freq[char] += 1;

    cached = defaultdict(int);

    for char in text[:len(word)]:
        cached[char] +=1;


    string_length = len(text);
    word_length = len(word);

    results = [];

    # print(text[-1]);


    for index in range(0,  string_length - word_length + 1 ):

        # if index == 0:
        #     if freq == cached:
        #         results.append(index);
        if index !=0:
            start_char = text[index - 1];
            end_char   = text[index + word_length - 1 ];


            # decrease start char freq
            cached[start_char] = cached[start_char] - 1;
            delete_if_zero(cached,start_char);
            # increase endchar freq
            cached[end_char] = cached[end_char] + 1;
            # print(start_char + ':' + end_char);
            # print(cached);

        if freq == cached:
            results.append(index);

    print(results);



# def find_anagram_indices(word,string):
#
#     lst = list(create_anagram(word));
#
#     length = len(string);
#     results = [];
#     for index in range( 0, length - len(word) + 1):
#         window = string[index: index + len(word)];
#         c1 = Counter(window);
#         c2 = Counter(word);
#
#         if c1 == c2:
#             results.append(index);

def create_anagram(word):

    if len(word) == 1:
        # considered it permutated
        return [word];
    else:
        permutated = [];
        for perm in create_anagram(word[1:]):
            for anchor in range(len(word)):
                permutated.append(perm[:anchor] + word[0] + perm[anchor:]);
        return permutated;

def find_anagram_indices(word,string):

    permutated = create_anagram(word);

    window_size = len(word);
    string_size = len(string);

    results = [];
    for i in range(string_size - window_size + 1):
        window = string[ i: i + window_size];
        print(window);
        if window in permutated:
            results.append(i);


def delete_if_zero(dict,char):
    if dict[char] == 0:
        del dict[char];

def anagram_indices(word,string):
    results = [];
    freq = defaultdict(int);

    for char in word:
        freq[char] +=1;
    # print(freq);
    for char in string[:len(word)]:
        freq[char] -=1;
        delete_if_zero(freq,char);

    # print(freq);

    if not freq:
        results.append(0);

    for i in range(len(word),len(string)):

        start_char = string[i-len(word)];
        end_char   = string[i];

        freq[start_char] += 1;

        # print(start_char + ' - ' + end_char);

        delete_if_zero(freq,start_char);

        freq[end_char] -=1;
        delete_if_zero(freq,end_char);
        # freq = sorted(freq.items())

        # print(freq);

        if not freq:
            begining_index = i - len(word) + 1;
            results.append(begining_index);
    print(results);

word = 'ab';
string = 'xabcba';
find_my_anagram(word,string);
