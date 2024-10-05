
#brute force solution     #sliding window problem 
class Solution:
    def count_distinct(self, nums, k):
        if not nums or k <= 0:
            return []
        
        lst = []
        
        for i in range(0,k):
            
            count = 1
            
            for j in range(i+1,i+k):
                
                if nums[i]!=nums[j]:
                    
                    count = count +1
                    
            lst.append(count)
                
        return lst
sol = Solution()

print(sol.count_distinct([1,2,1,3,4,2,3],4))
                