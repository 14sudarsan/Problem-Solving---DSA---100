class Solution:
    
    def prefixcheck(self,arr):
        
        n = len(arr)
        
        i = 0
        
        length = 0
        
        while i < n:
            
            if i == 0 or arr[i]>arr[i-1]:
                
                length = length +1
                
            
                
            i = i+1
            
        return length
            
            
    
sol = Solution()

print(sol.prefixcheck([5,3,4,5,8,9]))