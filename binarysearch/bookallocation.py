class Solution:
    
    def student(self,arr,pages):
        
        
        
        student = 1
        
        pagesofstudent = 0
        for i in range(len(arr)):
            
            if pagesofstudent+arr[i]<=pages:
                
                pagesofstudent = pagesofstudent+arr[i]
                
            else:
                
                student = student+1
                
                pagesofstudent = arr[i]
                
        return student
    
    
    def Binarysearch(self,arr,m):
        
        
        low = max(arr)
        
        high = sum(arr)
        
        
        while low <= high:
        
        
            mid = (low+high)//2
        
        
            student =  self.student(arr,mid)
        
        
            if student >m:
                low = mid+1
            
            else:
                high = mid-1
            
            
        return low
sol = Solution()

arr = [7,2,5,10,8]

m = 2
print(sol.Binarysearch(arr,m))