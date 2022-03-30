from DataStructures import Stack

def main():

    character_stack = Stack()
    while True:
        name = input("Enter character: ")
        if name == "%":
            break
        else:
            character_stack.push(name)

    while character_stack.size() > 0:
        print(character_stack.pop())



if __name__ == '__main__':
    main()