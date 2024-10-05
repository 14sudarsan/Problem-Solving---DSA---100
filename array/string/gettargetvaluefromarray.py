
#optimal solution  #using two pointer
arr = [2,6,5,8,11]
target =14
left = 0
right = len(arr)-1

sum =0
while(left < right):
    
    sum = arr[left]+ arr[right]
    
    
    
    
    
    if(sum == target):
        print(arr[left],arr[right])
        
        break
        
    elif(sum<target):
        
        left = left+1
        
    elif(sum >target):
        
        right = right-1
        


        
        
             
    