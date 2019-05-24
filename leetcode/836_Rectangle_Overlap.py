


def isRectangleOverlap(rect1,rect2):
    x1 = rect1[0];
    y1 = rect1[1];
    x2 = rect1[2];
    y2 = rect1[3];

    x3 = rect2[0];
    y3 = rect2[1];
    x4 = rect2[2];
    y4 = rect2[3];


    if x1 < x4 < x2 and  y1 < y4 < y2:
        return True;
    elif  x1 < x3 < x2 and  y1 < y4 < y2:
        return True;
    elif x1 < x4 < x2 and  y1 < y3 < y2:
        return True;
    elif x1 < x3 < x2 and  y1 < y3 < y2:
        return True;

    return False;


rect1 = [0,0,1,1];
rect2 = [1,0,2,1];

isOverlap = isRectangleOverlap(rect1,rect2);

print(str(isOverlap));
