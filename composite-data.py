import csv
import copy #module to make a deep copy of the data to store in memory

# define a dictionary that will serve as your composite type for reading the tabular data
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# iterate over the initial keys and values of the dictionary
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
#The items() function belongs to the dictionary data type. The items() function tells the for loop to traverse the collection owned by the dictionary data type.

#Define an empty list to hold the car inventory that you will read
myInventoryList = []

#with open syntax statement keeps a file open while you read data.
#It will automatically close the CSV file when the code inside the with block is finished running.
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            # By default, Python does a shallow copy of complex data types. A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable.
            # Without this line, you would have only one storage box, and only the last item in the list would be copied into memory.
            # The deepcopy makes sure that new storage boxes are created in memory to store the new tabular data that is being read.
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

print(myInventoryList) #myInventoryList is a list with dictionaries(properties) of each vehicle
# Looping through a list
for myCarProperties in myInventoryList:
    # Looping through a dictionary
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        
    print("-----") # This is part of the first for-loop