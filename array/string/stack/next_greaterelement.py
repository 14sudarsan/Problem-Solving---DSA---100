class Solution:
    
    def next_greaterelement(self,arr):
        
        stack = []
        
        n = len(arr)
        
        res = [-1]*n
        
        for i in range(n-1,-1,-1):
            
            
            while stack and stack[-1]<=arr[i]:# like if stack is non empty and stack[-1] value is less than the array value stack is pop
                
                stack.pop()                   #like if 6,5,3,2 in stack  arr val is 4  then 2<=4 ...yes..so 2 is eleminared
                                              # 6,5,3     3<=4 yes so 3 is eliminated  
                                              #6,5  5<=4 no       so the next great element is stack[-1] that is 5
            if stack:
                
                res[i] = stack[-1]
                
            
            stack.append(arr[i])
            
        return res
sol = Solution()

print(sol.next_greaterelement([4,17,5,3,1,2,5,3,1,2,4,6]))            
            