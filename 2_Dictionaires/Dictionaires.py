#this is a dictionary
dawson = {
    "first_name" : "Dawson",
    "last_name" : "Mercer",
    "age" : "25",
    "NetWorth" : 420.69,
    "Vaxxed" : True
}
#print all
print(dawson)

# if i want to print only one thing
print(dawson["first_name"])

#how to change a value in a dict
dawson["age"] = 9000
print(dawson["age"])

#how to add values to a dict
dawson["nationality"] = "Newfie"
print(dawson)

#delete something from dictionary
del dawson["NetWorth"]
print(dawson)


