class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                res = stack.pop() + stack.pop()
                stack.append(int(res))
            elif char == '-':
                min_by = stack.pop()
                res = stack.pop() - min_by
                stack.append(int(res))
            elif char == '/':
                div_by = stack.pop()
                res = float(stack.pop()) / div_by
                stack.append(int(res))
            elif char == '*':
                res = stack.pop()*stack.pop()
                stack.append(int(res))
            else:
                stack.append(int(char))

        return stack.pop()