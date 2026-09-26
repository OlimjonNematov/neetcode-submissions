from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        while r < len(nums):
            
            # remove smaller values from our deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # evict old maximum
            if l > q[0]:
                q.popleft()

            # add max output if we have reached a valid size
            if r +1 >= k:
                res.append(nums[q[0]])
                l+=1   
            r += 1

        return res
