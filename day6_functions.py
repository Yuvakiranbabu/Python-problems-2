'''
# using functions 
def greet_user(user):
    print(f"Hello {user}.")

# function to add two numbers
def add_num(a,b):
    c=a+b
    print(f"The addition of {a} and {b} is {c}")

#function to check if number is even
def even_num(x):
    if x%2==0:
        print(f"{x} is a even number.")

    else:
        print(f"{x} is not a even number.")

greet_user("Yuva kiran babu")
add_num(4,5)
even_num(9)
'''

#bonus challenge

use_calc='y'
while use_calc=='y':

    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    operation=input("Enter the operation you would like to perform (+,-,*,/): ")

    def add(a,b):
        return (a+b)# we can also use the variables declared outside function in our function

    def sub(a,b):
        return (a-b)

    def mul(a,b):
        return (a*b)

    def div(a,b):
        return (a/b)

    if operation=="+":
        print(f"addition is: {add(num1,num2)}")

    elif operation=="-":
        print(f"subtraction  is: {sub(num1,num2)}")

    elif operation=="*":
        print(f"multiplication is: {mul(num1,num2)}")

    elif operation=="/":
        if num2==0:
            print(f"Sorry the divisor cannot be zero!")
        else:
            print(f"division is: {div(num1,num2)}")

    else:
        print("Invalid operation")

    use_calc=input("do you want to use calculator again(y/n): ").lower()

print("Thank you for using calculator.")
        

