class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1;
        zeroCount = 0;

        for num in nums:
            if num == 0:
                zeroCount+=1
            else:
                totalProduct*=num

        res=[0]*len(nums)

        # if >1 zeroes, all will be 0
        if zeroCount>1:
            return res

        for i in range(len(nums)):
            if zeroCount==1 and nums[i]!= 0:
                res[i]=0
            elif nums[i]!= 0:
                print(str(totalProduct)+'-'+ str(nums[i]))
                res[i]=int(totalProduct/nums[i])
            else:
                res[i] = totalProduct

        return res;