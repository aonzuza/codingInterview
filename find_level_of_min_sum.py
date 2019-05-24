import numpy as np
from collections import defaultdict;

class Node:
    def __init__(self, val = None, left = None,right = None):
        self.val = val;
        self.left = left;
        self.right = right;

class Tree:
    def __init__(self,val):
        self.root = Node(val);

    def inorderTraversal(self):


        def _inorderTraversal(node):

            if not node:
                return;

            _inorderTraversal(node.left);
            print(node.val);
            _inorderTraversal(node.right);

        _inorderTraversal(self.root);

    def tree_to_array(self):

        def _tree_to_array(node):
            if not node:
                return [];
            return [node.val] + _tree_to_array(node.left) + _tree_to_array(node.right);

        return _tree_to_array(self.root);

    def find_min(self):

        def _find_min(node,level, dict):

            if not node:
                return dict;

            dict[level] = dict[level] + node.val;

            _find_min(node.left , level + 1, dict);
            _find_min(node.right, level + 1, dict);


            return dict

        return _find_min(self.root,0,defaultdict(int));


tree = Tree(9);
tree.root.left         = Node(5);
tree.root.right        = Node(3);
tree.root.left.left        = Node(10);
tree.root.left.right       = Node(1);
tree.root.right.left       = Node(2);
tree.root.right.right       = Node(6);
tree.root.left.left.right       = Node(18);
tree.root.right.left.left       = Node(-22);
