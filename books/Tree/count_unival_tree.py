class Node:
    def __init__(self,data,left = None,right = None):
        self.val  = data;
        self.left  = left;
        self.right = right;

class Tree:
    def __init__(self,data):
        self.root = Node(data);

    def count_unival(self,root):

        def _count_unival(node):
            if not node:
                return (True ,0);

            left_unival,total_left = _count_unival(node.left);
            right_unival,total_right = _count_unival(node.right);
            total_unival = total_left + total_right;

            if left_unival and right_unival:
                if node.left and node.left.val !=node.val:
                    return (False,total_unival);
                if node.right and node.right.val !=node.val:
                    return (False,total_unival);
                return True,total_unival + 1;


            return (False , total_unival);


        isUnival, totalUnival = _count_unival(self.root);

        return totalUnival;

tree                   = Tree(0);
tree.root.left         = Node(1);
tree.root.right        = Node(0);
tree.root.right.left   = Node(1);
tree.root.right.right    = Node(0);

tree.root.right.left.left = Node(1);
tree.root.right.left.right = Node(1);

total = tree.count_unival(tree.root);
print(total);
