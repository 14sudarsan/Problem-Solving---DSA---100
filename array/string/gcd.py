a = int(input(""))

b = int(input(""))

rem =1

if(a>b):
    
    diviend = a
    divisor = b
    
elif(a<b):
    diviend = b
    divisor = a
    
while rem!=0:
    
   rem = diviend%divisor
   
   if(rem == 0):
       
       print(divisor)
   else:
       diviend = divisor 
       divisor = rem
          
    
