n=int(input("enter total number"))
x=int(input("give any number"))
y=int(input("give any number"))
z=int(input(" give any number"))


lst = []

for i in range(1, n):
    
    if(i % x == 0 and i % y ==0  and i%z == 0 and i<n):
        
        print(i)
        
        lst.append(i)
        
print ("no of outputs"  , len(lst))
        
        
        


        