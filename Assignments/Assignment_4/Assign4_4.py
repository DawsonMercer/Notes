import random

def pick_6():
    my_set = set()
    while len(my_set) < 6:
        num = random.randint(1, 49)
        if num not in my_set:
            my_set.add(num)
    print(f"Your numbers: {my_set}")
    return my_set


def check_numbers(my_set, set_lottery):
    winning_nums = 0
    for number in set_lottery:
        if number in my_set:
            winning_nums +=1
    if winning_nums == 2:
        print("Free PLAY!")
    elif winning_nums == 3:
        print("You win $10!")
    elif winning_nums == 4:
        print("You win $90.50")
    elif winning_nums == 5:
        print("You win $5000!")
    elif winning_nums == 6:
        print("YOU WIN $13,000,000!!")
    else:
        print("Sorry please play again.")



def main():
    winning_nums = 0

    set_lottery = {9, 20, 27, 35, 37, 43}
    print(f"Lotto Numbers: {set_lottery}")
    choice = "y"
    while choice.lower() == "y":
        my_set = pick_6()
        check_numbers(my_set, set_lottery)
        choice = input("Continue? (y/n) ")

    print("Bye!")

if __name__ == '__main__':
    main()