class Solution:
    def interpret(self, s: str) -> str:
        i  = 0
        ans = []
        
        while i < len(s):

            if s[i] == "G":
                ans.append("G")
                i += 1
            elif s[i] == "(" and s[i+1] == ")":
                ans.append("o")
                i += 2
            elif s[i] == "(" and s[i+1] == "a":
                ans.append("al")
                i += 4
            
        return "".join(ans)
