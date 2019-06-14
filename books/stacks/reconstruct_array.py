class Stack:
    def __init__(self):
        self.stack = [];

    def push(self,val):
        self.stack.append(val);

    def pop(self):
        return self.stack.pop();

    def empty(self):
        return len(self.stack) == 0;

    def peek(self):
        return self.stack[-1];



def reconstruct(arr):

    stack = Stack();
    answer = [];
    length = len(arr) - 1;

    for i in range(length):

        next_sign = arr[i + 1];

        if next_sign == "-":
            stack.push(i);
        else:
            answer.append(i);
            while not stack.empty():
                answer.append(stack.pop());

    stack.push(length);

    while not stack.empty():
        answer.append(stack.pop());

    print(answer);


arr =[None,"+","-","+","-"];
print(arr);
reconstruct(arr);
