# Looping through a list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    #print(f"{item} is of the data type {type(item)}")
    
#Looping through a dictionary
myFavoriteFruitDictionary = {
  "Akua" : 3,
  "Saanvi" : "banana",
  "Paulo" : True
}
for key in myFavoriteFruitDictionary:
    print("{} is of the data type {}".format(key, type(key)))
for value in myFavoriteFruitDictionary.values():
    print("{} is of the data type {}".format(value, type(value)))
    
for key, value in myFavoriteFruitDictionary.items():
    print("{} : {} is of the data type {}". format(key,value,type(value)))
