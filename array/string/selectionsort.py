def Selection(arr):
     
    n = len(arr)
     
    for i in range(n):
        
        min = i
        
        for j in range(i+1,n):
            
            if  arr[j]< arr[min]:
                
                min = j
        #This is swapping        
        arr[i],arr[min] = arr[min],arr[i]
            

array = [64, 25, 12, 22, 11]

Selection(array)
print(array)
            