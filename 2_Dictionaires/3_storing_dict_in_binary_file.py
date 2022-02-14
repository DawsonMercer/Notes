import pickle

dawson = {
    "first_name" : "Dawson",
    "last_name" : "Mercer",
    "age" : "25",
    "NetWorth" : 420.69,
    "Vaxxed" : True
}

with open("dawson.bin", "wb") as file:
    pickle.dump(dawson, file)
    print("finished!")

with open("dawson.bin", "rb") as file:
    loaded_file = pickle.load(file)

print(loaded_file)
