class Solution:

    def encode(self, strs: List[str]) -> str:
        ansStr = ""
        # join, with a delimiter
        for i,s in enumerate(strs):
            ansStr+=str(len(s))
            ansStr+="#"
            ansStr+=s            
        # return a string
        print(ansStr)
        return ansStr

    def decode(self, s: str) -> List[str]:  
        ans = []
        i = 0

        while i <len(s):
            j = i

            # get wl indices
            while s[j]!= "#":
                j+=1;
     
            wlValue = int(s[i:j])

            i = j+1
            j = i+wlValue
            ans.append(s[i:j])
            i=j
        return ans





            

