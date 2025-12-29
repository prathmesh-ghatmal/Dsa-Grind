def bubblesort(arr,n):
    if n<=1:
        return
    did_swap=False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            did_swap=True
            arr[i],arr[i+1]=arr[i+1],arr[i]
    if not did_swap:
        return
    bubblesort(arr,n-1)


arr=[64, 25, 12, 22, 11]
bubblesort(arr,5)

for i in arr:
    print(i,end=" ")