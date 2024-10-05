class Solution:
    
    def possible(self,arr,day,m,k):
        
        bouquets = 0
        
        count = 0
        for i in range(0,len(arr)):
            
            if arr[i] <= day:
                
                count = count+1
                
            else:
                
                bouquets = bouquets + (count//k)
                
                count = 0
                
        bouquets = bouquets + (count//k)
        
        
        if bouquets >= m:
            
            return True
        else:
            
            return False
        
    def binarySearch(self,arr, m , k):
        
        start = min(arr)
        
        end = max(arr)
        
        while start <= end:
        
            mid = start + (end - start)//2
        
        
            check = self.possible(arr,mid,m,k)
        
        
            if check  == True:
            
                end = mid -1
            
            else:
            
                start = mid+1
            
        return start
    
sol = Solution()
arr = [7,7,7,7,13,11,12,7]
print(sol.binarySearch(arr,2,3))
            
            
                
        
                
        
        
                
                
                
                