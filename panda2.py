import pandas as pd
cellphone = pd.read_csv('cellphone.csv', index_col = 1)

# Print out country column as Pandas Series
print(cellphone['fc'])

# Print out country column as Pandas DataFrame
print(cellphone[['fc']])

print(cellphone[['fc', 'blue']])