class Order:
    def __init__(self, n: str):
        self.cust_name = n
        self.items = []
        self.total = 0.
        self.eligible_sf = False
    
    def insert_item(self, d: str, p = 0.0):
        item = {}
        item["index"] = len(self.items)
        item["desc"] = d
        item["price"] = p
        self.items.append(item)
        self.total += p

    def remove_item(self, i: int):
        for x in range(len(self.items)):
            if self.items[x]["index"] == i:
                self.total -= self.items[x]["price"]
                self.items.pop(x)
                break

    def eligible(self, e: bool):
        self.eligible_sf = e
    
    

