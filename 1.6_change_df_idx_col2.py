import pandas as pd

df = pd.DataFrame([[15, 'male', 'dragon'], [17, 'female', 'eagle']],
                  index=['juhun', 'juhyun'],
                  columns=['age', 'sex', 'school'])

print(df)

df.rename(columns={'age':'year', 'sex':'f/m', 'school':'status'}, inplace=True)
df.rename(index={'juhun':'student1', 'juhyun':'student2'}, inplace=True)

print(df)
