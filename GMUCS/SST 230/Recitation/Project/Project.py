import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
''' 
https://catalog.data.gov/dataset/tax-administrations-real-estate-assessed-values-08c4b/resource/7454dd8f-8e29-4b38-b844-b4ec63f23cb1
'''

df = pd.read_csv('GMUCS/SST 230/Recitation/Project/Tax_Rates.csv')


# for x in df.columns:
#     print(x)
# df.plot(x = df.colum,y=2, kind = 'bar')

# df.plot(x = 'OBJECTID',y='APRLAND',kind='bar')


# print([df['APRLAND'][x]-df['PRILAND'][x] for x in df.index])
# df.assign(tmp=df["APRLAND"]-df["PRILAND"])
df["tmp"] = [df['APRLAND'][x]-df['PRILAND'][x] for x in df.index]
df = df.sort_values(by='tmp',ascending=False)
# df.drop(columns='tmp')

start_ind = 0
end_ind = 100

# print(df.iloc[[x for x in range(start_ind,end_ind)],[0,2,3,6]])
print(df.iloc[[x for x in range(start_ind,end_ind)]])

# plt.bar(df["OBJECTID"][start_ind:end_ind],df["APRLAND"][start_ind:end_ind])
# plt.bar(df["OBJECTID"][start_ind:end_ind],df["PRILAND"][start_ind:end_ind])
# plt.legend()
# plt.show()