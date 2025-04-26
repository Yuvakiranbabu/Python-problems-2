'''
show_room_cars=["xuv 700","virtus","slavia","fortuner"] #to use lists put the name and use [] to create lists
ask_user=input("Enter the name of your favourite car: ").lower()
if ask_user in show_room_cars:
    print("yea your favourite car is available in the showroom")

else:
    print(f"sorry we dont have {ask_user} in our showroom right now.")
'''
#bonus challenge
showroom=["BMW M5","XUV 700","VIRTUS","INNOVA","MCLAREN P1","AUDI Q8"]
wish_list_size=int(input("Enter the number of cars in your wishlist: "))
wish_list=[]

for i in range(1,wish_list_size+1):
    car_list=input(f"Enter the name of your {i} car: ").upper()
    wish_list.append(car_list)#append used to add items to list 

available_cars=[]
unavailable_cars=[]
for cars in wish_list:
    if cars in showroom:
        available_cars.append(cars)
    
    else:
        unavailable_cars.append(cars)

print(f"available cars: {available_cars}")
print(f"unavailable cars: {unavailable_cars}")