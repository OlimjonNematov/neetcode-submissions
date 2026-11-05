class Solution:

    def encode(self, strs: List[str]) -> str:
        value = ""
        for s in strs:
            value += str(len(s)) + "#" + s
        return value

    def decode(self, s: str) -> List[str]: 
        ans = []

        # track pointer
        p1 = 0

        while p1<len(s):
            size = ''
            while s[p1]!= "#":
                size += s[p1]
                p1+=1

            size = int(size)
            p1+=1
            ans.append(s[p1:p1+size])
            p1+=size
        # start pointer past #, use len to get word, take that substring, add to ans
        return ans