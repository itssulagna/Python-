count=0
sentence = "Python is easy and Python is powerful"
words = sentence.split()
for i in words:
    if i=="Python":
        count=count+1
print(count)
    