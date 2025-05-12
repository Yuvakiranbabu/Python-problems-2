#using all the things i learnt from day 1 to 9

no_of_students=int(input("Enter the number of students in your class: "))
student_list=[]
for i in range(1,no_of_students+1):

    name=input("Enter the name of the student: ")
    age=int(input("Enter the age of the student: "))
    sub=input("Enter the favourite subject of the student: ")

    students_details={
        "name":name,
        "age":age,
        "fav_sub":sub
    }

    student_list.append(students_details)


for index,student in enumerate(student_list,start=1):
    print(f"{index} : {student['name']}")



def update_subject(index):
    up_sub=input("Enter the updated subject name: ")
    student_list[index]["fav_sub"]=up_sub


def remove_student(index):
    student_list.pop(index)


ask=True
while ask:
    action=int(input("Do you want to (1) Update Subject (2) Remove Student: "))
    if action==1:
        subject=int(input("Enter the index of the student you want to update subject: "))-1
        update_subject(subject)

    elif action==2:
        rem_stu=int(input("Enter the studet index number you want to remove: "))-1
        remove_student(rem_stu)

    print(student_list)

    repeat=input("Do you want to perform any action again(y/n): ")
    if repeat=="y":
        ask=True

    else:
        ask=False

print("Thank you for using student manager!!!")
