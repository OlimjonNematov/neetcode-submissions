class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = dict()

        for word in strs:
            sig="".join(sorted(word))
            if sig in signatures:
                signatures[sig].append(word)
            else:
                signatures[sig]=[word]
            ans = list(signatures.values())
        return ans

        