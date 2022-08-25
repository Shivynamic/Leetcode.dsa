class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rad = collections.Counter(ransomNote)
        mad = collections.Counter(magazine)
        for i in rad:
            if i not in mad or mad[i]<rad[i]:
                return False
        return True