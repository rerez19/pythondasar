import pandas as pd
cellphone = pd.read_csv('cellphone.csv', index_col = 0)

# Print out first 4 observations
print(cellphone[0:4])

# Print out fifth and sixth observation
print(cellphone[0:6])