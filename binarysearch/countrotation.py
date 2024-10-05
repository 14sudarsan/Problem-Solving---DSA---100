class Solution:
    
    def check(self, nums):
        
       
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
    
    def search(self,nums):
        
        pivot = self.check(nums)
        
        if pivot == -1:
            
            return 0
        
        else:
            
            return pivot +1


nums = [3,2,1,5,6,4]
sol = Solution()
result = sol.search(nums)
print(result)