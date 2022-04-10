def insertion_sort(lst):
    for index in range(1, len(lst)):
        if lst[index - 1] < lst[index]:
            lst[index - 1], lst[index] = lst[index], lst[index - 1]
    print(lst)

def main():
    lst = [9,100,7,6,18, 1]
    insertion_sort(lst)


if __name__ == "__main__":
    main()