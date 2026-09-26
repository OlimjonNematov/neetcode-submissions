class Solution:

    def encode(self, strs: List[str]) -> str:
        string_value = ""

        for string in strs:
            size=str(len(string))
            entry = size + "#" + string
            string_value+=entry

        return string_value

    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            size = ''
            while s[i] != "#":
                size+=s[i]
                i+=1
            size = int(size)
            i+=1
            res.append(s[i:i+size])
            i+=size

        return res