arr = [7,3,2,5,4,1]
a = sorted(arr)   # a =  1,2,3,4,5,7

# process is to check if sum of any two numbers in the array gives the value which is equal to any number in the array
count =0

for t in range(len(a)-1,0,-1):   #for t in rabge(start,stop,increment)
    
    i =0
    
    j=t-1
    
    while(a[i] <a[j]):
        
        sum = a[i]+a[j]
        
        if(sum == a[t]):
            
            print( ([a[i],a[j],a[t]]))
            
            i = i+1
            
            count = count+1
            
        elif(sum <a[t]):
            
            i =i+1
            
        elif(sum>a[t]):
            
            j = j-1
            
print("The number of triplets in the array" +     str(count))
        
        

        
    
    
