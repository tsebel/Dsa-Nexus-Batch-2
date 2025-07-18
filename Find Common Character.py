class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = list(words[0])
        for word in words[1:]:
            new_common = []
            for ch in common:
                if ch in word:
                    new_common.append(ch)
                    word = word.replace(ch, '', 1) 
            common = new_common
        
        return common
   
