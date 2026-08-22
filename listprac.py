# Create a list of 5 numbers and add a new number at the end.

num=[1,3,5,8]
num.append(7)
print(num)

# Create a list of names and insert "Rahul" at index 2.
name=["gayatri", "keerthana"]
name.insert(2,"Rahul")
print(name)

# Given [10, 20, 30, 20, 40, 20], remove the first occurrence of 20.
list3=[10, 20, 30, 20, 40, 20]
list3.remove(20)
print(list3)

# Given [5, 2, 8, 1, 9], sort the list in ascending and descending order.

list4=[5, 2, 8, 1, 9]
list4.sort()
print(list4)

list_4=[5, 2, 8, 1, 9]
list_4.sort(reverse=True)
print(list_4)

# Given [10, 20, 30, 40, 50], remove the last element and print the removed element.


list5=[10, 20, 30, 40, 50]
list5.remove(50)
print(list5)


# Given [1, 2, 2, 3, 2, 4], find how many times 2 occurs.
list6=[1, 2, 2, 3, 2, 4]
new=list6.count(2)
print(new)

# Given ["apple", "banana", "mango", "orange"], find the index of "mango".

list7=["apple", "banana", "mango", "orange"]
new1=list7.index("mango")
print(new1)

# Create two lists and combine the second list into the first using extend().

list8=["apple", "banana", "mango", "orange"]
list9=["hello","hi", "world"]
list8.extend(list9)
print(list8)

# Create a tuple (10, 20, 10, 30, 10, 40) and find how many times 10 occurs.

tuplea=(10, 20, 10, 30, 10, 40)
tupcount=tuplea.count(10)
print(tupcount)

# Given the tuple ("Python", "Java", "C++", "JavaScript"), find the index of "C++".

tupleb=("Python", "Java", "C++", "JavaScript")
indtup=tupleb.index("C++")
