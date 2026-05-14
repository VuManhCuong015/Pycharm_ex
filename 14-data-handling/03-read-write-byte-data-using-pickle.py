# Create a save a data into byte object
import pickle
data = {
    "name":"Cuong",
    "age":20,
    "profession":"intern",
    "salary":"0$",
}
myData = pickle.dumps(data)
print(pickle.loads(myData))