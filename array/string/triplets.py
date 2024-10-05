arr = [7,3,2,5,4,1]

a = sorted(arr) #1,2,3,4,5,7




for t in range(len(a) -1,0,-1):
    
    i = 0

    j = len(a)-2
    
    while(a[i] < a[j]):
        
        sum = a[i] + a[j]
        
        if(sum == a[t]):
            
            print(a[i] , a[j] , sum)
            
            i = i+1
            
            
            
        elif(sum < a[t]):
            
            i = i+1
            
        elif(sum > a[t]):
            
            j = j-1
            
        
    
    
    


