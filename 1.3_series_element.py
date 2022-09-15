import pandas as pd

tup_data = ('juhun', '1996-02-23', 'male', True)
sr = pd.Series(tup_data, index=['name', 'birth date', 'sex', 'student status'])
print(sr)

# select one
print(sr[0])
print(sr['name'])

# select over two
print(sr[[1, 2]])
print(sr[['birth date', 'sex']])

# select range
print(sr[1:3])
print(sr['birth date':'student status'])


