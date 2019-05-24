def advanceArray(lst):
    distance = 0;
    length = len(lst);
    for i in range(length):
        new_distance = i + lst[i];
        if new_distance > distance:
            distance = new_distance;
        if distance == i :
            break;


    return 'True' if distance >= length else 'False';


lst = [1,3,1,0,1,1,1];
result = advanceArray(lst);
print(result);
