import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        factors_map = {}

        # for each entry
        i = 0
        while i < len(nums):
            list_for_num = nums[:i] + nums [i+1:len(nums)]
            factors_map[i] = list_for_num
            i+=1

        for value in factors_map.values():
            ans.append(math.prod(value))

        return ans