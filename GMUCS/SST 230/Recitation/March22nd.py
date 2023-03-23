import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

exam_data = {
    'name': ['First','Second','Third','Fourth','Fith','Sixth'],
    'score': [10,6,9,np.nan,8,4],
    'attempts':[1,1,2,1,2,1],
    'quality': ['yes','no','yes','no','yes','no'] 
}
labels = ['a','b','c','d','e','f']
df = pd.DataFrame(exam_data, index=labels)


print(df,end='\n\n***********************************\n\n\n\n')

print(df.info(),end='\n\n***********************************\n\n\n\n')

print(df.iloc[[1,3,5],[1,2,3]],end='\n\n***********************************\n\n\n\n')

print(df[df['score'].isnull()],end='\n\n***********************************\n\n\n\n')

print(df[df['score'].between(6,10)],end='\n\n***********************************\n\n\n\n')

print(df['score'].mean(),end='\n\n***********************************\n\n\n\n')

df.loc['z'] = [1,'New','yes',6]
print(df,end = '\n\n')
df = df.drop('z')
print(df,end='\n\n***********************************\n\n\n\n')

df = df.sort_values(by=['name','score'],ascending=[False,True])
print(df,end='\n\n***********************************\n\n\n\n')

df = pd.DataFrame(exam_data,index=labels)
df = df.fillna(0)
print(df,end='\n\n***********************************\n\n\n\n')

df.to_csv('file.csv',sep='\t',index=False)
new_df = pd.read_csv('file.csv')
print(new_df,end='\n\n***********************************\n\n\n\n')
