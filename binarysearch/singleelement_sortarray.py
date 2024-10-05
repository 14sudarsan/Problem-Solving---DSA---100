class Solution(object):                #Two solutions are here both aresolution for leetcode
    
    
    #time complexiy is O(n)
    def singleNonDuplicate(self,nums):
        
        if len(nums)==1:
            
            return nums[0]
        
        for i in range(0,len(nums)):
            
            if i == 0:
                
                if nums[i]!=nums[i+1]:
                    
                    return nums[i]
                
            if i == len(nums)-1:
                
                if nums[i]!=nums[i-1]:
                    
                    return nums[i]
                
            if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                
                
                return nums[i]
            
            
            
            
sol = Solution()
print(sol.singleNonDuplicate([1,1,3,3,4,4,5,5,7,6,6]))

class Solution(object):
    def singleNonDuplicate(self, nums):
        
        if len(nums) == 1 :

            return nums[0]
        
        if nums[0]!= nums[1]:

            return nums[0]

        if nums[len(nums)-1] != nums[len(nums)-2]:

            return nums[len(nums)-1]
        start = 1
        end = len(nums) - 2

        while start <= end:
            mid = start + (end - start) // 2

            # Check the boundaries first
           

            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]

            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                # Move the start or end based on mid being even or odd
              
                    start = mid + 1
            else:
                    end = mid - 1

        return -1  # Fallback return, will execute when the loop exits

sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Expected output: 2
