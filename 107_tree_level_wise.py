from collections import defaultdict;

class Node:
    def __init__(self, val, left = None,right = None):
        self.val   = val;
        self.left  = left;
        self.right = right;

class Tree:
    def __init__(self,val):
        self.root = Node(val);
    def inorder_traversal(self):

        def _helper(node):
            if node == None:
                return;
            print(node.val);
            _helper(node.left);
            _helper(node.right);
        _helper(self.root);

    def level_wise_traversal(self):

        def _helper(node, level ,dict):
            if not node:
                return dict;

            dict[level].append(node.val);

            _helper(node.left  , level + 1, dict);
            _helper(node.right , level + 1, dict);

            return dict;

        return _helper(self.root, 0 , defaultdict(list));

    def q_level_wist_traversal(self):

        def _helper(level, queue ):

            while queue:
                node = queue.pop(0);

                if node.left:
                    queue.append(node.left);
                if node.right:
                    queue.append(node.right);
        lst = [];
        lst.append(self.root);
        return _helper( 0 , lst);

tree = Tree(9);
tree.root.left         = Node(5);
tree.root.right        = Node(3);
tree.root.left.left        = Node(10);
tree.root.left.right       = Node(1);
tree.root.right.left       = Node(2);
tree.root.right.right       = Node(6);
tree.root.left.left.right       = Node(18);
tree.root.right.left.left       = Node(22);
tree.q_level_wist_traversal();

lst = list();
lst.append(1);
# lst.insert(4,2);
print(lst);
