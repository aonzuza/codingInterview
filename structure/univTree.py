class Node:
    def __init__(self,data,left = None,right = None):
        self.data  = data;
        self.left  = left;
        self.right = right;

class Tree:
    def __init__(self,data):
        self.root = Node(data);
    def inorderTraversal(self, root):
        if root == None:
            return;
        self.inorderTraversal(root.left);
        print(root.data);
        self.inorderTraversal(root.right);
    def preOrderTraversal(self,root):
        if root == None:
            return;
        print(root.data);
        self.preOrderTraversal(root.left);
        self.preOrderTraversal(root.right);
    def postOrderTraversal(self,root):
        if root == None:
            return;
        self.postOrderTraversal(root.left);
        self.postOrderTraversal(root.right);
        print(root.data);

    def isUnival(self,root):
        def helper(root,value):
            if root == None:
                return True;
            if root.data == value:
                isLeftUnival  = helper(root.left, value);
                isRightUnival = helper(root.right,value);
                if isLeftUnival and isRightUnival:
                    return True;
            return False;
        return helper(root,root.data);

    def countUnival(self,root):
        def helper(root):
            if root == None:
                return 0;
            left  = self.countUnival(root.left);
            right = self.countUnival(root.right);
            if self.isUnival(root):
                return 1 + left + right;
            else:
                return left + right;

        return helper(root);

    def countUnival_2(self,root):
        def helper(root):
            if root == None:
                return 0,True;
            totalLeft , isLeftUnival  = helper(root.left);
            totalRight, isRightUnival = helper(root.right);
            if isLeftUnival and isRightUnival:
                if root.left != None and root.left.data != root.data:
                    return totalLeft + totalRight, False;
                if root.right != None and root.right.data != root.data:
                    return totalLeft + totalRight, False;
                return 1 + totalLeft + totalRight , True;
            return totalLeft + totalRight, False;

        totalUnival,_ = helper(root);
        return totalUnival;



tree                   = Tree(1);
tree.root.left         = Node(2);
tree.root.right        = Node(3);
tree.root.right.left   = Node(4);
tree.root.right.right    = Node(5);
total = tree.countUnival_2(tree.root);
print(total);
