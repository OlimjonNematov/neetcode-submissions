from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count all occurences
        counts = Counter(nums)
        print(counts)

        # keep track of the k most frequent
        heap=[]
        for key in counts.keys():
            print(key, counts[key])
            heapq.heappush(heap,(counts[key],key))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)
        # format and return result
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans;