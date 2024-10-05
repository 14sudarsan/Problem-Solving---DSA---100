class Solution:
    
    def collision(self,arr):
        
        stack = []
        
        
        for i in range(len(arr)):
            
            if arr[i] == abs(arr[i]):
                
                stack.append(arr[i])
                
            else:
                
                while stack!=[] and stack[-1]<=abs(arr[i]):
                    
                    if stack[-1] == abs(arr[i]):
                        stack.pop()
                        
                        break
                    
                    stack.pop()
                    
        return stack
    
sol = Solution()
print(sol.collision([1, 3, 4, -1, 2, -4]))  # Expected output: [3, 2]





