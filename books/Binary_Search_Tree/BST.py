class Node:

    def __init__(self,key,left=None,right=None):
        self.key = key;
        self.left = left;
        self.right = right;



class BST:
    def __init__(self):
        self.root = None;

    def insert(self,key):

        def _insert(root,key):
            if not root:
                return Node(key);

            if key < root.key:
                root.left = _insert(root.left,key);
            if key > root.key:
                root.right = _insert(root.right,key);

            return root;

        self.root = _insert(self.root,key);

    def find(self,key):

        def _find(root,key):

            if not root:
                return False;
            if key == root.key:
                return True;
            elif key < root.key:
                return _find(root.left,key);
            else:
                return _find(root.right,key);

        return _find(self.root,key);

    def delete(self,key):

        def _find_min_right(root):
            if not root.left:
                return root;

            return _find_min_right(root.left);

        def _delete(root,key):

            if key == root.key:

                if not root.left and not root.right:
                    return None;
                elif root.left and not root.right:
                    root.key , root.left.key = root.left.key , root.key;
                    root.left = _delete(root.left,key);
                    return root;
                elif not root.left and root.right:
                    root.key , root.right.key = root.right.key , root.key;
                    root.right = _delete(root.right,key);
                    return root;
                else:
                    # left and right;
                    min_right_node = _find_min_right(root.right);
                    root.key, min_right_node.key = min_right_node.key, root.key;
                    root.right = _delete(root.right ,key);
                    return root;

            if key < root.key:
                root.left = _delete(root.left,key);
            if key > root.key:
                root.right = _delete(root.right,key);

            return root;

        self.root = _delete(self.root,key);




keys = [8,3,10,1,6,9,20,4,7,25,19,25,24,30];
bst = BST();

for key in keys:
    bst.insert(key);

print(bst.root.right.right.right.left.right.key);
bst.delete(20);
print('--------------------');
print(bst.root.right.right.key);
# print(bst.root.right.right.left.key);
# print(bst.root.right.key);






















































#
# class Node:
#     def __init__(self,key,left = None,right = None):
#         self.key   = key;
#         self.left  = left;
#         self.right = right;
#
#
# class BST:
#     def __init__(self):
#         self.root = None;
#
#     def insert(self,key):
#
#         def _insert(root,key):
#             if not root:
#                 return Node(key);
#             #go left
#             if key < root.key:
#                 root.left = _insert(root.left,key);
#             if key > root.key:
#                 root.right = _insert(root.right,key);
#             return root;
#
#         self.root = _insert(self.root,key);
#
#     def find(self,key):
#
#         def _find(root,key):
#             if not root:
#                 return False;
#             if key == root.key:
#                 return True;
#
#             if key < root.key:
#                 return _find(root.left,key);
#             else:
#                 return _find(root.right,key);
#
#
#         return _find(self.root,key);
#
#     def delete(self,key):
#
#         def _find_min_right(node):
#             if not node.left:
#                 return node;
#             return _find_min_right(node.left);
#
#         def _delete(node,key):
#
#             if key == node.key:
#                 # start deleting process
#                 if not node.left and not node.right:
#                     return None;
#                 if node.left and not node.right:
#                     node.key , node.left.key = node.left.key , node.key;
#                     node.left = _delete(node.left,key);
#                     return node;
#                 if not node.left and node.right:
#                     node.key , node.right.key = node.right.key , node.key;
#                     node.right = _delete(node.right,key);
#                     return node;
#                 if node.left and node.right:
#                     min_right_node = _find_min_right(node.right);
#                     node.key , min_right_node.key = min_right_node.key,node.key;
#                     node.right = _delete(node.right,key);
#                     return node;
#             if key < node.key:
#                 node.right = _delete(node.left,key);
#             if key > node.key:
#                 node.left  = _delete(node.right,key);
#
#             return node;
#
#         self.root = _delete(self.root,key);
#         return self.root;


    # def insert(self,key):
    #
    #     def _insert(root,key):
    #
    #         if not root:
    #             return Node(key);
    #
    #         # go left
    #         if key < root.key:
    #             root.left = _insert(root.left,key);
    #         if key > root.key:
    #             root.right = _insert(root.right,key);
    #
    #         return root;
    #
    #
    #
    #     self.root = _insert(self.root,key);



# lst = [11,5,15,13,30,29,25,26];
# bst = BST();
#
# for key in lst:
#     bst.insert(key);
#
# # bst
# print(bst.root.right.key);
# #
# bst.delete(15);
# print(bst.root.right.key);

# print(bst.find(-1));
