from Assign4_1 import Queue, Stack


def mirror(queue):
    stack = Stack()
    queue2 = Queue()
    while queue.length() !=0:
        out = queue.peek()
        queue2.enqueue(queue.dequeue())
        stack.push(out)

    print(queue)
    print(queue2)
    print(stack)
    while queue2.length() != 0:
        queue.enqueue(queue2.dequeue())
    while stack.length() != 0:
        queue.enqueue(stack.pop())

    print(queue)


def main():
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    mirror(queue)


if __name__ == '__main__':
    main()