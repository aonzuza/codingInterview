class Stack:
    def __init__(self):
        self.stack = [];

    def push(self,val):
        self.stack.append(val);

    def pop(self):
        return self.stack.pop();

    def peek(self):
        return self.stack[-1];

class MaxStack:
    def __init__(self):
        self.stack = [];
        self.maxes = [];

    def push(self,val):

        if not self.maxes:
            self.maxes.append(val);
        else:
            self.maxes.append( max(self.maxes[-1],val) );

        self.stack.append(val);

    def pop(self):
        if self.maxes:
            self.maxes.pop();
        return self.stack.pop();

    def max(self):
        return self.maxes[-1];

mstk = MaxStack();
mstk.push(10);
mstk.push(2);
mstk.push(15);
mstk.push(4);
mstk.push(5);

print(mstk.stack);
print(mstk.maxes);

print(mstk.pop());
print(mstk.max());

print(mstk.pop());
print(mstk.max());

print(mstk.pop());
print(mstk.max());

print(mstk.pop());
print(mstk.max());

print(mstk.pop());
print(mstk.max());
