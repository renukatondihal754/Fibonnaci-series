n=int(input("enter a number\n"))
previous,current=0,1
if n==0:
    print(previous)
elif n==1:
    print(current)

else:
    count=2
    while count<n:
    # count=2
        previous,current=current,previous+current
        count+=1

print(current)
