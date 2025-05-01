'''
#using lists and loops
f1_cars=["Ferrari","Mercedes","Mclaren","Redubull","Williams"]
for i in f1_cars:
    print(i)

f1_cars.append("Aston martin")
print(f1_cars)
f1_cars.remove("Williams")
print(f1_cars)
print(f1_cars[0])
print(f1_cars[-1])
#using lists and loops
f1_cars=["Ferrari","Mercedes","Mclaren","Redubull","Williams"]
for i in f1_cars:
    print(i)

f1_cars.append("Aston martin")
print(f1_cars)
f1_cars.remove("Williams")
print(f1_cars)
print(f1_cars[0])
print(f1_cars[0:3])
'''

#bonus challenge

f1_cars_garage=["Ferrari","Mercedes","Mclaren","Redubull","Williams"]
print("Welcome to the formula 1 garage!!")
access_garage=True
while access_garage:
    action=int(input("1: Add a new car to the list \n2: Remove a car from the list \n3: Display all cars\n4: Search for a car in the list\n5: Exit\n" \
    "which action would you like to perfomr?(1-5): "))
    if action==1:
        newcar=input("Enter the car brand you want to add: ")
        f1_cars_garage.append(newcar)

    elif action==2:
        removecar=input("Enter the car brand you want to remove: ")
        f1_cars_garage.remove(removecar)

    elif action==3:
        print(f"The cars in the garage are")
        for index,car in enumerate(f1_cars_garage,start=1):
            print(index,car)

    elif action==4:
        search=input("Enter the car brand you want to search: ")
        if search in f1_cars_garage:
            print(f"The car you searched is in the list.")

        else:
            print(f"Sorry we dont {search} car brand in our garage")


    access_garage=input("Do you want to access garage again?(y/n): ").lower()
    if access_garage=="y":
        access_garage=True

    else:
        access_garage=False

print("Thank you for visiting our formula one garage")