class Solution:
    
    def check(self,arr):
        
        i = 0
        
        misunderstood = 0
        
        for j in range(1,len(arr)):
            
            if arr[i]!= arr[j]:
                
                misunderstood = misunderstood+1
                
                
        return misunderstood
    
    
sol = Solution()
print(sol.check([1,2,3,2,2]))
                
                