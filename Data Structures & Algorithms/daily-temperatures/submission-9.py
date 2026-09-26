class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # [temp, i]

        for i, temp in enumerate(temperatures):
            # if there is a day that is waiting in stack that is less than temp
            while stack and stack[-1][0] < temp:
                t, j = stack.pop()
                result[j] = i-j
            
            stack.append([temp,i])

        return result