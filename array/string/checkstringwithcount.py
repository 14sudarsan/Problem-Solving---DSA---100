a = "banana"
lst =[]


for i in range(0,len(a),1):
    
    count =0
    
    for j in range(0,len(a),1):
        
        if(a[i] == a[j] ):
            
            count = count+1
            
        
        
        
    final =    ( str(count) , str(a[i]))
    
 
    
    lst.append(final)

string = set(lst)

print(str(string))
    
    
        
                
     