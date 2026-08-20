N=int(input("Enter value"))
count=0
rem=0
while N>0:
    rem=N%10
    N=N//10
    if rem%2==0:
        count=count+1
print(count)