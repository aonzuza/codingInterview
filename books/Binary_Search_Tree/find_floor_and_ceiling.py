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

    def find_floor_ceiling(self,key):

        def _find_min_right(root):
            if not root:
                return None;
            if not root.left:
                return root.key;
            return _find_min_right(root.left);

        def _find_max_left(root):
            if not root:
                return None;
            if not root.right:
                return root.key;
            return _find_max_left(root.right);

        def _find_floor_ceiling(root,key):

            if key == root.key:
                return root;

            if key < root.key:
                return _find_floor_ceiling(root.left,key);
            if key > root.key:
                return _find_floor_ceiling(root.right,key);


        target = _find_floor_ceiling(self.root,key);

        return ( _find_max_left(target.left) , _find_min_right(target.right) );




keys = [8,3,10,6,9,20,7,25,19,25,24,30];
bst = BST();

for key in keys:
    bst.insert(key);


floor , ceiling = bst.find_floor_ceiling(3);
print(floor);
print(ceiling);

# print(bst.root.right.right.left.key);
# print(bst.root.right.key);
