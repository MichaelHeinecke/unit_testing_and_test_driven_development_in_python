from collections import Counter


class Checkout:
    def __init__(self):
        self.item_prices = {}
        self.shopping_cart = Counter()

    def add_item_price(self, item: str, price: int):
        self.item_prices[item] = price

    def add_item(self, item: str):
        if item not in self.item_prices.keys():
            raise Exception('Item has no price')
        self.shopping_cart[item] += 1

    def add_discount(self, item: str, number_of_items: int, price: int):
        if item in self.shopping_cart and self.shopping_cart[item] >= number_of_items:
            self.item_prices[item] = price

    def calculate_total(self):
        total = 0
        for item, count in self.shopping_cart.items():
            total += self.item_prices.get(item) * count
        return total
