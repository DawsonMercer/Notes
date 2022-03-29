# 1. Eric has a hockey card collection.  Eric has 2 Wayne Gretzky cards, 3 Mario Lemieux cards, 1 Sidney Crosby card,
# 1 Austin Mathews card and 2 Jaromir Jagr cards.  Store the cards in a dictionary where the key is the name of the card,
# and the value is the number of cards in the collection.  Add the following options to the program, 1) Add a Card, 2) List Cards, 3) Remove a card


def add_card(hockey_cards):
    key = input("Enter player: ")
    number = int(input("Enter number"))
    hockey_cards[key] = number


def list_cards(hockey_cards):
    for key, value in hockey_cards.items():
        print(f"{key} - {value}")

def remove_card(hockey_cards):
    remove = input("Name to remove: ")
    if remove in hockey_cards:
        hockey_cards.pop(remove)
    print(hockey_cards)


def main():

    hockey_cards = {"Wayne Gretzky": 2,
                    "Mario Lemieux": 3,
                    "Sidney Crosby": 1,
                    "Austin Mathews": 1,
                    "Jaromir Jagr": 2}
    print(hockey_cards)
    while True:
        choice = input("(a/l/r): ")
        if choice == "a":
            add_card(hockey_cards)
        elif choice == "l":
            list_cards(hockey_cards)
        elif choice == "r":
            remove_card(hockey_cards)
        elif choice == "c":
            break


if __name__ == "__main__":
    main()