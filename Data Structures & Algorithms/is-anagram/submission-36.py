class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        if(lenS!= len(t)):
            return False

        return sorted(s) == sorted(t)