class Node:
    def __init__(self,data, left = None,right = None):
        self.data  = data;
        self.left  = left;
        self.right = right;
class Tree:
    def __init__(self, data):
        self.root = Node(data);
    def inOrder(self,node):
        if node == None:
            return;
        self.inOrder(node.left);
        print(node.data);
        self.inOrder(node.right);
    def calTree(self,node):
        if node.left == None or node.right == None:
            return node.data;

        leftValue = self.calTree(node.left);
        operator  = node.data;
        rightValue = self.calTree(node.right);


        if operator == '+':
            return leftValue + rightValue;
        elif operator == '-':
            return leftValue - rightValue;
        elif operator == '*':
            return leftValue * rightValue;
        else:
            return leftValue / rightValue;



tree = Tree('*');
tree.root.left        = Node('+');
tree.root.right       = Node('+');
tree.root.left.left   = Node(3);
tree.root.left.right  = Node(2);
tree.root.right.left  = Node(4);
tree.root.right.right  = Node(5);


result = tree.calTree(tree.root);
print(result);
