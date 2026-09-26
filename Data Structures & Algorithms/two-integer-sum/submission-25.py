class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        i=0;
        for num in nums:
            values[num] = i
            i+=1
        print(values) 
        for i in range(len(nums)):
            diff = target - nums[i]
            print(i, "---", target, '-', nums[i] ,"=", diff )
            if values.get(diff) is not None:
                # print("found", i, nums[i])
                if values.get(diff)!=i:
                    return [i, values.get(diff)]
        return []