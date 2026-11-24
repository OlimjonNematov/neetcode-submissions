class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            comp = target - value
            if comp in seen:
                return [seen[comp], index]
            seen[value] = index
        return 