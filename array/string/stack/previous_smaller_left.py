class Solution:
    
    def previous_smaller(self,arr):
        
        stack = []
        
        n = len(arr)
        
        res = [-1]*n
        
        for i in range(0,len(arr)):
            
            
            while stack and stack[-1]>=arr[i]:
                
                stack.pop()
                
            if stack:
                
                res[i] =stack[-1]
                
            stack.append(arr[i])
            
        return res
sol = Solution()

print(sol.previous_smaller([4,10,5,8,20,15,3,12]))