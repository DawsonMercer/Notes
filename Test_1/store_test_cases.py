# PLEASE DO NOT MODIFY THIS FILE UNLESS DIRECTED TO DO SO
# Passing all tests does not guarantee full marks because everything asked in the question paper cannot be tested.
# Nonetheless, passing all tests mean you have probably gotten most of the marks.

from unittest import TestCase

import pytest  # You may have to install pytest using PyCharm's package manager at the bottom of the screen

from store import Product, ProductByWeight, ProductByUnit, ShoppingCart


class TestProduct(TestCase):
    def test_product_init(self):
        with pytest.raises(AssertionError):
            product = Product("iPhone", 123)
        with pytest.raises(AssertionError):
            product = Product(4.6, "apple")

    def test_product_name(self):
        car = Product("camry", "toyota")
        self.assertEqual(car.name, "camry")
        with pytest.raises(TypeError):
            car.name = 100
        car.name = "corolla"
        self.assertEqual(car.name, "corolla")

    def test_product_brand(self):
        app = Product("watsapp", "facebook")
        self.assertEqual(app.brand, "facebook")
        with pytest.raises(TypeError):
            app.brand = 3.14
        app.brand = "meta"
        self.assertEqual(app.brand, "meta")


class TestProductByWeight(TestCase):
    def test_product_by_weight_init(self):
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        self.assertTrue(isinstance(grapes, Product), "ProductByWeight must inherit from Product")
        with pytest.raises(AssertionError):
            grapes = ProductByWeight("Grapes", "Ocean Spray", "9.99")
        with pytest.raises(ValueError):
            grapes = ProductByWeight("Grapes", "Ocean Spray", -9.99)

    def test_product_by_weight_properties(self):
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        self.assertEqual(grapes.name, "Grapes")
        self.assertEqual(grapes.brand, "Ocean Spray")
        self.assertEqual(grapes.price_per_kg, 9.99)

    def test_product_by_weight_setter(self):
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        with pytest.raises(TypeError):
            grapes.price_per_kg = "9.99"
        with pytest.raises(ValueError):
            grapes.price_per_kg = -9.99
        grapes.price_per_kg = 10.99
        self.assertEqual(grapes.price_per_kg, 10.99)

    def test_product_by_weight_product_id_starts_with_PBW(self):
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        self.assertRegex(grapes.product_id, "PBW_[0-9]{3}")

    def test_product_by_weight_str(self):
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        self.assertIn("Grapes", str(grapes), "ProductByWeight must have a string representation containing its name")
        self.assertIn("Ocean Spray", str(grapes),
                      "ProductByWeight must have a string representation containing its brand")
        self.assertIn("PBW", str(grapes), "ProductByWeight must have a string representation containing its product_id")
        self.assertIn("9.99", str(grapes),
                      "ProductByWeight must have a string representation containing its price_per_kg")


class TestProductByUnit(TestCase):
    def test_product_by_unit_init(self):
        apples = ProductByUnit("Apples", "Gala", 0.99)
        self.assertTrue(isinstance(apples, Product), "ProductByUnit must inherit from Product")
        with pytest.raises(AssertionError):
            apples = ProductByUnit("Apples", "Gala", "0.99")
        with pytest.raises(ValueError):
            apples = ProductByUnit("Apples", "Gala", -0.99)

    def test_product_by_unit_properties(self):
        apples = ProductByUnit("Apples", "Gala", 0.99)
        self.assertEqual(apples.name, "Apples")
        self.assertEqual(apples.brand, "Gala")
        self.assertEqual(apples.price_per_unit, 0.99)

    def test_product_by_unit_setter(self):
        apples = ProductByUnit("Apples", "Gala", 0.99)
        with pytest.raises(TypeError):
            apples.price_per_unit = "0.99"
        with pytest.raises(ValueError):
            apples.price_per_unit = -0.99
        apples.price_per_unit = 1.99
        self.assertEqual(apples.price_per_unit, 1.99)

    def test_product_by_unit_product_id_starts_with_PU(self):
        apples = ProductByUnit("Apples", "Gala", 0.99)
        self.assertRegex(apples.product_id, "PBU_[0-9]{3}")

    def test_product_by_unit_str(self):
        apples = ProductByUnit("Apples", "Gala", 0.99)
        self.assertIn("Apples", str(apples), "ProductByUnit must have a string representation containing its name")
        self.assertIn("Gala", str(apples), "ProductByUnit must have a string representation containing its brand")
        self.assertIn("PBU", str(apples), "ProductByUnit must have a string representation containing its product_id")
        self.assertIn("0.99", str(apples),
                      "ProductByUnit must have a string representation containing its price_per_unit")


