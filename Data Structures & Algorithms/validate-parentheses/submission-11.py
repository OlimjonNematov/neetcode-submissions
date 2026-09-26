class Solution:
    def isValid(self, s: str) -> bool:
        ans = False
        # create a stack 
        stack = []
        # map the close
        close_map = {')':'(', ']':'[','}':'{'}

        for i,char in enumerate(s):
            if char in close_map:
                if stack and close_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) ==0