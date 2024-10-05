class Solution():      #1,4,3,2
    
    def Subarrayrange(self,nums):                                       #1
        
        sum = 0
        
        for i in range(len(nums)-1):
            
            largest = nums[i]
            
            smallest = nums[i]
            
            for j in range(i+1,len(nums)):
                
                largest = max(largest , nums[j])
                
                smallest = min(smallest , nums[j])
                
                
                sum = sum + largest - smallest
                
        return sum
sol = Solution()
print(sol.Subarrayrange([1,4,3,2]))
                
                