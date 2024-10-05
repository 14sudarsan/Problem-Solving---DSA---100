a = [5,5,3,3,1,5,5]

n = len(a)

half = n//2




for  i in range (0 , len(a) ,1):
    
    count  = 0
    
    for j in range(0,len(a),1):
        
        if(a[i] == a[j]):
            count = count+1
            
        if(count > half):
            
            print( a[i])


