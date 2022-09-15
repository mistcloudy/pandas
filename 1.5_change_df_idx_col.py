import pandas as pd

df = pd.DataFrame([[15, 'male', 'dragon'], [17, 'female', 'eagle']],
                  index=['juhun', 'juhyun'],
                  columns=['age', 'sex', 'school'])

print(df)
print(df.index)
print(df.columns)

df.index=['student1', 'student2']
df.columns=['year', 'f/m', 'status']

print(df)
print(df.index)
print(df.columns)