class Node:
    def __init__(self):
        # obj node
        self.childrens = {};
        self.isEndofWord = False;
class Trie:
    def __init__(self):
        self.root = Node();

    def insert(self,word):
        current = self.root;
        for char in word:
            if not current.childrens.get(char):
                current.childrens[char] = Node();
            current = current.childrens[char];
        current.isEndofWord = True;

    def search(self,word):
        current = self.root;
        for char in word:
            if not current.childrens.get(char):
                return False;
            current = current.childrens.get(char);
        return current.isEndofWord;

    def show(self):
        current = self.root;
        results = [];
        def _show_helper(current,word):
            if current.isEndofWord:
                results.append(word);
            for key in current.childrens:
                _show_helper(current.childrens[key], word + key);
        _show_helper(current,'');
        return results;

    def count(self):
        current = self.root;
        def _count_helper(current):
            counter = 0;
            if current.isEndofWord:
                counter = counter + 1;
            for key in current.childrens:
                counter += _count_helper(current.childrens[key]);
            return counter;

        return _count_helper(current);


    def suggestion_prefix(self,keyword):
        current = self.root;
        for char in keyword:
            if not current.childrens.get(char):
                return 'no match';
            current = current.childrens.get(char);

        # print(current);
        results = [];

        def _finder_helper(current,keyword):
            if current.isEndofWord:
                results.append(keyword);
            for key in current.childrens:
                _finder_helper(current.childrens[key],keyword + key);

        _finder_helper(current,keyword);
        return results;

    def suggestion_suffix(self,suffix):
        current = self.root;
        results = [];
        def _suggestion_suffix_helper(current,word):
            if current.isEndofWord == word.endswith(suffix) == True:
                results.append(word);
            for key in current.childrens:
                _suggestion_suffix_helper(current.childrens[key], word + key);
        _suggestion_suffix_helper(current,'');
        return results;

    def remove(self, keyword):
        current = self.root;
        level = 0;
        key_length = len(keyword) - 1;

        def _removable(current,keyword,level):
            #  we are at the end of keyowrd.
            if len(keyword) == 0:
                return;
            # check if key exists in the dict
            if keyword[0] not in current.childrens:
                print('no such word :' + keyword[0]);
                return;
            else:
                _removable(current.childrens[keyword[0]],keyword[1:], level + 1);
                # unflag the last char of keyword
                if level == key_length:
                    # even though the last child is not end of word , it is gonna be False anyway....
                    current.childrens[keyword[0]].isEndofWord = False;
                if current.childrens[keyword[0]].isEndofWord == False and current.childrens[keyword[0]] == None:
                    del  current.childrens[keyword[0]];

            return;
                # check if the node has children


        _removable(current,keyword,0);


words = ["the","a","there","anaswe","any","anything", "by","their"];

trie = Trie();

for word in words:
    trie.insert(word);

print(trie.show());
print(trie.remove('the'));
print(trie.show());
