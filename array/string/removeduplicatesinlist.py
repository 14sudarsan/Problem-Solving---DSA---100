a = [1,1,1,2,2,3,3]

i =0

list=[]
for j in range(1,len(a)):
    
    if(a[j] != a[i]):
        
        a[i+1] = a[j]
        
        
        list.append(a[i])
        
        
print(list)
        
        
        
        
            
            
    
    
    
    