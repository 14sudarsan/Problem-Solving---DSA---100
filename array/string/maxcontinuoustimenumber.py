arr = [1,1,1,1,1,0,0,0,0,0,0,2,2]

max = 0
 

for i in range(0,len(arr)):
    
    
    count =0
    
    
    
    for j in range(0,len(arr)):
        
        if(arr[i] == arr[j]):
            
            count = count+1
            
            
            
        elif(max < count):
            
            max = count
            

print(max)


            

    
    
    
                


    

  
    
    
    
    
    