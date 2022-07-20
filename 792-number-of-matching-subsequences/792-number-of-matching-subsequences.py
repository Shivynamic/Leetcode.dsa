from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(lambda: deque([]))
        for word in words:
            buckets[word[0]].append(word)
        
        answer = 0
        for c in s:
            for i in range(len(buckets[c])):
                word = buckets[c].popleft()
                # last character
                if len(word) == 1:
                    answer += 1
                    continue
                
                buckets[word[1]].append(word[1:])
                
        return answer