from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # indecies
        l = r = 0
        res = []

        while r < len(nums):
            
            # maintain deque as record of largest values in the array
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # evit any old maximas
            if l > q[0]:
                q.popleft()
            
            # append local maxima
            if r + 1 >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1

        return res
