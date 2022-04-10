import random

def pick_6():
    my_set = set()
    while len(my_set) < 6:
        num = random.randint(1, 49)
        if num not in my_set:
            my_set.add(num)
    print(f"Your numbers: {my_set}")
    return my_set



def check_numbers(my_set, set_lottery, winnings):
    winning_nums = 0
    for number in set_lottery:
        if number in my_set:
            winning_nums +=1
    if winning_nums == 2:
        print("Free PLAY!\n")
        winnings += 2
    elif winning_nums == 3:
        print("You win $10!\n")
        winnings += 10
    elif winning_nums == 4:
        print("You win $90.50\n")
        winnings +=90.50
    elif winning_nums == 5:
        print("You win $5000!\n")
        winnings +=5000
    elif winning_nums == 6:
        print("YOU WIN $13,000,000!!\n")
        winnings +=13000000
    else:
        print("Sorry please play again.")

    return winnings

def calculate_winnings(winnings, choice):
    cost = choice * 2
    total = winnings - cost

    print(f"\nSpent: ${cost}\nWinnings: ${winnings}\nTotal: ${total}")


def main():
    winning_nums = 0
    cost = 0
    set_lottery = {9, 20, 27, 35, 37, 43}
    print(f"Lotto Numbers: {set_lottery}")
    choice = int(input("Enter number of times to play the lottery: "))
    i = 0
    winnings = 0
    while i < choice:
        cost +=2
        my_set = pick_6()
        winnings = check_numbers(my_set, set_lottery, winnings)
        i+=1

    calculate_winnings(winnings, choice)

if __name__ == '__main__':
    main()