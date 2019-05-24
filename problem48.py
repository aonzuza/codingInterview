class Node:
    def __init__(self,val,left=None,right=None):
        self.val   = val;
        self.left  = left;
        self.right = right;
class Tree:
    def __init__(self,val):
        self.root = Node(val);

    def reconstruct(self,preOrderList, inOrderList):
        if len(preOrderList) == len(inOrderList) == 1:
            return Node(preOrderList[0]);

        root = Node(preOrderList[0]);
        root_index = inOrderList.index(preOrderList[0]);

        root.left  = self.reconstruct( preOrderList[1: 1 + root_index] , inOrderList[0:root_index]);
        root.right = self.reconstruct( preOrderList[1+ root_index : ], inOrderList[1+ root_index:] );
        return root;

    def inorder(self,node):
        if node == None:
            return;
        self.inorder(node.left);
        print(node.val);
        self.inorder(node.right);

    def preorder(self,node):
        if node == None:
            return;
        print(node.val);
        self.preorder(node.left);
        self.preorder(node.right);

    def postorder(self,node):
        if node == None:
            return;
        self.postorder(node.left);
        self.postorder(node.right);
        print(node.val);


inOrderList = ['d','b','e','a','f','c','g'];
preOrderList = ['a','b','d','e','c','f','g'];

tree = Tree('x');

reconstruct_root = tree.reconstruct( preOrderList ,inOrderList);

tree.postorder(reconstruct_root);



# else:
#     print('no')

# class Node:
#     def __init__(self,val,left=None,right=None):
#         self.val   = val;
#         self.left  = left;
#         self.right = right;
#
# class Tree:
#     def __init__(self,val):
#         self.root = Node(val);
#     def inorder(self,node):
#         if node == None:
#             return;
#         self.inorder(node.left);
#         print(node.val);
#         self.inorder(node.right);
#
#     def preorder(self,node):
#         if node == None:
#             return;
#         print(node.val);
#         self.preorder(node.left);
#         self.preorder(node.right);
#
#     def createPreorderTree(self,ary,level):
#         if level == 0:
#             return;
#         val = ary.pop(0);
#         node = Node(val);
#         level -= 1;
#         node.left  = self.createPreorderTree(ary,level);
#         node.right = self.createPreorderTree(ary,level);
#         return node;
#
#     def createInorderTree(self,ary,level):
#         if level == 0:
#             return;
#         level -= 1;
#         templeft  = self.createInorderTree(ary,level);
#         val = ary.pop(0);
#         node = Node(val);
#         node.left = templeft;
#         node.right = self.createInorderTree(ary,level);
#         return node;
#
# tree = Tree('a');
# tree.root.left  =  Node('b');
# tree.root.left.left  =  Node('d');
# tree.root.left.right  =  Node('e');
# tree.root.right =  Node('c');
# tree.root.right.left =  Node('f');
# tree.root.right.right =  Node('g');
#
#
# preOrderList = ['a','b','d','e','c','f','g'];
#
# level = (len(preOrderList) - 1) / 2;
#
# newPreorderTree = tree.createPreorderTree(preOrderList,level);
#
# inOrderList = ['d','b','e','a','f','c','g'];
# newInorderTree = tree.createInorderTree(inOrderList,level);
#
# tree.inorder(newInorderTree);
