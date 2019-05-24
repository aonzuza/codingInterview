def index_traveler(arr):

    finish_line = len(arr) - 1;
    current_index = 0;
    furthest_index = 0;
    for index,val in enumerate(arr):

        current_index = index + val;
        if current_index > furthest_index:
            furthest_index = current_index

        if index >= furthest_index and furthest_index != finish_line:
            return False;
    return True;


inputs = [3,3,0,0,5,0,0,1];
#  1 0 1 return false

can_finish = index_traveler(inputs);

print(can_finish);
