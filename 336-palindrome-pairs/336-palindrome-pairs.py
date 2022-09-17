class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word: str) -> bool:
            for i in range(len(word) >> 1):
                if word[i] != word[~i]:
                    return False
            return True
      
        words_dict: Dict[str,int] = {word[::-1]:i for i, word in enumerate(words)}
        ans: List[List[int]] = []

        for i in range(len(words)):
            if words[i] in words_dict:
                if i != words_dict[words[i]]:
                    ans.append([i,words_dict[words[i]]])
                elif len(words[i]) and "" in words_dict:
                    ans.append([words_dict[""],i])
                    ans.append([i,words_dict[""]])
            for j in range(1,len(words[i])):
                pref = words[i][:j]
                suff = words[i][j:]
                if suff in words_dict and isPalindrome(pref): 
                        ans.append([words_dict[suff],i])
                if pref in words_dict and isPalindrome(suff):
                        ans.append([i, words_dict[pref]])
        return ans