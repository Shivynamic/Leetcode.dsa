class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        for i in words:
            ans = ""
            for j in i:
                ans+=d[ord(j)-ord("a")]
            res.append(ans)
        return len(set(res))
        