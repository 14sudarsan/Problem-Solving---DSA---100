arr=[7,1,2,3,4,5,6]


n = int(input("num"))

temp = arr[0:n]  #arr 0:n

print(temp)




for i in range(n,len(arr)):     
    
            arr[i - len(temp) ] = arr[i]
    



    
for k in range(0 ,len(temp)):
        
    arr[(n-1)+k ] = temp[k]

print(arr)


    

    
    
        
        
    