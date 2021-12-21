# find maximum value in list
lst=[15,68,2,11,36,56,9]
maxNum = lst[0]
for i in range(0,len(lst)):
    if lst[i] > maxNum:
        maxNum = lst[i]
print(maxNum)
