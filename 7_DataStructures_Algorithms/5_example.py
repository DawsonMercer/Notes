from DataStructures import Queue

def stutter(og_queue):
    duplicate_list = []
    while og_queue.size() > 0:
        num = og_queue.dequeue()
        duplicate_list.extend((num, num))

    for num in duplicate_list:
        og_queue.enqueue(num)
    print(og_queue.queue)


def main():
    print("Stutter")
    og_queue = Queue()
    while True:
        number = int(input("ENter number: "))
        if number == -1:
            break
        else:
            og_queue.enqueue(number)

    stutter(og_queue)



if __name__ == '__main__':
    main()