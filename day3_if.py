'''
marks=int(input("Enter your marks(1-100): "))
if marks>=90:
    print("Your grade is A")

elif marks>=75 and marks<90:
    print("Your grade is B")

elif marks>=60 and marks<75:
    print("Your grade is C")

else:
    print("Sorry you failed!")
'''
#bonus challenge

age=int(input("Enter your age:"))
driving_license=input("do you have driving license(yes or no): ").lower()

if age>=18 and driving_license=="yes":
    print("Yes you are eligible to drive!")

elif age>=18 and driving_license=="no":
    print("You need a driving license to drive.")

elif age<18:
    print("You should be 18 or above to drive.")

