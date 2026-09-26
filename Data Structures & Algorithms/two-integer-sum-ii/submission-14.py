class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []

        for index in range(len(numbers)-1):
            if target-numbers[index] in numbers:
                return [index+1, numbers.index(target-numbers[index])+1]

        return res