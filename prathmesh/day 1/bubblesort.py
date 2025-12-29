def bubblesort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if swapped==False:
            return arr
    return arr


sorted=bubblesort([64, 25, 12, 22, 11])

for i in sorted:
    print(i,end=" ")
