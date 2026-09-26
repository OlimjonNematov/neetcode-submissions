class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()        
        
        for i,a in enumerate(nums):
            # a + b + c = 0
            if a > 0:
                break
            
            if i>0 and a == nums[i-1]:
                continue 

            p1 = i + 1
            p2 = len(nums)-1

            while p1<p2:
                threeSum = a + nums[p1] + nums[p2]

                if threeSum < 0:
                    p1+=1
                elif threeSum >0:
                    p2-=1
                else:
                    res.append([a,nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                    while nums[p1] == nums[p1-1] and p1<p2:
                        p1+=1

        return res