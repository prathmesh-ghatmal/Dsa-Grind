def insertionsort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
    return arr

sorted=insertionsort([64, 25, 12, 22, 11])

for i in sorted:
    print(i,end=" ")