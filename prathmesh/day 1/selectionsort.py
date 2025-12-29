def selectionsort(arr):
    for i in range(len(arr)) :
        minindex=i
        for j in range(i,len(arr)):
            if arr[minindex]>arr[j]:
                minindex=j
        if minindex!=i:
            arr[i],arr[minindex]=arr[minindex],arr[i]

    return arr

sorted=selectionsort([64, 25, 12, 22, 11])

for i in sorted:
    print(i,end=" ")

