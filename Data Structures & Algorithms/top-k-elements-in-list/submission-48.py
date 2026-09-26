class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cm = dict()
        for num in nums:
            if cm.get(num) is not None:
                cm[num]+=1
            else:
                cm[num]=1

        print(cm)
        sortedKeys = sorted(cm, key=cm.get);
        print(sortedKeys)
        i=len(sortedKeys)
        res=[]
        while i>0 and len(res)<k:  
            print(i)
            res.append(sortedKeys[(i-1)]);
            i-=1;
        return res