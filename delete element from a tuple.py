# delete element from a tuple
tpl = (1,2,3,5,6,7)
idx = 3
tp1 = tpl[:idx]
tp2 = tpl[idx+1:]
tpl = tp1 + tp2
print(tpl)
