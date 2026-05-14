# write and read json data from a file
import json
# define a json data
data = {
    "name":"Cuong",
    "age":21,
    "skills":"python"
}
#write json data to a file
# file = open("json-data.json", "w")
# with open("json/data.json","w") as f:
#     json.dump(data, f,indent=4)
# print("Json data has been written to json-data.json file")

# Read data from a file
myData = open("json-data.json", "r")
with open("json-data.json", "r") as f:
    loadedData = json.load(f)
    print(loadedData)