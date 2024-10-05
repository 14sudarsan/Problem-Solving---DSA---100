def reverse(number):
    
  reverse =0
  
  for i in str(number):
      
      value = number%10  #3
      reverse = reverse*10 +value #3
      number=number//10
      
      print (reverse)
      
print(reverse(6789))