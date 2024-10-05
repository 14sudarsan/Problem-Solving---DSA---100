class Solution:
    
    def nandr(self , n ,r):
        
        s = str(n)
        
        
        
        sum1 = 0
        
        for i in range(len(s)):
            
            sum1 = sum1 + int(s[i])
            
        sum2 = 0
        for j in range (r):
            
            sum2 = sum2 + sum1
            
  
        
        sumarray = [int(digit) for digit in str(sum2)]
        
        final = sum(sumarray)
        
        return final     
        
      
    
sol = Solution()
print(sol.nandr(1234,2))
            
            
            
            