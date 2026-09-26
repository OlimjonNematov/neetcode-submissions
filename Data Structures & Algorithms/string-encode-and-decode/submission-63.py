class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        
        for s in strs:
            l = len(s)
            ans+=str(l)
            ans+="#"
            ans+=s

        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans=[] 
        
        while i<len(s):
            j = i
            # first extract length as int
            while s[j]!="#":
                j+=1
            
            wl = int(s[i:j])

            # set i and j

            i = j + 1
            j = i + wl

            # extract the string and append to ans
            ans.append(s[i:j])
            i = j 


        return ans