#correct Solution
class Solution:
    
    def check(self,s):
        
        stack = []
        
        
        for i in range(len(s)):
            
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                
                stack.append(s[i])
                
            else:
                
                if not stack:
                    
                    return False
                
                char = stack.pop()
                
                if s[i]==")"and char == "(" or s[i]=="}" and char == "{" or s[i]=="]" and char =="[":
                    
                    pass
                
                else:
                    
                    
                    return False
                
        if len(stack)==0:
            
            return "Pairs Matched"
        
        else:
            
            return False
    
    
sol = Solution()
print(sol.check("[()[{()}]]"))