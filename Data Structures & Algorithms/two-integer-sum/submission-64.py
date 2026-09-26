class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i,num in enumerate(nums):
            goal = target - num
            if goal in seen:
                return [nums.index(goal),i]
            seen[num]=i
            