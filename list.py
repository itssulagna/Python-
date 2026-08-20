numbers = [12, 5, 8, 21, 4, 15, 10]
largest=numbers[0]
smallest=numbers[0]
sum=0
for i in numbers:
    sum=sum+i
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(sum)
print(largest)
print(smallest)
    