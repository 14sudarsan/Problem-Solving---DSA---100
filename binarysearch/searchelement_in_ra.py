class Solution:
    
    def __init__(self,nums):
        
        self.nums = nums
        
    def findpivot(self):
        
        start = 0
        
        end = len(self.nums)-1
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            
            if mid < end and self.nums[mid] > self.nums[mid+1]:
                
                return mid
            
            if mid > start and self.nums[mid] < self.nums[mid -1]:
                
                return mid-1
            
            if self.nums[mid] >= self.nums[start]:
                
                start = mid + 1
                
            else :
                
                end = mid -1
                
        return -1
    def binarysearch(self, low , high , target):
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.nums[mid] == target:
                return mid
                # Continue searching in the left half
            if mid < high and self.nums[mid+1] == target:
                return mid+1    
            elif self.nums[mid] < target:
                low = mid + 1
                
            else:
                
                high = mid - 1
                
        return -1
    
    def search(self,target):
        
        pivot = self.findpivot()
        
        if pivot == -1:
            
            return self.binarysearch(0, len(self.nums) - 1, target)
        
        if self.nums[0] <= target :
            return self.binarysearch(0, pivot-1, target)
        else:
            return self.binarysearch(pivot + 1, len(self.nums) - 1, target)    
    
    
nums = [4, 5, 6, 7, 0, 1, 2]
target = 6
solution = Solution(nums)
result = solution.search(target)
print(result) 
    



    
    
    
    
                
                
            
         