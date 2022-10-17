class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26
    
        
#         t = "abcdefghijklmnopqrstuvwxyz"
        
#         for i in t:
#             if i not in sentence:
#                 return False
#         return True
        