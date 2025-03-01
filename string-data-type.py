myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)) + "\n")

#Concatenating two strings
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString, "\n")

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
# Output a formatted string
print("{} you like a {} {}!".format(name, color,animal))