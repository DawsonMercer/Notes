from random import randint


class Player:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
        self.__rosh_list = ["Rock", "Paper", "Scissors"]

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def rosh_list(self):
        return self.__rosh_list

    @value.setter
    def value(self, value):
        self.__value = value


class Bart(Player):
    def __init__(self, name, value = ""):
        Player.__init__(self, name, value)

    def generate_roshambo(self):
        self.value = self.rosh_list[0]

class Lisa(Player):
    def __init__(self, name, value=""):
        Player.__init__(self, name, value)

    def generate_roshambo(self):
        i = randint(0, len(self.rosh_list)-1)
        self.value = self.rosh_list[i]


def get_rps():
    rps = input("\nRock, paper, or scissors? (r/p/s): ")
    value = None
    if rps == "r":
        value = "Rock"
    elif rps == "s":
        value = "Scissors"
    elif rps == "p":
        value = "Paper"
    return value


def play_game(player, opponent):
    wins = 0
    losses = 0
    while True:
        opponent.generate_roshambo()
        print(f"\n{player.name}: {player.value}")
        print(f"{opponent.name}: {opponent.value}")
        if player.value == opponent.value:
            print("Draw!")
        elif player.value == "Rock":
            if opponent.value == "Scissors":
                print(f"{player.name} wins!")
                wins +=1
            else:
                print(f"{opponent.name} wins!")
                losses +=1
        elif player.value == "Paper":
            if opponent.value == "Rock":
                print(f"{player.name} wins!")
                wins += 1
            else:
                print(f"{opponent.name} wins!")
                losses +=1
        elif player.value == "Scissors":
            if opponent.value == "Paper":
                print(f"{player.name} wins!")
                wins += 1
            else:
                print(f"{opponent.name} wins!")
                losses += 1
        choice = input("\nPlay again? (y/n): ")
        if choice.lower() == "y":
            value = get_rps()
            player.value = value
            continue
        else:
            print("\nThanks for playing!")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            break


def main():
    print("Roshambo Game\n")
    name = input("Enter your name: ")
    pick_op = input("\nWould you like to play Bart or Lisa? (b/l): ")

    value = get_rps()
    opponent = None
    if pick_op.lower() == "b":
        r = Bart("Bart")
        opponent = r
    else:
        l = Lisa("Lisa")
        opponent = l

    player = Player(name, value)
    play_game(player, opponent)


if __name__ =="__main__":
    main()