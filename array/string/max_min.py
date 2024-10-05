a = [1,5,4,3,9]

max = a[0]

low  = a[1]

for i in range(1,len(a)):
   
    if(max < a[i]):
        
        max = a[i]
        
print(max)

for j in range(0 , len(a)):
    
    if(a[j] < low ):
        
        low = a[j]
        
print(low)
