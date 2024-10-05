

# ARRAY   with all greatest numbers concept
lst = []

n = int(input("enter the number of elemnts to the list"))

for i in range(0,n):
    
    ele = int(input( "enter the list elements you want to add"))
    
    lst.append(ele)
    
listnum = lst

print( "This is the original list" + str(listnum))





max = listnum[0]

for i in range(1,len(listnum)):
    
    
    if max > listnum[i] :
        listnum[i] = max
        
        
        
        
        
         
         
    elif max < listnum[i]:
         max = listnum[i]
         
         
         
    
  
largest =  max

print("The  first greatest number is" + str(largest))

set =-1

for k in range(0,len(listnum)):
    
    if listnum[k]>set and listnum[k]!=largest:
        
        secondnumber = listnum[k]
        
print("the second greatest number" + str(secondnumber))
for z in range(0,len(listnum)):
    
    if listnum[z]!=largest and listnum[z]!=secondnumber :
        
        thirdnumber = listnum[z]
        
print("the third greatest number" + str(thirdnumber))


     

    
    


        
        
    
        
        
    
    
    


    

    
    
        
    
         
         
    
         
         
         


         
         
        
        
        
        
        
        
        
        

    
           
    
        
        
        


    