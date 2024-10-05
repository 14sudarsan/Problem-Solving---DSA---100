class Solution:
    
    def smoothed(self,n,nums,k):
        
        n = len(nums)
        if k <=0 or k > n:
            
            return [-1]
        
        lst = []
        
        for i in range(n-k+1):
            
            windowsum = sum(nums[i:i+k])
            
            windowavg = windowsum/k
            
        
            lst.append(round(windowavg,2))
        
        return lst
    
sol = Solution()
print(sol.smoothed(6,[1,1,1,2,1,1],3))