class TestShoppingCart(TestCase):
    def test_shopping_cart_init(self):
        cart = ShoppingCart()
        self.assertTrue(isinstance(cart, ShoppingCart))

    def test_shopping_cart_add_item_by_weight(self):
        cart = ShoppingCart()
        apples = ProductByUnit("Apples", "Gala", 0.99)
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        with pytest.raises(AssertionError):  # AssertionError: Product must be ProductByWeight
            cart.add_item_by_weight(apples, 9.99)
        with pytest.raises(AssertionError):  # AssertionError: weight must be a float
            cart.add_item_by_weight(grapes, '9.99')
        with pytest.raises(AssertionError):  # AssertionError: weight must be a positive float
            cart.add_item_by_weight(grapes, -9.99)
        cart.add_item_by_weight(grapes, 1.5)
        self.assertEqual(len(cart), 1)
        cart.add_item_by_weight(grapes, 1.2)
        self.assertEqual(len(cart), 1)

    def test_shopping_cart_remove_item_by_weight(self):
        cart = ShoppingCart()
        apples = ProductByUnit("Apples", "Gala", 0.99)
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        cart.add_item_by_weight(grapes, 1.5)
        with pytest.raises(AssertionError):  # AssertionError: Product must be ProductByWeight
            cart.remove_item_by_weight(apples, 9.99)
        with pytest.raises(AssertionError):  # AssertionError: weight must be a float
            cart.remove_item_by_weight(grapes, '0.99')
        with pytest.raises(AssertionError):  # AssertionError: weight must be a positive float
            cart.remove_item_by_weight(grapes, -0.99)
        with pytest.raises(ValueError):  # ValueError: Product not found in cart
            red_grapes = ProductByWeight("Red Grapes", "Ocean Spray", 9.99)
            cart.remove_item_by_weight(red_grapes, 1.5)
        cart.remove_item_by_weight(grapes, 1.0)
        self.assertEqual(len(cart), 1)
        cart.remove_item_by_weight(grapes, 0.5)
        self.assertEqual(len(cart), 0)

    def test_shopping_cart_add_item_by_quantity(self):
        cart = ShoppingCart()
        apples = ProductByUnit("Apples", "Gala", 0.99)
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        with pytest.raises(AssertionError):  # AssertionError: Product must be ProductByUnit
            cart.add_item_by_quantity(grapes, 9.99)
        with pytest.raises(AssertionError):  # AssertionError: quantity must be a int
            cart.add_item_by_quantity(apples, '9.99')
        with pytest.raises(AssertionError):  # AssertionError: quantity must be a positive int
            cart.add_item_by_quantity(apples, -5)
        cart.add_item_by_quantity(apples, 12)
        self.assertEqual(len(cart), 1)
        cart.add_item_by_quantity(apples, 6)
        self.assertEqual(len(cart), 1)

    def test_shopping_cart_remove_item_by_quantity(self):
        cart = ShoppingCart()
        apples = ProductByUnit("Apples", "Gala", 0.99)
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        cart.add_item_by_quantity(apples, 12)
        with pytest.raises(AssertionError):  # AssertionError: Product must be ProductByUnit
            cart.remove_item_by_quantity(grapes, 9.99)
        with pytest.raises(AssertionError):  # AssertionError: quantity must be an int
            cart.remove_item_by_quantity(apples, '9.99')
        with pytest.raises(AssertionError):  # AssertionError: quantity must be a positive int
            cart.remove_item_by_quantity(apples, -5)
        with pytest.raises(ValueError):  # ValueError: Product not found in cart
            red_apples = ProductByUnit("Red Apples", "Gala", 0.99)
            cart.remove_item_by_quantity(red_apples, 1)
        cart.remove_item_by_quantity(apples, 1)
        self.assertEqual(len(cart), 1)
        cart.remove_item_by_quantity(apples, 11)
        self.assertEqual(len(cart), 0)

    def test_shopping_cart_total_price(self):
        cart = ShoppingCart()
        apples = ProductByUnit("Apples", "Gala", 0.99)
        grapes = ProductByWeight("Grapes", "Ocean Spray", 9.99)
        cart.add_item_by_quantity(apples, 12)
        self.assertAlmostEqual(cart.get_total_price(), 11.879999999999999, places=2)
        cart.add_item_by_weight(grapes, 1.5)
        self.assertEqual(cart.get_total_price(), 26.865)
        cart.remove_item_by_quantity(apples, 4)
        self.assertEqual(cart.get_total_price(), 22.905)
        cart.remove_item_by_weight(grapes, 0.5)
        self.assertEqual(cart.get_total_price(), 17.91)
