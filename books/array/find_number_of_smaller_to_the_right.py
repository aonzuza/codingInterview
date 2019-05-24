import bisect;

a = [3,4,9,9];

results = [];
seen = [];
for num in reversed(a):

    index = bisect.bisect_left(seen , num);
    results.insert(0,index);
    seen.insert(index,num);


a = [7,3,5];
index = bisect.bisect_left(a, 8);

print(index);
