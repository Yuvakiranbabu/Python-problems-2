#using dictionaries

name=input("Enter your name: ")
age=int(input("Enter your age: "))
fav_sub=input("Enter your favourite subject: ")

student_details={
    "name":name,
    "age":age,
    "subject":fav_sub
}

print(student_details)

#updating dictionaries
student_details["subject"]="Python"

#printing dictionaries after update
print(f"after updating the subject {student_details}")

#using loops to go through dictionaries
for key,value in student_details.items():
    print(f"{key} : {value}")