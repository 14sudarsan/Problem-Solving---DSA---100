arr = [0,1,0,3,12]

temp =[]

temp2 = []

for i in range(0,len(arr)):
    
    if(arr[i] != 0):
        
        print(arr[i])
        
        temp.append(arr[i])
        

for j in range(0,len(arr)):
    
    if(arr[j] == 0):
        
       print(arr[j])
       temp2.append(arr[j])   

final = temp+temp2
print(final)    

       


