
def main():
    print("Anagrams - Question 3")
    choice = "y"
    while choice.lower() == "y":
        word_1 = input("Enter word 1: ")
        word_2 = input("Enter word 2: ")
        word_1 = word_1.lower()
        word_2 = word_2.lower()
        i = 0
        dict_1 = {}
        dict_2 = {}
        list_1 = []
        list_2 = []
        while i < len(word_1):
            list_1.append(word_1[i])
            list_2.append(word_2[i])
            i += 1
        list_1.sort()
        list_2.sort()
        for i in list_1:
            dict_1[i] = None
        for i in list_2:
            dict_2[i] = None

        if dict_1 == dict_2:
            print("You've got an anagram!\n")
        else:
            print(f"{word_1} and {word_2} are not anagrams.\n")
        choice = input("Try again? (y/n) ")
    print("Bye!")


if __name__ == "__main__":
    main()