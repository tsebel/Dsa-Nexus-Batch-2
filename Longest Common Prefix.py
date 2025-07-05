class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Loop through characters of the first word
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                # If i is out of bounds or mismatch, return prefix
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        
        return strs[0]
