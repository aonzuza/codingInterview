
class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data;
        self.left = left;
        self.right = right;


def construc_bst(n):


    def _construct(low,high):

        trees = [];

        if low > high:
            trees.append(None);
            return trees;

        for pivot in range(low,high+1):
            left_nodes = _construct(low, pivot -1);
            right_nodes = _construct(pivot+1,high);

            for left_node in left_nodes:
                for right_node in right_nodes:
                    node = Node(pivot,left = left_node,right = right_node);
                    trees.append(node);
        return trees;


    return _construct(1,n);

def preorder_traversal(root):
    result = []
    if root:
        result.append(root.data);
        result = result + preorder_traversal(root.left);
        result = result + preorder_traversal(root.right);
    return result;

n = 3;
trees = construc_bst(n);
# results = []
for tree in trees:
    print(preorder_traversal(tree));
    print('----------------');
