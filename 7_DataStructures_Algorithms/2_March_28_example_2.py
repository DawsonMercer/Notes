# 2. Eric has purchased an additional hockey card collection from another collector.
# This collection has 1 Gretzky card, 3 Alexander Ovechkin cards, 2 Mark Messier cards
# and 1 Bobby Hull card.  Write a program that takes the two dictionaries representing
# the two collections and returns a set which includes all the cards.


def main():
    hockey_cards = {"Wayne Gretzky": 2,
                    "Mario Lemieux": 3,
                    "Sidney Crosby": 1,
                    "Austin Mathews": 1,
                    "Jaromir Jagr": 2}

    purchased_hockey_cards = {"Wayne Gretzky": 1,
                    "Alexander Ovechkin": 2,
                    "Mark Messier": 2,
                    "Bobby Hull": 1}
    key_list = []
    this_set = set(hockey_cards)
    this_set.update(purchased_hockey_cards)
    # for key in hockey_cards:
    #     # key_list.append(key)
    #     this_set.add((key))
    # for key in purchased_hockey_cards:
    #     # key_list.append(key)
    #     this_set.add((key))
    # print(key_list)
    # # for key in key_list:
    # #     this_set.add((key))

    print(this_set)


if __name__ == '__main__':
    main()