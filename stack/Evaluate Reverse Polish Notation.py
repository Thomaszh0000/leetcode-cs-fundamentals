from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        time complexity : O(n)
        space complexity : O(n)
        problem : https://leetcode.com/problems/evaluate-reverse-polish-notation/
        approach : 
        Create an array stack.
        Use a for-loop, for token in tokens, if token is any of +-*/, 
        pop out stack[-1] and stack[-2] and append stack[-2] operate (depends on which operator token is) stack[-1]; 
        if token is a number, append it to stack.
        Finally, return stack[-1].
        """
        stack = []
        for token in tokens:
            if token in "+-*/":
                b, a = int(stack.pop()), int(stack.pop())
                if token == "+":
                    stack.append(a + b)
                if token == "-":
                    stack.append(a - b)
                if token == "*":
                    stack.append(a * b)
                if token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[-1]
