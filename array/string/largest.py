num = int(input("enter no of elements"))

lst =[]

for i in range (num):
    
    ele = int(input())
    
    lst.append(ele)
    
sortredlst = sorted(lst)

print(sortredlst)

print("largest" , sortredlst[-1])
print("second largest" ,sortredlst[-2])
print("third largest" , sortredlst[-3])


        

        
       