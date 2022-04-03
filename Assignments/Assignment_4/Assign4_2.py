from Assign4_1 import Stack
def reverse(stack):
    new_stack = Stack()
    while not stack.is_empty():
        new_stack.push(stack.pop())

    # print(stack)
    print(new_stack)


def main():
     stack = Stack()
     stack.push(1)
     stack.push(2)
     stack.push(3)
     stack.push(4)
     print(stack)
     reverse(stack)


if __name__ == '__main__':
    main()