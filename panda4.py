import pandas as pd
cellphone = pd.read_csv('cellphone.csv', index_col = 0)

# Print out observation for Japan
print(cellphone.iloc[8])

# Print out observations for Australia and Egypt
print(cellphone.loc[[{2}, {4}]])