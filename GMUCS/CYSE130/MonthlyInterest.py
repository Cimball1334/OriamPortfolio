
#THIS DOES NOT WORK OOPS


import math
p = int(input('Initial Sum '))
r = float(input('Interest Rate (%)'))
n = int(input('Time Period (years)'))

monthly_rate = (r/12)*100
interest = p*math.pow((1+monthly_rate),12*n)

print('The amount of interest earned in',n,'year is ${:.2f}'.format(interest))