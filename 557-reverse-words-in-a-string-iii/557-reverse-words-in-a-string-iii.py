class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        out = ""
        for i in t:
            a = i[::-1]
            out+= a +" "
        return out[:-1]
        