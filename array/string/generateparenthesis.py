class Solution():
    
    def generateparenthesis(self,n):
        
        match = {')':'('}
        
        value  = list(match.values())

        repeat = [value]*n
        
        

        for i in range(len(repeat)):
            
            if repeat[i] == match.values():
                
                repeat.append((match.keys()))
                
        
            final = "".join(repeat)
        
        return final
    
sol = Solution()

print(sol.generateparenthesis(3))
            
            
        
        