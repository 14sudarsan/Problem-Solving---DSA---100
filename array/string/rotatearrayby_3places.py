arr=[7,1,2,3,4,5,6]


temp = arr[0:3]  #arr 0:n

print(temp)



for i in range(3,len(arr)):     
    
            arr[i - len(temp)] = arr[i]
    



    
for k in range(1,len(temp)+1):
        
        arr[len(temp) + k] = temp[k-1]
        
        
print(arr)