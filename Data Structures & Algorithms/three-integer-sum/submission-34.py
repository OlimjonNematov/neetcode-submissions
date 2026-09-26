class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i,curr in enumerate(nums):
            if curr > 0:
                break

            if nums[i] == nums[i-1] and i> 0 :
                continue

            p1,p2 = i+1, len(nums)-1
            
            while p1<p2:
                sum = curr + nums[p1] + nums[p2]

                if sum>0:
                    p2-=1
                elif sum <0:
                    p1+=1
                else:
                    res.append([curr, nums[p1], nums[p2]])
                    p1+=1
                    p2-=1
                    while nums[p1] == nums[p1-1] and p1<p2:
                        p1+=1

        return res