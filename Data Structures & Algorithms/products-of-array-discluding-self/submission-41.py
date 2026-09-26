class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate through each num
        lProd=[] # [[2,4,6],[1,4,6],[1,2,4]]
        for num in nums:
            numCopy=nums[:]
            numCopy.remove(num)
            lProd.append(numCopy)
        res =[]
        i=0
        for i in range(len(lProd)):
            prod = 1
            for e in lProd[i]:
                prod*=e
            print(prod)
            res.append(prod)
            i+=1
        
        return res;