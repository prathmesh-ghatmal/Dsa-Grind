def insertionsort(arr,i,n):
    if i==n:
        return
    
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
    insertionsort(arr,i+1,n)

arr=[64, 25, 12, 22, 11]
insertionsort(arr,1,5)

for i in arr:
    print(i,end=" ")


    