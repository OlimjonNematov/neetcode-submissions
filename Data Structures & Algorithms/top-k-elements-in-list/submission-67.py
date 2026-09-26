class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        # save the count for every number 
        for num in nums:
            count[num] = 1 + count.get(num,0)

        # sort all the counts
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        ans = []
        # pop the top k counts
        for i in range(0,k):
            ans.append(arr.pop()[1])
        return ans