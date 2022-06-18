class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        #iterate over each word 
        for w in range(len(words)):
            word = words[w]
            # now we will form every suffix#prefix combination and we will use it as the key for respective word
            
            for j in range(len(word)-1 , -1 , -1): # for suffix
                
                for i in range(len(word)): # for prefix
                    
                    currS = word[:i+1] + "#" + word[len(word)-j-1:]  # "prefix#suffix"
                    self.d[currS] = w        # w = index 
                

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix + "#" + suffix) not in self.d:
            return -1
        
        return self.d[(prefix + "#" + suffix)]
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)