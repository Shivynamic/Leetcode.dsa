class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split(" ")
        i= len(t)-1
        print(t)
        while i>=0:
            if t[i]!='':
                return len(t[i])
            
            i-=1