from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the given list of tokens representing a reverse Polish notation (RPN) expression.
        
        Reverse Polish Notation (RPN) is a mathematical notation in which every operator follows all of its operands.
        
        Supported operators are '+', '-', '*', and '/'.
        
        Time Complexity: O(n)
        - The algorithm iterates through each token in the list once.
        
        Space Complexity: O(n)
        - The stack holds at most n/2 elements in the worst case, where n is the number of tokens.
        
        Intuition:
        - The solution utilizes a stack to evaluate the RPN expression.
        - Whenever an operator is encountered, the top two operands are popped from the stack, the operation is applied, and the result is pushed back onto the stack.
        - This process continues until all tokens are processed, resulting in the final result left on the stack.
        """
        stack = []
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](x, y))
            else:
                stack.append(int(token))

        return stack[-1]
