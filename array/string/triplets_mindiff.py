class Solution:
    
    def mindiff(self,a,b,c):
        
        a.sort()
        b.sort()
        c.sort()
        
        mindiff  = float("inf")
         
        i = 0
        j = 0
      
         
        
        result = (a[0],b[0],c[0])
        
        k = 0
        
        while i < len(a) and j < len(b) and k <len(c):
            
           
            
            
            currentmax = max(a[i],b[j],c[k])
            
            currentmin = min(a[i],b[j],c[k])
            
            
            currentdiff  = currentmax - currentmin
            
            
            if currentdiff < mindiff:
                
                mindiff = currentdiff
                
                result = (a[i],b[j],c[k])
                
            if currentmin == a[i]:
                
                i = i+1
                
            elif currentmin == b[j]:
                
                j=j+1
                
            else:
                
                k = k+1 
                
        return result,mindiff
sol = Solution()
print(sol.mindiff([1,4,10],[2,15,20],[10,12]))        
        