number = int(input())
sum =0

for i in range (1,number):
    
        
    if(number%i == 0):
        
        sum = sum+i
        
if(sum == number):
    
    print("The number is perfect" , number)
    
else:
    print("not")