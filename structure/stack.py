class Stack:
    def __init__(self):
        self.stack = [];
    def push(self,val):
        self.stack.append(val);
    def pop(self):
        self.stack.pop(-1);
    def show(self):

        for i in range(len(self.stack) - 1, -1 , -1 ):
            print(self.stack[i]);
    def count(self):
        return len(self.stack);

stack = Stack();
stack.push('a');
stack.push('b');
stack.push('c');
stack.push('d');
stack.push('e');

print(stack.count());
