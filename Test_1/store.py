# Test 1 Dawson Mercer

class Product:
    products_counter: int = 0

    def __init__(self, name: str, brand: str):
        if not isinstance(name, str):
            raise AssertionError("Name must be string")
        assert isinstance(brand, str), AssertionError("Brand must be string")
        self.__name = name
        self.__brand = brand
        Product.products_counter +=1

    @property
    def name(self):
        return self.__name

    @property
    def brand(self):
        return self.__brand

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be string")
        self.__name = new_name

    @brand.setter
    def brand(self, new_brand):
        if not isinstance(new_brand, str):
            raise TypeError("Brand must be string")
        self.__brand = new_brand


class ProductByWeight(Product):
    def __init__(self, name: str, brand: str, price_per_kg: float):
        Product.__init__(self, name, brand)
        assert isinstance(price_per_kg, float), TypeError("Price per kg must be float")
        if (price_per_kg < 0):
            raise ValueError("Price per kg must be greater than 0")
        self.__price_per_kg = price_per_kg
        self.__product_id = f"PBW_{str(Product.products_counter).zfill(3)}"

    @property
    def price_per_kg(self):
        return self.__price_per_kg

    @price_per_kg.setter
    def price_per_kg(self, new_price_per_kg):
        if not isinstance(new_price_per_kg, float):
            raise TypeError("Price per kg must be float")
        if (new_price_per_kg < 0):
            raise ValueError("Price per kg must be greater than 0")
        self.__price_per_kg = new_price_per_kg

    @property
    def product_id(self):
        return self.__product_id

    def __str__(self):
        return f"{self.name} by {self.brand}, ${self.price_per_kg}/kg ({self.product_id})"


class ProductByUnit(Product):
    def __init__(self, name: str, brand: str, price_per_unit: float):
        Product.__init__(self, name, brand)
        assert isinstance(price_per_unit, float), TypeError("Price per unit must be float")
        if (price_per_unit < 0):
            raise ValueError("Price per unit must be greater than 0")
        self.__price_per_unit = price_per_unit
        self.__product_id = f"PBU_{str(Product.products_counter).zfill(3)}"

    @property
    def price_per_unit(self):
        return self.__price_per_unit

    @price_per_unit.setter
    def price_per_unit(self, new_price_per_unit):
        if not isinstance(new_price_per_unit, float):
            TypeError("Price per unit must be float")
        if (new_price_per_unit < 0):
            raise ValueError("Price per unit must be greater than 0")
        self.__price_per_unit = new_price_per_unit

    @property
    def product_id(self):
        return self.__product_id

    def __str__(self):
        return f"{self.name} by {self.brand}, ${self.price_per_unit}/kg ({self.product_id})"


class ShoppingCart:
    def __init__(self):
        self.__cart_items = {}

    def add_item_by_weight(self, item, weight_in_kg):
        assert isinstance(item, ProductByWeight), TypeError("Item must be ProductByWeight")
        if not isinstance(weight_in_kg, float):
            raise AssertionError("Weight in kg must be float")
        if weight_in_kg <=0:
            raise AssertionError("weight in kg must be positive")

        if item.product_id in self.__cart_items:
            current_weight = self.__cart_items[item.product_id][1]
            new_weight = current_weight + weight_in_kg
            self.__cart_items[item.product_id] = [item, new_weight]
        else:
            self.__cart_items[item.product_id] = [item, weight_in_kg]

    def remove_item_by_weight(self, item, weight_in_kg):
        assert isinstance(item, ProductByWeight), TypeError("Item must be ProductByWeight")
        if not isinstance(weight_in_kg, float):
            raise AssertionError("Weight in kg must be float")
        if isinstance(weight_in_kg, str):
            raise AssertionError("Weight in kg must be float")

        if weight_in_kg <= 0:
            raise AssertionError("weight in kg must be positive")

        if item.product_id not in self.__cart_items:
            raise ValueError(f"{item.product_id} not in cart")
        else:
            current_weight = self.__cart_items[item.product_id][1]
            new_weight = current_weight - weight_in_kg
            if current_weight <= weight_in_kg:
                del self.__cart_items[item.product_id]
                print(f"{item.name}-{item.product_id} has been removed from the cart")
            else:
                self.__cart_items[item.product_id] = [item, new_weight]
                print(f"{item.name}-{item.product_id} weight removed. Updated weight: {new_weight}")



    def add_item_by_quantity(self, item, quantity):
        assert isinstance(item, ProductByUnit), TypeError("Item must be ProductByUnit")
        if isinstance(quantity, str):
            raise AssertionError("Quantity must be int")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be int")
        if isinstance(quantity, float):
            raise AssertionError("Quantity must be int")
        if quantity <= 0:
            raise AssertionError("Quantity must be greater than zero.")

        if item.product_id in self.__cart_items:
            current_quantity = self.__cart_items[item.product_id][1]
            new_quantity = current_quantity + quantity
            self.__cart_items[item.product_id] = [item, new_quantity]
        else:
            self.__cart_items[item.product_id] = [item, quantity]



    def remove_item_by_quantity(self, item, quantity):
        assert isinstance(item, ProductByUnit), TypeError("Item must be ProductByUnit")
        if not isinstance(quantity, int):
            raise AssertionError("Quantity must be int")
        if quantity <= 0:
            raise AssertionError("Quantity must be greater than zero.")
        if item.product_id not in self.__cart_items:
            raise ValueError(f"{item.product_id} not in cart")
        else:
            current_quantity = self.__cart_items[item.product_id][1]
            new_quantity = current_quantity - quantity
            if current_quantity <= quantity:
                del self.__cart_items[item.product_id]
                print(f"{item.name}-{item.product_id} has been removed from the cart.")
            else:
                self.__cart_items[item.product_id] = [item, new_quantity]
                print(f"{item.name}-{item.product_id} quantity removed. Updated quantity: {new_quantity}")

    def __str__(self):
        cart_list = ""
        for product_id_key in self.__cart_items:
            product_info = self.__cart_items[product_id_key]
            if isinstance(product_info[0], ProductByUnit):
                cart_list += f"{product_info[0]} - {product_info[1]} units\n"
            if isinstance(product_info[0], ProductByWeight):
                cart_list += f"{product_info[0]} - {product_info[1]}kg\n"

        return cart_list

    def __len__(self):
        return len(self.__cart_items)

    def get_total_price(self):
        total = 0
        for product_id_key in self.__cart_items:
            product_id = self.__cart_items[product_id_key]
            if isinstance(product_id[0], ProductByWeight):
                total += product_id[0].price_per_kg * product_id[1]
            if isinstance(product_id[0], ProductByUnit):
                total += product_id[0].price_per_unit * product_id[1]
        return total


if __name__ == "__main__":

    grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
    apples = ProductByUnit("Apples", "Gala", 0.99)
    cart = ShoppingCart()
    cart.add_item_by_weight(grapes, 3.0)
    cart.add_item_by_quantity(apples, 24)
    banana = ProductByWeight("BANANA", "BANANA", 9.99)
    print(cart)
    print(len(cart))
    print(cart.get_total_price())
    # cart.add_item_by_quantity(apples, 3)
    # cart.add_item_by_weight(grapes, 3.0)
    # print(cart)
    # # cart.remove_item_by_weight(banana, 1.5)
    # cart.remove_item_by_quantity(apples, 1)
    # print(cart)
    # cart.remove_item_by_weight(grapes, 5.0)
    # print(cart)
    # print(cart.get_total_price())

