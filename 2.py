target=100
total_score=0
num=1
shots_taken=0
print(f"target={target}")
while(total_score<target):
    turn=int(input(f"enter your {num} shot distance:"))
    total_score=total_score+turn
    num=num+1
    shots_taken=shots_taken+1

print(f'shots taken by the user to reach the target = {shots_taken}')
