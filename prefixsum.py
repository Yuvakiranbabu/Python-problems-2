arr=[5,1,3,2,4]
left=arr[0]
total=sum(arr)

for i in range(1,len(arr)):
    right=total-left
    print(left,right)
    if right == left:
        print(i)
        break
    left=left+arr[i]



