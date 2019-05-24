class Node():
    def __init__(self,val,left = None,right = None):

        self.val   = val;
        self.left  = left;
        self.right = right;

class Tree():
    def __init__(self,val):
        self.root = Node(val);



    def find_all_path_to_leaf(self):
        ans = [];
        path = [];

        def helper(root,path,ans):

            if root.left == root.right == None:
                path.append(root.val);
                ans.append(path);
                return;
            path.append(root.val);
            helper(root.left  , path[:] ,ans);
            helper(root.right , path[:] ,ans);
        # -------------- calling the helper---------------
        helper(self.root,path,ans);
        return ans;

tree = Tree(1);
tree.root.left  = Node(2);
tree.root.right = Node(3);
tree.root.left.left  = Node(4);
tree.root.left.right  = Node(5);

paths = tree.find_all_path_to_leaf();
print(paths);
