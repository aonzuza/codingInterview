# recursive function
def factorial(n):
    if n > 1 :
        return n * factorial(n-1);
    return 1;


x = 5;

y = factorial(3);

print(y);

#     def preOrder(self):
#
#         if self


# root = Node(1);
#
# print(root.val);

#
# class Dog:
#     def __init__(self,_name,_age = 15):
#         self.name = _name;
#         self.age  = _age;
#         self.walk = 1;
#     def walkSpeed(self):
#         return 99;
# class York:
#     def __init__(self,_name):
#         self.dog =  Dog(_name);
#
# bill = York("Bill");
# print(bill.dog.name);
# print(bill.dog.age);
# print(bill.dog.walkSpeed());
