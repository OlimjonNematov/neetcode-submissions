from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return as list
        ans = []
        counts = Counter(nums)

        # keep count of most frequent k elements
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, [counts[num],num])
            if len(heap)>k:
                heapq.heappop(heap)

        # format as array 
        print(heap)
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans;
