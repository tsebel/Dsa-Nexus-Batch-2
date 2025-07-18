       class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = [frozenset(word) for word in words]
        count = 0
        n = len(sets)
        for i in range(n):
            for j in range(i+1, n):
                if sets[i] == sets[j]:
                    count += 1
        
        return count
      
