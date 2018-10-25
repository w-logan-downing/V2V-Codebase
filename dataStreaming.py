import csv

file = "Data\\us101_test.csv"

carData = []            

def newEntry(line):
    template = {'ID': '', 'Global_Time': [], 'Real_Time': [], 'X': [], 'Y': [], 'Velocity': [], 'Lane_ID': []}
    template['ID'] = int(line[0])
    template['Global_Time'].append(line[1])
    template['Real_Time'].append(line[2])
    template['X'].append(float(line[3]))
    template['Y'].append(float(line[4]))
    template['Velocity'].append(float(line[5]))
    template['Lane_ID'].append(int(line[6]))
    return template

with open(file, 'r') as data:
    csv_reader = csv.reader(data)
    IDs = []
    next(csv_reader) # skip past the initial header row
    for line in csv_reader:

        if len(carData) == 0:
            carData.append(newEntry(line))
        else:
            
            for i in carData:
                present = True #assumes the ID is somewhere
                if i['ID'] is int(line[0]):
                    i['Global_Time'].append(line[1])
                    i['Real_Time'].append(line[2])
                    i['X'].append(float(line[3]))
                    i['Y'].append(float(line[4]))
                    i['Velocity'].append(float(line[5]))
                    i['Lane_ID'].append(int(line[6]))
                else:
                    present = False #if ID is never found, present is set to false

            if present is False:
                print("did it work")
                carData.append(newEntry(line))
#solution is sort of close
                  
import pprint
pp = pprint.PrettyPrinter()
pp.pprint(carData)

