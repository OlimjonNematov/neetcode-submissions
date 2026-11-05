from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep track of sigs
        ans = defaultdict(list)

        # loop thorugh each str in strs
        for s in strs:
            sig = "".join(sorted(s))
            # add to respective sig
            ans[sig].append(s)        
        
        return list(ans.values())
