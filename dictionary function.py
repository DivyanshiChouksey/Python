dct = {10:'red' , 35:'green' , 15:'white' , 2:'violet'}

c1 = sorted(dct.items(), key =lambda x : x[1])

print(dict(c1))
