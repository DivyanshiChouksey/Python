# print common element 
lst1 = [3,44,38,5,47,15,36]
lst2 = [26,27,2,44,47,15,50,48]

# method 1
for i in range (0,len(lst1)):
    for j in range(0,len(lst2)):
        if lst1[i] == lst2[j]:
            print(lst1[i])


# method 2
s1 = set(lst1)
s2 = set(lst2)
print(s1.intersection(s2))

# method 3 
for item in lst2:
    if item in lst1:
        print(item)
