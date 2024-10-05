class Solution:
    def check(self,arr,k):
        
        li = []
        
        for i in range(0,len(arr)-2):
            
            max = arr[i]
            for j in range(1,k):
                
                if arr[i+j] > max:
                    
                    max = arr[i+j]
                    
            li.append(max)
            
        return li
sol = Solution()
print(sol.check([1,2,3,4,5],3))
                    
                
        
        