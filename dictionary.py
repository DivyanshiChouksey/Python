# Dictionary
capitals = {'MP':'Bhopal','CG':'Raipur','Punjab':'Chandigarh'}
# print(capitals.keys())
# print(capitals.values())
capitals['MP'] = 'jabalpur'           #Update
capitals['Maharashtra'] = 'Mumbai'    #Insert
for state,capitals in zip(capitals.keys(),capitals.values()):
    print(state,capitals)
