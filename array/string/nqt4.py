
    
class Solution:
    
    def multi(self , n):
        
        lst = list(n)
        
        product = 1
        
        for i in range(len(lst)):
            
            
            
            product = product * int(lst[i])
            
            
        return product

sol = Solution()

print(sol.multi("5244"))
    
    
    
  
        
        
        
        
        
        
        
         