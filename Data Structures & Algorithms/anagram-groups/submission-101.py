from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep track of signatures
        ans = defaultdict(list)

        # loop through each str, add to sig dict
        for s in strs:
            sig = "".join(sorted(s))
            ans[sig].append(s)

        return list(ans.values())