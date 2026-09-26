class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sigs = dict()

        for s in strs:
            sig = "".join(sorted(s))
            
            if sig in sigs:
                sigs[sig].append(s)
            else:
                sigs[sig] = [s]

        return list(sigs.values())
        return sigs.values()  