
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[len(self.stack)-1]

    def clear(self):
        self.stack = []

    def length(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.stack)


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    def length(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("stack")
    print("Pop")
    print(stack.pop())
    print("Peek")
    print(stack.peek())
    print("Length")
    print(stack.length())
    print("is_empty")
    print(stack.is_empty())
    print("__str__")
    print(stack)
    print("clear")
    stack.clear()
    print(stack)

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print("\ndequeue")
    print(queue.dequeue())
    print("peek")
    print(queue.peek())
    print("length")
    print(queue.length())
    print("__str__")
    print(queue)




if __name__ == '__main__':
    main()
