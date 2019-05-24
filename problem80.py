class Node:
    def __init__(self, _val, _left = None,_right = None):
        self.val   = _val;
        self.left  = _left;
        self.right = _right;

class Tree:
    dict = {};
    def __init__(self,_val):
        self.root = Node(_val);

    def inorderTraversal(self,node):
        if node == None:
            return;
        self.inorderTraversal(node.left);
        print(node.val);
        self.inorderTraversal(node.right);

    def findLeaves(self,node,counter):
        counter +=1;
        if node.left == None and node.right == None:
            # print('counter is ' + str(counter));
            # print('valus is ' + str(node.val));
            # return (counter ,node.val);
            self.dict[counter] = node.val;

        if node.left != None:
            self.findLeaves(node.left,counter);
        if node.right != None:
            self.findLeaves(node.right,counter);


tree = Tree(3);
tree.root.left  = Node(4);
tree.root.left.left = Node(6);
tree.root.left.right = Node(7);
tree.root.right = Node(5);
tree.root.right.right = Node(8);
tree.root.right.right.right = Node(9);

# tree.inorderTraversal(tree.root);
tree.findLeaves(tree.root, 0);

maxLevel = max(tree.dict, key = tree.dict.get);
print(tree.dict[maxLevel]);
# print(tree.dict);
