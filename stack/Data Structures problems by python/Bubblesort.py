def Bubblesort(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        large = i
        
        for j in  range(0, n - i - 1):
            
            if arr[large]>arr[j]:
                
                min = j
                
                
                
        arr[i],arr[min] = arr[min],arr[i]
        
array = [64, 25, 12, 22, 11]

Bubblesort(array)

print(array)