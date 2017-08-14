flowerList = open("usdaPlants.txt","r")
lines = flowerList.readlines()
commonNames = []

for line in lines:
    if line.split(',')[3].strip('"') != "":
        commonNames.append(line.split(',')[3].strip('"'))

flowerList.close()
bruteForceDictionary = open("bruteForceDictionary.txt","w")


for name in commonNames:
    if name != "Common Name":
        bruteForceDictionary.write(name + "\n")

bruteForceDictionary.close()
print("file has been created")
