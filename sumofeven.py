sum=0
N=int(input("Enter value"))
for i in range(1,N+1):
    if i%2==0:
        sum=sum+i
print(sum)