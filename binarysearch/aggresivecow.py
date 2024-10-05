class Solution:
    
    def maximum_of_min_possible(self,arr,distance,days):
        
        cow = 1
        last = arr[0]
        
        for i in range(1,len(arr)):
            
            if arr[i]-last >= distance:
                
                cow = cow+1
                
                last = arr[i]
                
                
                
                
                
        if cow >= days:
                
                return True
            
        else:
                return False
            
    def binarysearch(self,arr,days):
        
        arr.sort()
        
        start = 0
        
        end = max(arr) - min(arr)
        
        
        while start <= end:
            
            mid = start + (end-start)//2
            
            
            minidistance = self.maximum_of_min_possible(arr,mid,days)
            
            
            if minidistance == True:
                
                start = mid +1
                
            else:
                
                end = mid -1
                
        return end
    
sol = Solution()
arr = [0,3,4,7,9,10]
days = 4

print(sol.binarysearch(arr,days))
