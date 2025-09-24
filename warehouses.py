

class Warehouses:
    def __init__(self, warehouses: list[dict]):
        '''
        class for managing multiple warehouses and their inventories
        '''
        self.warehouses = warehouses  # e.g. [{'name': 'wh1', 'inventory': {1: 5, 2: 5}}, {'name': 'wh2', 'inventory': {2: 10}}]

    def allocate_order(self, order: dict) -> dict:
        '''
        Allocates order items to warehouses, minimizing the number of warehouses used per order.

        Input:
        - order: a single order (item_id: qty), e.g. {1:5, 2:5}

        Output:
        - allocation: e.g. {'wh1': {1:4}, 'wh2': {1:1, 2:5}}, depending on warehouse inventories

        Note:
        - This method mutates both the input order and the warehouse inventories.
        '''
        allocation = {}
        order = order.copy()  # Work on a copy to avoid mutating the input

        # first check if order can be fulfilled at all
        total_inventory = {}
        for wh in self.warehouses:
            for item_id, qty in wh['inventory'].items():
                total_inventory[item_id] = total_inventory.get(item_id, 0) + qty

        for item in order.keys():
            if order[item] > total_inventory.get(item, 0):
                return {}  # cannot fulfill order
            
        # try to fulfill using a single warehouse first
        for wh in self.warehouses:
            if all(wh['inventory'].get(item, 0) >= qty for item, qty in order.items()):
                allocation[wh['name']] = order.copy()
                return allocation  # order fulfilled by single warehouse
            
        # greedy allocation: find the warehouse that can fulfill the most distinct items in the order,
        # then allocate from it, and repeat until order is fulfilled

        while order:
            best_wh = None
            best_fulfill = 0
            for wh in self.warehouses:
                fulfill_count = sum(1 for item, qty in order.items() if wh['inventory'].get(item, 0) >= qty)
                if fulfill_count > best_fulfill:
                    best_fulfill = fulfill_count
                    best_wh = wh

            if not best_wh:
                break  # no warehouse can fulfill any more items

            wh_name = best_wh['name']
            allocation[wh_name] = {}
            for item, qty in list(order.items()):
                available_qty = best_wh['inventory'].get(item, 0)
                if available_qty > 0:
                    allocated_qty = min(qty, available_qty)
                    allocation[wh_name][item] = allocated_qty
                    order[item] -= allocated_qty
                    if order[item] == 0:
                        del order[item]
                    best_wh['inventory'][item] -= allocated_qty
                    if best_wh['inventory'][item] == 0:
                        del best_wh['inventory'][item]

        if order:
            return {}  # could not fulfill entire order

        return allocation

if __name__ == "__main__":
    warehouses = Warehouses([
        {'name': 'wh1', 'inventory': {1: 5, 2: 5}},
        {'name': 'wh2', 'inventory': {1: 1, 2: 10}},
        {'name': 'wh3', 'inventory': {1: 5, 3: 10}}
    ])

    orders = [
        {1: 5, 2: 5},  # can be fulfilled by wh1
        {1: 6, 2: 5},  # needs wh1 and wh3
        {2: 15},       # cannot be fulfilled
        {3: 5},        # can be fulfilled by wh3
        {1: 11}        # cannot be fulfilled  # TODO should be able to be fulfilled by wh1 and wh3, but greedy algo fails
    ]

    for order in orders:
        allocation = warehouses.allocate_order(order)
        print(f"Order: {order} -> Allocation: {allocation}")