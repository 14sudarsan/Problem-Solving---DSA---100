class Solution:
    
    def element(self,arr,k):
        
        start = 0
        
        end = len(arr)-1
        
        
        while start <= end:
            
            mid = (start + end)//2
            
            missing = arr[mid] - (mid+1)
            
            
            if missing < k:
                
                start=mid+1
                
            else:
                
                end = mid -1
                
        return start+k
    
sol = Solution()
print(sol.element([1,2,3,4,5] ,6))