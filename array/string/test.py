a = [1,2,1,2,1,3,2]

count = 0

for i in range(0,len(a)-1,1):
    
    if(a[i] < a[i+1] and a[i+1] == a[i] +1):
        
        print(a[i] , a[i+1])
        count = count+1
        
print(count)
        