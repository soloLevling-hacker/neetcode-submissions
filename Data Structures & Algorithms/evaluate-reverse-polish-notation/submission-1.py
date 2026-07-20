'''
Reverse Polish Notation (RPN) Evaluation
Reverse Polish Notation is a mathematical notation where every operator follows all of its operands. For example, the expression 3 + 4 is written as 3 4 +. Evaluating RPN is straightforward using a stack.

Algorithm (Stack-based)
Initialize an empty stack.
Iterate through each token in the input list:
If the token is an operator (+, -, *, /):
Pop the top two numbers from the stack (note: the first popped is the right operand, the second is the left operand).
Apply the operator.
Push the result back onto the stack.
If the token is a number (integer), push it onto the stack (convert from string to int).
After processing all tokens, the stack will contain a single element – the final result.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))

            else:
                stack.append(int(token))
        return stack.pop()