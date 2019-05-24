

# simple
# fn = lambda x: x + 5;
# arr = [1,2,3,4,5];
#
# results = map(fn,arr);
#
# print(results);


# take 2 params
def add(t):
   x, y, z = t
   return x+y+z;

results = map(add, [(x, y,z) for x,y,z in zip([1,2,3],[4,5,6],[7,8,9]) ])

print(results);
