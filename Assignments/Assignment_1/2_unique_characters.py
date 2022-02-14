

def main():
    print("Unique Character - Question 2")
    print("Enter word or sentence and we'll tell you how many unique characters there are in it.\n")
    choice = 'y'
    while choice.lower() == 'y':
        word = input("Enter word or phrase: ")
        i = 0
        dictionary = {}
        while i < len(word):
            if word[i] not in dictionary.values():
                dictionary[i+1] = word[i]
            i+=1
        if len(dictionary) <=1:
            print(f"There is {len(dictionary)} unique character.\n")
        else:
            print(f"There are {len(dictionary)} unique characters.\n")

        choice = input("Would you like to check another word? (y/n) ")
    print("Bye!")


if __name__ == "__main__":
    main()