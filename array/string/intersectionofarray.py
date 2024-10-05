a= [1,2,2,1]
b=[2,2]

arr = []
visited = [0,0,0,0,0,0,0]

for i in range(0,len(a)):
    
    for j in range(0,len(b)):
        
        if a[i]==b[j] and visited[j] == 0:

            
            arr.append(a[i])
            visited[j] = 1
            break

            
print(arr)
