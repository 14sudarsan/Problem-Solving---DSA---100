a = str(input("enter the string"))
b = []
for i in range(0,len(a)):
    
    
    
    b.append(a[i])

c = set(b)
list = list(c)
mainlist = sorted(list)
for j in range(len(mainlist)):
    
    print(mainlist[j] ,end="")

