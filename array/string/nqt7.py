class Solution:
    
    def fine(self,n,arr,d,e,o):
        
        if d%2 == 0:
            
            count = 0
            for i in range(len(arr)):
                
                if arr[i]%2 != 0:
                    
                    count = count +1
                    
            fineeven = count * e
            
            return fineeven
        
        else:
            
            count1= 0
            
            for j in range (len(arr)):
                
                if arr[j]%2 == 0:
                    
                    count1 = count1+1
                    
            fineodd = count1 * o
            
            return fineodd 
sol = Solution()
print(sol.fine(5,[2,5,1,6,8],3,200,300))
                
                