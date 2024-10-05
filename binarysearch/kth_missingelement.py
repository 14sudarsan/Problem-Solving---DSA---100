class Solution:
    def check(self,nums,k):
        
        start = 0
        
        end = len(nums)-1
        
        while start <= end:
            
            mid = (start + end)//2
            
            missing = nums[mid] - (mid+1)
            
            if missing < k:
                start = mid+1
                
            else:
                end = mid-1
                
        return start+k
sol = Solution()
print(sol.check([2,3,4,7,11],5))