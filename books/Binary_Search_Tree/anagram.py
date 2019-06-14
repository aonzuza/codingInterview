class Node:
    def __init__(self,val,left=None,right=None):
        self.root = val;
        self.left = left;
        self.right = right;

class BST:

    def __init__(self):
        self.root = None;

    def insert(self,key):

        def _insert(root,key):
            if not root:
                return Node(key);

            if key < root.val:
                root.left = _insert(root.left,key);
            else:
                root.right = _insert(root.right,key);

            return root;

        self.root = _insert(self.root,key);




def mixer(nums):

    if len(nums) == 1:
        return [nums[0:1]];

    results = [];
    for option in mixer(nums[1:]):

        for index in range(len(nums)):

            # print('-----------------');
            result = option[:index] + nums[0:1] + option[index:];
            # result = [];
            # result.append(option[:index]);
            # result.append(nums[0:1]);
            # result.append(option[index:]);
            results.append(result);
    return results;


def anagram_generator(word):

    if len(word) == 1:
        return [word];

    results = [];
    for anagram in anagram_generator(word[1:]):

        for index in range(len(word)):

            result = anagram[:index] + word[0] + anagram[index:];
            results.append(result);
    return results;


def bst_node_generator(lst):
    trees = [];
    for row in lst:
        for num in row:
            tree = BST();
            tree.insert(num);
            trees.append(tree);
    return trees;






input = 'abc';

anagrams = anagram_generator(input);

mixes = mixer([1,2,3]);
trees = bst_node_generator(mixes);
print(trees);
