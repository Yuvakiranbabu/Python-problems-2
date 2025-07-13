#n=number of children
#c=number of chocoloates
n=int(input("number of children? "))
c=int(input("number of chocolates: "))
remaining_chocolates=c
got_choco=0

for i in range(n+1):
    if remaining_chocolates>=got_choco:
        got_choco=i
        remaining_chocolates=remaining_chocolates-i

    else:
        break

print(f'remaining chocolates:{remaining_chocolates}')
print(f'children got chocolates: {got_choco}')






