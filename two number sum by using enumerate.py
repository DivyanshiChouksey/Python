nums = [2,7,11,15]
target = 9
dct = {}
for i,num in enumerate (nums):
    if num in dct:
        print([dct[num],i])
    else:
        dct[target-num]= i 
