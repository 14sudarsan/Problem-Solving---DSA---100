class Solution:
    def smallestdivisor(self,arr,target):
        
        import math
        
        start = min(arr)
        
        end  = max(arr)
        
        
        total = 0
        
        while start <= end:
            
            
            mid = start+(end - start)
            
            for x in arr:
                
                total = total + math.ceil(x//mid)
                
                
            if total <= target:
                
                end = mid-1
                
            else:
                
                start = mid +1
        
        return start
    
sol = Solution()
print(sol.smallestdivisor([1,2,5,9],6))