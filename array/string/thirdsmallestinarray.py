n  = int(input("number elements in the list"))

list = []

for i in range (n):
    
    element = int(input("add element in the array"))
    
    
    list.append(element)
    
print(list)

sortedlist = sorted(list)
print(sortedlist)

print("The third smallest element" + str(sortedlist[2]))

indexvalue = sortedlist.index(sortedlist[2])

print(indexvalue)

