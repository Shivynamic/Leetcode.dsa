class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        re = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!= strs[0][i]:
                    return re
            re += strs[0][i]
            
        return re
        