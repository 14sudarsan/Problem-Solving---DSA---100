class Solution:
    
    def minsumofsubarray(self,n,s,nums):
        
        li = []
        start = 0
        
        cs = 0
        
        for end in range(0,len(nums)):
            
            cs = cs + nums[end]
            
            
            if cs > s:
                
                cs = 0
                
            if cs ==s:
                
                li.append([start+1,end+1])
                print(li)
                
                
          
                
                cs = 0
                
            end = start +1
            
            start = start+1
            
            return li[-1]
    
sol = Solution()
print(sol.minsumofsubarray(6,7,[2,3,1,2,4,5]))
    
                