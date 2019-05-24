def cons(a,b):
    def pair(f):
        return f(a,b);
    return pair;
#
def car(pair):
    input = lambda a,b : a;
    return pair(input);
def cdr(pair):
    input = lambda a,b : b;
    return pair(input);
#
#
# # x is pair
# # piar is a function of which input is another function that take two parameters
#pair = cons(9,10); # pair =  f(a,b)
#print(car(pair));

# y = car(pair);
#
# print(y);


# map
# x = [10,15,20,11,13];
#
#
# y = map(lambda i: i *2, x);

# print(list(y));

#  lambda
# x = lambda a, b : a * b;
# y = x(5,6);
#
# print(y);


#
#
#  Python Closures
# def dog(price):
#
#     def findPrice(vat):
#         return price * vat;
#     return findPrice;
#
#
# x = dog(1000);
# price = x(1.5);
# #
# print(price);
