from collections import deque,defaultdict;


class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data;
        self.left = left;
        self.right = right;

def smallest_level_2(q ,current_level ,level ,min_sum):

    if not q:
        return level;

    new_q = deque([]);
    current_level = current_level + 1;
    sum = 0;
    while q:
            node = q.popleft();

            if node.left:
                new_q.append(node.left);
                sum = sum + node.left.data;
            if node.right:
                new_q.append(node.right);
                sum = sum + node.right.data;
    if sum < min_sum:
        min_sum = sum;
        level = current_level;
    return smallest_level(new_q,current_level,level,min_sum);


def smallest_level(root):

    q = deque([]);
    hash_table = defaultdict(int);
    q.append((root , 0));
    print(type((root,0 )));
    while q:

        node , current_level = q.popleft();


        hash_table[current_level] = hash_table[current_level] + node.data;
        if node.left:
            q.append((node.left,current_level+1));
        if node.right:
            q.append((node.right,current_level+1));

    return min(hash_table,key = hash_table.get);





node = Node(3);

node.left = Node(-19);
# node.right = Node(3);

node.left.left = Node(4);
node.left.right = Node(-100);
# node.right.left = Node(6);
# node.right.right = Node(-40);


level = smallest_level(node);
print(level);
