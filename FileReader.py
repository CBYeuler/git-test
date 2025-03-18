import csv

#extract data based on conditions

with open("test.csv","r") as file:
    
    reader = csv.reader(file)
    
    for row in reader:
        print(row)

