class Solution:
    
    def mySqrt(self,x):
        
        
        start = 1
        
        end  = x
        
        #using binary search
        
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            if mid*mid <= x:
                
                answer = mid
                
                start = mid +1
                
            else:
                
                end = mid -1
                
        
        return answer
    
sol = Solution()
print(sol.mySqrt(54))
            
            