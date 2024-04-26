import csv

with open('cellphone.csv', 'r') as file:  
    reader = csv.reader(file)  
    for row in reader:  
        print(row)