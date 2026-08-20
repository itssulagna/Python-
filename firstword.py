s=input()
# h=s.lower().split()
# h.sort()
# print(h[0])

lowered=s.lower().split()
first=lowered[0]
for word in lowered:
    if word<first:
        first = word 
print(first)




