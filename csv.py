import csv

data = [    ['Name', 'Age', 'Country'],  
    ['Alice', '25', 'USA'],  
    ['Bob', '30', 'Canada'],  
    ['Charlie', '35', 'Australia'],
    ['Rezky', '25', 'Indonesia']  
]  
  
with open('data.csv', 'w') as file:  
    writer = csv.writer(file)  
    for row in data:  
        writer.writerow(row) 