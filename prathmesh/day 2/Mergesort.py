def merge(low,mid,high,arr):
    left,right=low,mid+1
    temp=[]
    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while left<=mid:
            temp.append(arr[left])
            left+=1
    while right<=high:
            temp.append(arr[right])
            right+=1
    for i in range(low,high+1):
            arr[i]=temp[i-low]

def mergesort(arr,low,high):
      
      if low>=high:
            return
      mid=low+(high-low)//2

      mergesort(arr,low,mid)
      mergesort(arr,mid+1,high)
      merge(low,mid,high,arr)
    

arr=[64, 25, 12, 22, 11]
mergesort(arr,0,4)

for i in arr:
    print(i,end=" ")
