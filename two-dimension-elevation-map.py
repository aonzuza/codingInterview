def calWaterUnits(lst):
    leftIndex = 0;
    leftHeight = 0;
    total = 0;
    sumR = 0;
    for rightIndex,rightHeight in enumerate(lst):

        if rightHeight >= leftHeight:
            # find an area
            area  = (rightIndex - leftIndex) * min(leftHeight,rightHeight);

            area  = area - sumR;
            total = total + area;

            #  commit area
            leftIndex = rightIndex;
            leftHeight = rightHeight;

            sumR = rightHeight;
        else:
            sumR += rightHeight;


        if rightIndex == (len(lst) - 1) and rightHeight < leftHeight:
            diffHeight = leftHeight - rightHeight;
            sumR  = sumR - diffHeight - rightHeight;

            area = rightHeight * (rightIndex - leftIndex);
            area  = area - sumR;
            area  = area if area > 0 else 0;
            total = total + area;
    return total;


lst = [3,0,2,1,2,0,1];

result = calWaterUnits(lst);
print(result);
