'''
residential = [ 2.861  3.0484  3.2602  3.342  3.3555  3.4234  3.5268  3.9185  3.9718  3.854  3.8934  4.3127  4.2153  4.1711  4.6605 ]
 
commercial = [2.5348  2.553  2.7084  2.8097  2.9167  3.9299  3.6561  3.3057  3.4761  3.4748  3.5968  3.7088  3.7172  3.7257  3.9367]
 
industrial =  [2.6408  2.74  2.7345  2.8019  2.796  2.8579  2.8597  2.8757  4.000  3.8998  2.6826  2.8427  2.8301  2.8542  2.8512]

Residential: $0.114 (11.4 cents) 

Commercial: $0.1319 (13.9 cents)

Industrial: $0.0672 (6.72 cents)
'''

import numpy as np
import matplotlib.pyplot as plt

residential = np.array([2.861, 3.0484, 3.2602, 3.342, 3.3555, 3.4234, 3.5268, 3.9185, 3.9718, 3.854, 3.8934, 4.3127, 4.2153, 4.1711, 4.6605 ])
commercial = np.array([2.5348,  2.553,  2.7084,  2.8097,  2.9167,  3.9299,  3.6561,  3.3057,  3.4761,  3.4748,  3.5968,  3.7088,  3.7172,  3.7257,  3.9367])
industrial = np.array([2.6408,  2.74,  2.7345,  2.8019,  2.796,  2.8579,  2.8597,  2.8757,  4.000,  3.8998,  2.6826,  2.8427,  2.8301,  2.8542,  2.8512])
x_axis = np.arange(2006,2021,1)

rescost = 0.114
comcost = 0.1319
indcost = 0.0672

#task 1

title = "Average US July Electrical Usage (2006-2020)"
plt.title(title)
plt.xlabel('Years')
plt.ylabel('10^9 KWh/day')

plt.plot(x_axis,residential,'g',label='residential')
plt.plot(x_axis,commercial,'b--',label='commercial')
plt.plot(x_axis,industrial,'m-.',label='industrial')

plt.legend()
# plt.show()

#task 2
adj = 10**9

print(f'Total cost/day for residential in 2006: {residential[0]*adj*rescost:e}')
print(f'Total cost/day for residential in 2014: {residential[8]*adj*rescost:e}')
print(f'Total cost/day for residential in 2015: {residential[9]*adj*rescost:e}')

print(f'Total cost/day for commercial in 2006: {commercial[0]*adj*comcost:e}')
print(f'Total cost/day for commercial in 2015: {commercial[8]*adj*comcost:e}')
print(f'Total cost/day for commercial in 2014: {commercial[9]*adj*comcost:e}')

print(f'Total cost/day for industrial in 2006: {industrial[0]*adj*indcost:e}')
print(f'Total cost/day for industrial in 2015: {industrial[8]*adj*indcost:e}')
print(f'Total cost/day for industrial in 2014: {industrial[9]*adj*indcost:e}')

#task 3

dif = commercial > industrial
print(f'Commercial usage is higher than industrial in {np.sum(dif)} different years, \nThose years are: {x_axis[dif]}')

#task 4
plt.close()

base = np.arange(len(residential))
coeff = np.polyfit(base,residential,1)
poly = np.poly1d(coeff)

J = sum((poly(base) - residential)**2) / (2 *len(residential) * rescost)

plt.scatter(x_axis,residential,color='red',marker='X',label='Data')
plt.plot(x_axis,poly(base),label='Line of Best Fit')
plt.text(1,1,f'J = {J:.2f} dollars')
plt.legend()
plt.show()