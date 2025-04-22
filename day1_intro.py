# day 1 of learning python
# use "" to write strings everywhere

print("hello world!!, classic first line to start coding huh")

name="ykb"
age=20

print("Hi guys i am",name,"and i am",age,"years old")
#same sentence using formatted string 
print(f"Hi guys i am {name} and i am {age} years old.")

like_pizza=input("hello do you like pizza?").strip().lower()
# functions used:strip removes the whitespace before and after the word and lower converts the word into lower case

if like_pizza=="yes":
    print("Yes i like pizza")
else:
    print("sorry i dont like pizza")


