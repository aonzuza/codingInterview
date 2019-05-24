# binary tree
class Node:
    def __init__(self,_val,_left = None,_right = None):
        self.val   = _val;
        self.left  = _left;
        self.right = _right;

class BinaryTree:
    def __init__(self,_root):
        self.root = Node(_root);

    def preOrderTraversal(self,node,output,loopNumber):
        #  if node is not empty print out
        # present -> left -> right
        loopNumber +=1;
        print("call function");
        if node :
            print("---------------------------start loop No"+str(loopNumber)+"---------------------");
            print("Print only. Current node is"+ str(node.val) +"output is "+output);
            output += str(node.val) + "-";
            print("Send left.Current node is"+ str(node.val) +"output is "+output);
            output  = self.preOrderTraversal(node.left,output,loopNumber);
            print("send right.Current node is"+ str(node.val) +"output is "+output);
            output  = self.preOrderTraversal(node.right,output,loopNumber);
        print("Node is empty.Return!! loop number "+ str(loopNumber));
        return output;

    def serializeTree(self,node,traversal):

        if node is None:
            return traversal.append(-1);

        traversal.append(node.val);
        self.serializeTree(node.left,traversal);
        self.serializeTree(node.right,traversal);

    def deserializeTree(self,mylist):

        # print(int(root.left));
        if len(mylist) == 0 :
            return;
        x  = mylist.pop(0);
        if x == -1:
            root = Node(-1);
            return root;

        root = Node(x);
        root.left = self.deserializeTree(mylist);
        root.right = self.deserializeTree(mylist);
        return root;


# tree = BinaryTree(1);
#
# tree.root.left        = Node(2);
# tree.root.left.left   = Node(4);
# tree.root.left.left.left = Node(8);
# tree.root.left.left.left.left = Node(-1);
# tree.root.left.left.left.right = Node(-1);
# tree.root.left.left.right       = Node(-1);
#
# tree.root.left.right = Node(5);
# tree.root.left.right.left = Node(-1);
# tree.root.left.right.right = Node(-1);
#
# tree.root.right = Node(3);
# tree.root.right.left = Node(6)
# tree.root.right.left.left = Node(-1)
# tree.root.right.left.right = Node(-1)
#
# tree.root.right.right = Node(7)
# tree.root.right.right = Node(-1)
# tree.root.right.right = Node(-1)
#


# print(x)

# traversal = [];
# tree.serializeTree(tree.root,traversal);
# print(traversal);
mylist = [1, 2, 4, 8, -1, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1];
newTree = BinaryTree(9);
y = newTree.deserializeTree(mylist);
print(y.right.left.val);
# print(newTree.root.val);

# print(newTree.root.left.val);
# print(newTree.root.left.left.val);
# print(newTree.root.left.left.left.val);
# print(newTree.root.left.left.right.val);
#print(newTree.root.left.left.left.left.val);
# print(newTree.root.left.left.val);
# print(newTree.root.left.left.left.val);
# print(newTree.root.left.left.left.left.val);
