class Node:
    def __init__(self,data,left = None,right = None):
        self.data  = data;
        self.left  = left;
        self.right = right;

class Tree:
    def __init__(self,data = None):
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

# def reconstruct_tree(preorder_arr,inorder_arr):
#     # this is a leaf node
#     def _reconstructor(node,arr,pivot):
#
#         if len(arr) == 1:
#             return None;
#
#         left_arr = arr[:pivot];
#         right_arr = arr[pivot+1:];
#
#         if left_arr:
#             center_left = len(left_arr) // 2;
#             node.left = Node(left_arr[center_left]);
#             _reconstructor(node.left,left_arr,center_left);
#         if right_arr:
#             center_right = len(right_arr) // 2;
#             node.right = Node(right_arr[center_right]);
#             _reconstructor(node.right,right_arr,center_right);
#
#
#     root_val = preorder_arr[0];
#     tree  = Tree(root_val);
#     pivot = inorder_arr.index(root_val);
#     _reconstructor(tree.root,inorder_arr,pivot)
#     return tree;

def reconstruct(preorder_arr,inorder_arr):

    if not preorder_arr and not inorder_arr:
        return None;

    if len(preorder_arr) == len(inorder_arr) == 1:
        return Node(preorder_arr[0]);

    val   = preorder_arr[0];
    pivot = inorder_arr.index(val);

    node = Node(val);
    node.left = reconstruct(preorder_arr[1: pivot + 1 ], inorder_arr[0: pivot] );
    node.right = reconstruct(preorder_arr[pivot+1:] , inorder_arr[pivot+1:]);

    return node;

#
# tree                   = Tree('a');
# tree.root.left         = Node('b');
# tree.root.right        = Node('c');
#
# tree.root.left.left = Node('d');
# tree.root.left.right = Node('e');
#
# tree.root.right.left = Node('f');
# tree.root.right.right = Node('g');
#
# tree.preOrderTraversal(tree.root);
# print('-------------------------');
# tree.inorderTraversal(tree.root);

preorder_arr = ['a','c','f','g'];

inorder_arr  = ['a','f','c','g'];


tree = Tree();
tree.root = reconstruct(preorder_arr,inorder_arr);

# tree.inorderTraversal(tree.root);

print(tree.root.right.right .data);
