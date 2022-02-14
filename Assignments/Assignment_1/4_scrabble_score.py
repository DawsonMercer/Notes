
def main():
    print("Scrabble Score - Question 4\n")
    alphabet = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
                'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4,
                'w': 4, 'x': 8, 'y': 4, 'z': 10}

    choice = "y"
    while choice.lower() == "y":
        word = input("Enter a word to compute your Scrabble Score: ")
        if word.isalpha():
            word = word.lower()
            i = 0
            score = 0
            while i < len(word):
                if word[i] in alphabet:
                    score += alphabet[word[i]]
                    i+=1
            print(f"Your Scrabble Score is: {score}\n")
            choice = input("Again? (y/n) ")
        else:
            print("Please enter letters.")
    print("Bye!")


if __name__ == "__main__":
    main()