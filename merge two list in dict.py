# merge two list in dictionary
# method 1
countries = ['India','US','Pakistan','Shrilanka','Russia','South Africa']
capitals = ['delhi','washington','islamabad','colombo','moscow','cape town']
dct = dict(zip(countries,capitals))
print(dct)

# method 2
countries = ['India','US','Pakistan','Shrilanka','Russia','South Africa']
capitals = ['delhi','washington','islamabad','colombo','moscow','cape town']
dct = {}
for country,capital in zip(countries,capitals):
    dct[country] = capital
print(dct)
