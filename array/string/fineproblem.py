a = [5,2,3,7]   #date is even

fine= 0
if(a[-1]%2 != 0):
    
    for i in range(len(a)):
    
        if(a[i]%2 != 0):
        
            fine = fine+200
        
print(fine)


    
    
for j in range(len(a)):
    
    if(a[j]%2 == 0):
        
        fine = fine+300
        
print(fine)
        
        



