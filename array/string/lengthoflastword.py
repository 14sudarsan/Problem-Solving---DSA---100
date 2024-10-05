class Solution:
    
    def lengthoflastword(self,s):
        n = len(s)
        i = len(s)-1
        
        length = 0
        
        
        while s[i] == " ":
            
            
            
            i = i-1
            
        while s[i]!=" ":
            
            i = i -1
            
            length = length +1
            
            
        return length
    
sol = Solution()

print(sol.lengthoflastword("Hello World"))
        
        
        