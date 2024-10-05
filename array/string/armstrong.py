number = int(input(""))

string = str(number)

length = len(string)




temp = number

sum = 0
while temp>0:
    
    digit = temp%10
    
    temp = temp //10
    
    sum = sum + digit ** length
    
if(sum == number):
    print("this is armstrong") 
    
else:
    print("not an armstrong")
    