'''
a=int(input("Enter the first number: "))# using int for type conversion input usually stores data
b=int(input("Enter the second number: "))# in string format so we use the data type converter
'''
#operators

'''
print(f"add {add}\nsub {sub}\nmul {mul}\ndiv {div}\nmodu {modu}\nfloor_div {floor_div}\nexponentiation {exponentiation}")

'''
#creating a simple calculator

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
add=a+b
sub=a-b
mul=a*b
div=a/b
modu=a%b
floor_div=a//b#gives only the non decimal number after dividing
exponentiation=a**b#this is power works like a^b
print("Choose the operation you would like to perform from the below list\n1.addition\n" \
"2.subtraction\n3.multiplication\n4.division\n5.modulus\n6.floor division\n7.exponentiation(power)")
operator=int(input("Enter the operator you want(1-7):"))
if operator==1:
    print(f"add {a}+{b}={add}")

elif operator==2:
    print(f"sub {a}-{b}={sub}")

elif operator==3:
    print(f"mul {a}*{b}={mul}")

elif operator==4:
    print(f"div {a}/{b}={div}")

elif operator==5:
    print(f"modu {a}%{b}={modu}")

elif operator==6:
    print(f"floor_div {a}//{b}={floor_div}")

elif operator==7:
    print(f"power {a}^{b}={exponentiation}")

else :
    print(f"Invalid input")