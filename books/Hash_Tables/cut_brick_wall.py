from collections import defaultdict;


def find_min_cut(wall):

    dd = defaultdict(int);
    selected_length = 0;

    for row in wall:

        length = 0;

        for brick in row[:-1]:
            length = length + brick;
            dd[length] = dd[length] + 1;

    return len(wall) - max(dd.values());




wall = [ [3,5,1,1], [2,3,3,2] , [5,5] , [4,4,2] , [1,3,3,3] , [1,1,6,1,1] ]
# selected_col = 0;
total_cut = find_min_cut(wall);
print(total_cut);
