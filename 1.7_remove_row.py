import pandas as pd

exam_data = {'Math' : [90, 80, 70], 'English' : [98, 89, 95], 'Music' : [85, 95, 100], 'Physical' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['A', 'B', 'C'])
print(df)

df2 = df[:]
df2.drop('B', inplace=True)
print(df2)

df3 = df[:]
df3.drop(['B', 'C'], axis=0, inplace=True)
print(df3)

df4 = df[:]
