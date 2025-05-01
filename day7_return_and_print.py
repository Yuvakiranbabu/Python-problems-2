which_function=int(input("Enter which function you would like to use (1-(finding sqaure) or 2-(largest number)): "))
while which_function==1 or which_function==2:
    if which_function==1:
        # creating a function to return the square of a number
        number=int(input("Enter the number for which you would like to find the square: "))
        def square(num):
            return pow(num,2) #or num**2 to calculate the square of a number
        result=square(number)
        print(f"The square of the number {number} is {result}.")
        use_again=input("Do you want to use any of the two functions again(yes or no): ")
        if use_again=="yes":
            which_function=int(input("Enter which function you would like to use (1-(finding sqaure) or 2-(largest number)): "))
            continue
        else:
            break

    elif which_function==2:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        num3=int(input("Enter the third number: "))
        def largest(a,b,c):
            if a>=b and a>=c:
                return a
            elif b>=a and b>=c:
                return b
            else:
                return c
            
        largest_number=largest(num1,num2,num3)
        print(f"The largest among the three entered numbers is {largest_number}.")
        use_again=input("Do you want to use any of the two functions again(yes or no): ")
        if use_again=="yes":
            which_function=int(input("Enter which function you would like to use (1-(finding sqaure) or 2-(largest number)): "))
            continue
        else:
            break

print(f"Thank you for using these functions")