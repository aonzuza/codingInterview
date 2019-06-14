class Stack:
    def __init__(self):
        self.stack = [];

    def push(self,val):
        self.stack.append(val);

    def pop(self):
        return self.stack.pop();

    def peek(self):
        return self.stack[-1];

class BalancedBracket:
    def __init__(self):
        self.stack = Stack();

    def isBalanced(self,brackets):


        for bracket in brackets:

            if bracket in ["{","[","("]:
                self.stack.push(bracket);
            else:
                openBracket = self.stack.pop();
                if bracket == "}" and openBracket != "{" \
                or bracket == "]" and openBracket != "[" \
                or bracket == ")" and openBracket != "(":
                    return False;

        return True;

bb = BalancedBracket();
isBalanced = bb.isBalanced("([}])");
print(isBalanced);
