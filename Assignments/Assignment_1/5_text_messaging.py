
def main():
    keypad_dict = {1: [".", ",", "?", "!", ":"],
               2: ["A", "B", "C"],
               3: ["D", "E", "F"],
               4: ["G", "H", "I"],
               5: ["J", "K", "L"],
               6: ['M', 'N', 'O'],
               7: ['P', 'Q', 'R', 'S'],
               8: ['T', 'U', 'V'],
               9: ['W', 'X', 'Y', 'Z'],
               0: " "}
    word = input("Input word or phrase: ")
    word = word.upper()

    counter_list = []
    for letter in word:
        for key in keypad_dict:
            value_list = keypad_dict[key]
            for list_letter in value_list:
                if letter == list_letter:
                    # print(f"{letter} is equal to button {key} and press it {(value_list.index(list_letter)+1)} times")
                    inner_list = [key, (value_list.index(list_letter) + 1)]
                    counter_list.append(inner_list)


    # print(counter_list)
    for inner_list in counter_list:
        counter = 1
        while counter <= inner_list[1]:
            print(inner_list[0], end='')
            counter += 1


if __name__ == "__main__":
    main()
