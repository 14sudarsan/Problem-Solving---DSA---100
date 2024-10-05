class Solution:
    def findpivot(self,nums):
        
        nums.sort()
        
        
        
        start = 0
        
        end = len(nums)-1
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            
            if mid < end and nums[mid] > nums[mid+1]:
                
                return mid
            
            if mid > start and nums[mid] < nums[mid -1]:
                
                return mid-1
            
            if nums[mid] >= nums[start]:
                
                start = mid + 1
                
            else :
                
                end = mid -1
                
        return -1
    
    def kthlargest(self,nums,k):
        
        pivot = self.findpivot(nums)
        
        
        out = pivot -(k-1)
        
        
        return out
    
sol = Solution()

nums = [3,2,1,5,6,4]
k = 2
print(sol.kthlargest(nums,k))
        
        
        