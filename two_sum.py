# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 return arr[i],arr[j]
#     return "no pair found"

# print(two_sum([-5,1,-40,20,6,8,7],15))


arr=[-5,1,-40,20,6,8,7]
target=15
arr.sort()
def two_sum(arr,target):
    left= 0
    right=len(arr)-1

    while left<right:
        summ=arr[left]+arr[right]
        if summ==target:
            return(f'pair {arr[left]},{arr[right]}')

        elif summ<target:
            left=left+1

        else:
            right=right-1

    return "no pair found" 


print(two_sum(arr,target))