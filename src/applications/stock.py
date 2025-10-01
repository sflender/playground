'''
A simple inventory management system for a store.
'''



from collections import defaultdict

class Store:
    def __init__(self):
        self.inventory = defaultdict(int)  # item_name -> quantity

    def add_item(self, item_name: str, quantity: int):
        self.inventory[item_name] += quantity
        
    def remove_item(self, item_name: str, quantity: int) -> bool:
        if self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            return True
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]  # clean up zero-quantity items
        return False  # not enough stock
    
    def check_stock(self, item_name: str) -> int:
        return self.inventory[item_name]
    
def restock_report(store: Store, desired_items):
    # Generate a report of items that are below desired stock levels and need restocking
    report = {}
    for item, desired_qty in desired_items.items():
        current_qty = store.check_stock(item)
        if current_qty < desired_qty:
            report[item] = desired_qty - current_qty
    return report


if __name__ == '__main__':
    store = Store()
    store.add_item('apple', 50)
    store.add_item('banana', 20)
    store.remove_item('apple', 10)
    print("Current stock of apples:", store.check_stock('apple'))
    
    desired_stock = {'apple': 100, 'banana': 50, 'orange': 30}
    report = restock_report(store, desired_stock)
    print("Restock report:", report)