countries = ['US','Columbia','Japan','Kenya']
countries.remove('Japan')
countries.append('China')
countries.insert(1, 'Canada')
print(countries)
print(countries[:3])
print(countries[-2:])

print(countries[::-1])
countries.reverse()
print(countries)

more_countires = ['Scotland','Portugal','Russia']

combined = countries + more_countires
print(combined)

