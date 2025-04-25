name=input("Enter your name: ")
age=input("Enter your age: ")
no_of_subjects=int(input("Enter the number of subjects: "))
average=0

for i in range(1,no_of_subjects+1):
    sub_name=input(f"Enter the name of the subject {i}:")
    sub_mark=int(input(f"Enter the marks secured in {sub_name}:"))
    average=average+sub_mark

average=average/no_of_subjects
print(f"average - {average}")

if average>=90:
    print("Your grade is A")

elif average>=75 and average<90:
    print("Your grade is B")

elif average>=60 and average<75:
    print("Your grade is C")

else:
    print("Sorry you failed!")
