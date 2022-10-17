class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        t = "abcdefghijklmnopqrstuvwxyz"
        
        for i in t:
            if i not in sentence:
                return False
        return True
        