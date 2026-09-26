class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i,num in enumerate(nums):
            reverseTarget = target-num
            if reverseTarget in seen:
                return [seen[reverseTarget],i]
            
            seen[num]=i 