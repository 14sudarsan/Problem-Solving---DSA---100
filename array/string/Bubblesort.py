class Solution:

    def Bubblesort(self,arr):
        
        n = len(arr)
        
        for i in range(n):
            
            large = i
            
            for j in  range(0, n - i - 1):
                
                if arr[large]>arr[j]:
                    
                    min = j
                    
                    
                    
            arr[i],arr[min] = arr[min],arr[i]
        

sol = Solution()
sol.Bubblesort([5,6,7,8])