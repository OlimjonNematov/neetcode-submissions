from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counts = Counter(nums)
        
        heap = []

        for value, count in counts.items():
            heapq.heappush(heap, (count, value))
            if len(heap) > k:
                heapq.heappop(heap)
            
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans
