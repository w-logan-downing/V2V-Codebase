import csv

file = "C:\\Users\\Downi\\OneDrive\\College\\GradSchool\\CS501ComputerScience&Engineering" \
       "\\ProSE\\V2V-Codebase\\Data\\exampleData.csv"

carData = []

with open(file, 'r') as data:
    csv_reader = csv.reader(data)

    next(csv_reader) #skip past the initial header row
    #list(csv_reader)
    for line in csv_reader:
        print(line)
        carData.append(line)

print(carData)