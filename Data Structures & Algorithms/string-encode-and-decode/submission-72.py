class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''

        for s in strs:
            ans += str(len(s))+'#'+s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i <len(s):
            size = ''
            while s[i]!='#':
                size+=s[i]
                i+=1
            i+=1
            size = int(size)
            word = s[i:i+size]
            i+=size
            ans.append(word)
            

        # move the pointer through the string, add the word to the ans
        # return ans
        return ans