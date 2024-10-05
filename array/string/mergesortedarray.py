arr1=[1,2,3,3,4,5]          #merge two sorted array
arr2 = [7,8,8,9]
i=0
j=0
final = []
while( (i < len(arr1)) and (j <len(arr2))):
    
    if(arr1[i] <= arr2[j]):
        
        final.append(arr1[i])
        
        i = i+1
   
    else:
        
        final.append(arr2[j])
        
        j = j+1
        
while(i < len(arr1)):
    
     final.append(arr1[i])
        
     i = i+1
        
while(j < len(arr2)):
    
     final.append(arr2[j])
        
     j = j+1

print(final)     
finalarray = set(final)  #using set to avoid the duplicate values in the array

print(list(finalarray)) # using the list function to print the sorted array has list







    
     
        

