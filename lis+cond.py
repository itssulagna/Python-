lst=[1,2,3,2,4,1,1,3,3,5]
count=0
flag=[]
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j] and lst[i] not in flag:
           
            flag.append(lst[i])
            count=count+1
print(count)
 
 