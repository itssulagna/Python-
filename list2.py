# Given a list of numbers, find the largest and smallest element without using max() or min().
a=[1,2,4,5]
large=a[0]
small=a[0]
for i in a:
    if large < i:
        large+=i
print(large)
for i in a:
     if small > i:
        small+=i
print(small)

# Given a list, create a new list containing only the even numbers.
a2=[4,8,3,1]
b2=[]
for i in a2:
    if i%2==0:
        b2.append(i)
print(b2)

# Given [10, 20, 10, 30, 20, 40, 30], remove the duplicates and create a list containing only unique values.
a3 = [10, 20, 10, 30, 20, 40, 30]
a4 = []
for i in a3:
    if i not in a4:
        a4.append(i)
print(a4)




# Given a list of numbers, find the second-largest element.

 a = [10, 20, 10, 30, 20, 40, 30]
largest = a[0]
second_largest = a[0]

for i in a:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)


