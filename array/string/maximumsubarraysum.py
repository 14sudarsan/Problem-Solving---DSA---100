arr = [-2,-3,4,-1,-2,1,5,-3]
# here sum of 4,-1,-2,1,5 is 7 that is the maximum sum comapring with sum of all the sub array
max =0 

for i in range(0,len(arr) ,1):
    
    sum = 0
    
    for j in range(i ,len(arr) ,1):
        
        sum = sum + arr[j]
        
       
        
        if(max < sum):
            
           
            
            max = sum
            
print(max)