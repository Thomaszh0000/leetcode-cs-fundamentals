class MinStack:
    """
    time complexity : O(1) for each operation
    space complexity : O(n)
    problem : https://leetcode.com/problems/min-stack/
    approach :
    1. __init__(self) :
    Declare self.minV as [float('inf')] (keep track of minimum of subarray for each element up to the current position) and self.stack as [].
    2. push(self, value: int):
    append value to the end of stach and append min(self.minV[-1], value) to the end of self.minV.
    3. pop(self):
    pop out self.minV and return self.stack.pop()
    4. top(self):
    return self.stack[-1]
    5. getMin(self):
    return self.minV[-1]
    """
    def __init__(self):
        self.minV = [float('inf')]
        self.stack = []
    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minV.append(min(self.minV[-1], value))
    def pop(self) -> None:
        self.minV.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minV[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
