#ask user to enter fname, lname, and age
#store that info in a dict
#print it

def main():
    dawson = {}
    dawson["first_name"] = input("Enter First name: ")
    dawson["last_name"] = input("Enter Last name: ")
    dawson["age"]= input("Enter age: ")


    print(dawson)
    #allow user to update age

    choice = input("Do you wish to update age? (y/n)")
    if choice.lower() == "y":
        dawson["age"] = input("Enter new age: ")
        print(dawson)
    else:
        print("Bye!")


if __name__ == "__main__":
    main()
