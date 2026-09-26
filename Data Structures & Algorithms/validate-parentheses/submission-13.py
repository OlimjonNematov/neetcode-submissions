class Solution:
    def isValid(self, s: str) -> bool:
        res = False
        stack = []

        close_map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in close_map:
                if stack and stack[-1] == close_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
