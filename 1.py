# weight = even, share equally
# weight= odd , you dont get the share

#other ways we can split

weight_of_watermelon=int(input("Enter the weight of the watermelon: "))
if weight_of_watermelon%2==0:
    print("you get half and i get half")
    for i in range(1,weight_of_watermelon):
        n=i
        y=weight_of_watermelon-i
        print(n,y)
else:
        print('you get nothing')