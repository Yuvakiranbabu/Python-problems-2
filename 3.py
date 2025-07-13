score=0
odd_num=0
while (odd_num<3):
    
    user_in=int(input("Enter the input: "))
    if user_in % 2 != 0 and user_in>0:
        score+=1
        odd_num=odd_num+1

    elif user_in % 2 == 0 and user_in>0:
        score-=1
    else:
        score-=0.5

print(score)


    

