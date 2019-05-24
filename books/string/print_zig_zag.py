

def print_zig_zag(string,k):


    for rowIndex in range(k):

        selectedCol = rowIndex;
        line = [" " for _ in string ];

        while selectedCol < len(string):

            line[selectedCol] = string[selectedCol];
            desc = is_descending(selectedCol, k );
            next_position = get_spaces(rowIndex,desc,k);
            selectedCol = selectedCol + next_position + 1;

        print("".join(line));



def get_spaces(rowIndex , desc, k):

    max_spaces =  ((k -1) * 2 ) - 1;

    if desc:
        spaces = max_spaces - ( rowIndex * 2);
    else:
        spaces = max_spaces - ( k - 1  - rowIndex) * 2;
    return spaces;


def is_descending(colIndex,k):

    return colIndex % (2 * (k-1)) < (k-1);



def print_zig_zag_2(string,k):

    lst = [x[:] for x in [ [' '] * len(string)] * k ]
    col = 0;
    row = 0;
    goingDown = True;
    while col < len(string):
        lst[row][col] = string[col];

        if goingDown:
            row = row + 1;
        else:
            row = row -1;

        if row == k - 1:
            goingDown  = False;
        elif row == 0:
            goingDown = True;

        col +=1;

    for row in lst:
        print("".join(row));


string = "thisisazigzag";
k = 2;
print_zig_zag_2(string,k);
