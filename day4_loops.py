'''
#understanding loops - for and while loop

#for loop

number=int(input("Enter the number till which you want to get printed: "))

for i in range(1,number+1):
    print(i)

#changing the above code slightly to get desired outcome

for i in range(1,number+1):
    if i%3==0 and i%5==0:
        print(f"{i}-fizzbuzz")#formatted string use f and then start with "" and insert variables using {}.

    elif i%3==0:
        print(f"{i}-fizz")

    elif i%5==0:
        print(f"{i}-buzz")

    else:
        print(i)

#using while loop

x=1
while x<=number:
    print(x)
    x=x+1

'''
#bonus challenge

start_count=int(input("Enter the number from where you want to start counting in reverse: "))
x=1

while x<=start_count:
    if start_count%2==0:
        start_count=start_count-1#use increment or decrement before using continue
        continue#when you use continue if condition satisfies it goes to the start of the loop 
    else:
        print(start_count)

    start_count=start_count-1

print("Blast off")