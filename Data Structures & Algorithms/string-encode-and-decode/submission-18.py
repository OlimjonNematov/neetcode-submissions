class Solution:

    def encode(self, strs: List[str]) -> str:
        # attach the length + delimeter, attatch it all into 
        e = ""

        for s in strs:
            e+=str(len(s))+"|"+s
    
        print(e);
        return e

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i in range(len(s)):
            print(i)
            wl = ''
            while s[i] != "|":
                wl += s[i]
                i += 1
            i+=1
            print(wl)
            wlInt = int(wl);
            word = s[i:i+wlInt]
            i+=wlInt
            res.append(word)


        return res
