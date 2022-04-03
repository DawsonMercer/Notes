from Assign4_1 import Stack
def reverse(num_list):
    new_stack = Stack()

    stack_lenght = len(num_list)
    while new_stack.length() != stack_lenght:
        new_stack.push(num_list.pop())
    # print(stack)
    print(new_stack)


def main():
    num_list = [1,2,3,4]
    print(num_list)
    reverse(num_list)


if __name__ == '__main__':
    main()