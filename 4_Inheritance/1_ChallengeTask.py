class Publication:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, period: str, publisher: str, title: str, price: float):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine:
    def __init__(self, title, publisher, price, period):
        super().__init__(period, publisher, title, price)



class Newspaper:
    def __init__(self, title, publisher, price, period):
        super().__init__(period, publisher, title, price)



b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)


