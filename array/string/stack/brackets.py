class Solution:
    
    def brackets(self,s):
        
        stack = []
        
        match = {')':'(' , ']':'[' , '}':'{'}
        
        
        for braclet in s:
            
            if braclet in match.values():
                
                stack.append(braclet)
                
            elif braclet in match.keys():
                
                if stack==[] or match[braclet] != stack.pop():
                    
                    
                    return False
                
            else:
                
                continue
        
        if stack == []:
            
            return True
        
sol = Solution()

print(sol.brackets("{[()]}"))
                
                
        
        
        