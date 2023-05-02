import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('GMUCS/SST 230/Recitation/Project/Tax_Data.csv')
df.info()
tax_data = pd.DataFrame(df).to_numpy()

'''
Direct Comparison of buildings current and previous tax rate
'''

shown_elemenets = 10
x_axis = np.arange(0,shown_elemenets,1)
# print(x_axis)

current = np.array([tax_data[x][3] for x in x_axis])
previous = np.array([tax_data[x][7] for x in x_axis])

# plt.bar(x=x_axis,height=previous,align='center')
# plt.bar(x=x_axis, height=current,align='edge',width=.4)


# plt.title('Comparison of Previous and Current Tax Rates on Property')
# plt.ylabel('Value')
# plt.xlabel('Building ID')

# plt.legend()
# plt.show()


'''
Show trend in difference between current and previous
'''
shown_elemenets = 10
x_axis = np.arange(0,shown_elemenets,1)
differences = current-previous
print(f'Average change in rate {sum(differences)/len(x_axis):.1f}$')


plt.bar(x_axis,differences)
plt.show()