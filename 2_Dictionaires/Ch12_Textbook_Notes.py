# ch 12 dictionaries

#dictionarys have a key followed by a colon then a value
#12-1

dictionary_name = {"key_1" : "value1",
                   "key2" : "value2"}
print(dictionary_name)

dictionary_name["key3"] = "value3"
print(dictionary_name)

#12-2
countries = {"CA" : "Canada",
             "US": "United States",
             "GB" : "Great Britain",
             "MX" : "Mexico"}

#prints Mexico
print(countries["MX"])

#set a value for a given value
print(countries["GB"])
countries["GB"] = "United Kingdom"
print(countries["GB"])

#add to dict
countries["FR"]= "France"
print(countries)

#check to see if in the dict using "in"
code = "EP"
if code in countries:
    country = countries[code]
    print(country)
else:
    print("Not in dict")

#get() method of a dict obj
country = countries.get("MX")
print(country)
country = countries.get("IE")
print(country)
country = countries.get("IE", "Cant find dat key bro")
print(country)


#12-3 how to delete items
del countries["MX"]
print(countries)
#del countries["IE"]

#check to see if code in dict
code = "IE"
if code in countries:
    country = countries[code]
    del countries[code]
    print(country + "was deleted")
else:
    print("there was no code with " + code)

#you can also delelte using pop()
popped = countries.pop("GB")
print(popped)
country = countries.pop("IE", "This doesnt exist in the dict")
print(country)

#code that uses pop() method to prevent key error

code = "IE"
country = countries.pop(code, "unknown country")
print(country + " was deleted")

#clear the dictionary with clear()
#countries.clear()
print(countries)

#12-4 how to loopp through keys and values

#keys return a view object that contains all of the keys in the dict
for code in countries.keys():
    print(code + "    " + countries[code])

#can also do it this way
#you dont need to call keys
for code in countries:
    print(code + "     " + countries[code])

#items() returns a view object that contains a tuple for each key/value paid int he dict
for code, name in countries.items():
    print(code + "::::" + name)

#values() useful when you want to work with the values for a dict but dont need to work with the keys
#values not keys
for name in countries.values():
    print(name)


#12-5 lists and dictionaries
#list(view) converts view object to a list
countries = {"CA" : "Canada",
             "US": "United States",
             "GB" : "Great Britain",
             "MX" : "Mexico"}
codes = list(countries.keys())
codes.sort()
for code in codes:
    print(f"{code} - {countries[code]}")

#dict(list) converts 2d list to a dict
countries = [["GB", "Great B"], ["CA", "Canada"], ["MX", "Mexico"]]
countries = dict(countries)
print(countries)