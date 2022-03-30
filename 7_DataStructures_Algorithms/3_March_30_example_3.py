from DataStructures import Queue

def get_in_line(customer_queue):
    name = input("PLease enter your name top be added to the line")
    customer_queue.enqueue(name)

def process_customer(customer_queue):
    if customer_queue.size() >0:
        name = customer_queue.dequeue()
        print(f"{name} is processed")
    else:
        print("no customers in line")

def main():

    customer_queue = Queue()
    while True:
        print("enter your selection")
        print("1. get in line")
        print("2. process customer")
        print("3. exit")

        selection = input("Input: ")
        if selection == "1":
            get_in_line(customer_queue)
        elif selection == "2":
            process_customer(customer_queue)
        elif selection == "3":
            break
        else:
            print("Invalid")

if __name__ == '__main__':
    main()