
class Cart:
    def __init__(self):
        self.items = []  # Each item is a dict: {'item_id': ..., 'cat_id': ..., 'price': ..., 'quantity': ...}

    def get_tax_rate(self, cat_id):
        tax_rates = {100: 0.05, 200: 0.1, 300: 0.15}  # example tax rates
        return tax_rates.get(cat_id, 0.08)  # default tax rate if category not found

    def add_item(self, item_id, cat_id, price, quantity):
        self.items.append({
            'item_id': item_id,
            'cat_id': cat_id,
            'price': price,
            'quantity': quantity
        })

    def clear_cart(self):
        self.items = []

    def total(self, discount_percent=0):
        total = sum(
            item['price'] * item['quantity'] * (1 + self.get_tax_rate(item['cat_id']))
            for item in self.items
        )
        return total * (1 - discount_percent)

if __name__ == "__main__":
    cart = Cart()
    cart.add_item(12, 100, 100, 2)
    cart.add_item(16, 200, 200, 1)
    print("Total price:", cart.total())
    cart.clear_cart()
    print("Total price after clearing cart:", cart.total())
