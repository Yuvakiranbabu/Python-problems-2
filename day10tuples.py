#using tuples
fav_numbers=(4,26)
num1,num2=fav_numbers#tuple unpacking
list_of_coordinates=[]
no_of_coordinates=int(input("how many coordinates do you want to upload: "))
for i in range(no_of_coordinates):
    x=float(input(f"Enter the x coordinate for {i+1} location: "))
    y=float(input(f"Enter the y coordinate for {i+1} location: "))

    coordinates=(x,y)
    list_of_coordinates.append(coordinates)

print(f"The list of coordinates are : {list_of_coordinates}")
print(f"the coordinates (4.5,4.5) appeared {list_of_coordinates.count((4.5,4.5))} times.")